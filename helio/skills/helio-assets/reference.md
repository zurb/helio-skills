# Assets — Reference

**Skill:** `helio-assets`
**Source:** Assets v0.1
**Source last synced:** 2026-05-23
**Notes:** Source doc had two minor AEO-rubric gaps (Problem opener; Action pointer). Both are addressed in the ADDED sections at the end of this file.

---

<!-- DERIVED FROM: 1xJdSBdMN32TbRp2DhHixt15Nr-i2Ybp1C0dWVXuvmno — Assets v0.1 -->

Images, videos, audio, and Figma prototypes — how to upload, where they're used, and what to know about delivery.

## What's Supported

- **Images** — JPG, JPEG, PNG, GIF
- **Video** — MP4 and common video formats; transcoded automatically for streaming
- **Audio** — MP3 and common audio formats; transcoded automatically
- **Figma prototypes** — Linked via Figma share URL, no upload needed

## Where Assets Are Used

| Section type | Asset role |
|---|---|
| **Click Test** | The static image participants click on |
| **Preference** | The variants being compared (one image per variation) |
| **Multiple Choice** | Optional image per choice |
| **Prototype Test** | Figma prototype URL (not a file upload) |
| **Section instructions** | Optional image or video for context |
| **Free Response, Likert, etc.** | Optional reference image in instructions |

You can also organize assets in your account's media library with folders, so common assets don't have to be re-uploaded for each study.

## Uploading

Helio's drag-drop / file picker uploader sends files directly to cloud storage rather than through Helio's servers.

For images, processing is near-instant — Helio reads the dimensions and generates the variants it needs (different sizes for thumbnails, large views, etc.). The image is ready to use as soon as the upload finishes.

For video and audio, processing takes longer because Helio transcodes the file into adaptive streaming outputs (multiple bitrate variants for both DASH and HLS, plus thumbnail frames for the player). You can watch progress on the asset; once status flips to Complete, the asset is ready.

**Limits:**

- Image dimensions are capped at 5000 × 10000 pixels (anything larger is auto-resized down).
- No explicit file size cap on video/audio, but the underlying transcoding service has its own quotas.

## Image Variants

Helio auto-generates multiple sizes for each uploaded image:

| Variant | Used for |
|---|---|
| **Square** (256×256) | Thumbnails, list views |
| **Medium** (282×226) | Card displays |
| **Large** (up to 750 wide) | Inline display in tests |
| **Favicon** (152×152) | Small icons |
| **Logo** (500×200) | Account / brand display |

You don't pick which variant to use — Helio loads the right one for each context.

## Video & Audio Playback

Videos and audio files use adaptive streaming, so participants get the right quality for their connection:

- **Bitrates:** 720p / 480p variants for DASH (Android, Chrome); 2 Mbps / 1.5 Mbps / 1 Mbps for HLS (Apple devices).
- **Audio:** MP3 at 160 kbps, stereo, 44.1 kHz.
- **Posters:** A thumbnail is auto-generated from a video frame for the player.

The streaming URLs are signed and refreshed each session.

## Figma Integration

For Prototype Tests, you paste a Figma share URL — Helio handles the rest.

**What Helio does with your Figma URL:**

- Embeds your prototype in the study via Figma's embed iframe.
- Caches per-screen images from Figma so the report can render heatmaps and path visualizations without re-fetching every time.
- Tracks node IDs (screens) as participants navigate through the prototype.

**Authentication:**

- Helio uses your Figma OAuth token (linked once at the account or user level).
- Your prototype must be accessible to that token — either publicly shared or in a file the token has access to.

**Rate limiting:**

- Figma rate-limits aggressively on bulk image fetches. Helio handles this with retries, chunking, and exponential backoff, so syncing a large prototype may take a moment but should succeed.

**What Helio can't do:**

- No direct file-syncing from Figma to a Helio design library.
- No automatic re-sync when you update the Figma file — if you change the prototype after launching, you may need to re-link.

