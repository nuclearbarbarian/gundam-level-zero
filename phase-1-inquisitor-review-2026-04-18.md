# Phase 1 Inquisitor Review — MechaPDS v0.1

**Date:** 2026-04-18
**Configuration:** `--agents 3-1-1 --lens design-system`
**Subject:** `/Users/emmetpenney/Gundam Level Zero/mechapds.md`
**Total findings:** 27 (4 Critical, 18 Major, 5 Minor from Critics)

## Verdict Summary

- **MUST FIX (18):** C1, C2, C3, C4, C5, C6, C8, C10, C11, C12, C13, C14, C17, C18, C20, C22, C24, C26
- **CONSIDER (5):** C9, C15, C16, C23, C27
- **DISMISSED (4):** C7, C19, C21, C25

## Must-Fix Actionable List (before Phase 2)

1. **Accessibility pass [C12][C13]** — Fix Warm Gray–on–Newsprint contrast (currently ~3.1:1; fails WCAG AA). Pair color-only signals with a second non-color cue. Add ARIA metadata and accessible alternates to SVG figures. Bound ALL CAPS to labels/caveats, not running text.
2. **Correct the Henry Gannett error [C14]** — Henry Gannett is MapLibre-interactive and cannot render BBN-style static plates. Swap to **John Quincy Adams + bespoke SVG overlay**. Update `mechapds.md` §Figure Conventions accordingly.
3. **Resolve Plantin [C1]** — Either license Plantin (Adobe Fonts / Monotype) or amend spec to permit Source Serif 4 as web-delivery face. Stop the spec/mockup mismatch.
4. **Write the "Integration Points" section [C8]** — Currently referenced in the Domain Assignment table but does not exist.
5. **Governance [C18]** — Add owner, change-control procedure, version log, criterion for surface-error → rule change.
6. **Mockup-to-spec correction pass [C3][C10][C15][C24]** — Remove Plex Mono 500; fix Plate 3 `IMP`/`TIP` literal labels; fix Plate 6 `[GAP]` cross-register misuse; fix Plate 2 inline `[GAP]` tokens; fix Plates 3–6 missing Chicago NB citations; resolve em-dash vs. `--` inconsistency.
7. **Web register [C4][C5][C6]** — Add section covering hover/focus/keyboard traversal, responsive behavior (esp. monospace ARPANET surfaces), nav/forms/footnotes/error-states/print-CSS coverage.
8. **Operationalize the honesty condition [C2]** — Add a falsifiability procedure: "before publishing a flat-node figure, enumerate ranking dimensions the depicted entities vary on; if any is load-bearing, use hierarchical grammar."
9. **Seam mechanics [C11]** — Specify embedded-figure container rules, padding minima, column and page-break behavior.
10. **Figure-extraction rule [C17]** — Every ARPANET figure must carry its register signal within its bounding box so grayscale/slide extraction preserves distinction.
11. **Source the load-bearing claims [C20]** — Cite page numbers for "1971+" italic convention and for "Chicago NB" format.
12. **Figure numbering [C22]** — Lock scheme (recommend per-register + chapter-prefixed), fix mockup drift.
13. **Citations on all mockup plates [C26]** — Rule 5 compliance.

## Consider List (discretionary)

- **[C9]** Promote italic-site-labels from carve-out to first-class rule.
- **[C15]** Pastiche risk — use domain labels (PROP, STRU, etc.) not literal `IMP`/`TIP`.
- **[C16]** Add "why this pairing" paragraph to preempt Swiss-modernism / DEC-manuals objection.
- **[C23]** Document Paper White vs. Newsprint as explicit register signal, or stop using it as one.
- **[C27]** Add TOC plate + one subsystem-specific logical map to preview as scale coverage.

## Dismissed

- **[C7]** Artifact-scoped Rule 1 vs. embedding Rule 7 — no contradiction; define "artifact" in the spec.
- **[C19]** "No internal gridlines" is register-scoped; doesn't conflict with parent PDS.
- **[C21]** English-Latin scope is deliberate; document it explicitly.
- **[C25]** Density scales with component count (1971 ≤24, mid-70s 25–60, 1977 appendix).

## Overall Assessment (Referee)

> The work is fundamentally sound as a framework. The register-split discipline, the honesty condition imported from Fidler as a binding non-negotiable, the figure-as-quotation seam logic, the "silence implies full coverage" uncertainty pledge, the decision to refuse hand-lettered typeface revival — these are real intellectual wins. MechaPDS has a defensible core thesis that no one in the critics' 27 findings actually dismantles. The critics won on execution, not on concept.
>
> But v0.1 is a framework shipped alongside a mockup that violates the framework, with a broken cross-reference, an untrue tooling claim, an unfalsifiable core rule, a WCAG-fail color combination, and no governance model.
>
> **The single most important thing to address before v0.2 is accessibility (C12/C13).** Every other issue is craft, governance, or spec hygiene — fixable on any timeline. Accessibility is a public-facing-site-for-policymakers project that is actively planning to ship Warm Gray on Newsprint and color-only uncertainty encoding. This is the fix that cannot wait for v0.3.
>
> Second-most: fix the Henry Gannett claim (C14). Third: write the missing "Integration Points" section (C8).
>
> The project's aesthetic thesis is strong enough that v0.2 should be a tightening pass, not a rewrite.

## Strengths the Critics Missed (from Defender)

1. Register-split-by-surface is the only posture that can carry two literal revivals simultaneously — most integration attempts merge-and-compromise.
2. Importing Fidler's critical-cartography rule into a commercial design system is a rare and intellectually serious move; disarms the BBN-pastiche critique the defense-analyst audience would raise.
3. Figure-as-quotation mental model at the seam is elegant and carries the credibility of art-history reproduction practice.
4. "Silence implies full coverage" is a falsifiable uncertainty pledge — rare in design systems.
5. Cover PDS-primary / ARPANET-subblock is a strong period citation mirroring actual period practice.
6. Resolved Questions section is a governance primitive most v0.1 specs lack.
7. Refusing hand-lettered typeface revival resists the classic literal-revival trap (mistaking surface for signal).
