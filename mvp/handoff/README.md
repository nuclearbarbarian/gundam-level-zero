# GLZ Handoff Bundle for Claude Design

This folder is a self-contained briefing for **Claude Design** (claude.ai/design).
Drag the whole folder into a new Design project and prompt with one of the
Suggested Prompts below.

## Contents

- **`mechapds.md`** — the full MechaPDS v0.2 design language spec. Treat this
  as binding: the project has an explicit register lock and a falsifiable
  honesty condition. Read §Posture, §The Four Binding Rules, §Color, and
  §Typography. Do not introduce typefaces or color encodings outside the spec.
- **`copy.md`** — drag-droppable copy bundle: tagline, The Case (~250 words),
  key stats, audience, anticipated Qs.
- **`tech-tree.svg`** — the Heavyarms Tech Tree v0.1 figure, ARPANET register.
  Use as-is or as visual reference; do not restyle.

## Project context (for Claude Design's prompt)

**Gundam Level Zero** is a defense industrial- and innovation-base benchmark
that uses Heavyarms-class production as the stress test. American-led with
allied industrial integration (Korea, Japan, Germany, Taiwan, Netherlands,
Switzerland baseline; UK/AU/CA via AUKUS §1080). PRC firmly excluded per
NSIBR. Audience: defense analysts (DARC paper commission). Not a procurement
proposal — a diagnostic + programmatic benchmark.

The project's design language is **MechaPDS**: 1940s American trade-journal
revival (PDS) for narrative + 1969–78 BBN ARPANET completion-report revival
(ARPANET) for data-dense surfaces. Two registers assigned by surface; hybrids
forbidden. Strict typography lock: Charter (PDS body) + IBM Plex Mono
(ARPANET + data). Monochrome default; spot color on PDS only with non-color
cue requirement.

## Suggested prompts for Claude Design

### A. Hackathon poster (one-page)

> Build a one-page MechaPDS-register hackathon poster for *Gundam Level
> Zero*. Use the tagline from `copy.md` as the headline, The Case as the body,
> and the key stats as a sidebar. Embed `tech-tree.svg` as the central figure.
> Strictly follow `mechapds.md` Rule 1 (register split by surface) and Rule 4
> (visible uncertainty). Output PDF + PNG.

### B. Pitch deck (~6 slides)

> Build a 6-slide pitch deck in MechaPDS register: (1) tagline + masthead;
> (2) The Case; (3) the seven research tracks; (4) the tech tree figure
> (`tech-tree.svg`); (5) allied integration partners + PRC exclusion;
> (6) status + ask (DARC paper in progress; phase 2 in progress; not a
> procurement proposal). Charter for headings/body, Plex Mono for data and
> chrome. Monochrome with one spot color (Industrial Red) reserved for
> exclusion / gap callouts. Output PPTX.

### C. One-pager handout (printable)

> Build a single-page printable handout in MechaPDS register, A4 portrait,
> for the hackathon judges' table. Headline = tagline. Body = The Case.
> Embed the tech tree figure at half-page. Sidebar = key stats. Footer =
> source disclosures from `copy.md`. Output PDF.

## Hard constraints

1. Do not introduce typefaces outside Charter / IBM Plex Mono / system
   fallbacks. (Source Serif 4 is permitted as Charter fallback only.)
2. Do not encode information by color alone — every color carries a
   non-color cue (bracket, glyph, label, weight). See MechaPDS Rule 4.
3. The honesty disclosures from `copy.md` ("13 of 21 gating nodes not yet
   started" etc.) must appear visibly on every artifact. Silence implies
   completeness; silence is not permitted.
4. PRC is excluded, not omitted. Show it as explicitly excluded per NSIBR.
5. This is a benchmark, not a procurement proposal. Do not let a poster
   read as advocacy for building a Gundam.

## Date

Bundle generated 2026-04-26 from `mvp/` working directory.
