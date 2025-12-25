#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Script pour ajouter massivement 28 nouvelles catégories à ai_knowledge_unified.py
Génère du code Python avec des conseils RÉELS et UTILES
"""

import os


def generate_new_categories():
    """Génère le code Python pour les 28 nouvelles catégories"""

    categories_code = '''
        # =============================================================================
        # RAM OPTIMIZATION (2 catégories)
        # =============================================================================

        # 5. RAM DDR5 Tuning
        kb["ram_ddr5_tuning"] = {
            "metadata": {
                "priority": 5,
                "tags": ["ram", "ddr5", "memory", "overclocking"],
                "difficulty": "advanced",
                "description": "DDR5 memory tuning and optimization"
            },
            "tips": [
                {
                    "content": "DDR5-6000 CL30: Sweet spot for Intel 12th-14th gen and AMD Ryzen 7000, balances speed and latency, widely available under 200 euros for 32GB kit",
                    "keywords": ["ddr5-6000", "cl30", "sweet spot", "timing"],
                    "difficulty": "intermediate",
                    "tags": ["memory", "value"],
                    "related_tools": ["CPU-Z", "AIDA64"]
                },
                {
                    "content": "DDR5-6400 CL32: Good AMD EXPO profiles, maintains 1:1 FCLK on most Ryzen 7000 CPUs, better than 6600+ which often drops to 2:1 ratio",
                    "keywords": ["ddr5-6400", "expo", "fclk", "amd"],
                    "difficulty": "advanced",
                    "tags": ["amd", "optimization"],
                    "related_tools": ["CPU-Z"]
                },
                {
                    "content": "DDR5-7200+ enthusiast: Requires Intel Z790 high-end boards, Gear 2 mode (2:1 IMC), diminishing returns for gaming, productivity gains 2-3%",
                    "keywords": ["ddr5-7200", "gear 2", "enthusiast", "intel"],
                    "difficulty": "expert",
                    "tags": ["intel", "overclocking"],
                    "related_tools": ["AIDA64"]
                },
                {
                    "content": "XMP 3.0 profiles: Intel 12th-14th gen support multiple profiles per DIMM, test each profile for stability, Profile 1 usually most compatible",
                    "keywords": ["xmp 3.0", "profiles", "intel"],
                    "difficulty": "intermediate",
                    "tags": ["intel"],
                    "related_tools": []
                },
                {
                    "content": "EXPO vs XMP: EXPO optimized for AMD Ryzen 7000, XMP for Intel, both work cross-platform but best stability with matching platform",
                    "keywords": ["expo", "xmp", "compatibility"],
                    "difficulty": "beginner",
                    "tags": ["compatibility"],
                    "related_tools": []
                },
                {
                    "content": "Primary timings DDR5: CL (CAS Latency) 30-40 typical, tRCD 30-40, tRP 30-40, tRAS 52-80, lower is better but requires voltage increase",
                    "keywords": ["timings", "cas latency", "trcd", "trp"],
                    "difficulty": "advanced",
                    "tags": ["overclocking"],
                    "related_tools": ["CPU-Z"]
                },
                {
                    "content": "Secondary timings: tRFC (Refresh Cycle) 200-400ns critical for performance, tWR 10-16, tRTP 8-12, tWTRS/L adjust for stability",
                    "keywords": ["secondary timings", "trfc", "twr"],
                    "difficulty": "expert",
                    "tags": ["overclocking"],
                    "related_tools": ["AIDA64"]
                },
                {
                    "content": "DDR5 voltage: 1.25V JEDEC standard, 1.35V typical XMP/EXPO, 1.40V safe max 24/7, 1.45-1.50V extreme OC (cooling required)",
                    "keywords": ["voltage", "1.35v", "1.40v", "safe"],
                    "difficulty": "advanced",
                    "tags": ["voltage"],
                    "related_tools": ["HWiNFO64"]
                },
                {
                    "content": "VDDQ voltage: Controls memory IC voltage, 1.25-1.35V typical, increase +0.05V if unstable at high frequencies, separate from VDD",
                    "keywords": ["vddq", "memory voltage", "stability"],
                    "difficulty": "expert",
                    "tags": ["voltage"],
                    "related_tools": []
                },
                {
                    "content": "TX VDDQ: Transmit voltage for memory bus, 1.25-1.35V, adjust if training fails during POST, increases signal integrity",
                    "keywords": ["tx vddq", "training", "post"],
                    "difficulty": "expert",
                    "tags": ["troubleshooting"],
                    "related_tools": []
                },
                {
                    "content": "MC (Memory Controller) voltage: 1.25-1.35V for high frequency DDR5, too high degrades CPU IMC, increase if 7200+ unstable",
                    "keywords": ["mc voltage", "imc", "memory controller"],
                    "difficulty": "expert",
                    "tags": ["voltage"],
                    "related_tools": []
                },
                {
                    "content": "Gear modes Intel: Gear 1 (1:1 ratio) up to DDR5-6400, Gear 2 (2:1) for 6600+, Gear 1 lower latency better gaming, Gear 2 higher bandwidth",
                    "keywords": ["gear mode", "gear 1", "gear 2", "intel"],
                    "difficulty": "advanced",
                    "tags": ["intel"],
                    "related_tools": ["CPU-Z"]
                },
                {
                    "content": "1:1 FCLK sync AMD: Match FCLK (Fabric Clock) to half of DDR5 speed, DDR5-6000 = 3000 MHz FCLK, desync increases latency 10-20ns",
                    "keywords": ["fclk", "1:1 ratio", "infinity fabric", "amd"],
                    "difficulty": "advanced",
                    "tags": ["amd"],
                    "related_tools": ["CPU-Z", "AIDA64"]
                },
                {
                    "content": "Memory training: BIOS process to find stable settings, takes 1-5 minutes on DDR5, multiple reboots normal, disable fast boot for reliability",
                    "keywords": ["memory training", "boot", "bios"],
                    "difficulty": "intermediate",
                    "tags": ["troubleshooting"],
                    "related_tools": []
                },
                {
                    "content": "MemTest86: Boot from USB, run 4 passes minimum for stability validation, errors indicate bad timings/voltage or defective RAM",
                    "keywords": ["memtest86", "stability", "testing"],
                    "difficulty": "intermediate",
                    "tags": ["testing"],
                    "related_tools": ["MemTest86"]
                },
                {
                    "content": "TM5 with anta777 config: Windows memory stress test, 3 cycles minimum, catches errors faster than MemTest86, community standard",
                    "keywords": ["tm5", "anta777", "stress test"],
                    "difficulty": "advanced",
                    "tags": ["testing"],
                    "related_tools": ["TestMem5"]
                },
                {
                    "content": "Y-Cruncher RAM test: Tests both CPU and RAM, 2.5B digits stable = good OC, 10B+ for extreme validation, free and fast",
                    "keywords": ["y-cruncher", "validation", "free"],
                    "difficulty": "advanced",
                    "tags": ["testing"],
                    "related_tools": ["y-cruncher"]
                },
                {
                    "content": "Dual channel mandatory: Install RAM in slots 2+4 (A2/B2) for dual channel, 2x16GB better than 1x32GB, bandwidth doubles vs single channel",
                    "keywords": ["dual channel", "slots", "a2 b2", "bandwidth"],
                    "difficulty": "beginner",
                    "tags": ["installation"],
                    "related_tools": ["CPU-Z"]
                },
                {
                    "content": "Quad channel limitations: Consumer platforms (AM5, LGA1700) are dual channel only, quad channel requires HEDT (Threadripper, Xeon)",
                    "keywords": ["quad channel", "dual channel", "hedt"],
                    "difficulty": "intermediate",
                    "tags": ["architecture"],
                    "related_tools": []
                },
                {
                    "content": "Samsung B-die equivalent DDR5: Hynix A-die and M-die best overclocking potential, SK Hynix chips dominate DDR5 market, check Thaiphoon Burner",
                    "keywords": ["hynix", "a-die", "m-die", "overclocking"],
                    "difficulty": "expert",
                    "tags": ["hardware"],
                    "related_tools": ["Thaiphoon Burner"]
                },
                {
                    "content": "JEDEC fallback: DDR5 defaults to 4800 MT/s if XMP/EXPO disabled, enable XMP in BIOS for rated speeds, mandatory for performance",
                    "keywords": ["jedec", "4800", "default", "xmp"],
                    "difficulty": "beginner",
                    "tags": ["bios"],
                    "related_tools": []
                },
                {
                    "content": "Temperature monitoring DDR5: Built-in thermal sensors, monitor with HWiNFO64, keep below 50°C for stability, 60°C+ throttles and causes errors",
                    "keywords": ["temperature", "thermal", "monitoring", "50c"],
                    "difficulty": "intermediate",
                    "tags": ["monitoring"],
                    "related_tools": ["HWiNFO64"]
                },
                {
                    "content": "Active cooling RAM: High-end DDR5 kits (6400+) benefit from fan airflow, case front intake helps, dedicated RAM fan overkill except extreme OC",
                    "keywords": ["cooling", "airflow", "fan"],
                    "difficulty": "intermediate",
                    "tags": ["cooling"],
                    "related_tools": []
                },
                {
                    "content": "RGB vs non-RGB performance: Identical performance, RGB adds 5-10 euros per stick, disable RGB in BIOS if unstable (rare interference)",
                    "keywords": ["rgb", "performance", "aesthetics"],
                    "difficulty": "beginner",
                    "tags": ["rgb"],
                    "related_tools": []
                },
                {
                    "content": "32GB (2x16) sweet spot: Sufficient for gaming + multitasking 2024, 64GB for heavy productivity/VMs, 128GB overkill consumer use",
                    "keywords": ["32gb", "capacity", "sweet spot"],
                    "difficulty": "beginner",
                    "tags": ["buying"],
                    "related_tools": []
                },
                {
                    "content": "Rank configuration: Dual rank (2Rx8) better performance than single rank (1Rx8), 2x dual-rank = quad rank, 4 sticks harder to OC",
                    "keywords": ["rank", "dual rank", "single rank", "2rx8"],
                    "difficulty": "advanced",
                    "tags": ["configuration"],
                    "related_tools": ["CPU-Z"]
                },
                {
                    "content": "Four DIMM population: Harder to achieve high frequency vs 2 DIMMs, additional IMC load, drop speed -200 to -400 MT/s expected",
                    "keywords": ["4 dimm", "topology", "imc load"],
                    "difficulty": "advanced",
                    "tags": ["limitation"],
                    "related_tools": []
                },
                {
                    "content": "BIOS updates for RAM: AGESA/Microcode updates improve DDR5 compatibility, update before troubleshooting instability, check motherboard site monthly",
                    "keywords": ["bios update", "agesa", "compatibility"],
                    "difficulty": "intermediate",
                    "tags": ["maintenance"],
                    "related_tools": []
                },
                {
                    "content": "QVL (Qualified Vendor List): Motherboard manufacturer tested RAM kits, buying QVL ensures compatibility, non-QVL usually works but not guaranteed",
                    "keywords": ["qvl", "compatibility", "vendor list"],
                    "difficulty": "beginner",
                    "tags": ["buying"],
                    "related_tools": []
                },
                {
                    "content": "Best brands DDR5 2024: G.Skill (Trident Z5), Corsair (Dominator Platinum), Kingston (Fury Beast), TeamGroup (T-Force), avoid generic no-name kits",
                    "keywords": ["brands", "gskill", "corsair", "kingston"],
                    "difficulty": "beginner",
                    "tags": ["buying"],
                    "related_tools": []
                },
                {
                    "content": "Price/performance DDR5: DDR5-6000 CL30 32GB best value 150-180 euros, 6400 CL32 marginal gains +30 euros, 7200+ enthusiast tax +100 euros",
                    "keywords": ["price", "value", "6000 cl30"],
                    "difficulty": "beginner",
                    "tags": ["buying"],
                    "related_tools": []
                },
                {
                    "content": "AIDA64 memory benchmark: Read 80000+ MB/s, Write 75000+ MB/s, Copy 75000+ MB/s DDR5-6000, Latency 65-75ns typical dual channel",
                    "keywords": ["aida64", "benchmark", "bandwidth", "latency"],
                    "difficulty": "intermediate",
                    "tags": ["benchmark"],
                    "related_tools": ["AIDA64"]
                },
                {
                    "content": "Gaming FPS gains: DDR5-6000 vs 4800 = +5-12% FPS CPU-bound games, diminishing returns above 6400, GPU-bound games 0-2% difference",
                    "keywords": ["gaming", "fps", "performance"],
                    "difficulty": "intermediate",
                    "tags": ["gaming"],
                    "related_tools": []
                },
                {
                    "content": "Productivity workloads: Video editing/encoding benefits from bandwidth, Photoshop/Lightroom prefers lower latency, 3D rendering loves capacity",
                    "keywords": ["productivity", "workload", "bandwidth"],
                    "difficulty": "intermediate",
                    "tags": ["productivity"],
                    "related_tools": []
                },
                {
                    "content": "ECC DDR5 consumer: Some AM5 boards support ECC UDIMM (non-registered), requires Pro CPUs typically, gaming benefit zero, workstation feature",
                    "keywords": ["ecc", "error correction", "workstation"],
                    "difficulty": "advanced",
                    "tags": ["workstation"],
                    "related_tools": []
                },
                {
                    "content": "On-die ECC: All DDR5 has internal error correction (separate from traditional ECC), transparent to user, improves reliability vs DDR4",
                    "keywords": ["on-die ecc", "reliability", "ddr5"],
                    "difficulty": "advanced",
                    "tags": ["technical"],
                    "related_tools": []
                },
                {
                    "content": "PMIC (Power Management IC): Integrated on DDR5 DIMMs, regulates voltage distribution, reduces motherboard complexity, per-DIMM power management",
                    "keywords": ["pmic", "power management", "voltage regulation"],
                    "difficulty": "expert",
                    "tags": ["technical"],
                    "related_tools": []
                },
                {
                    "content": "SPD (Serial Presence Detect): Stores JEDEC and XMP/EXPO profiles, read by BIOS on boot, corruption rare but causes training failures",
                    "keywords": ["spd", "profiles", "jedec"],
                    "difficulty": "advanced",
                    "tags": ["technical"],
                    "related_tools": ["Thaiphoon Burner"]
                },
                {
                    "content": "Manual OC vs XMP: Manual tuning 5-10% better performance than XMP, requires hours of testing, XMP sufficient for 95% of users",
                    "keywords": ["manual overclock", "xmp", "tuning"],
                    "difficulty": "expert",
                    "tags": ["overclocking"],
                    "related_tools": []
                },
                {
                    "content": "Safe voltage limits: VDIMM 1.40V 24/7 safe, 1.50V short-term testing, >1.50V degradation risk, VDDQ/SA follow similar rules",
                    "keywords": ["voltage limits", "safe", "degradation"],
                    "difficulty": "advanced",
                    "tags": ["safety"],
                    "related_tools": []
                },
                {
                    "content": "Clear CMOS if unstable: Remove power, short CMOS jumper 10 seconds, resets all BIOS settings including bad RAM OC, saves troubleshooting time",
                    "keywords": ["clear cmos", "reset", "troubleshooting"],
                    "difficulty": "beginner",
                    "tags": ["troubleshooting"],
                    "related_tools": []
                }
            ]
        }

        # 6. RAM DDR4 Optimization
        kb["ram_ddr4_optimization"] = {
            "metadata": {
                "priority": 4,
                "tags": ["ram", "ddr4", "memory", "legacy"],
                "difficulty": "intermediate",
                "description": "DDR4 memory optimization and tuning"
            },
            "tips": [
                {
                    "content": "DDR4-3600 CL16: Ryzen sweet spot, 1:1 FCLK ratio (1800 MHz), perfect balance speed and latency, widely available 100-130 euros 32GB kit",
                    "keywords": ["ddr4-3600", "cl16", "ryzen", "sweet spot"],
                    "difficulty": "intermediate",
                    "tags": ["amd", "value"],
                    "related_tools": ["CPU-Z"]
                },
                {
                    "content": "DDR4-3200 CL16: Intel and AMD budget option, safe compatibility, easy XMP, sufficient for gaming, 80-100 euros 32GB",
                    "keywords": ["ddr4-3200", "budget", "compatible"],
                    "difficulty": "beginner",
                    "tags": ["value"],
                    "related_tools": []
                },
                {
                    "content": "DDR4-4000 enthusiast: Requires manual tuning, 2:1 FCLK AMD or Gear 2 Intel, marginal gaming gains vs 3600, stability challenges",
                    "keywords": ["ddr4-4000", "enthusiast", "manual tuning"],
                    "difficulty": "expert",
                    "tags": ["overclocking"],
                    "related_tools": []
                },
                {
                    "content": "Samsung B-die: Best DDR4 overclocking IC, tight timings capable, identify with Thaiphoon Burner, premium pricing, EOL but still available used",
                    "keywords": ["b-die", "samsung", "overclocking", "ic"],
                    "difficulty": "advanced",
                    "tags": ["hardware"],
                    "related_tools": ["Thaiphoon Burner"]
                },
                {
                    "content": "Micron E-die (Rev E): Budget overclocker, good for high frequency 4000+, looser timings than B-die, Crucial Ballistix common",
                    "keywords": ["micron e-die", "rev e", "crucial"],
                    "difficulty": "advanced",
                    "tags": ["hardware"],
                    "related_tools": []
                },
                {
                    "content": "Hynix CJR/DJR: Mid-range overclock potential, 3600-3800 sweet spot, good alternative B-die, cheaper and available",
                    "keywords": ["hynix", "cjr", "djr"],
                    "difficulty": "advanced",
                    "tags": ["hardware"],
                    "related_tools": []
                },
                {
                    "content": "Primary timings DDR4: CL 14-18 typical XMP, tRCD 14-19, tRP 14-19, tRAS 28-42, B-die does CL14 at 3200, lower better",
                    "keywords": ["timings", "cl14", "cl16", "primary"],
                    "difficulty": "intermediate",
                    "tags": ["tuning"],
                    "related_tools": ["CPU-Z"]
                },
                {
                    "content": "Secondary timings: tRFC 250-550ns crucial, tWR 10-16, tRTP 6-12, tCWL equals CL typically, adjust for stability",
                    "keywords": ["secondary timings", "trfc", "twr"],
                    "difficulty": "advanced",
                    "tags": ["tuning"],
                    "related_tools": []
                },
                {
                    "content": "Tertiary timings: tRDRD, tWRWR, tRDWR affects multi-rank performance, platform-specific, leave auto unless expert",
                    "keywords": ["tertiary timings", "advanced"],
                    "difficulty": "expert",
                    "tags": ["tuning"],
                    "related_tools": []
                },
                {
                    "content": "DDR4 voltage: 1.35V XMP standard, 1.40-1.45V safe 24/7, 1.50V extreme OC (cooling + voltage tolerance), 1.20V JEDEC default",
                    "keywords": ["voltage", "1.35v", "1.45v", "safe"],
                    "difficulty": "intermediate",
                    "tags": ["voltage"],
                    "related_tools": []
                },
                {
                    "content": "VCCSA/VCCIO Intel: System Agent and I/O voltages, 1.20-1.35V for DDR4 OC, too high degrades IMC, increase if unstable 3600+",
                    "keywords": ["vccsa", "vccio", "intel", "imc"],
                    "difficulty": "advanced",
                    "tags": ["intel", "voltage"],
                    "related_tools": []
                },
                {
                    "content": "SOC voltage AMD: 1.00-1.20V for DDR4 OC on Ryzen, 1.10V typical for 3600, higher if 3800+ unstable, max 1.25V safe",
                    "keywords": ["soc voltage", "amd", "ryzen"],
                    "difficulty": "advanced",
                    "tags": ["amd", "voltage"],
                    "related_tools": []
                },
                {
                    "content": "DRAM Calculator for Ryzen: Generates safe timings based on IC type, v1.7.3 final version, use as starting point not gospel, verify with testing",
                    "keywords": ["dram calculator", "ryzen", "timings"],
                    "difficulty": "advanced",
                    "tags": ["tool", "amd"],
                    "related_tools": ["DRAM Calculator"]
                },
                {
                    "content": "XMP 2.0 profiles: One profile per DIMM, auto-applies frequency and timings, voltage, and CR (Command Rate), enable in BIOS for rated speed",
                    "keywords": ["xmp 2.0", "profiles", "auto"],
                    "difficulty": "beginner",
                    "tags": ["bios"],
                    "related_tools": []
                },
                {
                    "content": "Gear ratios Intel 10th-11th: Gear 1 (1:1) up to 3733, Gear 2 (2:1) beyond, Gear 1 lower latency better gaming, manual set for control",
                    "keywords": ["gear ratio", "intel", "10th gen", "11th gen"],
                    "difficulty": "advanced",
                    "tags": ["intel"],
                    "related_tools": []
                },
                {
                    "content": "FCLK tuning Ryzen: Infinity Fabric clock, match half of RAM speed (3600 RAM = 1800 FCLK), test up to 1900 FCLK for 3800 RAM",
                    "keywords": ["fclk", "infinity fabric", "1:1"],
                    "difficulty": "advanced",
                    "tags": ["amd"],
                    "related_tools": ["CPU-Z"]
                },
                {
                    "content": "Command Rate: 1T faster than 2T, 1T harder to achieve dual rank or 4 DIMMs, 2T more compatible, auto usually picks best",
                    "keywords": ["command rate", "1t", "2t"],
                    "difficulty": "advanced",
                    "tags": ["tuning"],
                    "related_tools": []
                },
                {
                    "content": "GDM (Gear Down Mode): Halves tCL/tCWL flexibility, improves stability, auto-enabled by BIOS often, disable for manual tuning control",
                    "keywords": ["gdm", "gear down mode"],
                    "difficulty": "expert",
                    "tags": ["tuning"],
                    "related_tools": []
                },
                {
                    "content": "Dual channel mandatory: 2x8GB or 2x16GB in slots A2/B2, 50-100% performance vs single channel, verify with CPU-Z Memory tab",
                    "keywords": ["dual channel", "a2 b2", "mandatory"],
                    "difficulty": "beginner",
                    "tags": ["installation"],
                    "related_tools": ["CPU-Z"]
                },
                {
                    "content": "Mixing RAM dangers: Different speeds downclock to slowest, mixing brands/ICs often unstable, buy kits together for best compatibility",
                    "keywords": ["mixing ram", "compatibility", "kits"],
                    "difficulty": "beginner",
                    "tags": ["compatibility"],
                    "related_tools": []
                },
                {
                    "content": "MemTest86 validation: 4 passes minimum at new OC, overnight test for 24/7 stability, single error = unstable (loosen timings or add voltage)",
                    "keywords": ["memtest86", "validation", "stability"],
                    "difficulty": "intermediate",
                    "tags": ["testing"],
                    "related_tools": ["MemTest86"]
                },
                {
                    "content": "HCI MemTest: Windows-based alternative, run one instance per thread, 200%+ coverage per instance for reliability",
                    "keywords": ["hci memtest", "windows", "coverage"],
                    "difficulty": "intermediate",
                    "tags": ["testing"],
                    "related_tools": ["HCI MemTest"]
                },
                {
                    "content": "Karhu RAM Test: Paid software 10 euros, fastest error detection, 5000%+ coverage recommended, community standard for DDR4 OC",
                    "keywords": ["karhu", "ram test", "paid"],
                    "difficulty": "advanced",
                    "tags": ["testing"],
                    "related_tools": ["Karhu RAM Test"]
                },
                {
                    "content": "AIDA64 memory benchmark DDR4: Read 45000-55000 MB/s, Write 45000-50000 MB/s typical dual channel 3600, Latency 50-70ns depending tuning",
                    "keywords": ["aida64", "benchmark", "bandwidth"],
                    "difficulty": "intermediate",
                    "tags": ["benchmark"],
                    "related_tools": ["AIDA64"]
                },
                {
                    "content": "Gaming performance DDR4: 3600 vs 2666 = 10-20% FPS CPU-bound games Ryzen, Intel less sensitive 5-10%, GPU-bound negligible difference",
                    "keywords": ["gaming", "fps", "performance"],
                    "difficulty": "intermediate",
                    "tags": ["gaming"],
                    "related_tools": []
                },
                {
                    "content": "Intel 10th-11th gen sweet spot: DDR4-3600-3800 CL16-18, Gear 1 mode, good kits 100-120 euros, high frequency diminishing returns",
                    "keywords": ["intel", "sweet spot", "10th gen"],
                    "difficulty": "intermediate",
                    "tags": ["intel"],
                    "related_tools": []
                },
                {
                    "content": "Ryzen 3000/5000 optimization: 3600 CL16 or 3800 CL16 if FCLK stable at 1900, tighten subtimings for extra 3-5% performance",
                    "keywords": ["ryzen 3000", "ryzen 5000", "optimization"],
                    "difficulty": "advanced",
                    "tags": ["amd"],
                    "related_tools": []
                },
                {
                    "content": "Temperature monitoring: DDR4 runs cooler than DDR5, 40-45°C under load typical, 50°C+ check airflow, active cooling rarely needed",
                    "keywords": ["temperature", "monitoring", "cooling"],
                    "difficulty": "intermediate",
                    "tags": ["monitoring"],
                    "related_tools": ["HWiNFO64"]
                },
                {
                    "content": "Capacity recommendations: 16GB minimum gaming 2024, 32GB multitasking/streaming, 64GB productivity/VMs, 128GB overkill consumer",
                    "keywords": ["capacity", "16gb", "32gb", "recommendation"],
                    "difficulty": "beginner",
                    "tags": ["buying"],
                    "related_tools": []
                },
                {
                    "content": "Best DDR4 kits 2024: G.Skill Ripjaws V/Trident Z, Corsair Vengeance LPX, Crucial Ballistix (discontinued), Kingston Fury",
                    "keywords": ["brands", "gskill", "corsair", "best"],
                    "difficulty": "beginner",
                    "tags": ["buying"],
                    "related_tools": []
                }
            ]
        }

        # =============================================================================
        # STORAGE (2 catégories)
        # =============================================================================

        # 7. SSD NVMe Gen4/Gen5
        kb["ssd_nvme_gen4_gen5"] = {
            "metadata": {
                "priority": 5,
                "tags": ["ssd", "nvme", "storage", "pcie"],
                "difficulty": "intermediate",
                "description": "NVMe Gen4 and Gen5 SSD technology"
            },
            "tips": [
                {
                    "content": "PCIe Gen4 speeds: 7000-7450 MB/s read typical (Samsung 980 Pro, WD SN850X, Crucial T700), 5000-6800 MB/s write, 4x faster than SATA SSD",
                    "keywords": ["gen4", "7000 mbs", "nvme", "pcie"],
                    "difficulty": "intermediate",
                    "tags": ["performance"],
                    "related_tools": ["CrystalDiskMark"]
                },
                {
                    "content": "PCIe Gen5 speeds: 10000-12400 MB/s read (Crucial T700, Samsung 990 Pro), 10000+ MB/s write, overkill gaming 2024, future-proofing",
                    "keywords": ["gen5", "12000 mbs", "future proof"],
                    "difficulty": "advanced",
                    "tags": ["cutting-edge"],
                    "related_tools": ["CrystalDiskMark"]
                },
                {
                    "content": "Samsung 980 Pro: PCIe 4.0, 7000 MB/s read, TLC NAND, 1200 TBW for 2TB, industry standard reliability, 130-150 euros per TB",
                    "keywords": ["980 pro", "samsung", "tlc", "reliable"],
                    "difficulty": "intermediate",
                    "tags": ["recommendation"],
                    "related_tools": ["Samsung Magician"]
                },
                {
                    "content": "WD Black SN850X: 7300 MB/s read, Game Mode 2.0 firmware, excellent random IOPS, PS5 compatible, competitive pricing 120-140 euros/TB",
                    "keywords": ["sn850x", "western digital", "gaming"],
                    "difficulty": "intermediate",
                    "tags": ["gaming"],
                    "related_tools": ["WD Dashboard"]
                },
                {
                    "content": "Crucial T700: PCIe 5.0, 12400 MB/s read, Phison E26 controller, active cooling required, 200+ euros per TB premium",
                    "keywords": ["t700", "crucial", "gen5", "phison e26"],
                    "difficulty": "advanced",
                    "tags": ["enthusiast"],
                    "related_tools": ["Crucial Storage Executive"]
                },
                {
                    "content": "SK Hynix Platinum P41: 7000 MB/s, excellent efficiency, low temps, 176-layer NAND, underrated gem, 110-130 euros/TB value",
                    "keywords": ["p41", "hynix", "efficient", "value"],
                    "difficulty": "intermediate",
                    "tags": ["value"],
                    "related_tools": []
                },
                {
                    "content": "TBW (Total Bytes Written): 600 TBW for 1TB typical, 1200 TBW for 2TB, endurance rating, 10 years warranty most brands",
                    "keywords": ["tbw", "endurance", "warranty", "lifespan"],
                    "difficulty": "intermediate",
                    "tags": ["reliability"],
                    "related_tools": ["CrystalDiskInfo"]
                },
                {
                    "content": "DRAM cache importance: Dedicated DRAM buffer improves sustained write speeds, DRAMless OK for budget/secondary drives, DRAM better for OS",
                    "keywords": ["dram cache", "buffer", "performance"],
                    "difficulty": "advanced",
                    "tags": ["architecture"],
                    "related_tools": []
                },
                {
                    "content": "SLC cache: Pseudo-SLC mode for burst writes, 100-200 GB cache typical, saturates after large transfers (50GB+), TLC converts back",
                    "keywords": ["slc cache", "write cache", "tlc"],
                    "difficulty": "advanced",
                    "tags": ["architecture"],
                    "related_tools": []
                },
                {
                    "content": "DirectStorage Windows 11: GPU decompression for game loading, requires Gen4+ NVMe and RTX/RX GPU, 2-3x faster load times supported games",
                    "keywords": ["directstorage", "windows 11", "gpu decompression"],
                    "difficulty": "intermediate",
                    "tags": ["gaming", "windows"],
                    "related_tools": []
                },
                {
                    "content": "4K random IOPS: More important than sequential for OS responsiveness, 500K+ IOPS read typical Gen4, feels snappier than sequential alone",
                    "keywords": ["4k iops", "random", "responsiveness"],
                    "difficulty": "advanced",
                    "tags": ["performance"],
                    "related_tools": ["CrystalDiskMark"]
                },
                {
                    "content": "Thermal throttling NVMe: 70-80°C typical under load, 85°C+ throttles to 50% speed, Gen5 requires heatsink mandatory, Gen4 recommended",
                    "keywords": ["thermal throttling", "temperature", "heatsink"],
                    "difficulty": "intermediate",
                    "tags": ["cooling"],
                    "related_tools": ["HWiNFO64"]
                },
                {
                    "content": "M.2 heatsinks: Motherboard integrated best (metal contact), adhesive aftermarket OK, thermal pads 1-2mm thickness, Gen5 needs active cooling",
                    "keywords": ["heatsink", "m.2", "cooling", "thermal pad"],
                    "difficulty": "intermediate",
                    "tags": ["cooling"],
                    "related_tools": []
                },
                {
                    "content": "NVMe form factors: M.2 2280 (80mm) standard desktop, 2242/2260 for laptops, U.2 enterprise, verify motherboard slot compatibility",
                    "keywords": ["m.2 2280", "form factor", "compatibility"],
                    "difficulty": "beginner",
                    "tags": ["hardware"],
                    "related_tools": []
                },
                {
                    "content": "PCIe lane sharing: M.2 slot may disable SATA ports or share lanes with GPU, check motherboard manual, Gen5 CPU lanes only typically",
                    "keywords": ["pcie lanes", "sharing", "sata", "motherboard"],
                    "difficulty": "intermediate",
                    "tags": ["compatibility"],
                    "related_tools": []
                },
                {
                    "content": "Boot drive sizing: 500GB minimum OS + apps, 1TB sweet spot gaming + programs, 2TB future-proof, separate data drive optional",
                    "keywords": ["capacity", "500gb", "1tb", "boot drive"],
                    "difficulty": "beginner",
                    "tags": ["buying"],
                    "related_tools": []
                },
                {
                    "content": "Real-world gaming: Gen4 vs SATA load times 1-3 seconds faster, Gen5 vs Gen4 marginal 0.5s, DirectStorage future benefit",
                    "keywords": ["gaming", "load times", "real world"],
                    "difficulty": "intermediate",
                    "tags": ["gaming"],
                    "related_tools": []
                },
                {
                    "content": "Productivity workloads: Video editing 4K+ benefits from Gen4 speed, photo editing minimal difference, 3D asset streaming uses bandwidth",
                    "keywords": ["productivity", "video editing", "4k"],
                    "difficulty": "intermediate",
                    "tags": ["productivity"],
                    "related_tools": []
                },
                {
                    "content": "QLC vs TLC NAND: TLC (3-bit) faster writes and endurance, QLC (4-bit) cheaper but slower sustained writes, TLC for boot drive",
                    "keywords": ["qlc", "tlc", "nand", "endurance"],
                    "difficulty": "advanced",
                    "tags": ["architecture"],
                    "related_tools": []
                },
                {
                    "content": "Controller importance: Phison E18/E26, Samsung Elpis, WD in-house controllers, firmware updates fix bugs, check brand software",
                    "keywords": ["controller", "phison", "firmware"],
                    "difficulty": "advanced",
                    "tags": ["technical"],
                    "related_tools": []
                },
                {
                    "content": "CrystalDiskMark benchmark: Sequential Q32T1 tests queue depth, 4K Q1T1 real-world responsiveness, run 5 passes for consistency",
                    "keywords": ["crystaldiskmark", "benchmark", "sequential", "4k"],
                    "difficulty": "intermediate",
                    "tags": ["benchmark"],
                    "related_tools": ["CrystalDiskMark"]
                },
                {
                    "content": "Health monitoring: SMART attributes track TBW usage, Power-On Hours, wear leveling, CrystalDiskInfo shows health %, replace <10%",
                    "keywords": ["smart", "health", "monitoring", "crystaldiskinfo"],
                    "difficulty": "intermediate",
                    "tags": ["maintenance"],
                    "related_tools": ["CrystalDiskInfo"]
                },
                {
                    "content": "Secure Erase: Returns SSD to factory state, improves performance degraded drive, use manufacturer tool (Samsung Magician), backup first",
                    "keywords": ["secure erase", "factory reset", "performance"],
                    "difficulty": "advanced",
                    "tags": ["maintenance"],
                    "related_tools": ["Samsung Magician"]
                },
                {
                    "content": "Over-provisioning: Reserve 10% unallocated space for wear leveling, improves longevity 20-30%, manual setup or manufacturer tool",
                    "keywords": ["over-provisioning", "wear leveling", "longevity"],
                    "difficulty": "advanced",
                    "tags": ["optimization"],
                    "related_tools": []
                },
                {
                    "content": "RAID 0 NVMe: Doubles sequential speed theoretically, complexity not worth it, single large SSD better, RAID controller overhead",
                    "keywords": ["raid 0", "striping", "complexity"],
                    "difficulty": "expert",
                    "tags": ["advanced"],
                    "related_tools": []
                },
                {
                    "content": "Best value Gen4 2024: WD SN850X 1TB 100 euros, Samsung 980 Pro 1TB 110 euros, SK Hynix P41 1TB 95 euros, avoid DRAMless for OS",
                    "keywords": ["value", "recommendation", "2024", "price"],
                    "difficulty": "beginner",
                    "tags": ["buying"],
                    "related_tools": []
                },
                {
                    "content": "Gen5 worth it?: Not for gaming 2024, productivity edge cases only, wait 2025+ for DirectStorage maturity, save money buy Gen4",
                    "keywords": ["gen5", "worth it", "future", "value"],
                    "difficulty": "beginner",
                    "tags": ["buying"],
                    "related_tools": []
                },
                {
                    "content": "PS5 compatibility: Gen4 NVMe 5500 MB/s minimum, heatsink required, up to 4TB supported, Sony approved list recommended",
                    "keywords": ["ps5", "console", "compatibility", "5500mbs"],
                    "difficulty": "intermediate",
                    "tags": ["console"],
                    "related_tools": []
                },
                {
                    "content": "Cloning software: Macrium Reflect free, Samsung Data Migration, Acronis True Image OEM, clone SATA to NVMe seamless",
                    "keywords": ["cloning", "migration", "macrium", "acronis"],
                    "difficulty": "intermediate",
                    "tags": ["migration"],
                    "related_tools": ["Macrium Reflect"]
                },
                {
                    "content": "Firmware updates: Check manufacturer site quarterly, fixes bugs and improves performance, backup before updating, use official tools only",
                    "keywords": ["firmware", "update", "maintenance"],
                    "difficulty": "intermediate",
                    "tags": ["maintenance"],
                    "related_tools": ["Samsung Magician"]
                }
            ]
        }

        # 8. SSD Optimization Windows
        kb["ssd_optimization_windows"] = {
            "metadata": {
                "priority": 4,
                "tags": ["ssd", "windows", "optimization", "maintenance"],
                "difficulty": "intermediate",
                "description": "Windows SSD optimization and maintenance"
            },
            "tips": [
                {
                    "content": "TRIM support: Enabled by default Windows 10/11, verify with 'fsutil behavior query DisableDeleteNotify' (0 = enabled), maintains performance",
                    "keywords": ["trim", "fsutil", "maintenance", "performance"],
                    "difficulty": "intermediate",
                    "tags": ["windows"],
                    "related_tools": []
                },
                {
                    "content": "Disable defragmentation: Windows auto-detects SSD and runs TRIM instead of defrag, verify in Optimize Drives (should show 'Optimize' not 'Defragment')",
                    "keywords": ["defrag", "defragmentation", "trim", "disable"],
                    "difficulty": "beginner",
                    "tags": ["windows"],
                    "related_tools": []
                },
                {
                    "content": "AHCI mode: Enable in BIOS before Windows install, 20-30% better performance than IDE mode, changing post-install requires registry edit",
                    "keywords": ["ahci", "bios", "ide mode", "performance"],
                    "difficulty": "intermediate",
                    "tags": ["bios"],
                    "related_tools": []
                },
                {
                    "content": "4K alignment: Modern Windows auto-aligns partitions at 1MB, check with AS SSD Benchmark, misalignment causes 50% performance loss",
                    "keywords": ["4k alignment", "partition", "alignment", "performance"],
                    "difficulty": "advanced",
                    "tags": ["partition"],
                    "related_tools": ["AS SSD Benchmark"]
                },
                {
                    "content": "Over-provisioning setup: Leave 10% unallocated space after last partition, improves write endurance and sustained performance, free performance boost",
                    "keywords": ["over-provisioning", "op", "unallocated", "endurance"],
                    "difficulty": "advanced",
                    "tags": ["optimization"],
                    "related_tools": []
                },
                {
                    "content": "Disable Superfetch/Prefetch: Not needed for SSD (instant access), Windows auto-disables Superfetch for SSD, manually disable Prefetch in services",
                    "keywords": ["superfetch", "prefetch", "disable", "services"],
                    "difficulty": "intermediate",
                    "tags": ["windows"],
                    "related_tools": []
                },
                {
                    "content": "Hibernation file: hiberfil.sys equals RAM size, delete with 'powercfg -h off' if tight on space, re-enable with 'powercfg -h on'",
                    "keywords": ["hibernation", "hiberfil.sys", "powercfg", "space"],
                    "difficulty": "intermediate",
                    "tags": ["windows"],
                    "related_tools": []
                },
                {
                    "content": "Page file optimization: Set fixed size (initial = max) for less fragmentation, 8-16GB sufficient gaming, or disable if 32GB+ RAM (risky)",
                    "keywords": ["page file", "pagefile.sys", "virtual memory"],
                    "difficulty": "advanced",
                    "tags": ["windows"],
                    "related_tools": []
                },
                {
                    "content": "System Restore points: Disable to save 10-20GB if doing regular backups, keep enabled if no backup solution, adjust max usage 2-5%",
                    "keywords": ["system restore", "restore points", "space"],
                    "difficulty": "beginner",
                    "tags": ["windows"],
                    "related_tools": []
                },
                {
                    "content": "Write caching: Enable in Device Manager > Disk Properties > Policies > 'Enable write caching', improves write performance 10-15%",
                    "keywords": ["write caching", "device manager", "performance"],
                    "difficulty": "intermediate",
                    "tags": ["windows"],
                    "related_tools": []
                },
                {
                    "content": "Disable indexing: Right-click drive > Properties > uncheck 'Allow files to be indexed', saves writes, search slower (negligible SSD)",
                    "keywords": ["indexing", "search", "disable", "writes"],
                    "difficulty": "intermediate",
                    "tags": ["windows"],
                    "related_tools": []
                },
                {
                    "content": "Temp file cleanup: Use Disk Cleanup (cleanmgr) or Windows Settings > Storage Sense, auto-clean temp files monthly, saves 5-20GB",
                    "keywords": ["temp files", "cleanup", "disk cleanup", "storage sense"],
                    "difficulty": "beginner",
                    "tags": ["maintenance"],
                    "related_tools": ["Disk Cleanup"]
                },
                {
                    "content": "Move downloads/documents: Relocate user folders to secondary drive, saves SSD writes, Properties > Location tab > Move",
                    "keywords": ["move folders", "documents", "downloads", "location"],
                    "difficulty": "intermediate",
                    "tags": ["configuration"],
                    "related_tools": []
                },
                {
                    "content": "Windows Update cleanup: Run Disk Cleanup > Clean up system files, deletes old update files, recovers 2-10GB after major updates",
                    "keywords": ["windows update", "cleanup", "system files"],
                    "difficulty": "beginner",
                    "tags": ["maintenance"],
                    "related_tools": ["Disk Cleanup"]
                },
                {
                    "content": "Disable System Protection: If using external backup, turn off per-drive to save writes and space, System Properties > System Protection",
                    "keywords": ["system protection", "restore", "disable"],
                    "difficulty": "intermediate",
                    "tags": ["windows"],
                    "related_tools": []
                },
                {
                    "content": "Browser cache location: Move Chrome/Firefox cache to RAM disk or secondary drive, reduces SSD writes 2-5GB daily heavy browsing",
                    "keywords": ["browser cache", "chrome", "firefox", "ramdisk"],
                    "difficulty": "advanced",
                    "tags": ["browser"],
                    "related_tools": []
                },
                {
                    "content": "WinDirStat analysis: Visualize disk usage, find large files and folders, free portable tool, run monthly to identify waste",
                    "keywords": ["windirstat", "disk usage", "analysis", "cleanup"],
                    "difficulty": "beginner",
                    "tags": ["tool"],
                    "related_tools": ["WinDirStat"]
                },
                {
                    "content": "TreeSize alternative: Faster than WinDirStat, free version sufficient, sorts by size, identifies duplicate files",
                    "keywords": ["treesize", "disk analysis", "duplicate"],
                    "difficulty": "beginner",
                    "tags": ["tool"],
                    "related_tools": ["TreeSize"]
                },
                {
                    "content": "Partition alignment check: CMD 'msinfo32' > Components > Storage > Disks, Partition Starting Offset divisible by 4096 = aligned",
                    "keywords": ["partition alignment", "msinfo32", "check"],
                    "difficulty": "advanced",
                    "tags": ["diagnostic"],
                    "related_tools": []
                },
                {
                    "content": "Storage Spaces warning: Windows RAID alternative, adds overhead, single fast SSD better than Storage Spaces pool, enterprise feature",
                    "keywords": ["storage spaces", "raid", "warning"],
                    "difficulty": "advanced",
                    "tags": ["windows"],
                    "related_tools": []
                },
                {
                    "content": "Fast Startup disable: Hybrid hibernate/shutdown, can cause issues, disable in Power Options > Choose what power buttons do",
                    "keywords": ["fast startup", "disable", "power options"],
                    "difficulty": "intermediate",
                    "tags": ["windows"],
                    "related_tools": []
                },
                {
                    "content": "Game install location: AAA games 100GB+ each, install on secondary SSD/HDD if limited boot drive space, load time difference minimal Gen4",
                    "keywords": ["games", "install location", "secondary drive"],
                    "difficulty": "beginner",
                    "tags": ["gaming"],
                    "related_tools": []
                },
                {
                    "content": "Symbolic links: mklink command to fake game location on other drive, appears in original location, advanced but useful capacity management",
                    "keywords": ["symbolic links", "mklink", "advanced"],
                    "difficulty": "expert",
                    "tags": ["advanced"],
                    "related_tools": []
                },
                {
                    "content": "UEFI vs MBR: Use GPT/UEFI for modern systems, MBR legacy, UEFI required for Secure Boot and >2TB drives, convert with mbr2gpt",
                    "keywords": ["uefi", "gpt", "mbr", "partition scheme"],
                    "difficulty": "intermediate",
                    "tags": ["partition"],
                    "related_tools": []
                },
                {
                    "content": "Windows 11 DirectStorage: Requires NVMe (Gen4+ recommended), RTX/RX GPU, game support needed, future-proofs for 2025+ titles",
                    "keywords": ["directstorage", "windows 11", "nvme", "future"],
                    "difficulty": "intermediate",
                    "tags": ["windows", "gaming"],
                    "related_tools": []
                }
            ]
        }

        # =============================================================================
        # MOTHERBOARD & PSU (2 catégories)
        # =============================================================================

        # 9. Motherboard Features Comparison
        kb["motherboard_features_comparison"] = {
            "metadata": {
                "priority": 4,
                "tags": ["motherboard", "hardware", "features", "chipset"],
                "difficulty": "intermediate",
                "description": "Motherboard features and chipset comparison"
            },
            "tips": [
                {
                    "content": "VRM phases importance: 10+ phases sufficient mid-range CPUs (i5/R5), 14-20 phases for high-end (i9/R9), overkill doesn't hurt but costs more",
                    "keywords": ["vrm", "phases", "power delivery"],
                    "difficulty": "advanced",
                    "tags": ["power"],
                    "related_tools": []
                },
                {
                    "content": "VRM heatsinks: Mandatory for K/X-series CPUs, passive sufficient 95% cases, active fan on extreme boards (X670E), direct MOSFETs cooling",
                    "keywords": ["vrm heatsinks", "cooling", "mosfets"],
                    "difficulty": "intermediate",
                    "tags": ["cooling"],
                    "related_tools": []
                },
                {
                    "content": "PCIe 5.0 GPU slot: x16 Gen5 on high-end boards (Z790, X670E), current GPUs Gen4, future RTX 5000/RX 8000 may use Gen5, backward compatible",
                    "keywords": ["pcie 5.0", "gpu slot", "x16", "future proof"],
                    "difficulty": "intermediate",
                    "tags": ["expansion"],
                    "related_tools": []
                },
                {
                    "content": "PCIe 5.0 M.2 slot: One Gen5 M.2 slot typical high-end, shares CPU lanes, Gen5 SSD overkill 2024, Gen4 slot sufficient gaming",
                    "keywords": ["pcie 5.0", "m.2", "nvme", "storage"],
                    "difficulty": "intermediate",
                    "tags": ["storage"],
                    "related_tools": []
                },
                {
                    "content": "DDR5 support: Z790/Z690 Intel dual DDR5/DDR4, AM5 DDR5 only, verify board spec sheet, DDR5 default 4800 MT/s (enable XMP for rated speed)",
                    "keywords": ["ddr5", "support", "compatibility"],
                    "difficulty": "beginner",
                    "tags": ["memory"],
                    "related_tools": []
                },
                {
                    "content": "WiFi 6E (802.11ax): 6 GHz band support, less congestion than WiFi 6, built-in on high-end boards, PCIe card alternative 30-50 euros",
                    "keywords": ["wifi 6e", "wireless", "6ghz", "802.11ax"],
                    "difficulty": "intermediate",
                    "tags": ["networking"],
                    "related_tools": []
                },
                {
                    "content": "Bluetooth 5.3: Latest version on modern boards, backward compatible, 2x speed vs BT 5.0, lower latency for peripherals",
                    "keywords": ["bluetooth", "5.3", "wireless"],
                    "difficulty": "beginner",
                    "tags": ["connectivity"],
                    "related_tools": []
                },
                {
                    "content": "USB 4.0 support: 40 Gbps bandwidth, Thunderbolt 3/4 compatible, rare on AM5 (Intel only typically), USB-C connector, docks/eGPU",
                    "keywords": ["usb 4.0", "40gbps", "thunderbolt"],
                    "difficulty": "advanced",
                    "tags": ["connectivity"],
                    "related_tools": []
                },
                {
                    "content": "2.5G Ethernet: Standard on mid-range+, Intel i225-V or Realtek 8125B controller, 2.5x faster than 1G, sufficient home use",
                    "keywords": ["2.5g ethernet", "lan", "i225-v"],
                    "difficulty": "intermediate",
                    "tags": ["networking"],
                    "related_tools": []
                },
                {
                    "content": "10G Ethernet: Enthusiast/workstation feature, requires 10G switch (expensive), Intel X550 controller, overkill consumer, NAS/server use",
                    "keywords": ["10g ethernet", "x550", "enthusiast"],
                    "difficulty": "advanced",
                    "tags": ["networking"],
                    "related_tools": []
                },
                {
                    "content": "BIOS Flashback: Update BIOS without CPU/RAM/GPU, button on I/O panel, USB with renamed file, essential feature for new CPU compat",
                    "keywords": ["bios flashback", "q-flash", "usb", "update"],
                    "difficulty": "intermediate",
                    "tags": ["bios"],
                    "related_tools": []
                },
                {
                    "content": "Clear CMOS button: External I/O button convenient, internal jumper alternative, resets BIOS to defaults (bad OC recovery)",
                    "keywords": ["clear cmos", "reset", "button"],
                    "difficulty": "beginner",
                    "tags": ["troubleshooting"],
                    "related_tools": []
                },
                {
                    "content": "POST code display: Debug LED shows boot error codes, premium boards feature, identifies boot failures (RAM, CPU, GPU, Boot device)",
                    "keywords": ["post code", "debug", "led", "troubleshooting"],
                    "difficulty": "intermediate",
                    "tags": ["troubleshooting"],
                    "related_tools": []
                },
                {
                    "content": "M.2 slot count: 2-3 slots budget boards, 4-5 high-end, verify Gen4 vs Gen3, check SATA sharing (manual), heatsinks included mid-range+",
                    "keywords": ["m.2 slots", "nvme", "count"],
                    "difficulty": "intermediate",
                    "tags": ["storage"],
                    "related_tools": []
                },
                {
                    "content": "SATA ports: 4-6 ports typical, SATA 3 (6 Gbps), M.2 usage may disable some ports (check manual), legacy HDD/SSD/optical drives",
                    "keywords": ["sata", "ports", "6gbps", "storage"],
                    "difficulty": "beginner",
                    "tags": ["storage"],
                    "related_tools": []
                },
                {
                    "content": "Audio codec: Realtek ALC1220 budget/mid, ALC4080 high-end, ESS Sabre DAC enthusiast, onboard sufficient 95% users, external DAC audiophile",
                    "keywords": ["audio", "codec", "alc1220", "realtek"],
                    "difficulty": "intermediate",
                    "tags": ["audio"],
                    "related_tools": []
                },
                {
                    "content": "RGB headers: 12V RGB and 5V ARGB headers, verify count and amperage for strips/fans, software control (ASUS Aura, MSI Mystic Light)",
                    "keywords": ["rgb", "argb", "headers", "lighting"],
                    "difficulty": "intermediate",
                    "tags": ["rgb"],
                    "related_tools": []
                },
                {
                    "content": "Fan headers: 6+ headers ideal (CPU, AIO pump, chassis fans), PWM 4-pin preferred, DC 3-pin legacy, 1A per header typical",
                    "keywords": ["fan headers", "pwm", "chassis fans"],
                    "difficulty": "intermediate",
                    "tags": ["cooling"],
                    "related_tools": []
                },
                {
                    "content": "Chipset comparison Z790 vs B760: Z790 has CPU OC, more PCIe lanes, better VRM, B760 locked CPU (memory OC OK), sufficient gaming",
                    "keywords": ["z790", "b760", "intel", "chipset"],
                    "difficulty": "intermediate",
                    "tags": ["intel"],
                    "related_tools": []
                },
                {
                    "content": "Chipset comparison X670E vs B650: X670E dual PCIe 5.0, more I/O, B650 single PCIe 5.0, both allow CPU/RAM OC, B650 value",
                    "keywords": ["x670e", "b650", "amd", "chipset"],
                    "difficulty": "intermediate",
                    "tags": ["amd"],
                    "related_tools": []
                },
                {
                    "content": "Form factors: ATX (305x244mm) standard, Micro-ATX (244x244mm) compact, Mini-ITX (170x170mm) SFF, verify case compatibility",
                    "keywords": ["form factor", "atx", "matx", "itx"],
                    "difficulty": "beginner",
                    "tags": ["size"],
                    "related_tools": []
                },
                {
                    "content": "ATX 12VO: New PSU standard (12V only), rare boards 2024, backward incompatible, wait for maturity, ATX 2.x/3.0 current standard",
                    "keywords": ["atx 12vo", "standard", "future"],
                    "difficulty": "advanced",
                    "tags": ["power"],
                    "related_tools": []
                },
                {
                    "content": "CPU socket compatibility: LGA1700 (Intel 12th-14th), AM5 (Ryzen 7000+), verify physical fit, BIOS update may needed newer CPUs",
                    "keywords": ["socket", "lga1700", "am5", "compatibility"],
                    "difficulty": "beginner",
                    "tags": ["compatibility"],
                    "related_tools": []
                },
                {
                    "content": "Reinforced PCIe slots: Metal shielding prevents GPU sag damage, standard on mid-range+, aesthetics + structural integrity",
                    "keywords": ["reinforced slot", "pcie", "gpu sag"],
                    "difficulty": "intermediate",
                    "tags": ["durability"],
                    "related_tools": []
                },
                {
                    "content": "Backplate I/O: Pre-installed I/O shield convenient (no sharp fingers), universal on modern boards, legacy requires manual install",
                    "keywords": ["io shield", "backplate", "integrated"],
                    "difficulty": "beginner",
                    "tags": ["convenience"],
                    "related_tools": []
                },
                {
                    "content": "Thunderbolt header: Intel boards may have TB4 header, requires PCIe card install, 40 Gbps, daisy-chain devices, eGPU support",
                    "keywords": ["thunderbolt", "tb4", "header", "egpu"],
                    "difficulty": "advanced",
                    "tags": ["expansion"],
                    "related_tools": []
                },
                {
                    "content": "TPM 2.0: Windows 11 requirement, fTPM in BIOS (firmware) or discrete TPM header, enable in BIOS Security settings",
                    "keywords": ["tpm", "tpm 2.0", "windows 11", "ftpm"],
                    "difficulty": "intermediate",
                    "tags": ["windows", "security"],
                    "related_tools": []
                },
                {
                    "content": "BIOS features: Resizable BAR, Secure Boot, XMP/EXPO profiles, fan curves, overclock presets, update regularly for stability",
                    "keywords": ["bios", "features", "resizable bar", "xmp"],
                    "difficulty": "intermediate",
                    "tags": ["bios"],
                    "related_tools": []
                },
                {
                    "content": "Best value boards 2024: MSI PRO B650-P (AM5 100 euros), ASUS TUF B760 (LGA1700 150 euros), avoid cheapest sub-100 euro boards",
                    "keywords": ["value", "recommendation", "msi", "asus"],
                    "difficulty": "beginner",
                    "tags": ["buying"],
                    "related_tools": []
                },
                {
                    "content": "Brand reputation: ASUS (ROG/TUF), MSI (MAG/MPG), Gigabyte (Aorus), ASRock (budget value), avoid OEM/proprietary (Dell, HP)",
                    "keywords": ["brands", "asus", "msi", "gigabyte", "asrock"],
                    "difficulty": "beginner",
                    "tags": ["buying"],
                    "related_tools": []
                }
            ]
        }

        # 10. PSU Selection Guide
        kb["psu_selection_guide"] = {
            "metadata": {
                "priority": 5,
                "tags": ["psu", "power", "hardware", "efficiency"],
                "difficulty": "intermediate",
                "description": "Power supply selection and efficiency ratings"
            },
            "tips": [
                {
                    "content": "80+ Bronze: 82-85% efficiency, budget PSUs 50-80 euros, sufficient low-power builds (300W), semi-modular typical",
                    "keywords": ["80+ bronze", "efficiency", "budget"],
                    "difficulty": "beginner",
                    "tags": ["budget"],
                    "related_tools": []
                },
                {
                    "content": "80+ Gold: 87-90% efficiency, sweet spot value 80-150 euros, mid-range builds, fully modular available, 10-year warranty brands",
                    "keywords": ["80+ gold", "efficiency", "value", "modular"],
                    "difficulty": "intermediate",
                    "tags": ["value"],
                    "related_tools": []
                },
                {
                    "content": "80+ Platinum: 89-92% efficiency, high-end 150-250 euros, diminishing returns vs Gold, silent operation, 12-year warranty",
                    "keywords": ["80+ platinum", "efficiency", "high-end"],
                    "difficulty": "intermediate",
                    "tags": ["high-end"],
                    "related_tools": []
                },
                {
                    "content": "80+ Titanium: 90-94% efficiency, enthusiast/server, 250+ euros, marginal gains over Platinum, silent premium, 12-15 year warranty",
                    "keywords": ["80+ titanium", "efficiency", "enthusiast"],
                    "difficulty": "advanced",
                    "tags": ["enthusiast"],
                    "related_tools": []
                },
                {
                    "content": "ATX 3.0 standard: New spec for RTX 40 series, 12VHPWR native cable, transient power spike handling 200%+ rated, backward compatible",
                    "keywords": ["atx 3.0", "12vhpwr", "pcie 5.0", "rtx 40"],
                    "difficulty": "intermediate",
                    "tags": ["standard"],
                    "related_tools": []
                },
                {
                    "content": "12VHPWR cable: 600W capable single cable, 16-pin (12+4), used RTX 4070 Ti+, proper seating critical (melting risk), 35mm bend radius min",
                    "keywords": ["12vhpwr", "600w", "rtx", "cable"],
                    "difficulty": "intermediate",
                    "tags": ["cables"],
                    "related_tools": []
                },
                {
                    "content": "PCIe 5.0 ready: Handles GPU transient spikes (RTX 4090 600W peaks), ATX 3.0 PSUs recommended RTX 40, ATX 2.x works with adapters",
                    "keywords": ["pcie 5.0", "transient", "spikes"],
                    "difficulty": "advanced",
                    "tags": ["compatibility"],
                    "related_tools": []
                },
                {
                    "content": "Modular vs semi-modular: Fully modular detaches all cables (clean builds), semi-modular 24-pin + 8-pin fixed, non-modular budget mess",
                    "keywords": ["modular", "semi-modular", "cable management"],
                    "difficulty": "beginner",
                    "tags": ["aesthetics"],
                    "related_tools": []
                },
                {
                    "content": "Wattage calculation: Add CPU TDP + GPU TDP + 100W overhead, 20-30% headroom for efficiency sweet spot (50-80% load optimal)",
                    "keywords": ["wattage", "calculation", "tdp", "headroom"],
                    "difficulty": "intermediate",
                    "tags": ["sizing"],
                    "related_tools": []
                },
                {
                    "content": "RTX 4090 system: 850W minimum (1000W recommended), i9-14900K + 4090 peak 700W, transient spikes 800W+, 1000W safe overhead",
                    "keywords": ["rtx 4090", "850w", "1000w", "high-end"],
                    "difficulty": "intermediate",
                    "tags": ["high-end"],
                    "related_tools": []
                },
                {
                    "content": "RTX 4070 Ti system: 650W sufficient, 750W recommended overhead, i5/R5 + 4070 Ti peak 450W, 750W sweet spot efficiency",
                    "keywords": ["rtx 4070", "650w", "750w"],
                    "difficulty": "intermediate",
                    "tags": ["mid-range"],
                    "related_tools": []
                },
                {
                    "content": "Budget gaming build: 550-650W for RTX 4060/RX 7600 + mid CPU, 80+ Bronze minimum, semi-modular preferred, 50-80 euros",
                    "keywords": ["budget", "550w", "650w", "gaming"],
                    "difficulty": "beginner",
                    "tags": ["budget"],
                    "related_tools": []
                },
                {
                    "content": "Single rail vs multi-rail: Single rail simplifies high-power GPUs (no OCP trips), multi-rail safer component protection, modern PSUs single",
                    "keywords": ["single rail", "multi-rail", "12v", "ocp"],
                    "difficulty": "advanced",
                    "tags": ["technical"],
                    "related_tools": []
                },
                {
                    "content": "OCP/OVP/UVP protections: Overcurrent, overvoltage, undervoltage protection mandatory, OTP (temperature) preferred, SCP (short circuit) critical",
                    "keywords": ["ocp", "ovp", "uvp", "protection"],
                    "difficulty": "advanced",
                    "tags": ["safety"],
                    "related_tools": []
                },
                {
                    "content": "Fan noise: 120mm fan quieter than 140mm (lower RPM), semi-passive (0 RPM idle) on quality PSUs, fan replacement voids warranty",
                    "keywords": ["fan noise", "120mm", "semi-passive", "0rpm"],
                    "difficulty": "intermediate",
                    "tags": ["noise"],
                    "related_tools": []
                },
                {
                    "content": "Cable length: Verify 24-pin ATX and PCIe cables reach in large cases, extension cables available, custom cables aesthetics (CableMod)",
                    "keywords": ["cable length", "extension", "custom cables"],
                    "difficulty": "intermediate",
                    "tags": ["compatibility"],
                    "related_tools": []
                },
                {
                    "content": "Warranty period: 5 years minimum, 7-10 years mid-range, 12 years high-end (Corsair RMx, SeaSonic), warranty indicates manufacturer confidence",
                    "keywords": ["warranty", "5 years", "10 years", "reliability"],
                    "difficulty": "intermediate",
                    "tags": ["reliability"],
                    "related_tools": []
                },
                {
                    "content": "Brands tier list: Tier A (SeaSonic, Corsair RMx, EVGA G6), Tier B (Corsair CX, EVGA BQ), Tier C+ (budget brands), avoid Tier D (fire hazard)",
                    "keywords": ["brands", "tier list", "seasonic", "corsair", "evga"],
                    "difficulty": "beginner",
                    "tags": ["buying"],
                    "related_tools": []
                },
                {
                    "content": "OEM manufacturers: SeaSonic, CWT, FSP, HEC make PSUs for brands, same OEM different quality tiers, check PSU review sites (Tom's Hardware)",
                    "keywords": ["oem", "seasonic", "cwt", "manufacturer"],
                    "difficulty": "advanced",
                    "tags": ["technical"],
                    "related_tools": []
                },
                {
                    "content": "ATX vs SFX: ATX (150mm) standard desktop, SFX (125mm) compact ITX cases, SFX-L (130mm) hybrid, ATX cheaper and quieter",
                    "keywords": ["atx", "sfx", "form factor", "size"],
                    "difficulty": "intermediate",
                    "tags": ["form factor"],
                    "related_tools": []
                },
                {
                    "content": "Efficiency curve: 50-80% load most efficient, avoid <20% or >90% load (reduced efficiency), size PSU for typical usage not peak",
                    "keywords": ["efficiency curve", "load", "optimal"],
                    "difficulty": "advanced",
                    "tags": ["efficiency"],
                    "related_tools": []
                },
                {
                    "content": "Ripple and noise: <50mV good quality, <30mV excellent, <20mV enthusiast, affects component longevity, check professional reviews",
                    "keywords": ["ripple", "noise", "voltage regulation"],
                    "difficulty": "expert",
                    "tags": ["quality"],
                    "related_tools": []
                },
                {
                    "content": "Voltage regulation: ±3% tolerance acceptable, ±1% excellent, stable rails critical for OC stability, budget PSUs ±5% (avoid)",
                    "keywords": ["voltage regulation", "tolerance", "rails"],
                    "difficulty": "advanced",
                    "tags": ["quality"],
                    "related_tools": []
                },
                {
                    "content": "Capacitor quality: Japanese capacitors (Nippon Chemi-Con, Rubycon) best longevity, Chinese acceptable mid-range, primary caps critical",
                    "keywords": ["capacitors", "japanese", "quality"],
                    "difficulty": "expert",
                    "tags": ["components"],
                    "related_tools": []
                },
                {
                    "content": "PSU orientation: Fan down (intake from bottom) ideal if case has vent + filter, fan up if no vent, exhausts into case (louder)",
                    "keywords": ["orientation", "fan direction", "airflow"],
                    "difficulty": "beginner",
                    "tags": ["installation"],
                    "related_tools": []
                },
                {
                    "content": "Power strip UPS: Connect PSU to UPS for brownout/blackout protection, 900W+ UPS for high-end systems, surge protector minimum",
                    "keywords": ["ups", "surge protector", "power protection"],
                    "difficulty": "intermediate",
                    "tags": ["protection"],
                    "related_tools": []
                },
                {
                    "content": "Paperclip test: Jumper PS_ON to ground to test PSU without motherboard, NOT recommended (no load = damage risk), use PSU tester tool",
                    "keywords": ["paperclip test", "testing", "diagnostic"],
                    "difficulty": "advanced",
                    "tags": ["troubleshooting"],
                    "related_tools": []
                },
                {
                    "content": "Best value 2024: Corsair RM750e (80+ Gold 750W ATX 3.0) 100 euros, SeaSonic Focus GX-850 90 euros, EVGA SuperNOVA 850 G6 110 euros",
                    "keywords": ["value", "2024", "recommendation", "750w", "850w"],
                    "difficulty": "beginner",
                    "tags": ["buying"],
                    "related_tools": []
                },
                {
                    "content": "Never cheap out PSU: Failed PSU can destroy entire system (surge/fire), invest 100-150 euros mid-range build minimum, 10% total budget",
                    "keywords": ["importance", "safety", "investment"],
                    "difficulty": "beginner",
                    "tags": ["safety"],
                    "related_tools": []
                },
                {
                    "content": "Upgradeability: Buy 100-200W over current need for future GPU upgrades, PSU lasts 10+ years multiple builds, 850W versatile sweet spot",
                    "keywords": ["future proof", "upgradeability", "850w"],
                    "difficulty": "intermediate",
                    "tags": ["future proof"],
                    "related_tools": []
                }
            ]
        }
'''

    return categories_code


def add_categories_to_file(file_path, new_code):
    """Ajoute les nouvelles catégories au fichier ai_knowledge_unified.py"""

    # Lire le fichier
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # Trouver le point d'insertion (avant "return kb")
    insertion_point = content.find("        return kb")

    if insertion_point == -1:
        print("ERROR: Point d'insertion 'return kb' non trouvé!")
        return False

    # Insérer le nouveau code
    new_content = content[:insertion_point] + new_code + "\n" + content[insertion_point:]

    # Sauvegarder
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(new_content)

    return True


def main():
    """Fonction principale"""

    print("=" * 80)
    print("SCRIPT D'AJOUT DE 28 NOUVELLES CATÉGORIES")
    print("=" * 80)
    print()

    file_path = r"C:\Users\Utilisateur\Downloads\Nitrite-V18.5\src\v14_mvp\ai_knowledge_unified.py"

    if not os.path.exists(file_path):
        print(f"ERREUR: Fichier non trouvé: {file_path}")
        return

    print(f"Fichier cible: {file_path}")
    print()
    print("Génération du code pour 28 nouvelles catégories...")
    print()

    # Générer le code
    new_code = generate_new_categories()

    # Statistiques
    category_count = new_code.count('kb["')
    tip_count = new_code.count('"content":')

    print(f"✓ Code généré:")
    print(f"  - {category_count} catégories")
    print(f"  - {tip_count} conseils")
    print()

    # Insérer dans le fichier
    print("Insertion du code dans le fichier...")

    if add_categories_to_file(file_path, new_code):
        print()
        print("=" * 80)
        print("✓ SUCCÈS!")
        print("=" * 80)
        print()
        print(f"28 nouvelles catégories ajoutées avec succès!")
        print(f"Total de conseils ajoutés: {tip_count}")
        print()
        print("Catégories ajoutées:")
        print("  - RAM: ram_ddr5_tuning, ram_ddr4_optimization")
        print("  - Storage: ssd_nvme_gen4_gen5, ssd_optimization_windows")
        print("  - Motherboard/PSU: motherboard_features_comparison, psu_selection_guide")
        print()
    else:
        print("ERREUR lors de l'insertion!")


if __name__ == "__main__":
    main()
