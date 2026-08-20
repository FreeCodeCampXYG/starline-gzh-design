> **Starline enhanced fork**: maintained by 墨点星痕 (starline) at [`FreeCodeCampXYG/starline-gzh-design`](https://github.com/FreeCodeCampXYG/starline-gzh-design), based on `isjiamu/gzh-design-skill` and community pull requests.

<div align="center">

# starline-gzh-design · WeChat Layout Skill

**Turn Markdown into polished HTML you can paste straight into the WeChat editor**

9 curated themes + theme generator · code blocks / images / GIFs · auto section numbers & keyword marks · two-gate quality checks

[![License: AGPL-3.0](https://img.shields.io/badge/License-AGPL--3.0-blue.svg)](LICENSE)
[![Claude Code](https://img.shields.io/badge/Claude%20Code-Skill-blue)](https://claude.ai/code)
[![Themes](https://img.shields.io/badge/themes-9%20+%20generator-1D4ED8)](references/theme-index.md)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg)](CONTRIBUTING.md)
[![Agents](https://img.shields.io/badge/Claude%20Code%20·%20Codex%20·%20Cursor-supported-8b5cf6.svg)](#-quick-start)

English ｜ [中文](README.md)

</div>

---

A layout Skill for AI agents (Claude Code / Codex / Cursor …). You write Markdown; it first identifies the reader's real job, then renders **fully inlined, paste-oriented WeChat HTML** — auto section numbers, keyword underlines, intro cards, code blocks, images, merged author signature — with scripts that deterministically block common platform risks.

## ✨ Features

- **9 curated themes**: Moyu Green (default) · Tech Cobalt · Klein Blue Art Editorial · Red & White · Graphite Minimal · Apple Open Course · Zen Whitespace · Moyu Ticket · Olive Journal — each a self-contained component library (design tokens + components + visual-hierarchy table + article-type recipe table).
- **Theme generator**: none fit? Describe a style in one line or drop a reference image, and generate a fresh component library saved for reuse (see `references/theme-generator.md`).
- **Hierarchy-first layout**: the reader's job, action, and outcome lead; frameworks such as 80/20, STAR, or a quadrant stay secondary unless the article is explicitly about them.
- **Full content support**: code blocks (dark/light, monospace), images, GIFs (with an animated badge), inline code, quotes, lists, product badges, Markdown hyperlinks (auto-converted to superscript footnotes + an end-of-article "References" list).
- **Smart layout**: auto section numbering (last chapter ∞ / ///), 1–3 keyword underlines per paragraph, intro card & TOC distilled from the body, de-duplicated signature.
- **Full-width CJK punctuation** in prose; kept as-is inside code blocks.
- **Paste-compatibility guardrails**: all styles inlined, every text node wrapped in `<span leaf="">`, and layout-critical 50% columns rejected; the real WeChat paste remains the final check.
- **Two-gate quality checks**: `component_lint.py` (library source) + `validate_gzh_html.py` (final output) form a reproducible edit → verify → fix loop.
- **One-click copy**: a local preview HTML with a **Copy** button — click to copy the rich text and paste straight into WeChat, no manual select-all.

> Boundary: the “local preview HTML” is a workspace file, not GitHub Pages, a static site, or a hosted web page. This Skill never claims a public URL without deployment evidence; see [`references/output-boundaries.md`](references/output-boundaries.md).

## ✅ Good for / ❌ Not for

**✅ Good for**: opinion/analysis · tutorials/how-tos · reviews/tool roundups · knowledge notes/methodology · interviews/features · data recaps · lifestyle/personal essays · case studies — turning Markdown / Word / PDF / plain text long-form into paste-ready WeChat HTML; also generating custom themes from a description or reference image.

**❌ Not for**: generic web/landing pages, GitHub Pages or static-site deployment (use a frontend/site skill) · slide decks (use a PPT skill) · pure image posters / social cards (use a social-card skill) · non-WeChat layout · **writing the article** (this skill only lays out — bring the Markdown first).

## 🗂 Common use cases

| Your content | How to lay it out |
|---|---|
| Opinion / deep long-form | Red & White or Graphite Minimal; keyword underlines + pull-quotes |
| Product review / tool roundup | Moyu Green, Tech Cobalt, or Moyu Ticket; step/tool-labels + cards, by recipe |
| Tutorial / how-to | Moyu Green for general guides; Tech Cobalt for AI, developer, and workflow content |
| Data recap / annual report | Moyu Green or Olive Journal; data cards + tables |
| Zen / minimal essay | Zen Whitespace; generous whitespace + centered serif quotes |
| Editorial notes / deep review | Olive Journal; editor's note + sections + dark summary box |
| Word / PDF draft → WeChat | auto-normalize format → then pick a theme by topic |
| A style beyond the built-ins | Theme generator: make one from a line or an image |

## 🎨 8 Curated Themes

Seven themes currently have repository gallery HTML; Klein Blue Art Editorial and Apple Open Course are registered but do not yet have local gallery files:

<table>
<tr>
<td width="33%" align="center"><img src="https://github.com/isjiamu/gzh-design-skill/releases/download/assets-v1/lf-moyu-green.png?v=1" width="250"><br><sub><b>Moyu Green (default)</b></sub></td>
<td width="33%" align="center"><img src="https://github.com/isjiamu/gzh-design-skill/releases/download/assets-v1/lf-red-white.png?v=1" width="250"><br><sub><b>Red & White</b></sub></td>
<td width="33%" align="center"><img src="https://github.com/isjiamu/gzh-design-skill/releases/download/assets-v1/lf-graphite-minimal.png?v=1" width="250"><br><sub><b>Graphite Minimal</b></sub></td>
</tr>
<tr>
<td align="center"><img src="https://github.com/isjiamu/gzh-design-skill/releases/download/assets-v1/lf-zen-whitespace.png?v=1" width="250"><br><sub><b>Zen Whitespace</b></sub></td>
<td align="center"><img src="https://github.com/isjiamu/gzh-design-skill/releases/download/assets-v1/lf-moyu-ticket.png?v=1" width="250"><br><sub><b>Moyu Ticket</b></sub></td>
<td align="center"><img src="https://github.com/isjiamu/gzh-design-skill/releases/download/assets-v1/lf-olive-journal.png?v=1" width="250"><br><sub><b>Olive Journal</b></sub></td>
</tr>
<tr>
<td colspan="3" align="center"><a href="docs/gallery/tech-cobalt.html"><b>Open the full interactive preview</b></a><br><sub><b>Tech Cobalt</b></sub></td>
</tr>
</table>

> 📚 **Theme previews → [docs/all-themes.md](docs/all-themes.md)**　|　or open `docs/gallery/index.html` for the 7 local interactive HTML previews; these files are not a GitHub Pages deployment.

### Theme cheat-sheet

| | Theme | Best for |
|---|---|---|
| ![](https://placehold.co/12/059669/059669.png) `#059669` | Moyu Green (default) | Tutorials, reviews, checklists, tool roundups |
| ![](https://placehold.co/12/1D4ED8/1D4ED8.png) `#1D4ED8` | Tech Cobalt | AI tools, developer tutorials, product docs, workflow guides |
| ![](https://placehold.co/12/002FA7/002FA7.png) `#002FA7` | Klein Blue Art Editorial | Art commentary, brand narratives, deep viewpoints, character features |
| ![](https://placehold.co/12/DC2626/DC2626.png) `#DC2626` | Red & White | Deep analysis, opinions, strong takes |
| ![](https://placehold.co/12/52525B/52525B.png) `#52525B` | Graphite Minimal | Design, tech commentary, premium brand |
| ![](https://placehold.co/12/4A5D52/4A5D52.png) `#4A5D52` | Zen Whitespace | Zen, minimal living, reflective essays |
| ![](https://placehold.co/12/059669/059669.png) `#059669` | Moyu Ticket | Tool comparisons, creative reviews (ticket motif) |
| ![](https://placehold.co/12/1e1f23/1e1f23.png) `#1e1f23` | Olive Journal | Editorial notes, deep reviews, case recaps |

> English slug, library file and underline CSS for each theme: see [`references/theme-index.md`](references/theme-index.md). Need another style? Have the AI generate one with the [theme generator](references/theme-generator.md).

## 🚀 Quick Start

```bash
# One-line install (recommended)
npx skills add https://github.com/FreeCodeCampXYG/starline-gzh-design

# Or manual clone
git clone https://github.com/FreeCodeCampXYG/starline-gzh-design.git ~/.claude/skills/starline-gzh-design
```

Or just ask **any agent** (Claude Code / Codex / Cursor …):

> Please find and install the skill at https://github.com/FreeCodeCampXYG/starline-gzh-design

Then, once installed, tell your agent:

> Lay out `article.md` as WeChat HTML using the Moyu Green theme.

## 📖 Workflow

1. **Calibrate hierarchy** — identify the reader job, one outcome, core path, and supporting frameworks.
2. **Pick a theme** — auto-suggests the best fit by topic and asks you to confirm (defaults to Moyu Green); or specify one, or generate a new one.
3. **Load libraries** — the chosen theme lib + the shared incremental lib (code/image/label).
4. **Parse Markdown** — headings, chapters, bold, highlight, quotes, images, code, lists.
5. **Assemble HTML** — from real components; apply numbering, underlines, full-width punctuation, signature, and full-width critical structures.
6. **Validate** — run `validate_gzh_html.py`, ship only at 0 ERROR.
7. **Output** — a clean fragment + a local preview HTML with a **Copy** button; open it, click "Copy to WeChat", then paste into the editor (no manual select-all). No Pages/site deployment is implied.

## 🧩 Platform limits (enforced)

Output obeys: no `<style>/<script>/<div>`, no `class/id`, no `position:fixed/absolute/sticky`, `float`, `@media/@keyframes`, `display:grid`, `width:50%`, `flex-basis:50%`, CSS variables, external fonts; all styles inlined; every text node wrapped in `<span leaf="">`. Checked deterministically by scripts, not by model discipline.

## 🔁 Verifiable loop

```bash
python3 scripts/component_lint.py .            # source gate: anti-patterns in libraries
python3 scripts/validate_gzh_html.py out.html  # output gate: final HTML compliance
```

Source gate flags `white-space:pre` (blank bloat), full-border dashed frames in prose, and forbidden platform items — must be 0 ERROR. Output gate flags forbidden tags, `<span leaf>` wrapping, half-width punctuation — must be 0 ERROR / 0 half-width WARN.

## 💡 Why it's built this way

- **Constraint beats freedom** — preset palettes + fixed components lock in a quality floor instead of letting the model improvise each time.
- **Paste compatibility by design** — fully inlined styles, every text node in `<span leaf="">`, and no layout-critical 50% columns; the real editor paste remains the final check.
- **Quality by script, not discipline** — two gates (`component_lint` at source + `validate_gzh_html` on output) deterministically check platform rules and punctuation.
- **Model-agnostic** — layout logic lives in libraries and scripts, not any one model's tricks; Claude / GPT / Gemini / Chinese models all produce the same result.
- **Agent-friendly** — input and output are plain-text Markdown / HTML any agent can read, write, edit and verify — native to Claude Code / Codex / Cursor.

## 📁 Structure

```
starline-gzh-design/
├── SKILL.md                 # layout workflow (agent entry)
├── references/              # 9 theme libs + generator + shared lib + theme-index + eval-cases
├── scripts/                 # validate_gzh_html.py + component_lint.py
├── assets/                  # sample-article.md + theme-previews/
└── docs/gallery/            # browser preview of themes
```

## 🎯 Principles

- **Constraint over freedom** — preset palettes and fixed components guarantee a quality floor.
- **Determinism to scripts** — hard rules go to the linters; the model only judges content.
- **Small labels, not dashed frames** — emphasis uses left bars / pill labels; dashed frames are reserved for the centered "asset placeholder".
- **Reproducible** — every lesson becomes a gotcha or a check, guarded by the verifiable loop.
- **Model-agnostic** — works with any capable LLM (Claude, GPT, Gemini, plus Chinese models like DeepSeek, Kimi, Qwen, GLM); layout lives in the libraries and linters, not model-specific tricks, so switching models keeps the same result.
- **Recipe over free choice** — pick the component combo from the theme's article-type recipe table first, then assemble; same-genre articles stay visually consistent.
- **Restrained color** — primary only at anchors (≤5/article), mostly white + gray, color as punctuation.

## 🧠 Make your own theme

### Theme generation — one line or one reference image

Not enough with the built-in 7? Have the AI make one. Driven by the second workflow in [`references/theme-generator.md`](references/theme-generator.md):

1. **Collect preferences** (asked all at once): theme description required (or a reference image); name / colors / font / radius / shadow / use-case auto-filled if blank.
2. **Generate a block library**: 45–75 blocks of full inline-style HTML saved to `assets/theme-previews/{id}.html` — review the whole page at once in a browser.
3. **Convert + register**: turn it into `references/theme-{id}.md` (add `<span leaf>`, the five required sections), register in theme-index, pass `component_lint.py` at 0 ERROR.
4. **First-class from then on**: use it exactly like a built-in theme.

> Try: *"Generate a new WeChat theme — mono magazine, Klein-blue accent, serif type"* or *"Build a component library from this reference image."*

### Color pairing — a repeatable palette structure the AI can auto-fill

Every theme is built on a **design-token palette** with fixed roles: a recognizable **primary** (anchors only, ≤5/article), **light tints** of it for card / quote / label backgrounds, one **contrasting accent** for highlights, a **neutral gray scale** carrying ~90% of the text, and a **light underline color** for per-paragraph keyword marks. Restraint: mostly white + gray, color only as punctuation, ≤2 highlights per paragraph.

Give just a primary color or a vibe, and the generator derives the whole harmonious palette (tints, borders, highlight, grays, underline) with readable contrast:

> *"Use #7C9EB2 misty-blue as the primary and generate a fresh travel-essay WeChat theme."*

## ❓ FAQ

**Will styles survive pasting into WeChat?** The Skill blocks common failure patterns with inline styles, `<span leaf="">`, full-width critical structures, and validators. WeChat may still rewrite styles, so the real editor paste is the final evidence.

**Can I add my own theme?** Two ways: (1) have the AI generate one via `references/theme-generator.md`; (2) hand-write one per `CONTRIBUTING.md` and open a PR.

**Can it output several themes at once?** Yes — say "lay this out in each of these themes" for a batch to choose from.

**How do I update?** Re-run `npx skills add https://github.com/FreeCodeCampXYG/starline-gzh-design`, or `git pull` in the install dir.

**What if the agent's output isn't compliant?** Run `scripts/validate_gzh_html.py`; fix on ERROR until both gates are green. Still stuck? Open an Issue.

## 🤝 Contributing · 📄 License

See [CONTRIBUTING.md](CONTRIBUTING.md). Maintained and enhanced by StarLine on top of [isjiamu/gzh-design-skill](https://github.com/isjiamu/gzh-design-skill) and community pull requests.

**AGPL-3.0 © 2026 StarLine.** Key terms:

1. **Attribution required** — keep the copyright and co-author notice.
2. **Derivatives must be open source** — any modified version, fork or redistribution must be released under AGPL-3.0 (or a compatible license) with full source.
3. **Network use must be open** — even deploying a modified version as a SaaS / web service (without distributing the code) requires publishing the source — this is what sets AGPL apart from GPL.
4. **No closed-source, proprietary, or paid-only distribution.**

Full terms in [LICENSE](LICENSE).

> 🤝 **AI Agent & model vendors welcome to co-create**: want to integrate gzh-design into your product or deeply co-build on it? We'd love that — contact StarLine for the co-creation agreement.
