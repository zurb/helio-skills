---
name: helio-assets
description: Use this skill when the user is working with assets in Helio — uploading images, video, audio, linking Figma prototypes, managing the media library, or troubleshooting asset delivery. Triggers — "Helio assets," "upload image," "upload video," "upload audio," "image variants," "signed URLs," "Figma integration," "Figma prototype URL," "Figma OAuth," "Figma sync," "media library," "asset library," "asset expired," "asset broken," "alt text," "video bitrates," "audio transcoding," "asset delivery." Do NOT use when the user wants section type spec (use `helio-section-types`), test build workflow (use `helio-asset-to-test`), or licensing/billing (use `helio-licensing`).
version: 0.1.0
source_doc_version: Assets v0.1
last_rebuilt: 2026-05-23

sources:
  - doc_id: 1xJdSBdMN32TbRp2DhHixt15Nr-i2Ybp1C0dWVXuvmno
    title: Assets v0.1
    drive_url: https://docs.google.com/document/d/1xJdSBdMN32TbRp2DhHixt15Nr-i2Ybp1C0dWVXuvmno/edit
    last_synced: 2026-05-23
---

You are helping the user work with **assets in Helio** — images, video, audio, and Figma prototypes.

## Core idea

Helio supports four asset types, each with its own upload path and delivery model:

1. **Images** (JPG, JPEG, PNG, GIF) — direct upload, near-instant processing, auto-generated variants
2. **Video** (MP4 and common formats) — transcoded into adaptive bitrate streams
3. **Audio** (MP3 and common formats) — same transcoding path
4. **Figma prototypes** — linked via share URL, no upload; uses Figma OAuth + cached node images

Where assets are used: Click Test (the image), Preference (the variants), Prototype Test (Figma URL), Multiple Choice (optional per-choice image), and section instructions (optional context image/video).

Everything is served via a signed-URL CDN (1 week for standard URLs, 1 year for public API URLs). Assets are account-scoped and reusable across studies — upload once, reference many times.

## Files to read

Read `reference.md` for the supported formats, upload mechanics (direct-to-storage upload, transcoding for video/audio), image variants, Figma integration (auth, caching, rate limiting), delivery model, lifecycle, and the gotchas (silent processing failures, no alt text fields, Figma token refresh).

## How to apply

1. Identify the asset type the user is working with (image, video, audio, Figma).
2. Surface upload mechanics: images are near-instant; video/audio take longer because transcoding runs.
3. For Figma: confirm OAuth is linked and the prototype is accessible to the token.
4. For asset delivery issues, check signed URL behavior — standard URLs are 1-week, API URLs are 1-year. Underlying assets refresh when the page loads.
5. Flag the silent failures: image dimensions defaulting to 0, video processing failures without auto-retry, Figma token expiration breaking sync.
6. For accessibility-sensitive research, surface the no-alt-text-field limitation — captioning and alt text need to go in surrounding section instructions or choice text.

## What's new in v0.1.0

Initial release. Sourced from Assets v0.1. AEO scorecard flagged Problem and Action gaps — both addressed in the ADDED sections.

## Handoffs

- For **section types that use assets** (Click, Preference, Prototype, etc.), use `helio-section-types`.
- For **the build workflow** (where asset upload is a UI-only step), use `helio-asset-to-test`.
- For **Figma-specific sync depth** (full sync/auth/embed behavior), note that's covered here in summary; deeper engineering detail lives in the Helio codebase docs.
- For **broader engineering-side details** (controllers, model names, feature flags), use `helio-features`.
- For **what participants see when an asset loads or fails**, use `helio-participant-experience`.
