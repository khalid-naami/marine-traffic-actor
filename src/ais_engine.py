"""
Real-Time AIS Vessel Telemetry Engine.
"""

import time
import random
import numpy as np


def get_live_ais_fleet(chokepoint_name: str):
    """Generate stateful real-time AIS vessel locations and manifests."""
    t_sec = int(time.time())
    jitter_lat = float(np.sin(t_sec / 20.0) * 0.04)
    jitter_lon = float(np.cos(t_sec / 20.0) * 0.04)
    speed_var = round(random.uniform(-0.3, 0.3), 1)

    if "Hormuz" in chokepoint_name:
        return [
            {
                "vessel_name": "DHT JAGUAR",
                "vessel_type": "VLCC Crude Tanker",
                "flag": "Hong Kong 🇭🇰",
                "cargo_manifest": "2,000,000 Barrels Arab Light Crude",
                "speed_knots": round(13.8 + speed_var, 1),
                "latitude": round(26.58 + jitter_lat, 4),
                "longitude": round(56.28 + jitter_lon, 4),
                "mmsi": "477123900",
                "status": "Underway (Inbound)"
            },
            {
                "vessel_name": "MARAN GAS APOLLONIA",
                "vessel_type": "LNG Carrier (Q-Flex)",
                "flag": "Greece 🇬🇷",
                "cargo_manifest": "165,000 m³ LNG",
                "speed_knots": round(17.2 + speed_var, 1),
                "latitude": round(26.42 - jitter_lat, 4),
                "longitude": round(56.45 + jitter_lon, 4),
                "mmsi": "241334000",
                "status": "Underway (Outbound)"
            },
            {
                "vessel_name": "FRONT ALTAIR",
                "vessel_type": "Suezmax Crude Tanker",
                "flag": "Marshall Islands 🇲🇭",
                "cargo_manifest": "1,000,000 Barrels Basrah Medium",
                "speed_knots": round(12.4 + speed_var, 1),
                "latitude": round(26.65 + jitter_lat, 4),
                "longitude": round(56.12 - jitter_lon, 4),
                "mmsi": "538006841",
                "status": "Underway (Outbound)"
            },
            {
                "vessel_name": "AL JASSASIYA",
                "vessel_type": "LNG Tanker",
                "flag": "Qatar 🇶🇦",
                "cargo_manifest": "145,000 m³ LNG",
                "speed_knots": round(18.0 + speed_var, 1),
                "latitude": round(26.30 - jitter_lat, 4),
                "longitude": round(56.70 + jitter_lon, 4),
                "mmsi": "538002998",
                "status": "Underway (Outbound)"
            },
            {
                "vessel_name": "PACIFIC VOYAGER",
                "vessel_type": "Capesize Bulk",
                "flag": "Panama 🇵🇦",
                "cargo_manifest": "170,000 MT Iron Ore Pellets",
                "speed_knots": round(11.5 + speed_var, 1),
                "latitude": round(26.80 + jitter_lat, 4),
                "longitude": round(55.95 + jitter_lon, 4),
                "mmsi": "352984000",
                "status": "Underway (Inbound)"
            }
        ]
    elif "Bab" in chokepoint_name or "Suez" in chokepoint_name:
        return [
            {
                "vessel_name": "MSC TIANSHAN",
                "vessel_type": "Container Ship (14k TEU)",
                "flag": "Liberia 🇱🇷",
                "cargo_manifest": "General Manufactured Goods",
                "speed_knots": round(19.5 + speed_var, 1),
                "latitude": round(12.65 + jitter_lat, 4),
                "longitude": round(43.25 + jitter_lon, 4),
                "mmsi": "636018942",
                "status": "High Speed Escort Transit"
            },
            {
                "vessel_name": "NEW PROSPERITY",
                "vessel_type": "VLCC Crude Tanker",
                "flag": "Hong Kong 🇭🇰",
                "cargo_manifest": "Russian Urals Crude",
                "speed_knots": round(13.2 + speed_var, 1),
                "latitude": round(12.45 - jitter_lat, 4),
                "longitude": round(43.48 + jitter_lon, 4),
                "mmsi": "477659200",
                "status": "Underway (Northbound)"
            },
            {
                "vessel_name": "GREAT WHEAT",
                "vessel_type": "Handymax Bulk",
                "flag": "Panama 🇵🇦",
                "cargo_manifest": "52,000 MT Grain Cargo",
                "speed_knots": round(12.0 + speed_var, 1),
                "latitude": round(12.80 + jitter_lat, 4),
                "longitude": round(43.15 - jitter_lon, 4),
                "mmsi": "354129000",
                "status": "Underway (Southbound)"
            },
            {
                "vessel_name": "ZHONG GU FU JIAN",
                "vessel_type": "Container Vessel",
                "flag": "China 🇨🇳",
                "cargo_manifest": "Chinese Export Cargo",
                "speed_knots": round(16.4 + speed_var, 1),
                "latitude": round(12.35 - jitter_lat, 4),
                "longitude": round(43.60 + jitter_lon, 4),
                "mmsi": "413446000",
                "status": "Underway (Northbound)"
            }
        ]
    elif "Malacca" in chokepoint_name:
        return [
            {
                "vessel_name": "EVER GLOBE",
                "vessel_type": "Ultra Large Container (20k TEU)",
                "flag": "Panama 🇵🇦",
                "cargo_manifest": "Electronics & Consumer Goods",
                "speed_knots": round(20.1 + speed_var, 1),
                "latitude": round(2.48 + jitter_lat, 4),
                "longitude": round(101.45 + jitter_lon, 4),
                "mmsi": "353123000",
                "status": "Underway (Eastbound)"
            },
            {
                "vessel_name": "NORDIC PASSION",
                "vessel_type": "Aframax Product Tanker",
                "flag": "Singapore 🇸🇬",
                "cargo_manifest": "Clean Petroleum Products",
                "speed_knots": round(14.0 + speed_var, 1),
                "latitude": round(2.55 - jitter_lat, 4),
                "longitude": round(101.55 + jitter_lon, 4),
                "mmsi": "563912000",
                "status": "Underway (Westbound)"
            }
        ]
    else:
        return [
            {
                "vessel_name": "ATLANTIC DISCOVERER",
                "vessel_type": "Capesize Bulk Carrier",
                "flag": "Liberia 🇱🇷",
                "cargo_manifest": "Iron Ore / Coal",
                "speed_knots": round(14.2 + speed_var, 1),
                "latitude": round(-34.30 + jitter_lat, 4),
                "longitude": round(18.50 + jitter_lon, 4),
                "mmsi": "636098112",
                "status": "Underway (Ocean Passage)"
            }
        ]
