#!/usr/bin/env python3
"""Build country-status GeoJSON layers + firm pin GeoJSON for the
Allied Industrial Integration map (Gannett).

Reads ne_countries_raw.geojson, filters by ISO_A2/A3 into four
categorical groups per ADR 0002, writes one GeoJSON per group.
Also writes firm pins from Japan + Korea Step 4 source cards.

Hackathon MVP — JP + KR researched only; DE/TW/NL/CH gap; AUKUS extension;
PRC excluded per NSIBR.
"""
import json
import os

HERE = os.path.dirname(os.path.abspath(__file__))
SRC = os.path.join(HERE, "ne_countries_raw.geojson")

# ADR 0002 partner classification
RESEARCHED   = {"USA", "JPN", "KOR"}
PENDING      = {"DEU", "TWN", "NLD", "CHE"}
AUKUS_EXT    = {"GBR", "AUS", "CAN"}
EXCLUDED     = {"CHN"}

with open(SRC) as f:
    raw = json.load(f)

def make_collection(features):
    return {"type": "FeatureCollection", "features": features}

def filter_by_a3(codes, status, label):
    out = []
    for ft in raw["features"]:
        props = ft["properties"]
        a3 = props.get("ADM0_A3") or props.get("SOV_A3")
        if a3 in codes:
            out.append({
                "type": "Feature",
                "geometry": ft["geometry"],
                "properties": {
                    "name": props.get("NAME") or props.get("SOVEREIGNT"),
                    "iso_a3": a3,
                    "status": status,
                    "status_label": label,
                }
            })
    return out

researched = filter_by_a3(RESEARCHED, "RESEARCHED", "Allied — researched (cards in hand)")
pending    = filter_by_a3(PENDING,    "PENDING",    "Allied — Step 4 pending")
aukus      = filter_by_a3(AUKUS_EXT,  "AUKUS",      "AUKUS §1080 extension")
excluded   = filter_by_a3(EXCLUDED,   "EXCLUDED",   "EXCLUDED per NSIBR / DFARS 2021-D015")

# Write four polygon layer files
for name, feats in [
    ("countries_researched", researched),
    ("countries_pending",    pending),
    ("countries_aukus",      aukus),
    ("countries_excluded",   excluded),
]:
    with open(os.path.join(HERE, f"{name}.geojson"), "w") as f:
        json.dump(make_collection(feats), f)
    print(f"wrote {name}.geojson — {len(feats)} feature(s)")

