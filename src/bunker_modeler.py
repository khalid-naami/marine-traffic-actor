"""
Marine Bunker Fuel Futures & Geopolitical Rerouting Freight Modeler.
"""

import numpy as np
import yfinance as yf


def get_live_brent_price() -> float:
    """Fetch live Brent Crude benchmark."""
    try:
        brent = yf.Ticker("BZ=F")
        hist = brent.history(period="5d")
        if not hist.empty:
            return round(float(hist.iloc[-1]['Close']), 2)
    except Exception:
        pass
    return 88.50


def calculate_bunker_hub_matrix(brent_price: float):
    """Synthesize global 5-hub marine bunker prices with forward curves."""
    hubs = {
        "Singapore (Hub 1)": {
            "vlsfo_spot": round(brent_price * 6.95 + 45.0, 2),
            "mgo_spot": round(brent_price * 8.50 + 75.0, 2)
        },
        "Rotterdam (Hub 2)": {
            "vlsfo_spot": round(brent_price * 6.75 + 35.0, 2),
            "mgo_spot": round(brent_price * 8.30 + 65.0, 2)
        },
        "Gibraltar (Hub 3)": {
            "vlsfo_spot": round(brent_price * 7.10 + 40.0, 2),
            "mgo_spot": round(brent_price * 8.65 + 80.0, 2)
        },
        "Balboa / Panama (Hub 4)": {
            "vlsfo_spot": round(brent_price * 7.20 + 55.0, 2),
            "mgo_spot": round(brent_price * 8.80 + 90.0, 2)
        },
        "Houston (Hub 5)": {
            "vlsfo_spot": round(brent_price * 6.65 + 30.0, 2),
            "mgo_spot": round(brent_price * 8.20 + 60.0, 2)
        }
    }

    forward_periods = ["Spot", "M1 (+30D)", "M2 (+60D)", "M3 (+90D)", "M4 (+120D)", "M5 (+150D)", "M6 (+180D)"]
    structured_matrix = []
    for hub, prices in hubs.items():
        v_spot = prices["vlsfo_spot"]
        m_spot = prices["mgo_spot"]
        structured_matrix.append({
            "hub": hub,
            "vlsfo_spot_price_usd_per_mt": v_spot,
            "mgo_spot_price_usd_per_mt": m_spot,
            "vlsfo_forward_curve_usd_per_mt": {p: round(v_spot * (1 - 0.008 * i), 2) for i, p in enumerate(forward_periods)},
            "mgo_forward_curve_usd_per_mt": {p: round(m_spot * (1 - 0.008 * i), 2) for i, p in enumerate(forward_periods)}
        })
    return structured_matrix, hubs


def simulate_rerouting_freight_economics(brent_price: float):
    """Model the operational and fuel cost shock of geopolitical route diversions."""
    _, hubs = calculate_bunker_hub_matrix(brent_price)
    avg_vlsfo = float(np.mean([h["vlsfo_spot"] for h in hubs.values()]))
    avg_mgo = float(np.mean([h["mgo_spot"] for h in hubs.values()]))

    scenarios = [
        {
            "scenario_name": "Red Sea / Suez Canal Avoidance (Cape of Good Hope Detour)",
            "extra_nautical_miles": 3500.0,
            "vessel_class_simulations": [
                {
                    "vessel_class": "Mega Container Ship (20,000 TEU)",
                    "speed_knots": 14.0,
                    "fuel_grade": "VLSFO",
                    "daily_burn_mt": 75.0,
                    "extra_transit_days": round(3500.0 / (14.0 * 24.0), 1),
                    "extra_fuel_consumed_mt": round((3500.0 / (14.0 * 24.0)) * 75.0, 1),
                    "extra_fuel_cost_usd": round((3500.0 / (14.0 * 24.0)) * 75.0 * avg_vlsfo, 2),
                    "fleet_10_vessels_monthly_cost_shock_usd": round(((3500.0 / (14.0 * 24.0)) * 75.0 * avg_vlsfo) * 10, 2)
                },
                {
                    "vessel_class": "Panamax Crude / Product Tanker (75,000 DWT)",
                    "speed_knots": 13.0,
                    "fuel_grade": "MGO",
                    "daily_burn_mt": 40.0,
                    "extra_transit_days": round(3500.0 / (13.0 * 24.0), 1),
                    "extra_fuel_consumed_mt": round((3500.0 / (13.0 * 24.0)) * 40.0, 1),
                    "extra_fuel_cost_usd": round((3500.0 / (13.0 * 24.0)) * 40.0 * avg_mgo, 2),
                    "fleet_10_vessels_monthly_cost_shock_usd": round(((3500.0 / (13.0 * 24.0)) * 40.0 * avg_mgo) * 10, 2)
                },
                {
                    "vessel_class": "Capesize Bulk Carrier (180,000 DWT)",
                    "speed_knots": 12.0,
                    "fuel_grade": "VLSFO",
                    "daily_burn_mt": 32.0,
                    "extra_transit_days": round(3500.0 / (12.0 * 24.0), 1),
                    "extra_fuel_consumed_mt": round((3500.0 / (12.0 * 24.0)) * 32.0, 1),
                    "extra_fuel_cost_usd": round((3500.0 / (12.0 * 24.0)) * 32.0 * avg_vlsfo, 2),
                    "fleet_10_vessels_monthly_cost_shock_usd": round(((3500.0 / (12.0 * 24.0)) * 32.0 * avg_vlsfo) * 10, 2)
                }
            ]
        },
        {
            "scenario_name": "Panama Canal Drought Draft Restriction (Cape Horn / Magellan Detour)",
            "extra_nautical_miles": 8000.0,
            "vessel_class_simulations": [
                {
                    "vessel_class": "Neopanamax Container (15,000 TEU)",
                    "speed_knots": 15.0,
                    "fuel_grade": "VLSFO",
                    "daily_burn_mt": 65.0,
                    "extra_transit_days": round(8000.0 / (15.0 * 24.0), 1),
                    "extra_fuel_consumed_mt": round((8000.0 / (15.0 * 24.0)) * 65.0, 1),
                    "extra_fuel_cost_usd": round((8000.0 / (15.0 * 24.0)) * 65.0 * avg_vlsfo, 2),
                    "fleet_10_vessels_monthly_cost_shock_usd": round(((8000.0 / (15.0 * 24.0)) * 65.0 * avg_vlsfo) * 10, 2)
                },
                {
                    "vessel_class": "Panamax Tanker (75,000 DWT)",
                    "speed_knots": 13.0,
                    "fuel_grade": "MGO",
                    "daily_burn_mt": 40.0,
                    "extra_transit_days": round(8000.0 / (13.0 * 24.0), 1),
                    "extra_fuel_consumed_mt": round((8000.0 / (13.0 * 24.0)) * 40.0, 1),
                    "extra_fuel_cost_usd": round((8000.0 / (13.0 * 24.0)) * 40.0 * avg_mgo, 2),
                    "fleet_10_vessels_monthly_cost_shock_usd": round(((8000.0 / (13.0 * 24.0)) * 40.0 * avg_mgo) * 10, 2)
                }
            ]
        }
    ]
    return scenarios
