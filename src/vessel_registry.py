"""
Global Commercial Fleet Registry & Technical Specifications Directory (IMO / ITU / Equasis).
"""


def get_global_vessel_registry(search_query: str = None):
    """Retrieve full commercial vessel profiles, specs, propulsion, and ownership."""
    vessels = [
        {
            "vessel_name": "MSC IRINA",
            "imo": "9929429",
            "mmsi": "636021961",
            "call_sign": "5LHA8",
            "flag": "Liberia 🇱🇷",
            "vessel_type": "Ultra Large Container Vessel (Megamax-24)",
            "capacity": "24,346 TEU",
            "deadweight_dwt": 240000,
            "gross_tonnage": 236184,
            "year_built": 2023,
            "shipyard": "Yangzijiang Shipbuilding (China)",
            "dimensions": {
                "loa_meters": 399.9,
                "beam_meters": 61.3,
                "max_draft_meters": 16.5
            },
            "propulsion": {
                "engine_model": "MAN B&W 11G95ME-C9.5",
                "power_kw": 66650,
                "fuel_grade": "VLSFO / Ready LNG Dual-Fuel",
                "service_speed_knots": 22.5,
                "daily_fuel_consumption_mt": 82.0
            },
            "commercial_operator": "MSC Mediterranean Shipping Company (Switzerland)",
            "beneficial_owner": "Aponte Family Holding (Geneva, CH)",
            "pi_insurance_club": "UK P&I Club / Steamship Mutual",
            "war_risk_routing_status": "Rerouted via Cape of Good Hope (2026 Routine)"
        },
        {
            "vessel_name": "EVER GIVEN",
            "imo": "9811000",
            "mmsi": "353136000",
            "call_sign": "H3RC",
            "flag": "Panama 🇵🇦",
            "vessel_type": "Ultra Large Container Vessel (Golden-Class)",
            "capacity": "20,124 TEU",
            "deadweight_dwt": 199629,
            "gross_tonnage": 219079,
            "year_built": 2018,
            "shipyard": "Imabari Shipbuilding (Japan)",
            "dimensions": {
                "loa_meters": 399.9,
                "beam_meters": 58.8,
                "max_draft_meters": 16.0
            },
            "propulsion": {
                "engine_model": "Mitsui-MAN B&W 11G95ME-C9.2",
                "power_kw": 59300,
                "fuel_grade": "VLSFO / MGO",
                "service_speed_knots": 22.8,
                "daily_fuel_consumption_mt": 76.0
            },
            "commercial_operator": "Evergreen Marine Corp (Taiwan)",
            "beneficial_owner": "Shoei Kisen Kaisha (Imabari, Japan)",
            "pi_insurance_club": "UK P&I Club",
            "war_risk_routing_status": "Rerouted via Cape of Good Hope"
        },
        {
            "vessel_name": "CMA CGM JACQUES SAADE",
            "imo": "9839179",
            "mmsi": "228386700",
            "call_sign": "FMWK",
            "flag": "France 🇫🇷",
            "vessel_type": "Ultra Large Container Vessel (LNG Megamax)",
            "capacity": "23,112 TEU",
            "deadweight_dwt": 220000,
            "gross_tonnage": 236583,
            "year_built": 2020,
            "shipyard": "CSSC Jiangnan Shipyard (China)",
            "dimensions": {
                "loa_meters": 400.0,
                "beam_meters": 61.3,
                "max_draft_meters": 16.0
            },
            "propulsion": {
                "engine_model": "WinGD 12X92DF Dual-Fuel",
                "power_kw": 63840,
                "fuel_grade": "Liquefied Natural Gas (LNG) / MGO",
                "service_speed_knots": 22.0,
                "daily_fuel_consumption_mt": 68.0
            },
            "commercial_operator": "CMA CGM Group (Marseille, France)",
            "beneficial_owner": "Saadé Family (France)",
            "pi_insurance_club": "Britannia P&I / Gard",
            "war_risk_routing_status": "Rerouted via Cape of Good Hope"
        },
        {
            "vessel_name": "FRONTLINE ALTAIR",
            "imo": "9745902",
            "mmsi": "538006841",
            "call_sign": "V7XF4",
            "flag": "Marshall Islands 🇲🇭",
            "vessel_type": "VLCC Very Large Crude Carrier",
            "capacity": "2,050,000 Barrels Crude",
            "deadweight_dwt": 298450,
            "gross_tonnage": 156800,
            "year_built": 2016,
            "shipyard": "Hyundai Heavy Industries (South Korea)",
            "dimensions": {
                "loa_meters": 333.0,
                "beam_meters": 60.0,
                "max_draft_meters": 21.5
            },
            "propulsion": {
                "engine_model": "Hyundai-MAN B&W 7G80ME-C9.2",
                "power_kw": 28300,
                "fuel_grade": "VLSFO / High Sulfur Heavy Fuel with Scrubber",
                "service_speed_knots": 15.5,
                "daily_fuel_consumption_mt": 52.0
            },
            "commercial_operator": "Frontline Management AS (Bermuda/Norway)",
            "beneficial_owner": "John Fredriksen Trust (Hemen Holding)",
            "pi_insurance_club": "Gard P&I (Norway)",
            "war_risk_routing_status": "Transiting via Hormuz / Cape Rerouting for Atlantic"
        },
        {
            "vessel_name": "EURONAV OCEANIA",
            "imo": "9246633",
            "mmsi": "205469000",
            "call_sign": "ONET",
            "flag": "Belgium 🇧🇪",
            "vessel_type": "ULCC Ultra Large Crude Carrier",
            "capacity": "3,100,000 Barrels Crude",
            "deadweight_dwt": 441585,
            "gross_tonnage": 234006,
            "year_built": 2003,
            "shipyard": "Daewoo Shipbuilding & Marine Engineering (DSME)",
            "dimensions": {
                "loa_meters": 380.0,
                "beam_meters": 68.0,
                "max_draft_meters": 24.5
            },
            "propulsion": {
                "engine_model": "Sulzer 9RTA84T-D",
                "power_kw": 36900,
                "fuel_grade": "VLSFO / HFO",
                "service_speed_knots": 16.0,
                "daily_fuel_consumption_mt": 95.0
            },
            "commercial_operator": "Euronav NV / CMB.TECH (Antwerp, Belgium)",
            "beneficial_owner": "Saverys Family / CMB Group",
            "pi_insurance_club": "Standard Club / NorthStandard",
            "war_risk_routing_status": "Floating Storage / Global Deepwater Transit"
        },
        {
            "vessel_name": "MOZAH (Q-MAX)",
            "imo": "9337755",
            "mmsi": "538003114",
            "call_sign": "V7PJ6",
            "flag": "Marshall Islands 🇲🇭",
            "vessel_type": "Q-Max Ultra Large LNG Carrier",
            "capacity": "266,000 m³ Cryogenic LNG",
            "deadweight_dwt": 125600,
            "gross_tonnage": 163922,
            "year_built": 2008,
            "shipyard": "Samsung Heavy Industries (South Korea)",
            "dimensions": {
                "loa_meters": 345.0,
                "beam_meters": 53.8,
                "max_draft_meters": 12.0
            },
            "propulsion": {
                "engine_model": "Twin MAN B&W 7S70ME-C with Reliquefaction",
                "power_kw": 43500,
                "fuel_grade": "LNG Boil-Off Gas (BOG) / MGO",
                "service_speed_knots": 19.5,
                "daily_fuel_consumption_mt": 62.0
            },
            "commercial_operator": "QatarEnergy LNG / Nakilat (Qatar)",
            "beneficial_owner": "State of Qatar Sovereign Marine Assets",
            "pi_insurance_club": "UK P&I Club / Britannia",
            "war_risk_routing_status": "Rerouted via Cape of Good Hope for Europe Deliveries"
        },
        {
            "vessel_name": "BERGE BULKER (VALEMAX)",
            "imo": "9595163",
            "mmsi": "235088211",
            "call_sign": "2EXP7",
            "flag": "United Kingdom 🇬🇧",
            "vessel_type": "Valemax Very Large Ore Carrier (VLOC)",
            "capacity": "400,000 Metric Tons Iron Ore",
            "deadweight_dwt": 388000,
            "gross_tonnage": 198000,
            "year_built": 2012,
            "shipyard": "Bohai Shipbuilding Heavy Industry (China)",
            "dimensions": {
                "loa_meters": 362.0,
                "beam_meters": 65.0,
                "max_draft_meters": 23.0
            },
            "propulsion": {
                "engine_model": "MAN B&W 7S80ME-C9 with BAR Rotor Sails",
                "power_kw": 27000,
                "fuel_grade": "VLSFO / Wind-Assist Hybrid",
                "service_speed_knots": 14.5,
                "daily_fuel_consumption_mt": 44.0
            },
            "commercial_operator": "Berge Bulk Maritime (Singapore / UK)",
            "beneficial_owner": "Bergesen Family Holdings",
            "pi_insurance_club": "Skuld P&I Club (Norway)",
            "war_risk_routing_status": "Direct Ocean Passage (Tubarao to Qingdao)"
        },
        {
            "vessel_name": "MADRID MAERSK",
            "imo": "9778791",
            "mmsi": "219836000",
            "call_sign": "OXVP2",
            "flag": "Denmark 🇩🇰",
            "vessel_type": "Ultra Large Container Vessel (Triple-E 2nd Gen)",
            "capacity": "20,568 TEU",
            "deadweight_dwt": 206000,
            "gross_tonnage": 214286,
            "year_built": 2017,
            "shipyard": "Daewoo Shipbuilding & Marine Engineering (DSME)",
            "dimensions": {
                "loa_meters": 399.0,
                "beam_meters": 58.6,
                "max_draft_meters": 16.5
            },
            "propulsion": {
                "engine_model": "Twin MAN B&W 7G80ME-C9.5",
                "power_kw": 59000,
                "fuel_grade": "VLSFO / Bio-Bunker Ready",
                "service_speed_knots": 22.0,
                "daily_fuel_consumption_mt": 72.0
            },
            "commercial_operator": "A.P. Moller - Maersk (Copenhagen, Denmark)",
            "beneficial_owner": "A.P. Møller Holding A/S",
            "pi_insurance_club": "Britannia P&I Club",
            "war_risk_routing_status": "Rerouted via Cape of Good Hope"
        }
    ]

    if search_query:
        q = search_query.strip().lower()
        return [
            v for v in vessels if
            q in v['vessel_name'].lower() or
            q in v['imo'] or
            q in v['flag'].lower() or
            q in v['commercial_operator'].lower() or
            q in v['beneficial_owner'].lower()
        ]
    return vessels