## How Assets Are Delivered

Everything is served from cloud storage via a signed-URL CDN.

**URL lifetime:**

- Standard signed URLs expire after **1 week**.
- For Helio's public API, signed URLs expire after **1 year** (so external consumers can cache).

If you share a screenshot or a report link externally, the *report link* itself doesn't expire — but the underlying asset URLs inside the report refresh when the page loads. There's nothing extra you need to do.

## Customer Uploads vs. Helio-Generated Assets

**Things you upload:**

- Images, videos, audio.
- Files referenced in your media library.

**Things Helio generates automatically:**

- Screenshots of websites (when you submit a URL to Design Analysis).
- Figma node images (cached after you link a prototype).
- Test thumbnails (for previews in the dashboard).

Helio-generated assets show up in your account's storage but aren't separately billed.

## Asset Lifecycle

- Assets are **account-scoped** — accessible to anyone in your account but not across accounts.
- Assets can be **reused across multiple sections and tests** — uploading once and referencing many times is the normal pattern.
- **Deletion is soft** — the asset is marked deleted but stays on S3 until cleanup. An asset that's actively referenced by a test can't be deleted.

## Good to Know


**Processing failures are mostly silent.** If image dimensions can't be read, they default to 0 and the asset is marked complete — visually broken but not technically errored. Video and audio failures show in the asset's status, but there's no automatic retry; you'd need to re-upload.

**No alt text fields yet.** Accessibility metadata isn't first-class for assets — alt text typically goes in the surrounding section instructions or choice text.

**Figma tokens don't auto-refresh.** If you've connected Figma and your token expires (rare with personal access tokens, more common with OAuth), Prototype Tests will fail to sync until you re-authenticate.

**Asset reuse across studies is fine.** The same image referenced by ten different tests counts as one asset — there's no per-test duplication.

<!-- /DERIVED -->

---

<!-- ADDED 2026-05-23 (skill-builder context; closes AEO scorecard Problem + Action gaps) -->

## What this solves

Asset handling failures are quiet — the test still runs but the data is corrupted. Broken Figma links, expired URLs, mis-sized images, missing alt text, and silent processing failures all degrade results without throwing errors. This skill covers what to do so they don't happen.

## When to use

Reach for this skill when the user is:

- Uploading images, video, or audio and confused about processing time / formats
- Linking a Figma prototype and configuring OAuth
- Hitting "broken image" displays in production (URL expiration, processing failure)
- Asking about accessibility (alt text, captions) and discovering Helio doesn't have first-class fields
- Reusing assets across studies and wondering about lifecycle
- Looking up image variant sizes or video bitrates

This is a reference, not a how-to. For where assets fit in test design, use `helio-section-types` (each section type's asset role) or `helio-asset-to-test` (the build workflow). For broader feature gating and plan tier, use `helio-features`.

## Failure modes

- **Treating "asset marked Complete" as "asset works."** Image dimensions defaulting to 0 still marks complete. Visually inspect after upload.
- **Forgetting Figma OAuth can expire.** Personal tokens are stable; OAuth needs occasional re-auth. Prototype Tests fail silently when the token's gone.
- **Updating a Figma prototype after a test launches.** No auto-resync. Re-link if you change the prototype.
- **Expecting alt text fields.** They don't exist for assets. Put accessibility info in section instructions.
- **Trying to delete an asset that's still referenced by a test.** Blocked. Remove the reference first.
- **Sharing a screenshot URL externally and expecting it to work forever.** Standard URLs expire in 1 week. The report link itself is stable, but external screenshot links aren't.

## Where to go next

- For section types that use assets: `helio-section-types`
- For the build workflow: `helio-asset-to-test`
- For broader engineering-side details (feature flags, model names): `helio-features`
- For what participants see during asset loading/failure: `helio-participant-experience`

<!-- /ADDED -->
