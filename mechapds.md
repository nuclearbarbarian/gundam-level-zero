# MechaPDS

**The PDS × ARPANET Integration System**
**Version 0.2** — 2026-04-18 (superseding v0.1 after Phase 1 Inquisitor review)
**Project:** Gundam Level Zero
**Sources:** Fidler & Currie (2015); Heart, McKenzie, McQuillan & Walden, ARPANET Completion Report (1978/1981). See `~/.claude/borges/source-cards/gundam-level-zero/INDEX.md`.

---

**MechaPDS** is the design language of the Gundam Level Zero project: an integration of two literal-revival design systems — the Penney Design System (1940s American trade-journal revival) and the ARPANET register (1969–1978 BBN completion-report revival) — governed by explicit domain assignment, a falsifiable honesty condition inherited from Fidler & Currie's critical-cartography analysis, and a closed typographic discipline per register.

v0.2 supersedes v0.1 following Phase 1 Inquisitor review (2026-04-18). See `phase-1-inquisitor-review-2026-04-18.md` and the Changelog at the end of this file.

---

## Definitions

- **Register** — PDS or ARPANET. A closed set of typographic, chromatic, and figurative conventions.
- **Surface** — a contiguous authored area governed by one register: a page, a figure, a callout, a map, a table, a navigation element.
- **Artifact** — a single bounded visual unit: one page, one figure, one map, one callout, one table. Not a document. An embedded figure inside a page is a distinct artifact from its host page; the boundary is the figure's frame.
- **Plate** — a specimen surface in documentation (including the Design Language Preview). Not a production form.
- **The seam** — the interface between a PDS artifact and an embedded ARPANET artifact. Always treated as a citation-style quotation.
- **Scope** — English text, Latin script. Foreign-language terms appear in glossary entries and citations only; Japanese source terms use Noto Sans JP as a documented secondary face.

---

## Posture — Why This Pairing

Both PDS and the ARPANET register are **literal revivals of American institutional print aesthetics**. Both operate under three shared constraints:

1. **Monochrome default** — 1940s trade press from wartime paper rationing; 1969–78 BBN report from government-contractor black-and-white production.
2. **Functional restraint** — no decoration; every element earns its place.
3. **Source discipline** — every claim, figure, and table carries provenance.

These properties are also shared with other institutional traditions (Swiss modernism, DEC technical manuals, RAND reports). What makes *this* pairing coherent for Gundam Level Zero is not shared lineage but **matched function**: both registers are American institutional voices speaking to mixed public/technical audiences on matters of industrial and technological consequence. The 1940s trade journal and the 1970s DARPA completion report are, together, the two most credible American voices for arguing that something industrial is possible. MechaPDS borrows both. The registers do not fuse — they are assigned to domains within one document.

---

## The Four Binding Rules

### Rule 1 — Register Split by Surface

PDS governs narrative, argument, tables-as-argument, document chrome, and figure captions. ARPANET register governs data-dense technical surfaces: logical maps, readiness matrices, geographic facility maps, monospace quantitative tables, traffic-style line charts, ARPANET bar charts.

**Hybrid artifacts are not permitted.** A single artifact uses one register throughout. Embeddings and seams (Rule 7 below, §Typography) are not hybrids — the embedded figure and the host page are distinct artifacts, bounded by the figure's frame.

### Rule 2 — Honesty Condition (operational)

A flat graph form (nodes of equal visual weight, links of equal visual weight) may only depict entities that are genuinely equivalent in the depicted dimension.

**Operational procedure — required before publishing any flat-node figure:**

1. Name the depicted dimension in a single sentence. ("This map depicts _____.")
2. List the depicted entities.
3. For each pair of entities, ask: are they equivalent in the depicted dimension? If yes, flat form is permitted for that pair. If no, hierarchical grammar is required.
4. For each *ranking* dimension the entities could be compared on (not just the depicted one), ask: is this ranking load-bearing for the figure's argument? If any answer is yes, flat form is forbidden; redraw with hierarchical grammar.
5. Record the four answers in a `<!-- [HONESTY-CHECK] ... -->` comment block in the figure's source file. Reviewers verify before publication.

