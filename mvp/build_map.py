#!/usr/bin/env python3
"""Build allied-integration map HTML by populating Henry Gannett's engine
with our ADR 0002 country layers + Step 4 firm pins.

ARPANET register per MechaPDS §Integration Points (line 132-133):
- All typography in Plex Mono (Gannett default fonts will be overridden post-build).
- Basemap = "none" — flat Paper White / Newsprint substrate, no OSM tiles.
"""
import json
import os

HERE = os.path.dirname(os.path.abspath(__file__))
ENGINE = os.path.expanduser("~/Skills/henry-gannett/engine.html")

def load(name):
    with open(os.path.join(HERE, f"{name}.geojson")) as f:
        return json.load(f)

researched = load("countries_researched")
pending    = load("countries_pending")
aukus      = load("countries_aukus")
excluded   = load("countries_excluded")
firms      = load("firms")

# MechaPDS color tokens
INK_BLACK     = "#1A1A1A"
PAPER_WHITE   = "#FDFCF9"
UTILITY_BLUE  = "#2B4B6F"
WARM_GRAY     = "#9C9788"
SAFETY_YELLOW = "#C4A035"
INDUSTRIAL_RED = "#8B2B2B"

CONFIG = {
    "title": "ALLIED INDUSTRIAL INTEGRATION",
    "subtitle": "Heavyarms-class supply chain — baseline partners + AUKUS extension + PRC exclusion",
    "source": "Source: Borges Source Cards, Gundam Level Zero Project (Step 4 Japan + Korea, ADR 0002).",
    "date": "Data as of 2026-04-26 — Hackathon MVP v0.0",
    "basemap": "raster",                  # desaturated OSM — closest to PDS substrate spec
    "center": [25, 60],                   # roughly between US and East Asia
    "zoom": 1.6,
    "layers": [
        # ---- Country status polygons (4 categorical layers, ARPANET monochrome) ----
        {
            "id": "researched",
            "label": "[●] RESEARCHED — cards in hand (US/JP/KR)",
            "type": "polygons",
            "data": researched,
            "fillColor": INK_BLACK,
            "fillOpacity": 0.55,
            "strokeColor": INK_BLACK,
            "strokeWidth": 1.25,
            "visible": True,
            "legendTitle": "RESEARCHED — STEP 4 COMPLETE"
        },
        {
            "id": "pending",
            "label": "[○] PENDING — Step 4 not yet carded (DE/TW/NL/CH)",
            "type": "polygons",
            "data": pending,
            "fillColor": PAPER_WHITE,
            "fillOpacity": 1.0,
            "strokeColor": INK_BLACK,
            "strokeWidth": 1.25,
            "visible": True,
            "legendTitle": "PENDING — STEP 4 GAP"
        },
        {
            "id": "aukus",
            "label": "[◇] AUKUS §1080 EXT (UK/AUS/CA)",
            "type": "polygons",
            "data": aukus,
            "fillColor": WARM_GRAY,
            "fillOpacity": 0.4,
            "strokeColor": INK_BLACK,
            "strokeWidth": 1,
            "visible": True,
            "legendTitle": "AUKUS §1080 NDAA FY24"
        },
        {
            "id": "excluded",
            "label": "[X] EXCLUDED — NSIBR / DFARS 2021-D015 (CN)",
            "type": "polygons",
            "data": excluded,
            "fillColor": INDUSTRIAL_RED,
            "fillOpacity": 0.55,
            "strokeColor": INK_BLACK,
            "strokeWidth": 2,
            "visible": True,
            "legendTitle": "EXCLUDED PER NSIBR"
        },
        # ---- Firm pin layer ----
        {
            "id": "firms",
            "label": "FIRMS — Step 4 carded suppliers + adversary-context",
            "type": "points",
            "data": firms,
            "color": INK_BLACK,
            "radius": 5,
            "strokeColor": INK_BLACK,
            "strokeWidth": 0.75,
            "opacity": 0.9,
            "visible": True,
            "legendTitle": "FIRMS",
            "filter": {"field": "tier", "label": "TIER"}
        }
    ]
}

# Read engine template
with open(ENGINE) as f:
    engine_html = f.read()

# Substitute placeholders
out = engine_html.replace("{{EXPLORER_TITLE}}", "GLZ — Allied Industrial Integration")
out = out.replace("{{EXPLORER_CONFIG_JSON}}", json.dumps(CONFIG))

# ---- MechaPDS typography lock patch ----
# Gannett ships with Source Serif 4 + Playfair Display + Plex Mono.
# MechaPDS §Integration Points: industrial-base map = ARPANET typography (Plex Mono only).
# We override the three CSS custom properties to force Plex Mono everywhere.
patch = """
  /* MechaPDS v0.2 typography lock — ARPANET register (Plex Mono only) */
  --font-serif: 'IBM Plex Mono', Consolas, monospace !important;
  --font-display: 'IBM Plex Mono', Consolas, monospace !important;
  --font-mono: 'IBM Plex Mono', Consolas, monospace !important;
"""
# Inject right before the existing :root closes (find first `}` after `--color-ink`)
marker = "--color-ink: #1A1A1A;"
out = out.replace(marker, marker + patch)

# Title font in Gannett uses display weight; force tracked uppercase per ARPANET convention
out = out.replace(
    ".sidebar-title {",
    ".sidebar-title { text-transform: uppercase; letter-spacing: 0.08em; font-weight: 500; "
)

# Output
with open(os.path.join(HERE, "allied-map.html"), "w") as f:
    f.write(out)

# Note: PBF font glyphs are only needed for Gannett's vector basemap ("light").
# We use "raster" so no fonts/ dir is needed. If you switch back to "light",
# copy ~/Skills/henry-gannett/fonts/output -> mvp/fonts before serving.

print(f"wrote allied-map.html — {len(out)} bytes")
print(f"  layers: {len(CONFIG['layers'])}  ("
      f"researched={len(researched['features'])}, "
      f"pending={len(pending['features'])}, "
      f"aukus={len(aukus['features'])}, "
      f"excluded={len(excluded['features'])}, "
      f"firms={len(firms['features'])})")