# Firm pins — sourced directly from Step 4 Japan + Korea memory cards
# All coordinates from public sources; flagged [GEO APPROX] where corp HQ is used as proxy
firms = [
    # ---- JAPAN — aerospace-Ti + heavy industrial supplier roster (Step 4 JP card)
    {"lat": 34.7333, "lon": 135.4167, "label": "Osaka Titanium Technologies", "country": "Japan",
     "subsystem": "Aerospace Ti sponge", "card": "GLZ-T6-STEP4-JP-METI-DID17",
     "tier": "PRIMARY", "note": "Amagasaki — duopoly with Toho Ti"},
    {"lat": 35.3296, "lon": 139.4081, "label": "Toho Titanium", "country": "Japan",
     "subsystem": "Aerospace Ti sponge", "card": "GLZ-T6-STEP4-JP-METI-DID17",
     "tier": "PRIMARY", "note": "Chigasaki, Kanagawa"},
    {"lat": 34.6901, "lon": 135.1955, "label": "Kobe Steel (Kobelco)", "country": "Japan",
     "subsystem": "Specialty steels + Ti mill", "card": "GLZ-T6-STEP4-JP-METI-DID17",
     "tier": "PRIMARY", "note": "Kobe HQ"},
    {"lat": 35.6762, "lon": 139.6503, "label": "Proterial (fmr Hitachi Metals)", "country": "Japan",
     "subsystem": "High-grade alloys + Ni superalloys", "card": "GLZ-T6-STEP4-JP-METI-DID17",
     "tier": "PRIMARY", "note": "Tokyo HQ — divested by Hitachi 2023"},
    {"lat": 35.1815, "lon": 136.9066, "label": "Daido Steel", "country": "Japan",
     "subsystem": "Specialty steel + forgings", "card": "GLZ-T6-STEP4-JP-METI-DID17",
     "tier": "PRIMARY", "note": "Nagoya"},
    {"lat": 35.6557, "lon": 139.7945, "label": "IHI Corporation", "country": "Japan",
     "subsystem": "Aero-engines + heavy fab", "card": "GLZ-T6-STEP4-JP-MOD-DBP",
     "tier": "PRIMARY", "note": "Toyosu, Tokyo"},
    {"lat": 35.6762, "lon": 139.7600, "label": "Mitsubishi Heavy Industries (MHI)", "country": "Japan",
     "subsystem": "Heavy fab + GCAP prime", "card": "GLZ-T6-STEP4-JP-MOD-DBP",
     "tier": "PRIMARY", "note": "Tokyo HQ — GCAP+F-X anchor"},

    # ---- KOREA — Step 4 KR card
    {"lat": 35.2278, "lon": 128.6817, "label": "Hanwha Aerospace", "country": "South Korea",
     "subsystem": "K9 howitzer + propulsion", "card": "GLZ-T6-STEP4-KR-CSIS-DAPA-2024",
     "tier": "PRIMARY", "note": "Changwon — K9 production"},
    {"lat": 34.8775, "lon": 128.7000, "label": "Hanwha Ocean", "country": "South Korea",
     "subsystem": "Submarines + naval fab", "card": "GLZ-T6-STEP4-KR-2024-2plus2",
     "tier": "PRIMARY", "note": "Geoje/Okpo — fmr DSME"},
    {"lat": 35.5384, "lon": 129.3114, "label": "HD Hyundai Heavy Industries", "country": "South Korea",
     "subsystem": "Naval shipbuilding + MRO", "card": "GLZ-T6-STEP4-KR-2024-2plus2",
     "tier": "PRIMARY", "note": "Ulsan — USN MRO certifying yard"},
    {"lat": 37.4290, "lon": 126.9890, "label": "DAPA HQ", "country": "South Korea",
     "subsystem": "Acquisition authority", "card": "GLZ-T6-STEP4-KR-MND-WP-2022",
     "tier": "GOVT", "note": "Gwacheon — Defense Acquisition Program Administration"},

    # ---- KOREA-CAPITAL-INTO-US-DIB (FDI architectural finding, ADR 0002 update needed)
    {"lat": 39.9020, "lon": -75.1430, "label": "Hanwha Philly Shipyard", "country": "South Korea (FDI in US)",
     "subsystem": "Shipbuilding capacity (US soil)", "card": "GLZ-T6-STEP4-KR-HANWHA-PHILLY",
     "tier": "PRIMARY", "note": "Philadelphia — Korean capital into US DIB; $150B MASGA"},

    # ---- US — government anchor pins for context
    {"lat": 38.8841, "lon": -77.1075, "label": "DARPA", "country": "United States",
     "subsystem": "Innovation funding", "card": "PROJECT REFERENCE",
     "tier": "GOVT", "note": "Arlington, VA"},
    {"lat": 38.8719, "lon": -77.0563, "label": "Department of War HQ", "country": "United States",
     "subsystem": "Acquisition authority", "card": "PROJECT REFERENCE",
     "tier": "GOVT", "note": "The Pentagon — fmr DoD"},

    # ---- ADVERSARY-VOICE / EXCLUSION-CONTEXT PINS
    {"lat": 48.3705, "lon": 10.8978, "label": "KUKA AG", "country": "Germany",
     "subsystem": "Industrial robotics — PRC-CAPTURED", "card": "GLZ-T6-AV-USCC-2025-CH6",
     "tier": "EXCLUDED-CAPTURED", "note": "Augsburg — Midea (PRC) acquired 2017; complicates DE roster"},
    {"lat": 22.5429, "lon": 114.0596, "label": "DJI", "country": "China",
     "subsystem": "70% global drone market", "card": "GLZ-T6-STEP4-JP-ANCHOR",
     "tier": "EXCLUDED", "note": "Shenzhen — exclusion floor for baseline UAS pooling"},
]

firm_features = []
for f in firms:
    firm_features.append({
        "type": "Feature",
        "geometry": {"type": "Point", "coordinates": [f["lon"], f["lat"]]},
        "properties": {
            "label": f["label"],
            "country": f["country"],
            "subsystem": f["subsystem"],
            "card": f["card"],
            "tier": f["tier"],
            "note": f["note"],
        }
    })

with open(os.path.join(HERE, "firms.geojson"), "w") as f:
    json.dump(make_collection(firm_features), f, indent=2)
print(f"wrote firms.geojson — {len(firm_features)} feature(s)")