Hierarchical grammar options when flat form fails: nested groupings (components enclosed within subsystems), tier labels (Tier-1 / Tier-2 / Tier-3 explicit), weighted borders (primary nodes bolder than secondary), or register split (move the hierarchical data out of the logical map into a matrix or ranked list).

### Rule 3 — Typography Lock (closed exception list)

**PDS surfaces** — Body and headings: Charter (working face) or Plantin (aspirational — see §Typefaces & Licensing). Data: IBM Plex Mono Regular. Weights: Regular (400) and Bold (700) only. Italic permitted for: captions, running-head document titles, standard body-text emphasis.

**ARPANET surfaces** — All text: IBM Plex Mono Regular (400). Italic permitted for site-name-equivalent labels, per BBN convention from the first logical map (December 1970) onward. This is a first-class rule, not a carve-out.

**Chrome** (page-wrapper typography: preview-panel labels, tab titles, skip links, build metadata): Plex Mono Medium (500) permitted. Chrome is documentation infrastructure, not artifact content.

**No additional exceptions are permitted without spec amendment (§Governance). Additions require a documented period source and a written ADR.**

### Rule 4 — Visible Uncertainty (one semantic rule, two surface forms, never color-only)

**Semantic rule:** every figure, table, and claim carries an explicit acknowledgment of any gap, estimate, scope limitation, or unverified source. Silence implies full coverage. Non-negotiable.

**PDS surface form:** bracketed bold tokens inline — **[GAP]**, **[ESTIMATE]**, **[DATED: YYYY-MM]**, **[UNVERIFIED]**, **[VERIFY AGAINST ORIGINAL]**, **[PAGE NUMBER FROM PDF INDEX]**. The bracket + bold combination is load-bearing. Industrial Red is decorative only; the signal must be legible in grayscale.

**ARPANET surface form:** parenthesized ALL CAPS, flush-left below the figure or after the relevant line, in Plex Mono Regular.

**Cross-register leakage is forbidden.** PDS `[GAP]` tokens do not appear on ARPANET surfaces. Parenthesized ALL CAPS caveats do not appear on PDS narrative. The two forms are idioms of the same rule — they do not mix within a single artifact.

**Color-pair rule:** any color-encoded information carries at least two non-color cues (bracket + bold + optional color; glyph + label + optional color). WCAG 1.4.1 compliance is non-negotiable.

---

## Domain Assignment

| Surface | Register | Notes |
|---|---|---|
| Project narrative, argument, body text | PDS | |
| Section and chapter headings | PDS | |
| Running heads and folios | Per register of the page | |
| Tables-as-argument (comparative, rhetorical) | PDS | Em-dash title `TABLE 3.—TITLE` |
| Readiness matrices, quantitative tables, data dumps | ARPANET | Pipe-separated monospace, double-hyphen captions |
| Section callouts, key-finding boxes | PDS | |
| Figure captions (commentary on any figure) | PDS italic Charter | Below the figure |
| Figure titles (internal to ARPANET figures) | ARPANET | Plex Mono, ALL CAPS, centered above figure body |
| Heavyarms subsystem logical map (Phase 3 Layer 2) | ARPANET logical | |
| Per-subsystem logical maps | ARPANET logical | Density point scales with component count (§Density Scaling) |
| Industrial-base geographic map | ARPANET geographic + PDS substrate | See §Integration Points |
| Gundam Level Zero readiness matrix | ARPANET monospace table | |
| Traffic / growth line charts | ARPANET | |
| Bar charts (categorical or time series) | ARPANET | |
| Choropleth / policy-data maps | PDS via John Quincy Adams | |
| Navigation UI (nav bar, breadcrumbs, tabs, menu items) | PDS | |
| Nav hover / focus / active states | PDS | See §Web Register |
| Form controls (filter dropdowns, search, toggles) | PDS | |
| Tooltips on interactive figures | Register of the underlying surface | |
| Code blocks and inline code | ARPANET Plex Mono | |
| Footnotes | PDS italic Charter 10pt | |
| Marginalia | PDS italic Charter 10pt | |
| Quoted blocks / pull quotes | PDS | |
| Long URLs in PDS body | PDS | Underlined; color optional, not load-bearing |
| Long URLs in ARPANET body | ARPANET | Underlined Plex Mono |
| Math and equations | ARPANET Plex Mono | Chapter-prefixed numbering |
| Images and photographs | Not permitted in v0.2 | Neither source register has a native treatment. Revisit in v0.3 if Phase 2 requires. |
| Video, audio, embedded media | Not permitted in v0.2 | Revisit. |
| Appendix front matter | PDS report convention | |
| Glossary entries | PDS | Foreign-script terms use Noto Sans JP |
| Index | PDS | |
| Table of contents | PDS | Dotted leaders; right-aligned chapter-prefixed page numbers |
| Error states, empty states, 404 | PDS narrative + ARPANET caveat strip | See §Web Register |
| Print stylesheet (`@media print`) | Preserves register distinction via frame, caption, and caveat; color becomes optional-decorative | |

