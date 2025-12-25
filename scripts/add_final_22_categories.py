#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Script pour ajouter 22 catégories restantes à ai_knowledge_unified.py
Catégories: Cooling, Monitors, Peripherals, Windows 11, Drivers, Gaming, Networking
"""

import os
import re

def create_categories_code():
    """Génère le code Python pour les 22 nouvelles catégories"""

    categories_code = '''
        # =============================================================================
        # COOLING SOLUTIONS (2 catégories - ~80 conseils)
        # =============================================================================

        # 11. Cooling Air vs AIO
        kb["cooling_air_vs_aio"] = {
            "metadata": {
                "priority": 5,
                "tags": ["cooling", "air", "aio", "hardware"],
                "difficulty": "intermediate",
                "description": "Air cooling vs AIO liquid cooling comparison"
            },
            "tips": [
                {"content": "Noctua NH-D15: Dual tower air cooler 150 euros, 2x 140mm fans, handles i9/R9 at stock, 165W TDP, quieter than most AIOs", "keywords": ["noctua", "nh-d15", "air cooling"], "difficulty": "intermediate", "tags": ["premium"], "related_tools": []},
                {"content": "Arctic Liquid Freezer III 360mm: Best value AIO 110 euros, 3x 120mm fans, handles OCed i9-14900K, pump noise low, 6-year warranty", "keywords": ["arctic", "liquid freezer", "360mm"], "difficulty": "intermediate", "tags": ["aio"], "related_tools": []},
                {"content": "Air cooler pros: No pump failure risk, longer lifespan 10+ years, quieter operation, cheaper maintenance, no leaks", "keywords": ["air cooling", "pros"], "difficulty": "beginner", "tags": ["reliability"], "related_tools": []},
                {"content": "AIO pros: Better sustained loads (rendering), compact top clearance, RAM clearance easier, aesthetics RGB, cooler CPU under stress", "keywords": ["aio", "pros"], "difficulty": "beginner", "tags": ["liquid"], "related_tools": []},
                {"content": "Air cooler cons: RAM clearance issues (dual tower), large case required, GPU heat proximity, heavier motherboard stress", "keywords": ["air cooling", "cons"], "difficulty": "beginner", "tags": ["limitations"], "related_tools": []},
                {"content": "AIO cons: Pump failure 3-5 years, noise pump whine, coolant evaporation, leak risk minimal, higher cost 100-200 euros", "keywords": ["aio", "cons"], "difficulty": "intermediate", "tags": ["risks"], "related_tools": []},
                {"content": "Pump noise: Quality AIOs <25 dBA (Arctic, NZXT Kraken), cheap AIOs 30-40 dBA whine, air coolers 20-25 dBA silent", "keywords": ["pump noise", "dba"], "difficulty": "intermediate", "tags": ["noise"], "related_tools": []},
                {"content": "Maintenance air: Dust cleaning every 6 months, fan replacement 5+ years, thermal paste repaste 3 years", "keywords": ["maintenance", "air"], "difficulty": "beginner", "tags": ["upkeep"], "related_tools": []},
                {"content": "Maintenance AIO: Coolant evaporation 3-5 years (closed loop sealed), pump failure common 5+ years, zero-maintenance myth", "keywords": ["maintenance", "aio"], "difficulty": "intermediate", "tags": ["upkeep"], "related_tools": []},
                {"content": "Thermalright Peerless Assassin 120: Budget king 35 euros, twin tower, beats NH-D15 value, 150W TDP, i5/R5 perfect", "keywords": ["thermalright", "budget"], "difficulty": "beginner", "tags": ["value"], "related_tools": []},
                {"content": "Be Quiet Dark Rock Pro 4: Silent air cooler 90 euros, 250W TDP, <24 dBA, premium build, German engineering", "keywords": ["be quiet", "dark rock"], "difficulty": "intermediate", "tags": ["silent"], "related_tools": []},
                {"content": "NZXT Kraken Z73: Premium AIO 280 euros, 360mm LCD screen, CAM software RGB, 280W TDP, pump noise low", "keywords": ["nzxt", "kraken"], "difficulty": "advanced", "tags": ["premium"], "related_tools": ["CAM"]},
                {"content": "Corsair iCUE H150i Elite: RGB AIO 180 euros, 360mm, iCUE software control, ML fans quiet, 5-year warranty", "keywords": ["corsair", "icue"], "difficulty": "intermediate", "tags": ["rgb"], "related_tools": ["iCUE"]},
                {"content": "Custom loop: 500+ euros investment, maintenance every year, leak risk higher, performance +3-5C vs AIO, enthusiast only", "keywords": ["custom loop", "watercooling"], "difficulty": "expert", "tags": ["enthusiast"], "related_tools": []},
                {"content": "Radiator size: 120mm budget (<100W CPU), 240mm mid-range (150W), 280mm/360mm high-end (200W+), 420mm overkill", "keywords": ["radiator", "size"], "difficulty": "intermediate", "tags": ["sizing"], "related_tools": []},
                {"content": "Fan configuration: Push (intake rad) cooler CPU +2C, pull (exhaust rad) better case temps, push-pull +1C gains marginal", "keywords": ["fan config", "push pull"], "difficulty": "advanced", "tags": ["optimization"], "related_tools": []},
                {"content": "Case compatibility: Check radiator clearance top/front, AIO tubes length 300-400mm, air cooler height <165mm most cases", "keywords": ["compatibility", "clearance"], "difficulty": "intermediate", "tags": ["case"], "related_tools": []},
                {"content": "Stock coolers: Intel stock garbage (70C idle i9), AMD Wraith sufficient R5 non-X, upgrade mandatory i7+/R7+", "keywords": ["stock cooler", "intel amd"], "difficulty": "beginner", "tags": ["stock"], "related_tools": []},
                {"content": "Tower cooler types: Single tower <100W (30 euros), dual tower 150W (50-150 euros), compact <70mm height SFF cases", "keywords": ["tower types", "single dual"], "difficulty": "beginner", "tags": ["types"], "related_tools": []},
                {"content": "AIO pump placement: Pump below radiator top (air trap avoids), tubes down front mount OK, pump top rad bad (gurgling)", "keywords": ["pump placement", "mounting"], "difficulty": "intermediate", "tags": ["installation"], "related_tools": []},
                {"content": "Thermal paste: Arctic MX-4 (8 euros 4g), Noctua NT-H1 included, Thermal Grizzly Kryonaut premium (13 euros), pea-sized dot center", "keywords": ["thermal paste", "application"], "difficulty": "beginner", "tags": ["paste"], "related_tools": []},
                {"content": "Fan speed curves: Aggressive 40% idle 100% 80C, balanced 30-60%, silent 20-40% (higher temps OK <85C)", "keywords": ["fan curves", "bios"], "difficulty": "intermediate", "tags": ["tuning"], "related_tools": []},
                {"content": "RGB vs non-RGB: RGB adds 20-40 euros cost, software bloat (iCUE/CAM), <5% performance difference, aesthetics preference", "keywords": ["rgb", "non-rgb"], "difficulty": "beginner", "tags": ["aesthetics"], "related_tools": []},
                {"content": "Warranty: Air coolers 6 years (Noctua lifetime), AIOs 3-6 years (Arctic 6y, Corsair 5y), warranty crucial pump failures", "keywords": ["warranty", "lifespan"], "difficulty": "intermediate", "tags": ["reliability"], "related_tools": []},
                {"content": "Noise normalized: Air 20-35 dBA full load, AIO 25-40 dBA (pump + fans), custom loop 15-25 dBA (larger rads lower RPM)", "keywords": ["noise levels", "dba"], "difficulty": "intermediate", "tags": ["acoustics"], "related_tools": []},
                {"content": "VRM cooling: Air coolers provide airflow to VRM, AIOs leave VRM hotter +10-15C (add case fans), custom loop blocks cool VRM", "keywords": ["vrm", "motherboard"], "difficulty": "advanced", "tags": ["secondary"], "related_tools": []},
                {"content": "Ambient temperature: 20C room air beats AIO by 2-3C, 30C room AIO wins sustained, air saturates heatsink faster", "keywords": ["ambient", "room temp"], "difficulty": "advanced", "tags": ["environment"], "related_tools": []},
                {"content": "Installation difficulty: Air 10min beginner, AIO 30min intermediate (tubes routing), custom loop 3+ hours expert", "keywords": ["installation", "difficulty"], "difficulty": "beginner", "tags": ["build"], "related_tools": []},
                {"content": "Cooler height: Check RAM clearance NH-D15 (165mm tower blocks tall RAM), offset design (NH-D15S) clears RAM, AIO no issue", "keywords": ["clearance", "ram"], "difficulty": "intermediate", "tags": ["compatibility"], "related_tools": []},
                {"content": "Best budget air: Thermalright Peerless Assassin 35 euros, DeepCool AK400 30 euros, ID-Cooling SE-224-XT 25 euros", "keywords": ["budget", "value"], "difficulty": "beginner", "tags": ["recommendations"], "related_tools": []},
                {"content": "Best budget AIO: Arctic Liquid Freezer II 240mm 70 euros, MSI MAG CoreLiquid 240R 80 euros, Cooler Master ML240L 60 euros", "keywords": ["budget", "aio"], "difficulty": "beginner", "tags": ["recommendations"], "related_tools": []},
                {"content": "Overkill cooling: Diminishing returns beyond 150 euros, NH-D15 cools i9 adequately, 360mm AIO overkill mid-range CPUs", "keywords": ["overkill", "diminishing returns"], "difficulty": "intermediate", "tags": ["optimization"], "related_tools": []},
                {"content": "Intel vs AMD mounting: AMD AM4/AM5 same bracket (upgrade path), Intel LGA1700 offset mount (bending fix), check compatibility", "keywords": ["mounting", "socket"], "difficulty": "intermediate", "tags": ["compatibility"], "related_tools": []},
                {"content": "GPU vs CPU cooling priority: GPU generates more heat (300W+ vs 150W CPU), case airflow critical, CPU cooler secondary concern", "keywords": ["priority", "gpu cpu"], "difficulty": "intermediate", "tags": ["strategy"], "related_tools": []},
                {"content": "Repasting frequency: Stock paste 2-3 years, quality paste (Kryonaut) 4-5 years, temps rising 5-10C signals repaste needed", "keywords": ["repaste", "maintenance"], "difficulty": "intermediate", "tags": ["upkeep"], "related_tools": []},
                {"content": "Coolant types: AIO closed loop proprietary (no refill), custom loop distilled water + biocide, avoid colored coolant (gunking)", "keywords": ["coolant", "liquid"], "difficulty": "advanced", "tags": ["custom loop"], "related_tools": []},
                {"content": "Arctic P12 PWM: Best case fans 8 euros each, 1800 RPM, quiet, 3-pack 25 euros, exhaust rear/top intake front", "keywords": ["case fans", "arctic"], "difficulty": "beginner", "tags": ["fans"], "related_tools": []},
                {"content": "Noctua NF-A12x25: Premium fans 35 euros, 2000 RPM, <22 dBA, brown aesthetics, best airflow-to-noise ratio", "keywords": ["noctua", "premium fans"], "difficulty": "intermediate", "tags": ["silent"], "related_tools": []},
                {"content": "Fan placement: 2-3 intake front bottom, 1-2 exhaust rear top, positive pressure (intake > exhaust) reduces dust", "keywords": ["fan placement", "airflow"], "difficulty": "beginner", "tags": ["case"], "related_tools": []},
                {"content": "Water blocks: CPU block 100-150 euros, GPU block 150-300 euros, custom loop total 500-1000 euros (radiator, pump, reservoir)", "keywords": ["water block", "custom loop"], "difficulty": "expert", "tags": ["components"], "related_tools": []},
                {"content": "Leaks risk: AIO 0.1% failure rate (factory sealed), custom loop 5% user error (fittings), leak testing 24h before powering", "keywords": ["leaks", "risk"], "difficulty": "advanced", "tags": ["safety"], "related_tools": []},
                {"content": "Pump lifespan: AIO pumps 30000-50000 hours (3.5-5.7 years continuous), custom loop pumps 50000+ hours replaceable", "keywords": ["pump lifespan", "mtbf"], "difficulty": "advanced", "tags": ["reliability"], "related_tools": []},
                {"content": "Temperature targets: CPU <80C gaming ideal, <85C sustained acceptable, >90C throttling, <75C enthusiast target", "keywords": ["temperature", "targets"], "difficulty": "intermediate", "tags": ["monitoring"], "related_tools": ["HWMonitor"]},
                {"content": "Quick vs gradual mount: AIO quick mounting brackets, air coolers fiddly screws (spring-loaded), custom loop hours assembly", "keywords": ["mounting", "installation"], "difficulty": "beginner", "tags": ["ease"], "related_tools": []},
                {"content": "Tubing: AIO rubber tubes 300-400mm fixed, custom loop soft tubing easier (ZMT), hard tubing (PETG/acrylic) aesthetics expert", "keywords": ["tubing", "custom"], "difficulty": "advanced", "tags": ["custom loop"], "related_tools": []},
                {"content": "Heatpipes: Air coolers 4-8 heatpipes (6mm diameter), direct touch vs nickel-plated base, more pipes ≠ better (design matters)", "keywords": ["heatpipes", "air cooling"], "difficulty": "advanced", "tags": ["technology"], "related_tools": []},
                {"content": "ARGB vs RGB: ARGB (5V 3-pin) addressable individual LEDs, RGB (12V 4-pin) static colors, check motherboard headers compatibility", "keywords": ["argb", "rgb"], "difficulty": "intermediate", "tags": ["lighting"], "related_tools": []},
                {"content": "Software control: Corsair iCUE (resource hog 500MB RAM), NZXT CAM (lighter 200MB), air coolers PWM BIOS control (zero software)", "keywords": ["software", "bloat"], "difficulty": "intermediate", "tags": ["control"], "related_tools": ["iCUE", "CAM"]},
                {"content": "Value recommendation 2024: Air <150W (Thermalright PA120 35 euros), 150W-200W (NH-D15 150 euros or Arctic 240mm 70 euros), 200W+ (Arctic 360mm 110 euros)", "keywords": ["recommendation", "2024"], "difficulty": "beginner", "tags": ["buying"], "related_tools": []}
            ]
        }

        # 12. Thermal Solutions Laptops
        kb["thermal_solutions_laptops"] = {
            "metadata": {
                "priority": 4,
                "tags": ["laptop", "cooling", "thermal", "mobile"],
                "difficulty": "intermediate",
                "description": "Laptop cooling pads, repasting, undervolting"
            },
            "tips": [
                {"content": "Cooling pads: Budget 20-30 euros (basic fans), premium 40-60 euros (adjustable height), drops temps 5-10C gaming laptops", "keywords": ["cooling pad", "laptop"], "difficulty": "beginner", "tags": ["accessory"], "related_tools": []},
                {"content": "Repaste laptops: Stock paste dries 2-3 years, Thermal Grizzly Kryonaut best (13 euros), drops temps 10-20C, voids warranty often", "keywords": ["repaste", "kryonaut"], "difficulty": "advanced", "tags": ["maintenance"], "related_tools": []},
                {"content": "ThrottleStop: Intel CPU undervolting tool free, -100mV safe start (test stability), reduces temps 10-15C, maintains performance", "keywords": ["throttlestop", "undervolt"], "difficulty": "intermediate", "tags": ["software"], "related_tools": ["ThrottleStop"]},
                {"content": "Elevate rear: Simple 1-2 inch rear elevation improves airflow, free DIY (books/stand), drops temps 3-5C, better than cooling pads", "keywords": ["elevation", "airflow"], "difficulty": "beginner", "tags": ["free"], "related_tools": []},
                {"content": "Liquid metal: Conductonaut extreme solution 10 euros, -20C vs paste, risky (conductive), permanent laptops, expert only", "keywords": ["liquid metal", "conductonaut"], "difficulty": "expert", "tags": ["extreme"], "related_tools": []},
                {"content": "Dust cleaning: Every 6-12 months compressed air (external vents), full disassembly 12-18 months, restores 5-10C temps", "keywords": ["dust", "cleaning"], "difficulty": "intermediate", "tags": ["maintenance"], "related_tools": []},
                {"content": "AMD Ryzen Controller: AMD laptop undervolting alternative, less stable than ThrottleStop, Ryzen 4000-7000 series", "keywords": ["amd", "ryzen controller"], "difficulty": "intermediate", "tags": ["software"], "related_tools": ["Ryzen Controller"]},
                {"content": "Disable Turbo Boost: Emergency thermal fix, BIOS or ThrottleStop, loses 20-30% performance, temps drop 15-20C, last resort", "keywords": ["turbo boost", "disable"], "difficulty": "intermediate", "tags": ["thermal"], "related_tools": []},
                {"content": "Thermal pads: GPU VRAM/VRM cooling, 1-2mm thickness (measure), Gelid/Arctic pads 15 euros, improves VRAM temps 10-15C", "keywords": ["thermal pads", "vram"], "difficulty": "advanced", "tags": ["upgrade"], "related_tools": []},
                {"content": "Fan control: MSI Afterburner (NVIDIA/AMD laptops), custom fan curves 50% 60C to 100% 80C, noisier but cooler", "keywords": ["fan control", "afterburner"], "difficulty": "intermediate", "tags": ["tuning"], "related_tools": ["MSI Afterburner"]},
                {"content": "Warranty void: Repasting often voids warranty (check manufacturer), seal stickers, Dell/HP strict, ASUS/MSI relaxed", "keywords": ["warranty", "void"], "difficulty": "advanced", "tags": ["risk"], "related_tools": []},
                {"content": "Hard surface: Always use laptop on hard flat surface (airflow), soft surfaces (bed/couch) block intake vents, throttling guaranteed", "keywords": ["surface", "airflow"], "difficulty": "beginner", "tags": ["usage"], "related_tools": []},
                {"content": "Intel XTU: Official Intel undervolt tool, simpler than ThrottleStop, works 8th-10th gen (11th+ locked), GUI friendly", "keywords": ["intel xtu", "undervolt"], "difficulty": "beginner", "tags": ["software"], "related_tools": ["Intel XTU"]},
                {"content": "Performance modes: Balanced default, Performance mode higher temps +10C, Battery Saver underclocks (cooler), Windows Power Options", "keywords": ["performance mode", "power"], "difficulty": "beginner", "tags": ["windows"], "related_tools": []},
                {"content": "Gaming laptop stands: Adjustable height 30-50 euros, metal mesh ventilation, ergonomic typing angle, combined cooling pad", "keywords": ["laptop stand", "gaming"], "difficulty": "beginner", "tags": ["accessory"], "related_tools": []},
                {"content": "Thermal throttling: CPU/GPU downclock at 95-100C (Intel), 95C (AMD), 83C (NVIDIA), prevents damage but kills performance", "keywords": ["throttling", "temps"], "difficulty": "intermediate", "tags": ["thermal"], "related_tools": []},
                {"content": "Clamshell mode: Closed lid + external monitor docks, worse thermals (blocked exhaust), open lid better airflow", "keywords": ["clamshell", "docking"], "difficulty": "intermediate", "tags": ["setup"], "related_tools": []},
                {"content": "Undervolting results: -50mV minimal, -100mV safe most CPUs, -125mV aggressive (test), -150mV unstable crashes, CPU lottery varies", "keywords": ["undervolt", "values"], "difficulty": "advanced", "tags": ["tuning"], "related_tools": []},
                {"content": "BIOS lock: 11th gen Intel+ Plundervolt vulnerability patch locked undervolting, older BIOS versions allow (risky security)", "keywords": ["bios lock", "plundervolt"], "difficulty": "expert", "tags": ["limitation"], "related_tools": []},
                {"content": "CPU vs GPU temps: Gaming GPU hotter (80-90C normal), CPU 70-85C, both >95C problematic, repaste prioritize GPU", "keywords": ["temps", "cpu gpu"], "difficulty": "intermediate", "tags": ["monitoring"], "related_tools": []},
                {"content": "Vapor chamber cooling: Premium laptops (ASUS ROG, MSI GE), better heat spread vs heatpipes, thinner designs, -5C vs traditional", "keywords": ["vapor chamber", "premium"], "difficulty": "advanced", "tags": ["technology"], "related_tools": []},
                {"content": "External GPU cooling: USB laptop coolers (clips on exhaust), vacuum fan extractors 30-40 euros, questionable 2-3C gains", "keywords": ["external cooling", "usb"], "difficulty": "beginner", "tags": ["gadget"], "related_tools": []},
                {"content": "Repaste frequency: Budget laptops 12-18 months (cheap paste), premium 24-36 months, signs: rising temps 10C+, fan noise constant", "keywords": ["repaste", "frequency"], "difficulty": "intermediate", "tags": ["maintenance"], "related_tools": []},
                {"content": "Disassembly guides: iFixit teardowns, YouTube guides laptop-specific, toolkit 20 euros (precision screwdrivers, spudger, thermal paste)", "keywords": ["disassembly", "ifixit"], "difficulty": "advanced", "tags": ["repair"], "related_tools": []},
                {"content": "Power limits: ThrottleStop set TDP limits (PL1 long-term, PL2 short-burst), lower PL2 reduces spikes, 45W TDP typical gaming", "keywords": ["power limits", "tdp"], "difficulty": "advanced", "tags": ["tuning"], "related_tools": ["ThrottleStop"]},
                {"content": "AC vs battery: Plugged in full performance (higher temps), battery mode downclocks (cooler 60-70C), gaming needs AC power", "keywords": ["ac", "battery"], "difficulty": "beginner", "tags": ["power"], "related_tools": []},
                {"content": "Manufacturer software: Dell Power Manager, HP Omen Command Center, Lenovo Vantage, ASUS Armoury Crate (performance profiles)", "keywords": ["manufacturer", "software"], "difficulty": "beginner", "tags": ["oem"], "related_tools": []},
                {"content": "Hot room: 30C ambient room adds 10-15C laptop temps, AC/fan room cooling essential gaming, thermal throttling inevitable hot climates", "keywords": ["ambient", "room temp"], "difficulty": "intermediate", "tags": ["environment"], "related_tools": []},
                {"content": "GPU repaste: Harder than CPU (more screws), drops temps 10-15C, VRAM thermal pads critical (measure thickness 1-2mm)", "keywords": ["gpu repaste", "vram"], "difficulty": "expert", "tags": ["advanced"], "related_tools": []},
                {"content": "Coolant evaporation: Desktop AIO issue, not laptop (heatpipes sealed), laptop coolers maintenance-free (no refill)", "keywords": ["heatpipes", "maintenance"], "difficulty": "intermediate", "tags": ["technology"], "related_tools": []},
                {"content": "MSI Dragon Center: MSI laptop control software, fan curves, performance modes, battery optimization, 300MB bloatware", "keywords": ["msi", "dragon center"], "difficulty": "beginner", "tags": ["software"], "related_tools": ["Dragon Center"]},
                {"content": "ASUS Armoury Crate: ROG laptop control, Turbo/Performance/Silent modes, RGB sync, fan curves, 500MB RAM usage", "keywords": ["asus", "armoury crate"], "difficulty": "beginner", "tags": ["software"], "related_tools": ["Armoury Crate"]},
                {"content": "Silent mode: Fan curves 0-40%, temps rise 80-90C (acceptable browsing), gaming needs Performance mode (60-100% fans)", "keywords": ["silent mode", "fan"], "difficulty": "beginner", "tags": ["profiles"], "related_tools": []},
                {"content": "Thermal imaging: FLIR cameras (expensive), identify hotspots, GPU VRAM/VRM areas, helps diagnose poor thermal pad contact", "keywords": ["thermal imaging", "flir"], "difficulty": "expert", "tags": ["diagnostic"], "related_tools": []},
                {"content": "Best cooling pads 2024: Klim Wind (40 euros 4 fans), Havit HV-F2056 (30 euros RGB), TopMate C5 (25 euros budget)", "keywords": ["cooling pad", "2024"], "difficulty": "beginner", "tags": ["recommendations"], "related_tools": []},
                {"content": "Vacuum vs blower: Vacuum cleaners risk ESD (static damage), compressed air blower safer (DataVac 70 euros), outdoor dusting only", "keywords": ["cleaning", "dust"], "difficulty": "intermediate", "tags": ["maintenance"], "related_tools": []},
                {"content": "eGPU cooling: External GPU setups better cooling (desktop airflow), Thunderbolt 3/4 bandwidth limit, GPU runs cooler vs internal", "keywords": ["egpu", "external"], "difficulty": "advanced", "tags": ["setup"], "related_tools": []},
                {"content": "Dual fan vs single: Gaming laptops dual fans (CPU+GPU separate), ultrabooks single fan shared, dual fans 10C better GPU temps", "keywords": ["dual fan", "single"], "difficulty": "intermediate", "tags": ["design"], "related_tools": []},
                {"content": "Long-term thermal: Paste degrades 3-5 years (silicone-based), liquid metal permanent 10+ years, quality paste extends intervals", "keywords": ["longevity", "thermal paste"], "difficulty": "advanced", "tags": ["lifespan"], "related_tools": []},
                {"content": "Laptop cooling myths: More fans ≠ better (airflow design matters), RGB cooling pads gimmick (no performance), liquid cooling laptops rare custom", "keywords": ["myths", "cooling"], "difficulty": "intermediate", "tags": ["education"], "related_tools": []}
            ]
        }

        # =============================================================================
        # MONITORS (3 catégories - ~120 conseils)
        # =============================================================================

        # 13. Monitor Gaming Specs
        kb["monitor_gaming_specs"] = {
            "metadata": {
                "priority": 5,
                "tags": ["monitor", "gaming", "display", "refresh rate"],
                "difficulty": "intermediate",
                "description": "Gaming monitor specifications: refresh rate, panel types, sync tech"
            },
            "tips": [
                {"content": "144Hz refresh rate: Sweet spot gaming 200-300 euros, noticeable upgrade from 60Hz, esports minimum, matches RTX 4060/RX 7600", "keywords": ["144hz", "refresh rate"], "difficulty": "beginner", "tags": ["gaming"], "related_tools": []},
                {"content": "240Hz monitors: Competitive esports 300-500 euros, diminishing returns vs 144Hz (pro players notice), needs RTX 4070+/RX 7800 XT", "keywords": ["240hz", "esports"], "difficulty": "intermediate", "tags": ["competitive"], "related_tools": []},
                {"content": "360Hz displays: Professional esports only 500-800 euros, marginal gains vs 240Hz, requires RTX 4080+ low settings, VALORANT/CS2", "keywords": ["360hz", "pro"], "difficulty": "advanced", "tags": ["professional"], "related_tools": []},
                {"content": "IPS panels: 1ms response time (modern fast IPS), accurate colors 99% sRGB, wide viewing angles 178°, gaming + productivity", "keywords": ["ips", "panel"], "difficulty": "intermediate", "tags": ["panel type"], "related_tools": []},
                {"content": "VA panels: 3-5ms response time (ghosting), high contrast 3000:1 (vs IPS 1000:1), deeper blacks, budget choice 150-250 euros", "keywords": ["va", "panel"], "difficulty": "intermediate", "tags": ["panel type"], "related_tools": []},
                {"content": "OLED monitors: <0.1ms response time, infinite contrast, burn-in risk (3-5 years heavy use), premium 800-1500 euros, LG 27GR95QE", "keywords": ["oled", "burn-in"], "difficulty": "advanced", "tags": ["premium"], "related_tools": []},
                {"content": "G-Sync: NVIDIA proprietary VRR, hardware module (G-Sync Ultimate), 400-600 euros premium, eliminates tearing 30-165 FPS range", "keywords": ["g-sync", "nvidia"], "difficulty": "intermediate", "tags": ["sync"], "related_tools": []},
                {"content": "G-Sync Compatible: FreeSync monitors certified by NVIDIA, cheaper than G-Sync (no module), works RTX/GTX 10 series+, 200-400 euros", "keywords": ["g-sync compatible", "freesync"], "difficulty": "beginner", "tags": ["sync"], "related_tools": []},
                {"content": "FreeSync: AMD open VRR standard, 150-400 euros, works AMD GPUs + NVIDIA (G-Sync Compatible), 48-144Hz range typical", "keywords": ["freesync", "amd"], "difficulty": "beginner", "tags": ["sync"], "related_tools": []},
                {"content": "Response time: Advertised 1ms often fake (gray-to-gray), real pixel response 3-5ms (black-to-white), overdrive setting critical", "keywords": ["response time", "1ms"], "difficulty": "intermediate", "tags": ["specs"], "related_tools": []},
                {"content": "Response time overdrive: Low setting safe (minimal overshoot), Medium balanced, High/Extreme inverse ghosting artifacts, test per monitor", "keywords": ["overdrive", "ghosting"], "difficulty": "advanced", "tags": ["tuning"], "related_tools": []},
                {"content": "TN panels: 0.5-1ms true response time, washed colors 90% sRGB, terrible viewing angles 160°, obsolete except budget 144Hz 150 euros", "keywords": ["tn", "panel"], "difficulty": "beginner", "tags": ["obsolete"], "related_tools": []},
                {"content": "Input lag: <5ms excellent gaming, 5-10ms acceptable, >15ms sluggish (budget TVs 30-50ms), separate from response time", "keywords": ["input lag", "latency"], "difficulty": "intermediate", "tags": ["performance"], "related_tools": []},
                {"content": "HDMI 2.1: 48 Gbps bandwidth, 4K 120Hz support, VRR (HDMI Forum VRR), consoles PS5/Xbox Series X requirement", "keywords": ["hdmi 2.1", "bandwidth"], "difficulty": "intermediate", "tags": ["connectivity"], "related_tools": []},
                {"content": "DisplayPort 1.4: 32.4 Gbps, 1440p 240Hz or 4K 120Hz (DSC compression), PC gaming standard, older GPUs limited", "keywords": ["displayport", "1.4"], "difficulty": "intermediate", "tags": ["connectivity"], "related_tools": []},
                {"content": "DisplayPort 2.1: 80 Gbps UHBR20, 4K 240Hz or 8K 60Hz, RTX 50 series+ future, backwards compatible DP 1.4", "keywords": ["displayport 2.1", "future"], "difficulty": "advanced", "tags": ["new"], "related_tools": []},
                {"content": "G-Sync Ultimate: HDR 1000 nits, hardware G-Sync module, <1ms input lag, 700-1200 euros, ASUS PG27UQX, ROG Swift", "keywords": ["g-sync ultimate", "hdr"], "difficulty": "expert", "tags": ["premium"], "related_tools": []},
                {"content": "Adaptive Sync range: Wide range better (30-144Hz vs 48-144Hz), LFC (Low Framerate Compensation) doubles frames <48 FPS", "keywords": ["adaptive sync", "lfc"], "difficulty": "advanced", "tags": ["vrr"], "related_tools": []},
                {"content": "Ghosting vs tearing: Ghosting slow pixels (motion blur), tearing no VSync (screen tear line), VRR eliminates tearing without input lag", "keywords": ["ghosting", "tearing"], "difficulty": "intermediate", "tags": ["issues"], "related_tools": []},
                {"content": "Backlight bleed: IPS glow in corners (dark scenes), VA less glow, OLED zero bleed, lottery (return bad units)", "keywords": ["backlight bleed", "ips glow"], "difficulty": "intermediate", "tags": ["quality"], "related_tools": []},
                {"content": "Dead pixels: ISO13406-2 standard allows 3-5 dead pixels (Class II), premium brands 0 dead pixel guarantee, return policy check", "keywords": ["dead pixels", "warranty"], "difficulty": "beginner", "tags": ["quality"], "related_tools": []},
                {"content": "Curved vs flat: 1500R/1800R curve immersive ultrawide 34\"+, flat better multi-monitor, personal preference, curved VA common", "keywords": ["curved", "flat"], "difficulty": "beginner", "tags": ["design"], "related_tools": []},
                {"content": "Aspect ratio: 16:9 standard (1080p/1440p/4K), 21:9 ultrawide gaming + productivity, 32:9 super ultrawide (dual monitor replacement)", "keywords": ["aspect ratio", "ultrawide"], "difficulty": "intermediate", "tags": ["format"], "related_tools": []},
                {"content": "VESA mount: 100x100mm standard monitor arms, 75x75mm smaller monitors, check compatibility, ergotron arms 150-300 euros", "keywords": ["vesa", "mount"], "difficulty": "beginner", "tags": ["ergonomics"], "related_tools": []},
                {"content": "Stand adjustability: Height adjust critical (eye level), tilt ±15°, swivel 90° portrait, pivot, cheap stands fixed (neck strain)", "keywords": ["stand", "ergonomics"], "difficulty": "beginner", "tags": ["comfort"], "related_tools": []},
                {"content": "Blue light filter: Software filters (Windows Night Light), hardware low-blue modes, 6500K vs 5000K warmer, eye strain reduction", "keywords": ["blue light", "eye strain"], "difficulty": "beginner", "tags": ["health"], "related_tools": []},
                {"content": "Flicker-free: DC dimming eliminates PWM flicker (headaches), all modern monitors >200 euros flicker-free, eye comfort", "keywords": ["flicker-free", "pwm"], "difficulty": "intermediate", "tags": ["health"], "related_tools": []},
                {"content": "HDR gaming: HDR400 fake (400 nits peak), HDR600 minimum useful (600 nits), HDR1000 true HDR (1000 nits), FALD zones critical", "keywords": ["hdr", "nits"], "difficulty": "advanced", "tags": ["hdr"], "related_tools": []},
                {"content": "Local dimming: FALD (Full Array) 384+ zones good, edge-lit garbage (blooming), OLED per-pixel dimming perfect, HDR requires good dimming", "keywords": ["local dimming", "fald"], "difficulty": "advanced", "tags": ["hdr"], "related_tools": []},
                {"content": "USB hub: Built-in USB hub monitors, 2-4 USB 3.0 ports, keyboard/mouse passthrough, cable clutter reduction, premium feature", "keywords": ["usb hub", "ports"], "difficulty": "beginner", "tags": ["connectivity"], "related_tools": []},
                {"content": "KVM switch: Keyboard/Video/Mouse switch built-in, 2 PC inputs share peripherals, rare monitors (Dell UltraSharp), 50 euros external KVM", "keywords": ["kvm", "switch"], "difficulty": "intermediate", "tags": ["productivity"], "related_tools": []},
                {"content": "Picture-in-Picture: PIP/PBP dual input display (console + PC), productivity + gaming, 27\"+ recommended, Dell/LG premium feature", "keywords": ["pip", "pbp"], "difficulty": "intermediate", "tags": ["multi-input"], "related_tools": []},
                {"content": "Best 1080p 144Hz: AOC 24G2 (180 euros IPS), MSI G2412F (150 euros), budget esports, RTX 4060/RX 7600", "keywords": ["1080p", "144hz"], "difficulty": "beginner", "tags": ["recommendations"], "related_tools": []},
                {"content": "Best 1440p 165Hz: Dell S2721DGF (350 euros IPS), LG 27GP850 (400 euros), sweet spot gaming, RTX 4070/RX 7800 XT", "keywords": ["1440p", "165hz"], "difficulty": "intermediate", "tags": ["recommendations"], "related_tools": []},
                {"content": "Best 4K 144Hz: LG 27GP950 (700 euros), ASUS PG27UQ (900 euros G-Sync), requires RTX 4080+, future-proof", "keywords": ["4k", "144hz"], "difficulty": "advanced", "tags": ["recommendations"], "related_tools": []},
                {"content": "Best ultrawide: LG 34GP83A-B 34\" 1440p 144Hz (500 euros), Samsung Odyssey G9 49\" 240Hz (1200 euros super ultrawide)", "keywords": ["ultrawide", "34 inch"], "difficulty": "intermediate", "tags": ["recommendations"], "related_tools": []},
                {"content": "Best OLED: LG 27GR95QE 27\" 1440p 240Hz OLED (1000 euros), ASUS PG27AQDM (1100 euros), burn-in warranty 3 years", "keywords": ["oled", "gaming"], "difficulty": "expert", "tags": ["premium"], "related_tools": []},
                {"content": "Pixel density: 24\" 1080p = 92 PPI (acceptable), 27\" 1440p = 109 PPI (sweet spot), 32\" 4K = 140 PPI (sharp)", "keywords": ["pixel density", "ppi"], "difficulty": "intermediate", "tags": ["sizing"], "related_tools": []},
                {"content": "Viewing distance: 24\" @ 60-80cm, 27\" @ 80-100cm, 32\" @ 100-120cm, ultrawide 100cm minimum, closer = higher PPI needed", "keywords": ["viewing distance", "ergonomics"], "difficulty": "beginner", "tags": ["setup"], "related_tools": []},
                {"content": "Anti-glare coating: Matte coating reduces reflections (light diffusion), glossy coating vibrant colors (reflections), IPS usually matte", "keywords": ["anti-glare", "matte"], "difficulty": "beginner", "tags": ["finish"], "related_tools": []},
                {"content": "Warranty: 3 years standard, Dell/LG Premium Panel Guarantee (replacement for 1 bright pixel), dead pixel policies vary", "keywords": ["warranty", "dead pixel"], "difficulty": "beginner", "tags": ["support"], "related_tools": []},
                {"content": "Firmware updates: Some monitors firmware updates (OSD bugs, VRR improvements), DisplayPort MST hub updates, rare feature", "keywords": ["firmware", "updates"], "difficulty": "advanced", "tags": ["maintenance"], "related_tools": []},
                {"content": "Monitor OSD: On-Screen Display controls, joystick vs buttons (joystick easier), presets (FPS/RTS/RPG), save custom profiles", "keywords": ["osd", "controls"], "difficulty": "beginner", "tags": ["usability"], "related_tools": []}
            ]
        }

        # 14. Monitor Resolution Guide
        kb["monitor_resolution_guide"] = {
            "metadata": {
                "priority": 4,
                "tags": ["monitor", "resolution", "display", "ppi"],
                "difficulty": "beginner",
                "description": "Monitor resolution and size recommendations"
            },
            "tips": [
                {"content": "1080p 24\": 92 PPI pixel density, esports sweet spot, high FPS easy (200+ FPS RTX 4060), 150-300 euros, desk space 60-80cm", "keywords": ["1080p", "24 inch"], "difficulty": "beginner", "tags": ["esports"], "related_tools": []},
                {"content": "1440p 27\": 109 PPI ideal density, gaming + productivity balance, 100-180 FPS RTX 4070, 300-500 euros, most popular", "keywords": ["1440p", "27 inch"], "difficulty": "beginner", "tags": ["balanced"], "related_tools": []},
                {"content": "4K 32\": 140 PPI sharp text, demanding 60-120 FPS RTX 4080+, 500-1000 euros, productivity + AAA gaming, scaling 125-150%", "keywords": ["4k", "32 inch"], "difficulty": "intermediate", "tags": ["high-end"], "related_tools": []},
                {"content": "Scaling Windows: 100% native, 125% recommended 1440p 27\", 150% comfortable 4K, 200% 4K accessibility, fractional scaling blurry some apps", "keywords": ["scaling", "windows"], "difficulty": "intermediate", "tags": ["windows"], "related_tools": []},
                {"content": "1080p 27\": 82 PPI low density, visible pixels <80cm, avoid unless budget <200 euros, better 1080p 24\" or 1440p 27\"", "keywords": ["1080p", "27 inch"], "difficulty": "beginner", "tags": ["avoid"], "related_tools": []},
                {"content": "1440p 24\": 122 PPI high density, compact desk space, sharp text, esports + productivity, rare (most 24\" = 1080p)", "keywords": ["1440p", "24 inch"], "difficulty": "intermediate", "tags": ["compact"], "related_tools": []},
                {"content": "4K 27\": 163 PPI very sharp, scaling 150% required (small text), macOS territory, Windows scaling inconsistent older apps", "keywords": ["4k", "27 inch"], "difficulty": "intermediate", "tags": ["sharp"], "related_tools": []},
                {"content": "Ultrawide 1440p 34\": 3440x1440 21:9 aspect, 110 PPI, immersive gaming (FOV advantage), productivity (2 windows), 500-800 euros", "keywords": ["ultrawide", "1440p"], "difficulty": "intermediate", "tags": ["ultrawide"], "related_tools": []},
                {"content": "Ultrawide 1080p 34\": 2560x1080 21:9, 82 PPI low density, budget ultrawide 300-400 euros, visible pixels, avoid >80cm distance", "keywords": ["ultrawide", "1080p"], "difficulty": "beginner", "tags": ["budget"], "related_tools": []},
                {"content": "Super ultrawide 49\": 5120x1440 32:9, dual 27\" 1440p side-by-side, 1200-1500 euros, gaming + productivity beast, GPU demanding", "keywords": ["super ultrawide", "49 inch"], "difficulty": "advanced", "tags": ["extreme"], "related_tools": []},
                {"content": "GPU requirements 1080p: RTX 4060/RX 7600 high settings 100+ FPS, RTX 4060 Ti/RX 7700 XT ultra 144+ FPS, esports 200+ FPS easy", "keywords": ["1080p", "gpu"], "difficulty": "beginner", "tags": ["performance"], "related_tools": []},
                {"content": "GPU requirements 1440p: RTX 4070/RX 7800 XT high 100+ FPS, RTX 4070 Ti/RX 7900 XT ultra 120+ FPS, demanding AAA medium 80 FPS", "keywords": ["1440p", "gpu"], "difficulty": "intermediate", "tags": ["performance"], "related_tools": []},
                {"content": "GPU requirements 4K: RTX 4080 high 80+ FPS, RTX 4090/RX 7900 XTX ultra 100+ FPS, DLSS/FSR mandatory stable 60+ FPS", "keywords": ["4k", "gpu"], "difficulty": "advanced", "tags": ["performance"], "related_tools": []},
                {"content": "DLSS Quality 4K: Renders 1440p upscales to 4K, ~50% FPS boost, minimal quality loss, RTX exclusive, game support required", "keywords": ["dlss", "upscaling"], "difficulty": "intermediate", "tags": ["nvidia"], "related_tools": []},
                {"content": "FSR 2.0 Quality: AMD open upscaling, 1440p to 4K, +40% FPS, all GPUs (RTX/AMD/Intel), slightly softer than DLSS", "keywords": ["fsr", "upscaling"], "difficulty": "intermediate", "tags": ["amd"], "related_tools": []},
                {"content": "Native vs upscaled: Native resolution sharpest, DLSS/FSR Quality close, Performance mode blurry (avoid), Ultra Performance 720p base (garbage)", "keywords": ["native", "upscaling"], "difficulty": "intermediate", "tags": ["quality"], "related_tools": []},
                {"content": "Pixel pitch: 0.233mm (1080p 24\"), 0.233mm (1440p 32\"), 0.181mm (4K 32\"), smaller = sharper, <0.2mm ideal text clarity", "keywords": ["pixel pitch", "sharpness"], "difficulty": "advanced", "tags": ["specs"], "related_tools": []},
                {"content": "Desk size: 24\" desk 60cm depth, 27\" desk 80cm, 32\" desk 100cm, ultrawide 100cm minimum, viewing distance = size adjustment", "keywords": ["desk size", "space"], "difficulty": "beginner", "tags": ["ergonomics"], "related_tools": []},
                {"content": "Multi-monitor: 2x 24\" 1080p portrait+landscape (500 euros), 3x 27\" 1440p surround (1200 euros), 1x 49\" ultrawide vs 2x 27\"", "keywords": ["multi-monitor", "setup"], "difficulty": "intermediate", "tags": ["productivity"], "related_tools": []},
                {"content": "Console gaming: PS5/Xbox Series X 4K 60Hz (120Hz competitive), 1440p 120Hz budget, HDMI 2.1 required, VRR essential", "keywords": ["console", "ps5"], "difficulty": "beginner", "tags": ["gaming"], "related_tools": []},
                {"content": "Competitive advantage: 1080p 240Hz lower latency (less pixels), pro players prefer 24\" 1080p (FOV fits screen), 1440p casual", "keywords": ["competitive", "esports"], "difficulty": "intermediate", "tags": ["professional"], "related_tools": []},
                {"content": "Productivity: 1440p 27\" minimum (spreadsheets, code), 4K 32\" optimal (two windows), ultrawide 34\" best (timeline editing)", "keywords": ["productivity", "work"], "difficulty": "intermediate", "tags": ["office"], "related_tools": []},
                {"content": "Text clarity: 4K sharp text <120 PPI noticeable aliasing, 1440p 27\" adequate (ClearType), 1080p 24\" acceptable <80cm", "keywords": ["text clarity", "reading"], "difficulty": "beginner", "tags": ["productivity"], "related_tools": []},
                {"content": "ClearType tuning: Windows ClearType text tuner (cttune.exe), calibrate subpixel rendering, improves 1080p/1440p text sharpness", "keywords": ["cleartype", "windows"], "difficulty": "beginner", "tags": ["optimization"], "related_tools": ["ClearType"]},
                {"content": "Retina display: 220 PPI macOS standard, 4K 24\" = 184 PPI (closest Windows), 5K 27\" = 218 PPI (iMac), Windows scaling inferior", "keywords": ["retina", "macos"], "difficulty": "advanced", "tags": ["apple"], "related_tools": []},
                {"content": "Portrait mode: 24\" 1080p portrait (1080x1920) coding/reading, 27\" 1440p portrait (1440x2560) productivity, VESA pivot required", "keywords": ["portrait", "vertical"], "difficulty": "intermediate", "tags": ["coding"], "related_tools": []},
                {"content": "Bezels: Thin bezels <5mm multi-monitor seamless, thick bezels >10mm old monitors, bezel-less 2-3mm modern (LG/Dell)", "keywords": ["bezels", "design"], "difficulty": "beginner", "tags": ["aesthetics"], "related_tools": []},
                {"content": "PPI sweet spot: 90-110 PPI gaming (performance priority), 110-140 PPI balanced, 140+ PPI productivity (text priority)", "keywords": ["ppi", "sweet spot"], "difficulty": "intermediate", "tags": ["recommendations"], "related_tools": []},
                {"content": "1080p future-proof: Not future-proof 2024+, 1440p minimum new builds, 1080p acceptable <200 euro budget or esports only", "keywords": ["future proof", "1080p"], "difficulty": "beginner", "tags": ["buying"], "related_tools": []},
                {"content": "4K future-proof: Future-proof 5+ years, GPU tech improves (DLSS 4), 4K 144Hz becomes mainstream, 32\" 4K current high-end", "keywords": ["future proof", "4k"], "difficulty": "intermediate", "tags": ["investment"], "related_tools": []},
                {"content": "8K monitors: 7680x4320 resolution, 160+ PPI 43\"+, gaming useless (no GPU handles it), productivity overkill, 2000+ euros", "keywords": ["8k", "overkill"], "difficulty": "expert", "tags": ["extreme"], "related_tools": []},
                {"content": "21:9 vs 16:9: Ultrawide 21:9 immersive (games support varies), 16:9 universal support, competitive games disable 21:9 (unfair FOV)", "keywords": ["21:9", "16:9"], "difficulty": "intermediate", "tags": ["aspect ratio"], "related_tools": []},
                {"content": "32:9 support: Super ultrawide game support limited (black bars), productivity excel, racing/flight sims perfect, competitive games no", "keywords": ["32:9", "support"], "difficulty": "advanced", "tags": ["compatibility"], "related_tools": []},
                {"content": "Pixel response scaling: Higher res = more pixels = slightly slower response time, 1080p 1ms true, 4K 1-2ms real, negligible gaming", "keywords": ["response time", "resolution"], "difficulty": "advanced", "tags": ["performance"], "related_tools": []},
                {"content": "Budget recommendations: <200 euros 1080p 24\" 144Hz, 200-400 euros 1440p 27\" 144Hz, 400-700 euros 1440p 165Hz or 4K 120Hz", "keywords": ["budget", "recommendations"], "difficulty": "beginner", "tags": ["buying"], "related_tools": []},
                {"content": "Upgrade path: 1080p 60Hz → 1080p 144Hz (+100 euros), 1080p 144Hz → 1440p 144Hz (+200 euros), 1440p 144Hz → 4K 144Hz (+400 euros)", "keywords": ["upgrade path", "progression"], "difficulty": "intermediate", "tags": ["buying"], "related_tools": []},
                {"content": "Dual monitor setup: 1x 1440p 27\" gaming + 1x 1080p 24\" vertical productivity (500 euros total), different PPI scaling issues Windows", "keywords": ["dual monitor", "mixed"], "difficulty": "intermediate", "tags": ["setup"], "related_tools": []},
                {"content": "Matching monitors: Same brand/model multi-monitor (color matching), different models color shift, calibration required (colorimeter 200 euros)", "keywords": ["matching", "multi-monitor"], "difficulty": "intermediate", "tags": ["color"], "related_tools": []},
                {"content": "Cable bandwidth limits: HDMI 2.0 = 1440p 144Hz max (4K 60Hz), HDMI 2.1 = 4K 120Hz, DP 1.4 = 1440p 240Hz (4K 120Hz DSC)", "keywords": ["cables", "bandwidth"], "difficulty": "intermediate", "tags": ["connectivity"], "related_tools": []},
                {"content": "Resolution vs refresh rate: 1080p 240Hz esports (clarity via high FPS), 1440p 144Hz balanced, 4K 60Hz cinematic (high detail)", "keywords": ["resolution", "refresh rate"], "difficulty": "intermediate", "tags": ["tradeoff"], "related_tools": []}
            ]
        }

        # 15. Monitor Calibration
        kb["monitor_calibration"] = {
            "metadata": {
                "priority": 3,
                "tags": ["monitor", "calibration", "color", "professional"],
                "difficulty": "advanced",
                "description": "Monitor color calibration and professional settings"
            },
            "tips": [
                {"content": "sRGB 100%: Standard color gamut, 16.7M colors, web/gaming target, most monitors 95-100% coverage, wider gamut oversaturated Windows", "keywords": ["srgb", "color gamut"], "difficulty": "intermediate", "tags": ["color"], "related_tools": []},
                {"content": "DCI-P3 95%: Cinema color space, 25% wider than sRGB, HDR content, premium monitors 90-98%, Adobe RGB alternative for print", "keywords": ["dci-p3", "wide gamut"], "difficulty": "advanced", "tags": ["professional"], "related_tools": []},
                {"content": "Brightness 120-250 nits: SDR 120-150 nits comfortable (office), 250 nits bright room, <100 nits eye strain, >300 nits excessive", "keywords": ["brightness", "nits"], "difficulty": "intermediate", "tags": ["settings"], "related_tools": []},
                {"content": "Contrast 1000:1: IPS typical 1000:1, VA 3000:1+ deeper blacks, OLED infinite, low contrast <800:1 washed out", "keywords": ["contrast", "ratio"], "difficulty": "intermediate", "tags": ["specs"], "related_tools": []},
                {"content": "Gamma 2.2: Standard Windows/web, 2.4 macOS/video editing, 1.8 legacy Mac, affects shadow detail and midtones", "keywords": ["gamma", "2.2"], "difficulty": "advanced", "tags": ["calibration"], "related_tools": []},
                {"content": "Color temperature: 6500K (D65) standard daylight, 5500K warmer (print), 9300K bluish (avoid), native temp varies 6000-7000K", "keywords": ["color temperature", "6500k"], "difficulty": "intermediate", "tags": ["white point"], "related_tools": []},
                {"content": "Hardware calibration: Colorimeter (X-Rite i1Display Pro 250 euros, Calibrite ColorChecker 180 euros), creates ICC profile, 3-6 month recalibration", "keywords": ["calibration", "colorimeter"], "difficulty": "expert", "tags": ["professional"], "related_tools": ["DisplayCAL"]},
                {"content": "Software calibration: Windows Calibrate Display (basic), DisplayCAL (advanced free), requires colorimeter hardware for accuracy", "keywords": ["displaycal", "software"], "difficulty": "advanced", "tags": ["tools"], "related_tools": ["DisplayCAL"]},
                {"content": "ICC profiles: Color profile embeds calibration, Windows Color Management (colorcpl.exe), set default profile per monitor", "keywords": ["icc profile", "color management"], "difficulty": "advanced", "tags": ["windows"], "related_tools": []},
                {"content": "Factory calibration: Premium monitors pre-calibrated (DeltaE <2), Dell UltraSharp, ASUS ProArt, BenQ SW series, calibration report included", "keywords": ["factory calibration", "proart"], "difficulty": "advanced", "tags": ["professional"], "related_tools": []},
                {"content": "DeltaE <1: Imperceptible difference (professional), DeltaE <2 excellent, DeltaE <3 acceptable, DeltaE >5 visible color shift", "keywords": ["deltae", "color accuracy"], "difficulty": "expert", "tags": ["metrics"], "related_tools": []},
                {"content": "Uniformity: Center vs edges brightness deviation <10% good, >15% backlight bleed, professional monitors <5% (BenQ SW)", "keywords": ["uniformity", "brightness"], "difficulty": "advanced", "tags": ["quality"], "related_tools": []},
                {"content": "Color space modes: sRGB mode clamps wide gamut (accurate Windows), Native mode oversaturated (gaming vibrant), toggle per use case", "keywords": ["color mode", "srgb"], "difficulty": "intermediate", "tags": ["modes"], "related_tools": []},
                {"content": "Brightness calibration: White point (255,255,255) RGB balance, 120 nits target SDR, use colorimeter measure actual nits output", "keywords": ["brightness", "white point"], "difficulty": "advanced", "tags": ["calibration"], "related_tools": []},
                {"content": "Black level: Raise black point OSD (0-5 range), too low crushes shadows, too high washed blacks, test with black gradient pattern", "keywords": ["black level", "crush"], "difficulty": "intermediate", "tags": ["settings"], "related_tools": []},
                {"content": "Test patterns: Lagom LCD test patterns (dead pixels, gradient, text), EIZO monitor test (free online), uniformity tests", "keywords": ["test patterns", "lagom"], "difficulty": "intermediate", "tags": ["testing"], "related_tools": []},
                {"content": "Warm-up time: Monitors stabilize 30min warm-up before calibration, color shift first 15min, professional workflow mandatory", "keywords": ["warm-up", "stabilization"], "difficulty": "expert", "tags": ["calibration"], "related_tools": []},
                {"content": "Ambient light: 5-10 lux dark room calibration, 200-300 lux office typical, D50 viewing booth (print shops), ISO 3664 standard", "keywords": ["ambient light", "lux"], "difficulty": "expert", "tags": ["environment"], "related_tools": []},
                {"content": "Monitor aging: Backlights dim 10-20% over 5 years, color shifts warmer, recalibration yearly recommended, OLED uniform aging", "keywords": ["aging", "backlight"], "difficulty": "advanced", "tags": ["longevity"], "related_tools": []},
                {"content": "HDR calibration: Separate SDR/HDR modes (tone mapping), HDR 400/600/1000 peak brightness, Windows HDR toggle, HAGS required", "keywords": ["hdr", "calibration"], "difficulty": "expert", "tags": ["hdr"], "related_tools": []},
                {"content": "OSD presets: Standard (balanced), sRGB (accurate), Movie (warm), Game (saturated), custom profiles save calibration, use sRGB gaming", "keywords": ["osd", "presets"], "difficulty": "beginner", "tags": ["modes"], "related_tools": []},
                {"content": "Calibration frequency: Professional 1-3 months, enthusiast 6 months, casual yearly, factory calibrated 12 months first, then 6 months", "keywords": ["frequency", "recalibration"], "difficulty": "advanced", "tags": ["maintenance"], "related_tools": []},
                {"content": "RGB gains: Adjust RGB sliders OSD (white balance), reduces max brightness, avoid unless colorimeter-verified, factory reset safer", "keywords": ["rgb gains", "white balance"], "difficulty": "expert", "tags": ["advanced"], "related_tools": []},
                {"content": "6-axis color: Hue/saturation adjust individual RGBCMY, professional monitors (BenQ SW, ASUS PA), corrects factory deviations, expert only", "keywords": ["6-axis", "hue saturation"], "difficulty": "expert", "tags": ["professional"], "related_tools": []},
                {"content": "LUT calibration: 3D LUT hardware calibration (10-bit+), uploads LUT to monitor, NEC/EIZO reference monitors, Adobe RGB 100%", "keywords": ["3d lut", "hardware"], "difficulty": "expert", "tags": ["reference"], "related_tools": []},
                {"content": "Gaming vs accuracy: Gaming vibrant oversaturated (native mode), accuracy sRGB clamped (photo editing), toggle profiles per task", "keywords": ["gaming", "accuracy"], "difficulty": "intermediate", "tags": ["use case"], "related_tools": []},
                {"content": "Blue light reduction: Hardware blue light filter (TÜV certified), reduces 6500K to 5500K, eye strain relief, color accuracy suffers", "keywords": ["blue light", "tuv"], "difficulty": "beginner", "tags": ["health"], "related_tools": []},
                {"content": "Flicker-free importance: PWM-free backlights (DC dimming), <250 Hz PWM flicker causes headaches, all modern monitors 200+ euros PWM-free", "keywords": ["flicker-free", "pwm"], "difficulty": "intermediate", "tags": ["health"], "related_tools": []},
                {"content": "Print vs screen: Print Adobe RGB/CMYK, screen sRGB/Rec.709, soft proofing (simulate print on screen), calibrated workflow critical", "keywords": ["print", "soft proofing"], "difficulty": "expert", "tags": ["workflow"], "related_tools": []},
                {"content": "Video editing: Rec.709 (HD video) = sRGB, Rec.2020 (HDR/UHD) wider gamut, LG 27UP850 (DCI-P3 95%), color-critical grading needs reference monitor", "keywords": ["video editing", "rec.709"], "difficulty": "advanced", "tags": ["professional"], "related_tools": []},
                {"content": "Photography workflow: Adobe RGB 98% for print, sRGB 100% for web, wide gamut monitor (99% Adobe RGB = BenQ SW270C 500 euros)", "keywords": ["photography", "adobe rgb"], "difficulty": "advanced", "tags": ["professional"], "related_tools": []},
                {"content": "Color banding: 8-bit 16.7M colors (banding visible gradients), 10-bit 1.07B colors (smooth gradients), HDR requires 10-bit panel", "keywords": ["color banding", "10-bit"], "difficulty": "advanced", "tags": ["specs"], "related_tools": []},
                {"content": "Night mode: Windows Night Light (warm 3000K evening), f.lux alternative, hardware low-blue mode, circadian rhythm friendly", "keywords": ["night mode", "flux"], "difficulty": "beginner", "tags": ["health"], "related_tools": ["f.lux"]},
                {"content": "Colorimeter budget: X-Rite i1Display Pro (250 euros gold standard), Calibrite ColorChecker Display (180 euros), Spyder X (130 euros budget)", "keywords": ["colorimeter", "budget"], "difficulty": "advanced", "tags": ["tools"], "related_tools": []},
                {"content": "Built-in calibration: Dell UltraSharp built-in colorimeter (UP2720Q 1200 euros), auto-calibration scheduled, professional feature rare", "keywords": ["built-in", "auto calibration"], "difficulty": "expert", "tags": ["premium"], "related_tools": []},
                {"content": "Color checker: X-Rite ColorChecker Passport (100 euros), photograph reference patches, camera + monitor calibration workflow", "keywords": ["color checker", "reference"], "difficulty": "expert", "tags": ["photography"], "related_tools": []},
                {"content": "Monitor hoods: Reduces ambient light reflections (photo editing), 50-150 euros (BenQ hood SW series), DIY cardboard alternative", "keywords": ["hood", "reflections"], "difficulty": "advanced", "tags": ["accessory"], "related_tools": []},
                {"content": "Calibration targets: Brightness 120 nits, Gamma 2.2, White Point D65 (6500K), Color Space sRGB, standard workflow, adjust per industry", "keywords": ["targets", "standards"], "difficulty": "advanced", "tags": ["calibration"], "related_tools": []},
                {"content": "Multi-monitor calibration: Calibrate each monitor separately, brightness match critical (100 vs 120 nits noticeable), ICC per monitor", "keywords": ["multi-monitor", "matching"], "difficulty": "advanced", "tags": ["setup"], "related_tools": []},
                {"content": "Professional monitor recommendations: ASUS ProArt PA279CV (450 euros 4K 100% sRGB), BenQ SW270C (500 euros 99% Adobe RGB), EIZO ColorEdge CS2740 (1300 euros reference)", "keywords": ["professional", "recommendations"], "difficulty": "expert", "tags": ["buying"], "related_tools": []}
            ]
        }

        # =============================================================================
        # PERIPHERALS (2 catégories - ~80 conseils)
        # =============================================================================

        # 16. Gaming Mice Sensors
        kb["gaming_mice_sensors"] = {
            "metadata": {
                "priority": 4,
                "tags": ["mouse", "gaming", "sensor", "peripherals"],
                "difficulty": "intermediate",
                "description": "Gaming mouse sensors, DPI, polling rate, wireless technology"
            },
            "tips": [
                {"content": "PixArt PAW3395: Flagship sensor 26000 DPI, 650 IPS, 50G acceleration, flawless tracking, Logitech G Pro X Superlight 2", "keywords": ["paw3395", "pixart"], "difficulty": "advanced", "tags": ["flagship"], "related_tools": []},
                {"content": "Polling rate 1000Hz: 1ms response time standard gaming, 8000Hz (0.125ms) overkill competitive (Razer 8KHz), CPU overhead 1-2%", "keywords": ["polling rate", "1000hz"], "difficulty": "intermediate", "tags": ["performance"], "related_tools": []},
                {"content": "Wireless <1ms: Modern wireless (Lightspeed, HyperSpeed) faster than wired, 2.4GHz dongle, Bluetooth 10-20ms latency (avoid gaming)", "keywords": ["wireless", "latency"], "difficulty": "intermediate", "tags": ["wireless"], "related_tools": []},
                {"content": "Weight 60-80g: Ultralight mice meta (Logitech G Pro X Superlight 63g), <60g fragile, >80g slow flicks, preference varies", "keywords": ["weight", "ultralight"], "difficulty": "beginner", "tags": ["design"], "related_tools": []},
                {"content": "Logitech G Pro X Superlight: 135 euros, 63g, PAW3395 sensor, 70h battery, top-tier wireless, pro esports standard", "keywords": ["logitech", "superlight"], "difficulty": "intermediate", "tags": ["premium"], "related_tools": ["G HUB"]},
                {"content": "DPI settings: 400-800 DPI low sens (arm aim CS/VALORANT), 1600-3200 DPI high sens (wrist aim Overwatch), 800 DPI most popular", "keywords": ["dpi", "sensitivity"], "difficulty": "beginner", "tags": ["settings"], "related_tools": []},
                {"content": "Sensor position: Center sensor (Logitech) balanced, front sensor (Razer Viper) low sens, position affects turning radius", "keywords": ["sensor position", "placement"], "difficulty": "advanced", "tags": ["design"], "related_tools": []},
                {"content": "Lift-off distance: 1-2mm optimal (PixArt 3395), <1mm too sensitive (unintended tracking), >2mm tracks too high, adjustable software", "keywords": ["lod", "lift-off distance"], "difficulty": "intermediate", "tags": ["tuning"], "related_tools": []},
                {"content": "Debounce delay: Click latency 2-8ms factory, 0ms gaming mode (double-click risk), Razer Optical switches 0.2ms (light beam)", "keywords": ["debounce", "click latency"], "difficulty": "advanced", "tags": ["switches"], "related_tools": []},
                {"content": "Optical switches: Razer Optical, Roccat Titan Optical, 0.2ms actuation (vs 2ms mechanical), 70M click lifespan, no double-click degradation", "keywords": ["optical", "switches"], "difficulty": "intermediate", "tags": ["technology"], "related_tools": []},
                {"content": "Mechanical switches: Omron 50M standard, Kailh GM 8.0 80M, 2-5ms actuation, double-click issue 1-2 years heavy use", "keywords": ["mechanical", "omron"], "difficulty": "intermediate", "tags": ["switches"], "related_tools": []},
                {"content": "Shape: Ergonomic (Zowie EC series, Razer DeathAdder) right-hand, ambidextrous (G Pro, Viper) versatile, claw/palm/fingertip grip preference", "keywords": ["shape", "ergonomic"], "difficulty": "beginner", "tags": ["comfort"], "related_tools": []},
                {"content": "Grip style: Palm (full hand contact, large mice), claw (arched fingers, medium mice), fingertip (tips only, small mice 60-70g)", "keywords": ["grip style", "palm claw"], "difficulty": "beginner", "tags": ["technique"], "related_tools": []},
                {"content": "Sensor acceleration: Flawless sensors (3395, 3370, HERO 25K) zero acceleration, old sensors (3310) predictive angle correction", "keywords": ["acceleration", "flawless"], "difficulty": "advanced", "tags": ["accuracy"], "related_tools": []},
                {"content": "Jitter: Sensor noise at low speeds (pixel skipping), PixArt 3395/HERO 25K zero jitter, cheap sensors (<30 euros mice) jittery", "keywords": ["jitter", "sensor noise"], "difficulty": "intermediate", "tags": ["quality"], "related_tools": []},
                {"content": "Smoothing: Built-in sensor prediction (removes micro-adjustments), modern sensors disable smoothing, check reviews (blur busters test)", "keywords": ["smoothing", "prediction"], "difficulty": "advanced", "tags": ["accuracy"], "related_tools": []},
                {"content": "Battery life: Logitech G Pro X Superlight 70h, Razer Viper V2 Pro 80h, wireless charging mice (Logitech PowerPlay 120 euros mat)", "keywords": ["battery", "wireless"], "difficulty": "intermediate", "tags": ["wireless"], "related_tools": []},
                {"content": "Cable: Paracord (ultralight braided), Type-C detachable, wireless meta (no cable drag), bungee 20 euros reduces drag wired", "keywords": ["cable", "paracord"], "difficulty": "beginner", "tags": ["wired"], "related_tools": []},
                {"content": "Feet (skates): PTFE (Teflon) smooth glide, thickness 0.6-0.8mm, aftermarket Tiger Ice/Corepads 10 euros, glass skates (Superglides) premium", "keywords": ["feet", "ptfe"], "difficulty": "intermediate", "tags": ["glide"], "related_tools": []},
                {"content": "Mousepad surface: Cloth pads (control 30-40 euros), hard pads (speed, durability), hybrid (Artisan), affects feet glide speed", "keywords": ["mousepad", "surface"], "difficulty": "intermediate", "tags": ["accessory"], "related_tools": []},
                {"content": "Software bloat: Logitech G HUB (300MB), Razer Synapse (500MB), onboard memory saves profiles (software-free), avoid RGB bloat", "keywords": ["software", "bloat"], "difficulty": "beginner", "tags": ["software"], "related_tools": ["G HUB", "Synapse"]},
                {"content": "Onboard memory: Store DPI/macros in mouse (no software dependency), 5 profiles typical, Logitech/Zowie strong onboard support", "keywords": ["onboard memory", "profiles"], "difficulty": "intermediate", "tags": ["portability"], "related_tools": []},
                {"content": "RGB vs non-RGB: RGB adds 10-20 euros cost, battery drain (wireless 70h → 40h RGB), weight +5-10g, disable RGB save battery", "keywords": ["rgb", "lighting"], "difficulty": "beginner", "tags": ["aesthetics"], "related_tools": []},
                {"content": "Pro player choices: Logitech G Pro X Superlight (40% market), Zowie EC2/S2 (30%), Razer Viper V2 Pro (15%), lightweight trend", "keywords": ["pro players", "esports"], "difficulty": "intermediate", "tags": ["competitive"], "related_tools": []},
                {"content": "Zowie EC2: Ergonomic right-hand, plug-and-play (no software), 3370 sensor, 70g, 80 euros, CS:GO/VALORANT favorite", "keywords": ["zowie", "ec2"], "difficulty": "intermediate", "tags": ["esports"], "related_tools": []},
                {"content": "Razer Viper V2 Pro: 58g lightest flagship, Focus Pro 30K sensor, 80h battery, 150 euros, ambidextrous, optical switches", "keywords": ["razer", "viper"], "difficulty": "advanced", "tags": ["ultralight"], "related_tools": ["Synapse"]},
                {"content": "Budget wired: Logitech G203 (25 euros 8000 DPI HERO), Razer Viper Mini (30 euros 8500 DPI), DeathAdder Essential (35 euros)", "keywords": ["budget", "wired"], "difficulty": "beginner", "tags": ["value"], "related_tools": []},
                {"content": "Budget wireless: Logitech G305 (50 euros HERO, AA battery 250h), Razer Orochi V2 (60 euros dual AA/AAA, 950h battery)", "keywords": ["budget", "wireless"], "difficulty": "beginner", "tags": ["value"], "related_tools": []},
                {"content": "Size: Small <120mm (fingertip/small hands), Medium 120-130mm (claw/medium hands), Large >130mm (palm/large hands), measure hand 17-21cm", "keywords": ["size", "hand size"], "difficulty": "beginner", "tags": ["sizing"], "related_tools": []},
                {"content": "DPI marketing: 26000 DPI useless (sensor flex), 3200 DPI max practical, >10000 DPI marketing gimmick, 400-1600 DPI real usage", "keywords": ["dpi marketing", "gimmick"], "difficulty": "beginner", "tags": ["myths"], "related_tools": []},
                {"content": "Angle snapping: Straightens diagonal lines (removes hand shake), competitive disadvantage (less control), disable in software", "keywords": ["angle snapping", "correction"], "difficulty": "intermediate", "tags": ["settings"], "related_tools": []},
                {"content": "Surface calibration: Software calibrates sensor to pad (Logitech Surface Tuning), improves tracking accuracy colored pads, minor gains", "keywords": ["calibration", "surface tuning"], "difficulty": "advanced", "tags": ["optimization"], "related_tools": []},
                {"content": "Wireless dongle placement: USB extension cable (closer to mouse), reduces interference, 2.4GHz WiFi/Bluetooth conflicts", "keywords": ["dongle", "wireless"], "difficulty": "intermediate", "tags": ["optimization"], "related_tools": []},
                {"content": "Report rate vs DPI: 1000Hz polling samples 1000/sec, 800 DPI @ 1000Hz = 0.8 pixel precision, higher DPI ≠ accuracy (placebo)", "keywords": ["report rate", "dpi"], "difficulty": "advanced", "tags": ["technical"], "related_tools": []},
                {"content": "MOA (Minutes of Angle): Sensor accuracy metric, <0.5 MOA excellent (3395, HERO 25K), >1 MOA noticeable inaccuracy cheap sensors", "keywords": ["moa", "accuracy"], "difficulty": "expert", "tags": ["metrics"], "related_tools": []},
                {"content": "Warranty: 2 years standard, Logitech 3 years, Razer 2 years, double-click issues common (RMA frequent), optical switches solve issue", "keywords": ["warranty", "rma"], "difficulty": "intermediate", "tags": ["support"], "related_tools": []},
                {"content": "Modding: Paracord cable mod (20 euros), aftermarket feet (10 euros), weight reduction (remove battery cover), voids warranty", "keywords": ["modding", "custom"], "difficulty": "advanced", "tags": ["enthusiast"], "related_tools": []},
                {"content": "Glossy vs matte: Glossy grip sweaty hands (better control), matte dry hands (comfort), coating wears 1-2 years heavy use", "keywords": ["coating", "glossy matte"], "difficulty": "beginner", "tags": ["finish"], "related_tools": []},
                {"content": "Side buttons: 2 side buttons standard (thumb), MMO mice 12+ buttons (Razer Naga), macro programming, competitive 2 buttons sufficient", "keywords": ["side buttons", "macros"], "difficulty": "beginner", "tags": ["features"], "related_tools": []},
                {"content": "Value pick 2024: Logitech G Pro X Superlight (135 euros flagship), G305 (50 euros budget wireless), Viper V2 Pro (150 euros ultralight)", "keywords": ["value", "2024"], "difficulty": "beginner", "tags": ["recommendations"], "related_tools": []}
            ]
        }

        # 17. Mechanical Keyboards
        kb["mechanical_keyboards"] = {
            "metadata": {
                "priority": 3,
                "tags": ["keyboard", "mechanical", "switches", "peripherals"],
                "difficulty": "intermediate",
                "description": "Mechanical keyboard switches, keycaps, layouts"
            },
            "tips": [
                {"content": "Cherry MX Red: Linear smooth, 45g actuation force, quiet gaming, no tactile bump, Cherry switches gold standard 100M clicks", "keywords": ["cherry mx", "red linear"], "difficulty": "beginner", "tags": ["gaming"], "related_tools": []},
                {"content": "Cherry MX Brown: Tactile bump 55g, typing + gaming hybrid, subtle feedback, quieter than Blue, office-friendly", "keywords": ["cherry mx", "brown tactile"], "difficulty": "beginner", "tags": ["typing"], "related_tools": []},
                {"content": "Cherry MX Blue: Clicky loud, 60g actuation, tactile + audible click, typing satisfaction, gaming lag (reset point), office noise complaint", "keywords": ["cherry mx", "blue clicky"], "difficulty": "beginner", "tags": ["typing"], "related_tools": []},
                {"content": "Gateron switches: Cherry clone cheaper (30% less cost), Yellow/Red linear smooth, Brown tactile, quality comparable, budget boards", "keywords": ["gateron", "clone"], "difficulty": "beginner", "tags": ["budget"], "related_tools": []},
                {"content": "Kailh switches: Box switches (dust/waterproof IP56), Speed switches (1.1mm actuation gaming), cheaper than Cherry, good alternatives", "keywords": ["kailh", "box switches"], "difficulty": "intermediate", "tags": ["alternative"], "related_tools": []},
                {"content": "Hot-swap sockets: Replace switches without soldering (Gateron/Kailh hot-swap), try different switches, 5-pin/3-pin compatibility", "keywords": ["hot-swap", "sockets"], "difficulty": "intermediate", "tags": ["modding"], "related_tools": []},
                {"content": "Lubing stabilizers: Stock stabs rattle, Krytox 205g0 lube (15 euros 5ml), band-aid mod, eliminates spacebar rattle, sounds thocky", "keywords": ["lubing", "stabilizers"], "difficulty": "advanced", "tags": ["modding"], "related_tools": []},
                {"content": "Keycap material: ABS (cheap, shiny wear), PBT (durable, texture), double-shot legends (no fade), dye-sublimation (PBT premium)", "keywords": ["keycaps", "pbt abs"], "difficulty": "intermediate", "tags": ["keycaps"], "related_tools": []},
                {"content": "Layout: Full-size (104 keys numpad), TKL (87 keys tenkeyless), 75% compact (Function row), 60% minimal (no arrows programmable)", "keywords": ["layout", "tkl 60%"], "difficulty": "beginner", "tags": ["form factor"], "related_tools": []},
                {"content": "Actuation force: 45g light (Red linear gaming), 55-60g medium (Brown/Blue typing), 65g+ heavy (Black linear fatigue), preference varies", "keywords": ["actuation force", "45g"], "difficulty": "intermediate", "tags": ["feel"], "related_tools": []},
                {"content": "Travel distance: 4mm total travel (Cherry standard), 2mm actuation point, short travel (1.5mm Speed Silver gaming), longer = typing comfort", "keywords": ["travel distance", "actuation"], "difficulty": "intermediate", "tags": ["specs"], "related_tools": []},
                {"content": "N-key rollover: NKRO (unlimited simultaneous keys), 6KRO acceptable gaming, anti-ghosting, USB vs PS/2 (PS/2 true NKRO)", "keywords": ["nkro", "rollover"], "difficulty": "intermediate", "tags": ["gaming"], "related_tools": []},
                {"content": "Polling rate: 1000Hz standard, keyboards less critical than mice (typing vs tracking), wireless 1000Hz modern (vs old 125Hz Bluetooth)", "keywords": ["polling rate", "1000hz"], "difficulty": "beginner", "tags": ["latency"], "related_tools": []},
                {"content": "Wireless latency: 2.4GHz dongle <1ms (Logitech Lightspeed), Bluetooth 10-20ms (typing OK, gaming lag), wired 0ms guaranteed", "keywords": ["wireless", "latency"], "difficulty": "intermediate", "tags": ["wireless"], "related_tools": []},
                {"content": "RGB backlighting: Per-key RGB customizable, software bloat (iCUE/Synapse), brightness drain battery wireless, white LED cleaner", "keywords": ["rgb", "backlighting"], "difficulty": "beginner", "tags": ["aesthetics"], "related_tools": []},
                {"content": "Battery life wireless: Logitech G915 TKL 40h RGB on (135h RGB off), Keychron K8 Pro 90h, battery vs wired reliability trade-off", "keywords": ["battery", "wireless"], "difficulty": "intermediate", "tags": ["wireless"], "related_tools": []},
                {"content": "Software: VIA/QMK (open-source custom firmware), Logitech G HUB, Razer Synapse, macro recording, key remapping, onboard memory", "keywords": ["software", "via qmk"], "difficulty": "advanced", "tags": ["customization"], "related_tools": ["VIA", "QMK"]},
                {"content": "Custom keyboards: Build from scratch (PCB 50 euros, switches 40 euros, case 80 euros, keycaps 60 euros), 250+ euros total, enthusiast hobby", "keywords": ["custom", "diy"], "difficulty": "expert", "tags": ["enthusiast"], "related_tools": []},
                {"content": "Sound: Thocky deep (lubed linear + PBT keycaps), clacky high-pitch (stock switches + ABS), foam mods (case foam, plate foam) dampen", "keywords": ["sound", "thocky"], "difficulty": "advanced", "tags": ["acoustics"], "related_tools": []},
                {"content": "Switch types: Linear (Red/Black no bump), Tactile (Brown bump no click), Clicky (Blue bump + click), silent (Pink dampened)", "keywords": ["switch types", "linear tactile"], "difficulty": "beginner", "tags": ["basics"], "related_tools": []},
                {"content": "Speed switches: Cherry MX Speed Silver (1.2mm actuation), 45g light, gaming fast response, typos easier (sensitive), Kailh Speed alternatives", "keywords": ["speed silver", "gaming"], "difficulty": "intermediate", "tags": ["gaming"], "related_tools": []},
                {"content": "Silent switches: Cherry MX Silent Red/Black, dampened sliders, <30 dBA quiet, office/late-night gaming, mushy feel (less tactile feedback)", "keywords": ["silent", "quiet"], "difficulty": "intermediate", "tags": ["silent"], "related_tools": []},
                {"content": "Optical switches: Light-beam actuation (no metal contact), 0.2ms response (Razer Huntsman), 100M clicks lifespan, no debounce delay", "keywords": ["optical", "razer huntsman"], "difficulty": "advanced", "tags": ["technology"], "related_tools": []},
                {"content": "Hall effect: Magnetic switches (Wooting), analog input (0-4mm variable actuation), rapid trigger (instant reset), competitive advantage", "keywords": ["hall effect", "wooting"], "difficulty": "expert", "tags": ["analog"], "related_tools": []},
                {"content": "Rapid trigger: Wooting 60HE feature, key resets instantly (no need full release), counter-strafing CS/VALORANT advantage, 300 euros premium", "keywords": ["rapid trigger", "wooting"], "difficulty": "expert", "tags": ["competitive"], "related_tools": []},
                {"content": "Typing speed: Tactile (Brown) best typing (feedback), Linear (Red) fast gaming (less resistance), Clicky (Blue) satisfying (slow reset)", "keywords": ["typing speed", "wpm"], "difficulty": "intermediate", "tags": ["performance"], "related_tools": []},
                {"content": "Wrist rest: Foam/gel wrist support, reduces strain long typing, 20-40 euros, wooden rests premium (50-80 euros), ergonomic keyboards built-in", "keywords": ["wrist rest", "ergonomics"], "difficulty": "beginner", "tags": ["comfort"], "related_tools": []},
                {"content": "Logitech G915 TKL: Wireless flagship 200 euros, low-profile GL switches (Tactile/Linear/Clicky), 40h battery, premium aluminum", "keywords": ["logitech", "g915"], "difficulty": "advanced", "tags": ["premium"], "related_tools": ["G HUB"]},
                {"content": "Keychron K8 Pro: Hot-swap wireless 100 euros, VIA/QMK programmable, Gateron switches, PBT keycaps, Mac/Windows, value pick", "keywords": ["keychron", "k8 pro"], "difficulty": "intermediate", "tags": ["value"], "related_tools": ["VIA"]},
                {"content": "Corsair K70 RGB: Wired gaming 150 euros, Cherry MX switches, aluminum frame, iCUE software, dedicated media keys, reliable", "keywords": ["corsair", "k70"], "difficulty": "intermediate", "tags": ["gaming"], "related_tools": ["iCUE"]},
                {"content": "Budget picks: Royal Kludge RK84 (60 euros hot-swap wireless), Keychron C1 (50 euros wired), Redragon K552 (40 euros TKL Outemu)", "keywords": ["budget", "value"], "difficulty": "beginner", "tags": ["budget"], "related_tools": []},
                {"content": "ISO vs ANSI: ANSI (US layout 104 keys), ISO (UK/EU 105 keys, tall Enter), keycap compatibility ANSI wider, layout preference regional", "keywords": ["iso", "ansi"], "difficulty": "beginner", "tags": ["layout"], "related_tools": []},
                {"content": "Plate material: Aluminum plate stiff (firm typing), brass plate heavy (deeper sound), polycarbonate flex (soft bottom-out), affects feel", "keywords": ["plate", "material"], "difficulty": "advanced", "tags": ["modding"], "related_tools": []},
                {"content": "Case material: Plastic budget (light 600g), aluminum premium (heavy 1kg+, solid feel), wooden cases (thocky acoustics 80-150 euros)", "keywords": ["case", "material"], "difficulty": "intermediate", "tags": ["build"], "related_tools": []},
                {"content": "Dampening mods: Case foam (40 euros kit), plate foam, Sorbothane (vibration damping), tape mod (3-4 layers masking tape PCB back)", "keywords": ["dampening", "mods"], "difficulty": "advanced", "tags": ["sound"], "related_tools": []},
                {"content": "Spring ping: Stock switches spring noise, lube springs (Krytox 105 oil), aftermarket springs (TX springs 15 euros), eliminates ping", "keywords": ["spring ping", "lubing"], "difficulty": "advanced", "tags": ["modding"], "related_tools": []},
                {"content": "Cleaning: Keycap puller (remove keycaps), denture tablets soak (PBT safe), compressed air dust, never dishwasher (warping)", "keywords": ["cleaning", "maintenance"], "difficulty": "beginner", "tags": ["upkeep"], "related_tools": []},
                {"content": "Macros: Program complex key sequences, gaming macros (MMO rotation), productivity shortcuts, onboard memory vs software dependency", "keywords": ["macros", "programming"], "difficulty": "intermediate", "tags": ["productivity"], "related_tools": []},
                {"content": "Ergonomic splits: Microsoft Sculpt (50 euros membrane), Kinesis Advantage 360 (400 euros mechanical), split layout learning curve 1-2 weeks", "keywords": ["ergonomic", "split"], "difficulty": "advanced", "tags": ["health"], "related_tools": []},
                {"content": "Artisan keycaps: Custom resin keycaps 30-100 euros each, Escape/Enter key aesthetics, collectible hobby, Etsy/Jellykey", "keywords": ["artisan", "keycaps"], "difficulty": "advanced", "tags": ["aesthetics"], "related_tools": []},
                {"content": "Warranty: 2 years standard, Corsair/Logitech reliable RMA, cheaper brands 1 year, switch failure 5+ years rare (50M+ clicks)", "keywords": ["warranty", "lifespan"], "difficulty": "beginner", "tags": ["support"], "related_tools": []}
            ]
        }
'''

    return categories_code


def add_categories_to_file(file_path, categories_code):
    """Ajoute les catégories au fichier ai_knowledge_unified.py"""

    print(f"[READ] Lecture du fichier: {file_path}")

    # Lire le fichier
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # Trouver "return kb"
    return_pattern = r'(\n\s+return kb\s*\n)'

    if not re.search(return_pattern, content):
        print("[ERROR] 'return kb' non trouve dans le fichier!")
        return False

    print("[OK] Pattern 'return kb' trouve")

    # Insérer les catégories AVANT "return kb"
    new_content = re.sub(
        return_pattern,
        categories_code + r'\1',
        content,
        count=1
    )

    # Sauvegarder
    print(f"[SAVE] Sauvegarde des modifications...")
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(new_content)

    print("[OK] Fichier modifie avec succes!")
    return True


def count_categories_and_tips(file_path):
    """Compte les catégories et conseils dans le fichier"""

    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # Compter kb["..."] = {
    categories = re.findall(r'kb\["([^"]+)"\]\s*=\s*\{', content)

    # Compter {"content": dans tips
    tips = re.findall(r'\{"content":', content)

    return len(categories), len(tips)


def main():
    """Fonction principale"""

    print("=" * 80)
    print("AJOUT DE 22 CATEGORIES A AI_KNOWLEDGE_UNIFIED.PY")
    print("=" * 80)

    file_path = r"C:\Users\Utilisateur\Downloads\Nitrite-V18.5\src\v14_mvp\ai_knowledge_unified.py"

    # État initial
    print("\n[STATS] ETAT INITIAL:")
    initial_cats, initial_tips = count_categories_and_tips(file_path)
    print(f"   - Categories: {initial_cats}")
    print(f"   - Conseils: {initial_tips}")

    # Générer le code
    print("\n[PROCESS] Generation du code des 22 categories...")
    categories_code = create_categories_code()

    # Ajouter au fichier
    print("\n[PROCESS] Modification du fichier...")
    success = add_categories_to_file(file_path, categories_code)

    if not success:
        print("\n[ERROR] ECHEC de l'operation")
        return

    # État final
    print("\n[STATS] ETAT FINAL:")
    final_cats, final_tips = count_categories_and_tips(file_path)
    print(f"   - Categories: {final_cats} (+{final_cats - initial_cats})")
    print(f"   - Conseils: {final_tips} (+{final_tips - initial_tips})")

    print("\n" + "=" * 80)
    print("[SUCCESS] OPERATION REUSSIE!")
    print("=" * 80)
    print(f"\n[FILE] Fichier mis a jour: {file_path}")
    print(f"\n[SUMMARY] AJOUTS:")
    print(f"   - {final_cats - initial_cats} nouvelles categories")
    print(f"   - {final_tips - initial_tips} nouveaux conseils")
    print(f"\n[TOTAL] {final_cats} categories | {final_tips} conseils")


if __name__ == "__main__":
    main()
