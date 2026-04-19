# Gundam Level Zero

**Argument:** Building Gundams is possible, and America should build them. The project identifies the threshold at which Gundam production moves from speculative to buildable — "Gundam Level Zero" — and maps what it will take to reach it.

**Reference spec:** Trowa Barton's Heavyarms Custom (*Gundam Wing: Endless Waltz*). Treated as a design brief, not a frame-perfect blueprint.

**Audience:** General public. Credibility earned with defense analysts.

**Publication format:** Interactive static website (MapLibre / D3 / embedded graphics). No backend.

---

## Research Questions

**Phase 1 — Aesthetic.** How do ARPANET's visual conventions (BBN topology/logical maps, completion-report document design, teletype-era typography) integrate with the Penney Design System without either system subordinating the other? Output: "MechaPDS" governing Phase 3 visual decisions.

**Phase 2 — Feasibility.** What must change in the US industrial base, supply chain, force structure, and doctrinal posture for a Heavyarms-class platform to be buildable? Where are the real gating bottlenecks?

Seven research tracks:
- T1 Propulsion & power (actuators, hydraulics, power-to-weight, storage)
- T2 Structure & materials (frame metallurgy, composite armor, survivability)
- T3 Mobility & balance (legged locomotion at 20–40 tons, terrain reasoning)
- T4 Sensing & autonomy (pilot-assist, sensor fusion, EW resilience)
- T5 Armament integration (Heavyarms loadout: projectile, beam-analogue, melee)
- T6 Industrial base & supply chain (specialty alloys, rare earths, machine-tool capacity, heavy-fab throughput)
- T7 Doctrinal & tactical utility (urban combat, littoral/island chains, cost-per-kill vs. UGV/drone alternatives)

**Phase 3 — The Product.** Three-layer static site: The Case (narrative argument, sourced), The Spec (Heavyarms exploded-diagram, per-subsystem Source Card links), Gundam Level Zero (gating-technology readiness display with explicit threshold logic).

---

## Confirmed Assumptions (2026-04-18)

1. The argument is specifically American.
2. Heavyarms Custom is a design brief, not a frame-perfect blueprint.
3. "Gundam Level Zero" is a threshold, not an endpoint.
4. Audience is the general public; credibility earned with defense analysts.
5. Final product is an interactive static site; Henry Gannett / John Quincy Adams scaffolds Phase 3 maps.
6. ARPANET aesthetic = literal revival, same posture as PDS's 1940s trade-journal revival.

---

## Reference Sources

- **DARC** (defenseanalyses.org) — canonical source for Phase 2 T7 (modern combat theater, UGV/drone economics, force-structure evolution). Reference-tier.
- **Foundation for American Innovation (FAI)** (thefai.org) — canonical source list for Phase 2 across tracks, especially T6 (industrial base, supply chain) and T7 (doctrine, acquisition reform). Reference-tier.

---

## Terminology

- **Current name:** Department of War (DoW). The executive agency formerly known as the Department of Defense was renamed in 2025.
- **Historical sources:** most of the authoritative documentary record uses "Department of Defense" (DoD), including the BBN ARPANET Completion Report (1978/1981), all DoD-published reports through 2025, and peer-reviewed research citing those documents. This is expected, not a mistake.
- **Public-facing project text (Phase 3 narrative, figure titles, captions):** "Department of War" / "DoW" / "Secretary of War."
- **Source Cards and citations:** use whatever the source itself uses. Do not retroactively rename. If a 2020 CRS report says "Department of Defense," the Source Card says "Department of Defense." The honesty condition applies: the register of the source is preserved, even when the name has since changed.
- **Phase 3 public surfaces** may carry a brief footnote on first DoD citation: "*Cited as 'Department of Defense' in the source; currently the Department of War.*"

---

## Skill Chain

Borges (research) → Ultan (sourcing rigor) → Inquisitor (phase-boundary review) → Ignatius (after-action, at phase close).

Source Cards saved to `~/.claude/borges/source-cards/gundam-level-zero/`.

---

## Status

- **Phase 1 — IN PROGRESS (started 2026-04-18)**
  - Fidler & Currie (2015) — analyzed, Source Card saved.
  - BBN Completion Report (1978/1981) — partial read (~56 of 208 pp, focused on visual conventions), Source Card saved.
  - Synthesis memo drafted.
  - **MechaPDS** v0.2 (integrated design language; name locked 2026-04-18). File: `mechapds.md`.
  - v0.1 drafted; resolved four user questions; produced Design Language Preview mockup.
  - Phase 1 Inquisitor review completed 2026-04-18 (`--agents 3-1-1 --lens design-system`): 27 findings → 18 MUST FIX, 5 CONSIDER, 4 DISMISSED. Full review at `phase-1-inquisitor-review-2026-04-18.md`.
  - **v0.2 drafted** in response to Inquisitor review: adds §Definitions, §Integration Points, §Typefaces & Licensing, §Web Register, §Accessibility, §Sourced Claims, §Governance, §Changelog. Corrects Henry Gannett → John Quincy Adams + bespoke SVG overlay. Switches working face Plantin → Charter. Operationalizes honesty condition. Fixes v0.1 mockup. ADR 0001 logs the v0.1 → v0.2 decision.
  - Governance scaffolding created: `adr/` directory, `surface-errors.md` log.
  - Pending: Ignatius after-action review to close Phase 1.
- Phase 2 — Not started.
- Phase 3 — Not started.