**Any Phase 3 surface not in this table requires a ruling before use.** See §Governance.

---

## Integration Points

Some surfaces are genuinely hybrid: the data is geographic (suggesting PDS map styling) but the argument is industrial-topological (suggesting ARPANET logical-map discipline). MechaPDS handles hybrid cases in three configurations.

### 1. ARPANET-primary with PDS assist
Example: the industrial-base geographic map. Use ARPANET register for all typography, legend, caveats, and node symbols. Use PDS map conventions for the geographic substrate (accurate Census TopoJSON via John Quincy Adams, simplified coastlines, Water Blue fills at low saturation permitted on the substrate only). The PDS contribution is substrate; all foreground content is ARPANET.

### 2. PDS-primary with ARPANET stamp
Example: the project cover. Full PDS report-cover treatment (Charter display type, em-dash rule) with an ARPANET sub-block at the base of the page (Plex Mono Regular, centered, report number + date). The ARPANET sub-block is a period citation, not a dual register.

### 3. PDS-primary with embedded ARPANET figure
Example: a narrative page containing a readiness matrix. The page is PDS throughout. The embedded ARPANET figure sits in a thin black frame (0.5 pt Ink Black border, Paper White interior, 14 pt internal padding minimum) with a PDS italic caption below. The frame is the seam.

**No other hybrid configurations are permitted in v0.2.** New hybrid cases become surface errors → spec amendment per §Governance.

---

## Typefaces & Licensing

### Decision (v0.2): Charter as working PDS face; Plantin aspirational

Plantin is Monotype-licensed and requires Adobe Fonts for web delivery — a served-domain requirement incompatible with the project's "no backend, static site" posture. **MechaPDS adopts Charter** (Matthew Carter, 1987) as the working PDS face. Charter is freely web-licensable (Bitstream Charter distribution; IBM Charter distribution) and has the structural properties Plantin was chosen for (robust, slightly condensed, institutional) without the licensing problem.

Plantin remains aspirational. If the project acquires Adobe Fonts or a Monotype web license in Phase 3, the MechaPDS face switches to Plantin with no other change. The CSS fallback ladder is: `'Plantin', 'Charter', 'Source Serif 4', Georgia, serif`.

**Source Serif 4** (Adobe, 2014/2021) is added as the third fallback. Not period-accurate but freely web-licensed. Authorized as fallback only; if Charter is unavailable, a small banner notes the document is rendering in a degraded-typeface state.

### IBM Plex Mono

SIL OFL, freely licensed. Self-hosted via WOFF2 subset or served from `fonts.googleapis.com`. Regular (400) on artifact surfaces; Medium (500) on chrome only.

### Font-loading policy

- WOFF2 preferred.
- `font-display: swap` — no FOIT.
- Fallback chain: `'Charter', 'Source Serif 4', Georgia, serif` and `'IBM Plex Mono', Consolas, monospace`.
- Face load failure surfaces a banner: `(MECHAPDS RENDERING IN FALLBACK TYPE.)` — the honesty condition applies to the system itself.

---

## Color

