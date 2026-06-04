#!/usr/bin/env python3
"""
Validate every SKILL.md (and accompanying reference.md) in the Helio marketplace.

Usage (run from marketplace root):
    python3 scripts/validate-skills.py

SKILL.md checks (per-skill):
  - Opening and closing --- frontmatter delimiters
  - Valid YAML inside the frontmatter
  - Required fields: name, description
  - name field matches the folder name
  - description length within Anthropic's 1024-char limit
  - description is at least 50 chars (too short = won't disambiguate)
  - No bare "Word:" substrings inside description (would break YAML re-parse)
  - sources manifest entries each have doc_id

reference.md checks (per-skill, only if reference.md exists):
  - DERIVED FROM count matches /DERIVED count
  - ADDED count matches /ADDED count
  - Every doc_id in SKILL.md's sources: manifest appears in a DERIVED FROM marker
  - Every doc_id in a DERIVED FROM marker appears in SKILL.md's sources: manifest

Marketplace-level checks:
  - No duplicate skill names across the marketplace

Exits 0 if all skills pass, 1 if any fail.
"""

import os
import re
import sys
from collections import Counter

# Try pyyaml for richer parsing; fall back to manual extraction if unavailable.
try:
    import yaml
    HAS_YAML = True
except ImportError:
    HAS_YAML = False


def parse_frontmatter(fm_text):
    """Parse YAML frontmatter. Uses pyyaml if available, otherwise regex fallback."""
    if HAS_YAML:
        return yaml.safe_load(fm_text)
    # Fallback: extract name and description with regex (good enough for required fields)
    result = {}
    name_m = re.search(r"^name:\s*(.+)$", fm_text, re.MULTILINE)
    if name_m:
        result["name"] = name_m.group(1).strip()
    # description spans until the next top-level key or end of frontmatter
    desc_m = re.search(r"^description:\s*(.+?)(?=\n[a-z_]+:|\Z)", fm_text, re.MULTILINE | re.DOTALL)
    if desc_m:
        result["description"] = desc_m.group(1).strip()
    # Optional fields
    for key in ("version", "source_doc_version", "last_rebuilt"):
        m = re.search(rf"^{key}:\s*(.+)$", fm_text, re.MULTILINE)
        if m:
            result[key] = m.group(1).strip()
    # sources: doc_id list (regex fallback — best effort)
    sources = []
    for m in re.finditer(r"^\s*-\s*doc_id:\s*(.+)$", fm_text, re.MULTILINE):
        sources.append({"doc_id": m.group(1).strip()})
    if sources:
        result["sources"] = sources
    return result


SKILLS_DIR = "helio/skills"
MAX_DESCRIPTION_LENGTH = 1024
MIN_DESCRIPTION_LENGTH = 50

GREEN = "\033[32m"
RED = "\033[31m"
YELLOW = "\033[33m"
DIM = "\033[2m"
RESET = "\033[0m"


def validate_skill_md(folder_name, skill_path):
    """Return (issues_list, parsed_frontmatter_or_None) for a single SKILL.md."""
    issues = []

    if not os.path.exists(skill_path):
        return ["missing SKILL.md"], None

    with open(skill_path, "rb") as f:
        raw = f.read()

    if raw.startswith(b"\xef\xbb\xbf"):
        issues.append("file starts with BOM (remove)")

    text = raw.decode("utf-8", errors="replace")
    lines = text.splitlines()

    if not lines or lines[0].strip() != "---":
        issues.append(f"first line not '---' (got {lines[0][:50]!r})")
        return issues, None

    closing_idx = None
    for i, line in enumerate(lines[1:], start=1):
        if line.strip() == "---":
            closing_idx = i
            break

    if closing_idx is None:
        issues.append("no closing '---'")
        return issues, None

    fm_text = "\n".join(lines[1:closing_idx])

    try:
        parsed = parse_frontmatter(fm_text)
    except Exception as e:
        issues.append(f"YAML parse error: {str(e)[:120]}")
        return issues, None

    if not isinstance(parsed, dict):
        issues.append(f"frontmatter must be a YAML dict, got {type(parsed).__name__}")
        return issues, None

    name = parsed.get("name")
    desc = parsed.get("description")

    if not name:
        issues.append("missing 'name' field")
    elif name != folder_name:
        issues.append(f"name {name!r} != folder {folder_name!r}")

    if not desc:
        issues.append("missing 'description' field")
    elif not isinstance(desc, str):
        issues.append(f"description must be a string, got {type(desc).__name__}")
    else:
        if len(desc) > MAX_DESCRIPTION_LENGTH:
            issues.append(f"description {len(desc)} chars > {MAX_DESCRIPTION_LENGTH} max")
        if len(desc) < MIN_DESCRIPTION_LENGTH:
            issues.append(f"description {len(desc)} chars — too short to disambiguate")
        # Bare Word: substring breaks YAML if not quoted (re-parses as new key)
        bare_keys = re.findall(r"\s([A-Za-z][A-Za-z0-9_]*?):\s", desc)
        if bare_keys:
            issues.append(f"description contains bare 'Word:' substring(s): {bare_keys[:3]} (use em-dash or comma instead)")

    # Source manifest sanity (each entry must have doc_id)
    sources = parsed.get("sources")
    if sources is not None:
        if not isinstance(sources, list):
            issues.append("sources: must be a YAML list")
        else:
            for i, src in enumerate(sources):
                if not isinstance(src, dict):
                    issues.append(f"sources[{i}] is not a dict")
                elif not src.get("doc_id"):
                    issues.append(f"sources[{i}] missing doc_id")

    return issues, parsed


