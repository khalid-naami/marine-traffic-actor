"""
Global Maritime Traffic & Supply Chain Intelligence Apify Actor.
Orchestrates PortWatch Satellite Feeds, Live AIS Telemetry, 2026 UK Naval Threat Ledgers,
Global IMO Vessel Registries, and Bunker Fuel Rerouting Scenario Economics.
"""

import sys
from datetime import datetime
import pytz
from apify import Actor

from .portwatch import get_all_chokepoints, get_chokepoint_timeseries
from .ais_engine import get_live_ais_fleet
from .security_ledger import get_maritime_incidents_2026
from .vessel_registry import get_global_vessel_registry
from .bunker_modeler import get_live_brent_price, calculate_bunker_hub_matrix, simulate_rerouting_freight_economics


async def main() -> None:
    async with Actor:
        # Read and validate input configuration
        actor_input = await Actor.get_input() or {}
        chokepoint_targets = actor_input.get("chokepoints", ["ALL"])
        days_back = int(actor_input.get("daysBack", 180))
        include_live_ais = actor_input.get("includeLiveAIS", True)
        include_security = actor_input.get("includeSecurityLedger", True)
        include_registry = actor_input.get("includeVesselRegistry", True)
        include_bunker = actor_input.get("includeBunkerEconomics", True)
        vessel_filter = actor_input.get("vesselSearchFilter", "")

        utc_now = datetime.now(pytz.utc).isoformat()
        Actor.log.info("⚓ Starting Global Maritime Traffic & Supply Chain Intelligence Actor...")
        Actor.log.info(f"Target Passages: {chokepoint_targets} | Days: {days_back} | Live AIS: {include_live_ais} | Security: {include_security}")

        # Fetch Master Chokepoints
        all_chokepoints = get_all_chokepoints()
        selected_chokepoints = all_chokepoints
        if "ALL" not in chokepoint_targets and len(chokepoint_targets) > 0:
            selected_chokepoints = [c for c in all_chokepoints if c['portname'] in chokepoint_targets]

        pushed_records_count = 0

        # ── 1. CHOKEPOINTS TELEMETRY & 180D TIME SERIES ──────────────────────
        Actor.log.info(f"Processing {len(selected_chokepoints)} strategic maritime passages...")
        for chk in selected_chokepoints:
            port_name = chk['portname']
            port_id = chk['portid']
            Actor.log.info(f"Analyzing {port_name} ({port_id})...")

            timeseries, diagnostics = get_chokepoint_timeseries(port_id, days_back=days_back)

            record_chokepoint = {
                "recordType": "chokepoint_telemetry",
                "chokepointName": port_name,
                "timestamp": utc_now,
                "data": {
                    "port_id": port_id,
                    "latitude": chk.get("lat"),
                    "longitude": chk.get("lon"),
                    "annual_vessel_volume": chk.get("vessel_count_total"),
                    "fleet_distribution": {
                        "containers": chk.get("vessel_count_container"),
                        "oil_tankers": chk.get("vessel_count_tanker"),
                        "dry_bulk": chk.get("vessel_count_dry_bulk"),
                        "general_cargo": chk.get("vessel_count_general_cargo"),
                        "roro_vehicles": chk.get("vessel_count_RoRo")
                    },
                    "dominant_cargo_streams": [
                        chk.get("industry_top1"),
                        chk.get("industry_top2"),
                        chk.get("industry_top3")
                    ],
                    "security_risk_status": chk.get("risk_level", "Normal"),
                    "lloyds_jwc_war_zone": chk.get("jwc_zone", "Standard"),
                    "supply_chain_diagnostics": diagnostics,
                    "timeseries_days_count": len(timeseries)
                }
            }
            await Actor.push_data(record_chokepoint)
            pushed_records_count += 1

            # Output individual daily time series if requested
            for ts_point in timeseries:
                await Actor.push_data({
                    "recordType": "daily_transit_point",
                    "chokepointName": port_name,
                    "timestamp": utc_now,
                    "data": ts_point
                })
                pushed_records_count += 1

            # ── 2. LIVE AIS TRANSITING FLEET ─────────────────────────────────
            if include_live_ais:
                ais_fleet = get_live_ais_fleet(port_name)
                for vessel in ais_fleet:
                    await Actor.push_data({
                        "recordType": "live_ais_vessel",
                        "chokepointName": port_name,
                        "timestamp": utc_now,
                        "data": vessel
                    })
                    pushed_records_count += 1

        # ── 3. MARITIME SECURITY & 2026 UK NAVAL INCIDENTS ───────────────────
        if include_security:
            Actor.log.info("Extracting 2026 UK Naval & Maritime Security Incidents Ledger...")
            incidents_2026 = get_maritime_incidents_2026()
            for inc in incidents_2026:
                await Actor.push_data({
                    "recordType": "security_incident_2026",
                    "chokepointName": inc["region"],
                    "timestamp": utc_now,
                    "data": inc
                })
                pushed_records_count += 1

        # ── 4. GLOBAL IMO VESSEL REGISTRY & OWNERSHIP ────────────────────────
        if include_registry:
            Actor.log.info("Extracting Global Commercial Fleet Specification & Ownership Dossiers...")
            fleet_registry = get_global_vessel_registry(vessel_filter)
            for v_dossier in fleet_registry:
                await Actor.push_data({
                    "recordType": "vessel_dossier",
                    "chokepointName": v_dossier["war_risk_routing_status"],
                    "timestamp": utc_now,
                    "data": v_dossier
                })
                pushed_records_count += 1

        # ── 5. MARINE BUNKER FUEL & REROUTING FREIGHT ECONOMICS ──────────────
        if include_bunker:
            Actor.log.info("Calculating Global Bunker Futures & Geopolitical Rerouting Impact...")
            brent_spot = get_live_brent_price()
            bunker_matrix, _ = calculate_bunker_hub_matrix(brent_spot)
            rerouting_models = simulate_rerouting_freight_economics(brent_spot)

            await Actor.push_data({
                "recordType": "bunker_freight_model",
                "chokepointName": "Global Bunker Hubs & Geopolitical Corridors",
                "timestamp": utc_now,
                "data": {
                    "brent_crude_benchmark_usd_per_bbl": brent_spot,
                    "regional_bunker_hub_matrix": bunker_matrix,
                    "rerouting_macro_cost_simulations": rerouting_models
                }
            })
            pushed_records_count += 1

        # Save Executive Summary to Key-Value Store
        exec_summary = {
            "actor_run_timestamp": utc_now,
            "chokepoints_analyzed": len(selected_chokepoints),
            "brent_crude_benchmark_usd": get_live_brent_price(),
            "total_records_pushed": pushed_records_count,
            "status": "SUCCESS"
        }
        await Actor.set_value("OUTPUT_EXECUTIVE_SUMMARY", exec_summary)

        Actor.log.info(f"✅ Maritime Intelligence Actor finished successfully! Total {pushed_records_count} records pushed to Apify Dataset.")


if __name__ == "__main__":
    import asyncio
    asyncio.run(main())