- **Default: monochrome.** Ink Black on Newsprint (PDS) or Paper White (ARPANET).
- **Spot color on PDS surfaces only.** Industrial Red, Utility Blue, Safety Yellow, Technical Green per parent PDS. One accent per page section maximum.
- **Monochrome on ARPANET surfaces.** Ink Black only.
- **Color-pair rule:** no information encoded by color alone. Every color signal is paired with at least one non-color cue.
- **Grayscale reproduction:** every artifact must remain legible in grayscale print. Verified before publication.
- **Paper White vs. Newsprint as register signal** (addressing v0.1 ambiguity): PDS pages and PDS figure interiors use Newsprint (`#F5F2E8`). ARPANET pages and embedded ARPANET figure interiors use Paper White (`#FDFCF9`). This is a register signal — do not mix.

---

## Typography (detail)

### PDS
- Body: Charter Regular, 12pt minimum, 1.5 line-height, justified in formal documents, left-aligned for dashboards.
- Headings: Charter Bold per PDS type scale (30/24/19/15/12pt).
- Data: Plex Mono Regular 10pt minimum in tables.
- Italic: captions, running-head document titles, body emphasis.

### ARPANET
- All text: Plex Mono Regular 12pt minimum (up from v0.1's 11pt — accessibility floor). 1.5 line-height.
- ALL CAPS reserved for: section titles, parenthesized caveats, figure titles, table column headers, legend entries.
- Title Case for subsection headings.
- Sentence case for body text.
- Italic: site-name-equivalent labels only (Rule 3, first-class).
- No bold, no underline (except URLs), no color.

### Seam mechanics

Embedded ARPANET figures within PDS pages:
- **Frame:** 0.5 pt Ink Black border, four sides closed.
- **Interior background:** Paper White (`#FDFCF9`).
- **Internal padding:** 14 pt minimum all sides; 22 pt preferred horizontal.
- **External margin:** 24 pt minimum above and below within PDS page flow.
- **Column behavior:** an embedded figure spans all columns or occupies a single column's full width. Partial-column figures not permitted.
- **Page break:** figures do not break across pages. Oversize figures are split with continuation notation (`Figure II-3, continued`) or the page breaks above.
- **Caption:** PDS italic Charter 10pt, below the frame, left-aligned.

### Chrome exception

The Design Language Preview and other documentation pages may use Plex Mono Medium (500) for preview-panel labels, tab titles, skip links, and build metadata only. Chrome is not artifact content and does not count against the typography lock.

---

## Figure Conventions

### Figure numbering (locked in v0.2)

**Per-register, per-chapter, with chapter prefix.**

- PDS figures: `Figure II-3 — Short Title` (em-dash, Charter italic).
- PDS tables: `TABLE II-3.—SHORT TITLE` (em-dash, Charter Bold).
- ARPANET figures: `Figure II-3 -- SHORT TITLE` (double-hyphen, Plex Mono).
- ARPANET tables embedded inside figures inherit the figure's number.

Every figure on every artifact carries a number. No untitled figures.

### Figure extraction rule

Every ARPANET figure's bounding box contains, within itself (not in sibling DOM or surrounding chrome):
- Figure number.
- Figure title (ALL CAPS, centered above figure body).
- Figure caption with at least one uncertainty/scope caveat.
- Source citation in ARPANET form: `(SOURCE: Author, Title, Year, p. #.)`.

This ensures register distinction and honesty substrate survive screenshot, slide, and grayscale reproduction.

### Geographic maps

**Tooling:** John Quincy Adams with bespoke SVG overlay for BBN-specific glyphs.

*(The v0.1 claim "Henry Gannett with `--basemap none` and a custom MAP_CONFIG; no new tooling needed" was factually wrong. Henry Gannett is a MapLibre-based interactive slippy-map tool; it cannot produce static BBN-style plates. Corrected in v0.2.)*

JQA produces self-contained static SVG via Census-based TopoJSON (`us-states-10m.json`, `us-counties-10m.json`). The bespoke SVG overlay adds BBN-specific node shapes, cluster ellipses, radial labels, zigzag links, and the caveat block. The overlay is hand-authored SVG composited onto the JQA substrate.

Node grammar:
- `●` filled circle for primary / tier-1 facility.
- `Ⓣ` circled-T for government facility or tier-1 alternative.
- `◻` square for tier-2 supplier.
- `▲` triangle for replicated-redundant / cluster anchor.
- Cluster ellipses enclose dense regions; labels radiate outward.
- Zigzag for classified, off-continent, or over-water links.

Legend bottom-left, terse, ARPANET typography. Caveat block in ALL CAPS parenthesized below the map. Source citation below the caveat.

### Logical maps

Node grammar:
- Boxed squares with **domain labels** (PROP, STRU, POWR, SENS, C2, ARMT) for primary subsystems. *Not* literal "IMP" / "TIP" — those are BBN-program-specific nouns; using them for non-networking subjects reads as pastiche (addressed in v0.2 following Phase 1 review).
- Triangles for replicated-redundant subsystems.
- Ellipses (sparse density) or rectangles (mid/dense density) for components.
- Orthogonal links preferred.
- Zigzag for high-latency or pilot-in-the-loop signal links.
- Italic Plex Mono for site-name-equivalent subsystem labels.

**Honesty pre-check (Rule 2) applies before any logical map publishes.**

### Density scaling

| Component count | Density point | Host shape | Precedent |
|---|---|---|---|
| ≤ 24 | Sparse-architectural | Ellipse | BBN April 1971 – March 1972 |
| 25–60 | Mid-density | Rectangle | BBN November 1974 – January 1975 |
| 61+ | Dense-crowded | Rectangle | BBN March 1977 |

Grammar is stable across the range; only density scales with component count. A primary map at 24 components and a per-subsystem map at 60 components may use different density points within the same chapter — this is correct use, not drift.

### Data figures

**Line charts:** framed axis box, no internal gridlines (ARPANET register). Single-line preferred. Log scale where appropriate. Decade tick labels. Double-hyphen em-dash substitute in captions.

**Bar charts:** horizontal for categorical, vertical for time series. Solid Ink Black fill, 0.5 pt stroke. Zero baseline (never truncated; if truncated, state explicitly). Direct-labeled values at bar end / top. Frame axis box. No internal gridlines.

**Measurement-legibility carve-out:** multi-track time series or scatter plots, where reading a specific value is load-bearing, route to the PDS register (where horizontal-only Gray 15 gridlines are permitted per parent PDS). This is register selection by chart function, not rule conflict.

**Tables as argument:** PDS em-dash title, Plex Mono right-aligned numerals, heavy rule above totals row, Chicago NB source citation below.

### Source citations on every figure

**No figure, map, table, or chart lacks a source citation.** Chicago Manual of Style 18th edition Notes-Bibliography system:

- PDS surfaces: italic Charter, below the caption.
- ARPANET surfaces: parenthesized inline, flush-left, Plex Mono: `(SOURCE: Author, *Title* (Place: Publisher, Year), p. #.)`

Placeholder figures may use `(SOURCE: PLACEHOLDER — TO BE FILLED FROM PHASE 2 RESEARCH.)` in the ARPANET form or the PDS italic equivalent. Placeholder citations are counted as uncertainty flags and do not exempt the figure from §Governance review.

---

## Web Register

MechaPDS Phase 3 ships as an interactive static website. The print posture of both source registers does not cover interactive surfaces; this section is the ruleset for them.

### Responsive behavior

- **Desktop (≥1024px):** canonical register rendering.
- **Tablet (768–1023px):** PDS narrative reflows at full width; ARPANET figures maintain width with horizontal scroll permitted.
- **Phone (≤767px):** ARPANET monospace matrices collapse to stacked card views (each matrix row = one card with label as bold Plex Mono heading and column values as `Label: value` lines). Original matrix accessible via "View as table" expanding horizontal scroll. Logical maps scale via SVG viewBox; below 400px a fallback message displays. Geographic maps scale similarly.
- **Print stylesheet (`@media print`):** forces light background, monochrome (color decorative-only), preserves register frames, forces page breaks above figures, hides interactive controls.

### Interactive states

- **Hover on PDS surfaces:** subtle underline intensifies; cursor becomes pointer.
- **Hover on ARPANET surfaces:** bracket treatment inverts (`[label]` → `〉label〈`).
- **Focus:** 2 pt Ink Black outline. Never color-only. Visible on all interactive elements.
- **Active:** briefly inverted color (black background, Paper White text) for 100 ms. Linear easing only.
- **Disabled:** 50% opacity plus explicit disabled-label note. Never color-only.

### Keyboard traversal

- All interactive elements reachable via Tab.
- Logical-map and geographic-map nodes keyboard-focusable in reading order.
- Arrow keys pan/zoom maps; `+` / `-` zoom; `0` resets.
- `Esc` closes any open tooltip or inspector.
- Skip-link at page top jumps to main content.

### URL as citation anchor

Every section and every figure has a stable URL fragment (`#fig-II-3`, `#section-1-2`). URLs are intended to be cited. No URL-hash rewriting.

### Tooltip typography

Tooltips over ARPANET surfaces use ARPANET register. Tooltips over PDS surfaces use PDS register. Tooltips carry their own uncertainty caveats where applicable.

### Dark mode

**Refused.** MechaPDS is a literal revival of black-ink-on-light-paper institutional print. No period precedent exists for dark mode. Users with dark-mode preference may apply browser-level invert filters at their discretion; MechaPDS does not serve a dark-mode stylesheet.

### Reduced motion

All animations are disabled when `prefers-reduced-motion: reduce` is set. MechaPDS has minimal motion anyway (no transitions beyond the 100 ms active-state invert).

### Loading, empty, error states

- **Loading:** ARPANET caveat strip at the top of the affected surface: `(LOADING. …)`. No spinner animation.
- **Empty state:** PDS narrative explaining why, with an ARPANET caveat strip confirming the data is known-absent, not merely missing.
- **Error state:** PDS narrative describing the error, with an ARPANET caveat strip naming the failure mode: `(DATA FETCH FAILED. CONTENT UNAVAILABLE.)`.
- **404:** PDS narrative with an ARPANET stamp-block at the bottom noting the missing URL and the suggested entry point.

---

## Accessibility

Accessibility is a binding commitment, not a compliance afterthought. The project ships to a public audience including policymakers, journalists, and the assistive-technology community.

### Contrast

- Body text: 4.5:1 minimum (WCAG AA normal text).
- Large text (≥18pt or ≥14pt bold): 3:1 minimum (WCAG AA large text).
- **Warm Gray (`#9C9788`) on Newsprint (`#F5F2E8`) computes to ~2.6:1 and FAILS AA.** Forbidden for body text. Use Warm Gray only for ornamental rules or Paper White ground with bold weight.
- Substitute: **Gray 70 (`#5C5C5C`) on Newsprint** computes to ~6.5:1 and passes. Use for captions and secondary text.

### Font-size floors

- PDS body: 12 pt minimum.
- ARPANET body: 12 pt minimum (up from v0.1's 11 pt).
- Captions: 10 pt minimum, paired with bold or italic treatment.
- Legend glyphs: 10 pt minimum, paired with labels.

### ALL CAPS scope

ALL CAPS restricted to: section and figure titles; parenthesized caveats (ARPANET); table column headers; legend entries. **Forbidden for running body text.** Body copy is sentence case.

### SVG metadata

Every `<svg>` figure carries:
- `role="img"`.
- `<title>` — concise name of the figure.
- `<desc>` — sentence or two describing what the figure shows.
- `aria-labelledby` pointing to the title.
- `aria-describedby` pointing to the desc.

Every interactive SVG node carries:
- `tabindex="0"`.
- `aria-label` with the node's meaning in plain language.
- Keyboard activation handlers for Enter and Space.

### Accessible alternates for data figures

Every readiness matrix, bar chart, and quantitative table offers a "View as accessible HTML table" control that re-renders the data as a standard `<table>` with proper `<thead>`, `<tbody>`, `<th scope>` attributes, keyboard-accessible and screen-reader-tested.

### Color-pair rule (restating Rule 4)

No information encoded by color alone. Every color signal paired with ≥1 non-color cue (glyph, label, weight, bracket, position). WCAG 1.4.1 verified before publication.

### Testing

- Automated: axe-core or equivalent on all Phase 3 pages.
- Manual: keyboard-only traversal of every interactive surface; screen-reader smoke test (VoiceOver macOS, NVDA Windows) on cover, narrative, one logical map, one geographic map, one readiness matrix.
- Contrast ratios verified with WebAIM contrast checker.

---

## Sourced Claims

Every load-bearing period-revival claim in MechaPDS cites its source.

| Claim | Source | Citation |
|---|---|---|
| Italic site-name labels in BBN logical maps (from December 1970) | BBN Completion Report, Appendix B | Heart et al. (1981), Appendix B. Italic site labels visible on the first published logical map (Dec 1970) and every subsequent logical map through March 1977. **[Corrected from v0.1 claim of "1971+" — italic convention is present from the inaugural logical map.]** |
| Host-ellipse convention (pre-Nov 1974) → host-rectangle convention (Nov 1974 onward) | BBN Completion Report, Appendix B | Heart et al. (1981), Appendix B, comparing logical maps of June 1974 (ellipses) and November 1974 (rectangles). |
| "No claim can be made for its accuracy" disclaimer idiom (1976 onward) | BBN Completion Report, Appendix B | Heart et al. (1981), logical maps July 1976 and later. |
| Double-hyphen em-dash substitute in figure captions | BBN Completion Report Ch. III §1.4.5.1 | Heart et al. (1981), p. III-75: "Figure 4 -- Growth in Average Host Internode Traffic." |
| Nodalism critique and honesty condition | Fidler & Currie (2015) | Fidler and Currie, "The Production and Interpretation of ARPANET Maps," *IEEE Annals of the History of Computing* 37, no. 1 (Jan–Mar 2015): 44–55. Nodalism on p. 45; flat-subnet condition on p. 52. |
| Chicago NB citation standard | Borges skill requirement | `/Users/emmetpenney/Skills/Borges.md` §Citation Format, citing *Chicago Manual of Style*, 18th ed., Notes-Bibliography system. Parent PDS does not explicitly name a citation standard; MechaPDS extends to Chicago NB per Borges convention. |
| Monochrome-by-constraint aesthetic heritage | Parent PDS §Design Philosophy | `PENNEY-DESIGN-SYSTEM.md`, Core Principles §5 ("Functional Restraint"). |

Any future claim requires addition to this table or removal from the spec.

---

## Governance

### Owner
Emmet Penney is the owner of MechaPDS through v1.0. Amendments require owner approval.

### Versioning (SemVer-like)
- **Patch (v0.1 → v0.1.1):** spelling, clarification, non-substantive tightening.
- **Minor (v0.1 → v0.2):** new sections, new rules, new domains, closed-list additions. Requires documented surface error or review finding.
- **Major (v0.x → v1.0):** declared when Phase 3 Chapter I publishes without unresolved surface errors.

### Change control

1. A **surface error** is logged when a Phase 2 or Phase 3 artifact cannot be produced without a ruling not in MechaPDS.
2. A surface error is **promoted to a rule change** when it recurs across ≥2 artifacts, or ≥1 artifact where design review finds it likely to recur.
3. Rule changes are proposed via a written **ADR (Architecture Decision Record)** in `~/Gundam Level Zero/adr/NNNN-title.md`:
   - Context — what situation forced the decision.
   - Options considered.
   - Decision.
   - Consequences.
   - Date + version that adopts it.
4. The owner approves or rejects the ADR. Approved ADRs merge into the spec at the next version bump.

### Surface-error log
Running log at `~/Gundam Level Zero/surface-errors.md`. Fields: date, artifact, error description, resolution (ad hoc / promoted to ADR), ADR link if promoted.

### Review cadence
- Inquisitor (`--agents 3-1-1 --lens design-system`) before each minor version bump.
- Ignatius after each phase closes.
- The v0.1 → v0.2 transition driven by Phase 1 Inquisitor review on 2026-04-18 is the reference case.

---

## Resolved Questions

1. **Density point** — Scales with component count per §Density Scaling (updated from v0.1's single-register lock).
2. **Label treatment** — IBM Plex Mono. Confirmed.
3. **Phase 3 cover** — Yes. PDS-primary with ARPANET stamp sub-block. Confirmed.
4. **Skill invocation** — John Quincy Adams + bespoke SVG overlay for BBN-specific glyphs. Henry Gannett reserved for interactive non-BBN-styled maps if any Phase 3 surface requires them. Corrected from v0.1.
5. **Integration Points section** — Written (§Integration Points). Resolved.
6. **Governance model** — Defined (§Governance). Resolved.
7. **Accessibility** — Binding commitment (§Accessibility). Resolved.
8. **Typefaces** — Charter as working PDS face; Plex Mono as ARPANET face. Plantin aspirational pending Adobe Fonts licensing.

---

## Naming

System name **MechaPDS** locked 2026-04-18. Spelling: MechaPDS (no space, capital M, capital PDS). Filenames: `mechapds.md`, `mechapds-*.html`. Constituent systems named as "PDS" and "ARPANET register" when the distinction is load-bearing.

---

## Changelog

### v0.2 — 2026-04-18
Responding to Phase 1 Inquisitor review (18 MUST FIX + 5 CONSIDER findings).

**New sections:**
- §Definitions (artifact, surface, register, plate, seam, scope).
- §Posture — Why This Pairing (justifies PDS × ARPANET against near-miss traditions).
- §Integration Points (three hybrid configurations).
- §Typefaces & Licensing (Charter working face; Plantin aspirational).
- §Web Register (responsive, interactive, print, dark-mode, reduced-motion rules).
- §Accessibility (WCAG AA commitments; contrast, font-size floors, ARIA, alternates).
- §Sourced Claims (citation table).
- §Governance (owner, SemVer, ADR format, surface-error log).
- §Changelog (this section).

**Rule changes:**
- Rule 3 typography lock: italic for site-name labels promoted from exception to first-class rule; chrome exception for Plex Mono Medium documented; closed-list policy for future additions.
- Rule 4 uncertainty: cross-register leakage forbidden; color-pair rule; PDS red decorative-only.
- Density scaling: component-count-based (replaces v0.1 single-register lock).

**Corrections:**
- Henry Gannett → John Quincy Adams + bespoke SVG overlay for BBN-style static maps. (v0.1 claimed Henry Gannett could produce these; factually wrong — Henry Gannett is MapLibre-interactive.)
- Italic site-name labels: present from December 1970, not "1971+".
- Plantin → Charter as working face (licensing incompatible with no-backend static site).
- ARPANET body size: 11pt → 12pt minimum (accessibility floor).
- "IMP" / "TIP" literal labels on Heavyarms subsystems → domain labels (PROP, STRU, POWR, SENS, C2, ARMT). Literal BBN acronyms reserved for direct ARPANET-subject contexts only.

**Expanded coverage:**
- Domain assignment adds: navigation UI, form controls, hover/focus/active states, code blocks, footnotes, marginalia, pull quotes, long URLs, math, TOC, glossary, index, error/empty/404 states, print stylesheet.
- Seam mechanics specified (frame, padding, column behavior, page-break).
- Figure extraction rule (every ARPANET figure carries number/title/caption/caveat/citation within its bounding box).
- Figure numbering locked (per-register, per-chapter, chapter-prefixed).

**Retained from v0.1:**
- Register-split-by-surface posture.
- Fidler honesty condition (now operational).
- Figure-as-quotation seam logic.
- Cover PDS-primary / ARPANET-subblock period citation.
- "Silence implies full coverage" uncertainty pledge.
- Refusal of hand-lettered typeface revival.
- Dark-mode refusal (now with explicit rationale).

### v0.1 — 2026-04-18
Initial draft. See archived Phase 1 Inquisitor review at `phase-1-inquisitor-review-2026-04-18.md`.