def validate_reference_md(skill_dir, parsed_frontmatter):
    """Return list of issues for the skill's reference.md (if present)."""
    ref_path = os.path.join(skill_dir, "reference.md")
    if not os.path.exists(ref_path):
        return []  # No reference.md is allowed (small skills can skip it)

    issues = []
    with open(ref_path, encoding="utf-8") as f:
        ref_text = f.read()

    # DERIVED / /DERIVED marker balance
    derived_opens = re.findall(r"<!--\s*DERIVED FROM:\s*([A-Za-z0-9_-]+)", ref_text)
    derived_closes = len(re.findall(r"<!--\s*/DERIVED\s*-->", ref_text))

    if len(derived_opens) != derived_closes:
        issues.append(
            f"reference.md DERIVED marker imbalance: {len(derived_opens)} opens vs {derived_closes} closes"
        )

    # ADDED / /ADDED marker balance
    added_opens = len(re.findall(r"<!--\s*ADDED\s", ref_text))
    added_closes = len(re.findall(r"<!--\s*/ADDED\s*-->", ref_text))

    if added_opens != added_closes:
        issues.append(
            f"reference.md ADDED marker imbalance: {added_opens} opens vs {added_closes} closes"
        )

    # Source manifest doc_ids must match DERIVED FROM doc_ids (bidirectional)
    if parsed_frontmatter and isinstance(parsed_frontmatter.get("sources"), list):
        manifest_ids = {s.get("doc_id") for s in parsed_frontmatter["sources"] if isinstance(s, dict)}
        manifest_ids.discard(None)
        marker_ids = set(derived_opens)

        missing_in_markers = manifest_ids - marker_ids
        missing_in_manifest = marker_ids - manifest_ids

        if missing_in_markers:
            issues.append(
                f"sources manifest doc_id(s) not found in reference.md DERIVED markers: {sorted(missing_in_markers)}"
            )
        if missing_in_manifest:
            issues.append(
                f"reference.md DERIVED FROM doc_id(s) not in SKILL.md sources manifest: {sorted(missing_in_manifest)}"
            )

    return issues


def main():
    if not os.path.isdir(SKILLS_DIR):
        print(f"{RED}ERROR{RESET}: {SKILLS_DIR}/ not found. Run from marketplace root.")
        sys.exit(2)

    folders = sorted(d for d in os.listdir(SKILLS_DIR) if os.path.isdir(os.path.join(SKILLS_DIR, d)))
    if not folders:
        print(f"{RED}ERROR{RESET}: no skill folders found in {SKILLS_DIR}/")
        sys.exit(2)

    results = []
    names_seen = []

    for folder in folders:
        skill_dir = os.path.join(SKILLS_DIR, folder)
        skill_path = os.path.join(skill_dir, "SKILL.md")
        issues, parsed = validate_skill_md(folder, skill_path)

        if parsed is not None:
            issues.extend(validate_reference_md(skill_dir, parsed))

        results.append((folder, issues))

        # Capture name for duplicate check
        if parsed and isinstance(parsed, dict) and parsed.get("name"):
            names_seen.append(parsed["name"])

    # Duplicate name check across marketplace
    name_counts = Counter(names_seen)
    duplicates = {n: c for n, c in name_counts.items() if c > 1}

    # Print report
    failed = [r for r in results if r[1]]
    passed = [r for r in results if not r[1]]

    for folder, issues in results:
        if not issues:
            print(f"  {GREEN}OK{RESET}   {folder}")
        else:
            print(f"  {RED}FAIL{RESET} {folder}")
            for issue in issues:
                print(f"         {DIM}-{RESET} {issue}")

    print()
    print(f"{DIM}─────────────────────────────────────{RESET}")
    print(f"  Total:   {len(results)}")
    print(f"  {GREEN}Passed:  {len(passed)}{RESET}")
    if failed:
        print(f"  {RED}Failed:  {len(failed)}{RESET}")
    if duplicates:
        print(f"  {YELLOW}Duplicate names: {duplicates}{RESET}")

    sys.exit(0 if not failed and not duplicates else 1)


if __name__ == "__main__":
    main()
