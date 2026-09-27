# 🚢 Global Maritime Traffic & Supply Chain Intelligence Actor

**Real-time IMF/UN PortWatch satellite transits, AIS fleet telemetry, 2026 UK naval security attack ledgers (UKMTO, Ambrey London, MAIB, Lloyd's JWC), global commercial IMO vessel registries, and marine bunker freight rerouting simulations.**

---

## 🌟 What Does This Actor Do?

This actor extracts, aggregates, and computes institutional-grade intelligence across the global maritime supply chain:

1. **Strategic Chokepoints Satellite Telemetry (PortWatch UN/IMF):**
   - Annual transit volumes, deadweight capacity, vessel breakdown (Container, Crude Tanker, Bulk Carrier, General Cargo, Ro-Ro).
   - Dominant cargo streams, geopolitical risk rankings, and Lloyd's Joint War Committee (JWC) listed area classifications.
2. **180-Day Daily Transit Time Series & Disruption Diagnostics:**
   - Day-over-day vessel counts and capacity series.
   - Algorithmic 30-day disruption diagnostic metrics detecting supply chain contraction or expansion.
3. **Live AIS Transiting Fleet Radar:**
   - Active vessels underway in strategic waterways with speed, GPS coordinates, flag, reported cargo manifest, and MMSI identifiers.
4. **2026 Maritime Security & UK Naval Threat Ledger:**
   - Documented 2026 attacks, ballistic missiles, explosive USV boats, and armed boardings with official references from **UKMTO (UK Royal Navy)**, **Ambrey Intelligence London**, **UK MAIB**, and **Lloyd's JWC War Risk Ratings (JWLA)**.
5. **Global Commercial Fleet Registry & Ownership Directory (IMO/ITU/Equasis):**
   - Technical specifications, engine models, fuel grades, service speed, daily fuel consumption (MT/day), commercial operator, beneficial owner, P&I Club, and War Risk routing statuses.
6. **Marine Bunker Futures & Geopolitical Rerouting Freight Modeler:**
   - Live Brent crude benchmark (`BZ=F`) and 5-Hub bunker price matrix (Singapore, Rotterdam, Gibraltar, Balboa, Houston) across VLSFO & MGO with forward curves.
   - Rerouting simulation calculating extra nautical miles, days at sea, fuel burned, and per-voyage/fleet cost shocks when diverting around Africa or South America.

---

## 📥 Input Configuration

| Field | Type | Default | Description |
| :--- | :--- | :--- | :--- |
| `chokepoints` | Array | `["ALL"]` | List of passages to analyze (`ALL`, `Bab el-Mandeb Strait`, `Suez Canal`, `Strait of Hormuz`, `Strait of Malacca`, `Panama Canal`, `Strait of Gibraltar`, etc.). |
| `daysBack` | Integer | `180` | Time series lookback for daily transits and 30-day disruption diagnostics. |
| `includeLiveAIS` | Boolean | `true` | Include active AIS vessels in regional waterways. |
| `includeSecurityLedger` | Boolean | `true` | Include 2026 UK naval security attacks and UKMTO warning bulletins. |
| `includeVesselRegistry` | Boolean | `true` | Include global commercial vessel specifications and ownership chains. |
| `includeBunkerEconomics` | Boolean | `true` | Include 5-hub marine bunker price matrix and rerouting freight simulations. |
| `vesselSearchFilter` | String | `""` | Optional search filter for specific ship name, IMO, or operator. |

---

## 📤 Output Dataset Format

The actor outputs clean, structured JSON objects with a `recordType` field:

### 1. Strategic Chokepoint Telemetry (`chokepoint_telemetry`)
```json
{
  "recordType": "chokepoint_telemetry",
  "chokepointName": "Bab el-Mandeb Strait",
  "timestamp": "2026-09-27T10:00:00Z",
  "data": {
    "port_id": "choke003",
    "annual_vessel_volume": 21850,
    "fleet_distribution": {
      "containers": 8900,
      "oil_tankers": 5700,
      "dry_bulk": 4800
    },
    "security_risk_status": "Critical (Security Zone 2026)",
    "lloyds_jwc_war_zone": "JWLA-032 (High Risk War Zone - 1.0% Surcharge)",
    "supply_chain_diagnostics": {
      "baseline_180d_avg_daily_transits": 48.5,
      "recent_30d_avg_daily_transits": 28.2,
      "flow_deviation_pct": -41.86,
      "supply_chain_state": "CONTRACTION / REROUTING PRESSURE"
    }
  }
}
```

### 2. 2026 UK Maritime Security Incident (`security_incident_2026`)
```json
{
  "recordType": "security_incident_2026",
  "chokepointName": "Bab el-Mandeb / Southern Red Sea",
  "timestamp": "2026-09-27T10:00:00Z",
  "data": {
    "incident_id": "INC-2026-0924-01",
    "date": "2026-09-24",
    "vessel_name": "MT Blue Ocean Star",
    "imo": "9488392",
    "flag": "Liberia 🇱🇷",
    "vessel_type": "Aframax Crude Oil Tanker",
    "attack_type": "USV Explosive Boat Swarm Attack",
    "uk_reporting_authority": "UKMTO (Royal Navy) & Ambrey London",
    "advisory_ref": "UKMTO Incident 142/2026",
    "lloyds_jwc_rating": "JWLA-032 (High War Risk - Level 5)",
    "summary": "Targeted 45 nm SW of Mokha by two uncrewed surface vessels (USVs). Verified by Ambrey London: Private security repelled craft."
  }
}
```

### 3. Vessel Registry & Ownership Dossier (`vessel_dossier`)
```json
{
  "recordType": "vessel_dossier",
  "chokepointName": "Rerouted via Cape of Good Hope (2026 Routine)",
  "timestamp": "2026-09-27T10:00:00Z",
  "data": {
    "vessel_name": "MSC IRINA",
    "imo": "9929429",
    "mmsi": "636021961",
    "flag": "Liberia 🇱🇷",
    "vessel_type": "Ultra Large Container Vessel (Megamax-24)",
    "capacity": "24,346 TEU",
    "deadweight_dwt": 240000,
    "dimensions": { "loa_meters": 399.9, "beam_meters": 61.3, "max_draft_meters": 16.5 },
    "commercial_operator": "MSC Mediterranean Shipping Company (Switzerland)",
    "beneficial_owner": "Aponte Family Holding (Geneva, CH)",
    "pi_insurance_club": "UK P&I Club / Steamship Mutual"
  }
}
```

---

## ⚡ Integration & API Usage

You can run this Actor via the Apify API, Python SDK, or JavaScript SDK:

```python
from apify_client import ApifyClient

client = ApifyClient("<YOUR_APIFY_API_TOKEN>")

run = client.actor("your-username/marine-traffic-actor").call(run_input={
    "chokepoints": ["ALL"],
    "daysBack": 180,
    "includeLiveAIS": True,
    "includeSecurityLedger": True,
    "includeVesselRegistry": True,
    "includeBunkerEconomics": True
})

for item in client.dataset(run["defaultDatasetId"]).iterate_items():
    print(item)
```
