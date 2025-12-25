#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Script d'enrichissement Batch 3 - Knowledge Base NiTriTe V18.5
Ajoute 15 nouvelles catégories (benchmarking, overclocking avancé, diagnostics, sécurité)
Insertion avant 'return kb' à la ligne 2500
"""

import re
from pathlib import Path


def create_batch_3_categories():
    """Crée les 15 nouvelles catégories du Batch 3"""

    categories = {}

    # =============================================================================
    # 1. BENCHMARKING TOOLS
    # =============================================================================
    categories["benchmarking_tools"] = {
        "metadata": {
            "priority": 4,
            "tags": ["benchmark", "testing", "performance", "comparison"],
            "difficulty": "intermediate",
            "description": "Benchmarking tools and methodology for performance testing"
        },
        "tips": [
            {"content": "3DMark Time Spy: DirectX 12 GPU benchmark, industry standard, Graphics score (GPU only) vs Overall score (CPU+GPU), compare with same hardware online", "keywords": ["3dmark", "time spy", "gpu", "benchmark"], "difficulty": "beginner", "tags": ["gaming"], "related_tools": ["3DMark"]},
            {"content": "Cinebench R23: CPU multi-core rendering benchmark, 10 min run for stability, compare single-core (gaming) vs multi-core (productivity) scores", "keywords": ["cinebench", "r23", "cpu", "rendering"], "difficulty": "beginner", "tags": ["cpu"], "related_tools": ["Cinebench"]},
            {"content": "Geekbench 6: Cross-platform CPU benchmark, single-core (ST) important for gaming, multi-core (MT) for productivity, GPU compute tests available", "keywords": ["geekbench", "cpu", "single-core", "multi-core"], "difficulty": "beginner", "tags": ["cpu"], "related_tools": ["Geekbench"]},
            {"content": "UserBenchmark: Quick all-system benchmark (CPU/GPU/RAM/SSD), percentile ranking vs similar hardware, good for spotting underperforming components", "keywords": ["userbenchmark", "system", "percentile"], "difficulty": "beginner", "tags": ["diagnostic"], "related_tools": ["UserBenchmark"]},
            {"content": "CrystalDiskMark: SSD/HDD speed test, Sequential Q32T1 (large files), 4K Q1T1 (OS responsiveness), NVMe should hit 5000+ MB/s read Gen4", "keywords": ["crystaldiskmark", "ssd", "nvme", "speed"], "difficulty": "intermediate", "tags": ["storage"], "related_tools": ["CrystalDiskMark"]},
            {"content": "Benchmark methodology: Close all background apps, 30 min warm-up period, run 3x and average, note temps/clocks, consistent ambient temp 20-24°C", "keywords": ["methodology", "testing", "consistency"], "difficulty": "intermediate", "tags": ["best practices"], "related_tools": []},
            {"content": "Before/after testing: Baseline stock settings first, change ONE variable at time, document every change, screenshot scores for comparison", "keywords": ["testing", "baseline", "documentation"], "difficulty": "intermediate", "tags": ["methodology"], "related_tools": []},
            {"content": "Real-world vs synthetic: Synthetics (3DMark) show max potential, game benchmarks (built-in tools) show actual performance, test both for complete picture", "keywords": ["synthetic", "real-world", "gaming"], "difficulty": "intermediate", "tags": ["testing"], "related_tools": []},
            {"content": "Percentile interpretation: 50th percentile = average, 80th+ = good overclock/silicon lottery, <30th = investigate bottleneck/thermal throttling", "keywords": ["percentile", "silicon lottery", "performance"], "difficulty": "advanced", "tags": ["analysis"], "related_tools": ["UserBenchmark"]},
            {"content": "CPU benchmark comparison: Cinebench (rendering), Geekbench (general), CPU-Z (single-thread), Blender (production), Corona (ray tracing) - each tests different workloads", "keywords": ["cpu", "comparison", "workload"], "difficulty": "advanced", "tags": ["cpu"], "related_tools": ["Cinebench", "Geekbench", "CPU-Z"]},
        ]
    }

    # =============================================================================
    # 2. CPU OVERCLOCKING ADVANCED
    # =============================================================================
    categories["cpu_overclocking_advanced"] = {
        "metadata": {
            "priority": 5,
            "tags": ["overclocking", "cpu", "voltage", "stability", "advanced"],
            "difficulty": "advanced",
            "description": "Advanced CPU overclocking techniques, voltage tuning, and stability testing"
        },
        "tips": [
            {"content": "Voltage hierarchy: VCore (CPU core voltage), VCCSA (System Agent for IMC/PCIe), VCCIO (I/O voltage for memory), VCore most critical for stability", "keywords": ["voltage", "vcore", "vccsa", "vccio"], "difficulty": "advanced", "tags": ["overclocking"], "related_tools": []},
            {"content": "LLC (Load Line Calibration): Combats Vdroop under load, Level 5-6 (medium) recommended, Level 8 (turbo) causes overshoot dangerous, monitor with HWiNFO64", "keywords": ["llc", "load line", "vdroop", "voltage"], "difficulty": "advanced", "tags": ["voltage"], "related_tools": ["HWiNFO64"]},
            {"content": "AVX offset: Reduces frequency during AVX workloads (extreme heat), -2 to -4 offset typical (5.2 GHz → 5.0 GHz AVX), prevents thermal throttling Prime95", "keywords": ["avx", "offset", "prime95", "thermal"], "difficulty": "advanced", "tags": ["stability"], "related_tools": []},
            {"content": "Voltage scaling: +0.05V per 100 MHz rough guide, diminishing returns after 1.35V, 1.4V+ daily unsafe (degradation), silicon lottery huge variance", "keywords": ["voltage", "scaling", "degradation", "silicon lottery"], "difficulty": "advanced", "tags": ["overclocking"], "related_tools": []},
            {"content": "VCore safe limits: Intel 1.35V daily, 1.40V short-term, 1.45V+ benchmark only, AMD Ryzen 1.30V daily, 1.35V max, auto voltage often overshoots", "keywords": ["vcore", "safe limits", "intel", "amd"], "difficulty": "advanced", "tags": ["safety"], "related_tools": []},
            {"content": "Stability testing ladder: 1) OCCT 15min (quick check), 2) Cinebench R23 30min (realistic load), 3) Prime95 Small FFT 1hr (heat), 4) y-cruncher 30min (AVX2), 5) OCCT AVX2 overnight", "keywords": ["stability", "testing", "prime95", "occt"], "difficulty": "advanced", "tags": ["testing"], "related_tools": ["OCCT", "Prime95", "y-cruncher"]},
            {"content": "Fixed vs Adaptive voltage: Fixed = constant voltage (easier), Adaptive = voltage scales with frequency (better efficiency), Adaptive can spike dangerous if limits not set", "keywords": ["fixed", "adaptive", "voltage mode"], "difficulty": "advanced", "tags": ["voltage"], "related_tools": []},
            {"content": "Cooling requirements: 5.0 GHz = 240mm AIO minimum, 5.2 GHz = 360mm AIO, 5.4+ GHz = Custom loop/chiller, ambient temp 20°C vs 30°C loses 100-200 MHz", "keywords": ["cooling", "aio", "custom loop", "frequency"], "difficulty": "advanced", "tags": ["cooling"], "related_tools": []},
            {"content": "Ring/Cache ratio: Uncore frequency, affects L3 cache speed, keep within 300-500 MHz of core (5.0 core = 4.5-4.7 ring), too high causes WHEA errors", "keywords": ["ring", "cache", "uncore", "whea"], "difficulty": "expert", "tags": ["advanced"], "related_tools": ["HWiNFO64"]},
            {"content": "WHEA errors: Windows Hardware Error Architecture, WHEA ID 19 (memory), WHEA 18 (CPU cache), check Event Viewer, errors indicate instability even if no crash", "keywords": ["whea", "errors", "event viewer", "stability"], "difficulty": "expert", "tags": ["diagnostics"], "related_tools": ["Event Viewer", "HWiNFO64"]},
            {"content": "Per-core tuning: Disable worst cores (E-cores or weak P-cores), OC best cores higher, i9-14900K might hit 5.8 GHz 2 cores, 5.5 GHz all P-cores, HWiNFO shows per-core quality", "keywords": ["per-core", "tuning", "silicon lottery"], "difficulty": "expert", "tags": ["advanced"], "related_tools": ["HWiNFO64"]},
            {"content": "Current limits: IccMax (max current), set 1.25x TDP (250W CPU = 312A IccMax), too low throttles under load, too high risks VRM damage, 90°C VRM = reduce current", "keywords": ["current", "iccmax", "vrm", "thermal"], "difficulty": "expert", "tags": ["power"], "related_tools": []},
        ]
    }

    # =============================================================================
    # 3. RAM OVERCLOCKING TIGHTENING
    # =============================================================================
    categories["ram_overclocking_tightening"] = {
        "metadata": {
            "priority": 5,
            "tags": ["ram", "memory", "overclocking", "timings", "stability"],
            "difficulty": "advanced",
            "description": "Advanced RAM overclocking, timing optimization, and stability testing"
        },
        "tips": [
            {"content": "Primary timings: CAS Latency (CL), tRCD, tRP, tRAS - shown as 16-18-18-36, lower = faster, CL most important (DDR4-3600 CL16 > DDR4-4000 CL20)", "keywords": ["timings", "cl", "trcd", "trp", "tras"], "difficulty": "intermediate", "tags": ["memory"], "related_tools": []},
            {"content": "Secondary timings: tRFC (Refresh Cycle, huge impact), tRRD, tFAW, tWR, tWTR - often auto values loose, manual tuning gains 5-10% performance", "keywords": ["secondary", "trfc", "trrd", "tfaw"], "difficulty": "advanced", "tags": ["optimization"], "related_tools": []},
            {"content": "Tertiary timings: Extremely granular (100+ settings), tREFI (refresh interval) safest to increase, gains 1-3%, requires deep knowledge per memory IC", "keywords": ["tertiary", "trefi", "advanced"], "difficulty": "expert", "tags": ["advanced"], "related_tools": []},
            {"content": "tRFC tuning: Refresh time, 300-350ns target DDR4, Samsung B-die 250ns possible, Hynix/Micron 300-400ns, wrong value = instant crashes, TestMem5 validates", "keywords": ["trfc", "refresh", "samsung b-die"], "difficulty": "advanced", "tags": ["stability"], "related_tools": ["TestMem5"]},
            {"content": "Memory ICs: Samsung B-die (best OCing, tight CL), Hynix DJR/CJR (budget sweet spot), Micron E-die (high frequency loose timings), Thaiphoon Burner identifies IC", "keywords": ["memory ic", "b-die", "hynix", "micron"], "difficulty": "advanced", "tags": ["hardware"], "related_tools": ["Thaiphoon Burner"]},
            {"content": "Voltage scaling: 1.35V XMP standard, 1.40V safe daily, 1.45V good cooling required, 1.50V max (Samsung B-die only), 1.55V+ degradation risk", "keywords": ["voltage", "safe limits", "degradation"], "difficulty": "advanced", "tags": ["safety"], "related_tools": []},
            {"content": "VCCSA/VCCIO tuning: SA 1.15-1.25V, IO 1.10-1.20V for DDR4-3600+, too low = training failures, too high = IMC degradation, increments of 0.05V", "keywords": ["vccsa", "vccio", "imc", "training"], "difficulty": "advanced", "tags": ["voltage"], "related_tools": []},
            {"content": "TestMem5 with anta777 config: Gold standard RAM stability, 3 cycles minimum (6-8 hrs), Config @anta777 Extreme (25 tests), no errors = stable, 1 error = unstable", "keywords": ["testmem5", "anta777", "stability", "testing"], "difficulty": "advanced", "tags": ["testing"], "related_tools": ["TestMem5"]},
            {"content": "Gear modes: Gear 1 (1:1 memory:controller, best latency DDR4-3600), Gear 2 (1:2 ratio, DDR4-4000+ bandwidth), Gear 1 usually faster gaming despite lower frequency", "keywords": ["gear mode", "gear 1", "gear 2", "latency"], "difficulty": "advanced", "tags": ["performance"], "related_tools": []},
            {"content": "Subtimings ladder approach: Start XMP, lower tRFC by 50, test, repeat. Then tighten primaries 1 step, test. Secondary groups (RRD/FAW), test. Rollback last change if unstable", "keywords": ["tuning", "methodology", "incremental"], "difficulty": "advanced", "tags": ["methodology"], "related_tools": []},
            {"content": "RTL/IOL training: Round Trip Latency and IO Latency, auto values often +2-4 ticks loose, manual tuning difficult (wrong = no POST), gains 1-2ns latency, extreme tuning only", "keywords": ["rtl", "iol", "latency", "training"], "difficulty": "expert", "tags": ["advanced"], "related_tools": []},
            {"content": "Command Rate: 1T vs 2T, 1T = faster (single clock command), 2T = easier stability, 1T requires good IMC + memory IC, gains ~2ns latency DDR4", "keywords": ["command rate", "1t", "2t"], "difficulty": "advanced", "tags": ["performance"], "related_tools": []},
        ]
    }

    # =============================================================================
    # 4. GPU OVERCLOCKING CURVES
    # =============================================================================
    categories["gpu_overclocking_curves"] = {
        "metadata": {
            "priority": 4,
            "tags": ["gpu", "overclocking", "voltage", "curve", "nvidia", "amd"],
            "difficulty": "intermediate",
            "description": "GPU overclocking with voltage curves, power limits, and stability testing"
        },
        "tips": [
            {"content": "Core clock vs Memory clock: Core affects shaders/CUDA (3D rendering), Memory affects bandwidth (high-res textures), both important, memory OC often +10-15% FPS alone", "keywords": ["core", "memory", "bandwidth"], "difficulty": "intermediate", "tags": ["performance"], "related_tools": ["MSI Afterburner"]},
            {"content": "MSI Afterburner curve editor: Ctrl+F opens voltage/frequency curve, flatten curve 900mV+ for efficiency, reduce voltage same frequency = less heat/noise", "keywords": ["afterburner", "curve", "voltage", "efficiency"], "difficulty": "intermediate", "tags": ["undervolting"], "related_tools": ["MSI Afterburner"]},
            {"content": "NVIDIA Scanner (RTX 40-series): Built-in auto-OC, press 'OC Scanner' in Afterburner, 20 min test, applies safe curve, gains 50-100 MHz typical, good baseline before manual", "keywords": ["scanner", "nvidia", "auto-oc", "rtx"], "difficulty": "beginner", "tags": ["nvidia"], "related_tools": ["MSI Afterburner"]},
            {"content": "Power limit: +20% typical max slider, more power = higher sustained boost, RTX 4090 450W stock can pull 500W+, PSU headroom critical (850W PSU minimum)", "keywords": ["power limit", "tdp", "psu"], "difficulty": "intermediate", "tags": ["power"], "related_tools": ["MSI Afterburner"]},
            {"content": "Memory overclocking limits: GDDR6X (RTX 40/30-series) +500-1000 MHz typical, GDDR6 +1000-1500 MHz, artifacts/crashes = reduce by 100 MHz, memory errors silent (texture corruption)", "keywords": ["memory", "gddr6x", "artifacts"], "difficulty": "intermediate", "tags": ["overclocking"], "related_tools": ["MSI Afterburner"]},
            {"content": "Temperature targets: 60-70°C = excellent (quiet), 70-80°C = good (normal), 80-85°C = acceptable (throttle point), 85°C+ = thermal limit (reduce power/OC)", "keywords": ["temperature", "thermal", "throttling"], "difficulty": "beginner", "tags": ["cooling"], "related_tools": ["HWiNFO64"]},
            {"content": "Fan curve tuning: 30% idle (silent), 50% at 60°C, 75% at 75°C, 100% at 85°C, hysteresis 5°C prevents oscillation, custom curve > auto for quieter operation", "keywords": ["fan curve", "cooling", "noise"], "difficulty": "intermediate", "tags": ["cooling"], "related_tools": ["MSI Afterburner"]},
            {"content": "Stability testing GPU: 3DMark Time Spy stress test (99%+ pass), Furmark 15 min (power virus), Heaven Benchmark 1 hr loop, game-specific testing (Cyberpunk, RDR2)", "keywords": ["stability", "stress test", "furmark", "3dmark"], "difficulty": "intermediate", "tags": ["testing"], "related_tools": ["3DMark", "Furmark", "Heaven"]},
            {"content": "Undervolting for efficiency: RTX 4090 stock 1.07V 2800 MHz → 0.95V 2700 MHz = -50W, -10°C, -3% FPS, better quieter performance, sweet spot 0.900-0.950V", "keywords": ["undervolting", "efficiency", "temperature"], "difficulty": "intermediate", "tags": ["undervolting"], "related_tools": ["MSI Afterburner"]},
            {"content": "AMD Radeon overclocking: More Power Tools (MPT) unlocks higher limits, increase power limit first, core clock +100-200 MHz, memory +100-200 MHz (GDDR6), test incremental", "keywords": ["amd", "radeon", "mpt"], "difficulty": "intermediate", "tags": ["amd"], "related_tools": ["AMD Adrenalin", "More Power Tools"]},
            {"content": "VRAM junction temp: GDDR6X critical metric (RTX 3080/3090/4090), 95°C throttle point, 85°C target, pad mod + active cooling if 95°C+, HWiNFO64 sensor monitoring", "keywords": ["vram", "junction", "gddr6x", "thermal pads"], "difficulty": "advanced", "tags": ["cooling"], "related_tools": ["HWiNFO64"]},
        ]
    }

    # =============================================================================
    # 5. BIOS/UEFI SETTINGS
    # =============================================================================
    categories["bios_uefi_settings"] = {
        "metadata": {
            "priority": 5,
            "tags": ["bios", "uefi", "settings", "xmp", "pbo", "optimization"],
            "difficulty": "intermediate",
            "description": "Essential BIOS/UEFI settings for performance, stability, and compatibility"
        },
        "tips": [
            {"content": "XMP/EXPO profiles: Intel XMP (Extreme Memory Profile), AMD EXPO (Extended Profiles for Overclocking), enables RAM rated speeds, Profile 1 vs 2 (try both), instability = increase VCCSA/VCCIO +0.05V", "keywords": ["xmp", "expo", "memory", "profile"], "difficulty": "beginner", "tags": ["memory"], "related_tools": []},
            {"content": "AMD PBO (Precision Boost Overdrive): Auto-OC for Ryzen, PBO Limits (Motherboard), Curve Optimizer -10 to -30 (negative = more boost), +200 MHz Max Boost, stability test required", "keywords": ["pbo", "amd", "ryzen", "curve optimizer"], "difficulty": "intermediate", "tags": ["amd"], "related_tools": []},
            {"content": "Curve Optimizer (AMD): Per-core voltage offset, Negative = undervolt for higher boost, start -10 all cores, increment -5 until unstable, best cores can go -30, WHEA errors = reduce", "keywords": ["curve optimizer", "undervolt", "per-core"], "difficulty": "advanced", "tags": ["amd"], "related_tools": []},
            {"content": "Resizable BAR (ReBAR): Enable Above 4G Decoding + ReBAR, requires UEFI BIOS + RTX 30/40 or RX 6000/7000, 5-15% FPS gains certain games (Forza, Cyberpunk), no downside", "keywords": ["rebar", "resizable bar", "4g decoding"], "difficulty": "intermediate", "tags": ["gaming"], "related_tools": []},
            {"content": "Fast Boot: UEFI fast boot skips hardware checks, faster POST (3s vs 15s), disable if troubleshooting, Windows Fast Startup separate setting (disable for dual-boot)", "keywords": ["fast boot", "post", "startup"], "difficulty": "beginner", "tags": ["boot"], "related_tools": []},
            {"content": "Secure Boot: UEFI security feature, blocks unsigned drivers/OS, required Windows 11, disable if using Linux dual-boot or old hardware drivers, re-enable after setup", "keywords": ["secure boot", "windows 11", "uefi"], "difficulty": "intermediate", "tags": ["security"], "related_tools": []},
            {"content": "CSM (Compatibility Support Module): Legacy BIOS mode, disable for pure UEFI (faster boot), required for old GPUs or OS, conflicts with Secure Boot + ReBAR", "keywords": ["csm", "legacy", "compatibility"], "difficulty": "intermediate", "tags": ["compatibility"], "related_tools": []},
            {"content": "C-States: CPU power saving (C0 = active, C6 = deep sleep), enable for efficiency, disable for benchmark stability (prevents frequency drops), minimal gaming impact enabled", "keywords": ["c-states", "power saving", "efficiency"], "difficulty": "intermediate", "tags": ["power"], "related_tools": []},
            {"content": "BIOS update procedure: Download from motherboard vendor (ASUS/MSI/Gigabyte), USB FAT32 format, rename file per manual, Q-Flash/EZ Flash tool, NEVER power off during update, clear CMOS after", "keywords": ["bios update", "firmware", "flash"], "difficulty": "advanced", "tags": ["maintenance"], "related_tools": []},
            {"content": "Load Optimized Defaults: Reset BIOS to factory, use after failed OC or corruption, loses all settings, screenshot BIOS pages before experimenting for easy restore", "keywords": ["defaults", "reset", "troubleshooting"], "difficulty": "beginner", "tags": ["troubleshooting"], "related_tools": []},
            {"content": "BIOS profiles: Save/Load profiles (OC profile, stock profile, testing profile), quick switching without reconfiguring, export to USB backup, helps A/B testing", "keywords": ["profiles", "backup", "save"], "difficulty": "intermediate", "tags": ["workflow"], "related_tools": []},
        ]
    }

    # =============================================================================
    # 6. STORAGE RAID CONFIGURATIONS
    # =============================================================================
    categories["storage_raid_configurations"] = {
        "metadata": {
            "priority": 3,
            "tags": ["storage", "raid", "redundancy", "performance"],
            "difficulty": "advanced",
            "description": "RAID configurations, performance vs redundancy, setup and troubleshooting"
        },
        "tips": [
            {"content": "RAID 0 (Striping): 2+ drives, data split across drives, DOUBLE speed (2x 1GB/s = 2GB/s), ZERO redundancy (1 drive fails = all data lost), gaming/scratch disk only", "keywords": ["raid 0", "striping", "performance", "no redundancy"], "difficulty": "intermediate", "tags": ["performance"], "related_tools": []},
            {"content": "RAID 1 (Mirroring): 2 drives, identical copy both drives, 50% capacity (2x 1TB = 1TB usable), read speed 2x, write speed 1x, 1 drive failure OK, critical data protection", "keywords": ["raid 1", "mirroring", "redundancy"], "difficulty": "intermediate", "tags": ["backup"], "related_tools": []},
            {"content": "RAID 5 (Parity): 3+ drives, data + parity distributed, 1 drive failure tolerated, (N-1) capacity (3x 1TB = 2TB), good balance redundancy/capacity, slow writes (parity calc)", "keywords": ["raid 5", "parity", "redundancy"], "difficulty": "advanced", "tags": ["redundancy"], "related_tools": []},
            {"content": "RAID 10 (1+0): 4+ drives, mirrored stripes, RAID 1 pairs in RAID 0, 50% capacity, fast + redundant, expensive (4x 1TB = 2TB usable), enterprise/workstation ideal", "keywords": ["raid 10", "raid 1+0", "performance", "redundancy"], "difficulty": "advanced", "tags": ["enterprise"], "related_tools": []},
            {"content": "Hardware RAID: Dedicated controller (LSI/Adaptec), battery-backed cache, faster parity calc, OS-independent, expensive ($300-2000), RAID card failure = data access issue", "keywords": ["hardware raid", "controller", "cache"], "difficulty": "advanced", "tags": ["hardware"], "related_tools": []},
            {"content": "Software RAID: Windows Storage Spaces / Linux mdadm / FreeNAS, CPU-based, free, flexible, slower than HW RAID, sufficient for most users, no vendor lock-in", "keywords": ["software raid", "storage spaces", "mdadm"], "difficulty": "advanced", "tags": ["software"], "related_tools": ["Storage Spaces"]},
            {"content": "RAID is NOT backup: RAID protects hardware failure, NOT deletion/corruption/ransomware, always 3-2-1 backup (3 copies, 2 media, 1 offsite) separate from RAID", "keywords": ["backup", "3-2-1", "ransomware"], "difficulty": "intermediate", "tags": ["backup"], "related_tools": []},
            {"content": "RAID 5 write hole: Power loss during parity write = corruption, hardware RAID BBU (battery backup) mitigates, software RAID risk, RAID 6 (dual parity) safer", "keywords": ["raid 5", "write hole", "corruption", "battery backup"], "difficulty": "expert", "tags": ["reliability"], "related_tools": []},
            {"content": "NVMe RAID limitations: PCIe lanes exhausted quickly (4x drives = 16 lanes), Intel VROC (Virtual RAID on CPU) or motherboard chipset RAID, bootable RAID tricky (UEFI support required)", "keywords": ["nvme", "raid", "vroc", "pcie lanes"], "difficulty": "expert", "tags": ["nvme"], "related_tools": []},
            {"content": "RAID rebuild time: RAID 5 with 4TB drives = 10-20 hrs rebuild, 2nd drive failure during rebuild = data loss, RAID 6 safer (dual parity), URE (Unrecoverable Read Error) risk large drives", "keywords": ["rebuild", "ure", "raid 6"], "difficulty": "advanced", "tags": ["reliability"], "related_tools": []},
        ]
    }

    # =============================================================================
    # 7. BACKUP STRATEGIES
    # =============================================================================
    categories["backup_strategies"] = {
        "metadata": {
            "priority": 4,
            "tags": ["backup", "recovery", "data protection", "disaster recovery"],
            "difficulty": "intermediate",
            "description": "Comprehensive backup strategies, tools, and disaster recovery planning"
        },
        "tips": [
            {"content": "3-2-1 Rule: 3 copies of data (original + 2 backups), 2 different media types (HDD + cloud), 1 offsite copy (cloud or physical location), gold standard data protection", "keywords": ["3-2-1", "backup", "offsite", "redundancy"], "difficulty": "intermediate", "tags": ["backup"], "related_tools": []},
            {"content": "Macrium Reflect Free: Disk imaging tool, full system backup, bootable rescue media, incremental backups (fast), compression saves space, restore entire system after crash", "keywords": ["macrium reflect", "disk image", "backup"], "difficulty": "intermediate", "tags": ["backup"], "related_tools": ["Macrium Reflect"]},
            {"content": "Incremental vs Differential vs Full: Full = everything (slow, large), Incremental = changes since last backup (fast, chain), Differential = changes since last full (medium), Full weekly + Incremental daily", "keywords": ["incremental", "differential", "full backup"], "difficulty": "intermediate", "tags": ["methodology"], "related_tools": []},
            {"content": "Cloud backup services: Backblaze (unlimited $70/yr), Google Drive (2TB $100/yr), OneDrive (1TB with Office), automatic upload, version history, ransomware protection offsite", "keywords": ["cloud backup", "backblaze", "onedrive"], "difficulty": "beginner", "tags": ["cloud"], "related_tools": ["Backblaze", "OneDrive"]},
            {"content": "Backup verification: Test restore regularly (quarterly), verify backup integrity (checksum), automated backups can silently fail, mock disaster recovery drill annually", "keywords": ["verification", "restore test", "integrity"], "difficulty": "intermediate", "tags": ["best practices"], "related_tools": []},
            {"content": "Backup rotation: Grandfather-Father-Son (GFS) scheme, Daily (7 days), Weekly (4 weeks), Monthly (12 months), balances space vs history, automate with scheduler", "keywords": ["rotation", "gfs", "retention"], "difficulty": "advanced", "tags": ["methodology"], "related_tools": []},
            {"content": "NAS backup target: Synology/QNAP NAS, network backup destination, RAID protection, automatic snapshots, SMB/NFS shares, accessible all PCs, 2-bay minimum (RAID 1)", "keywords": ["nas", "synology", "qnap", "network backup"], "difficulty": "intermediate", "tags": ["nas"], "related_tools": []},
            {"content": "Ransomware protection: Offline backups (disconnect drive), immutable backups (cloud), shadow copies disabled by ransomware, 3-2-1 rule critical, avoid always-connected backup drives", "keywords": ["ransomware", "offline", "immutable"], "difficulty": "intermediate", "tags": ["security"], "related_tools": []},
            {"content": "Bootable rescue media: Windows Recovery USB (Create via Settings), Macrium Reflect WinPE, allows restore without working OS, test boot BEFORE disaster, update annually", "keywords": ["rescue media", "winpe", "bootable usb"], "difficulty": "intermediate", "tags": ["recovery"], "related_tools": ["Macrium Reflect"]},
            {"content": "Backup priority tiers: Tier 1 (critical docs, photos, projects) - daily cloud, Tier 2 (applications, settings) - weekly image, Tier 3 (games, downloads) - no backup (redownloadable)", "keywords": ["priority", "tiers", "strategy"], "difficulty": "intermediate", "tags": ["planning"], "related_tools": []},
            {"content": "Version control for code: Git + GitHub/GitLab, NOT same as backup (code-focused), handles versions/branches, complements traditional backup, push daily, private repos for personal projects", "keywords": ["git", "version control", "github"], "difficulty": "intermediate", "tags": ["development"], "related_tools": ["Git", "GitHub"]},
        ]
    }

    # =============================================================================
    # 8. SECURITY ANTIVIRUS
    # =============================================================================
    categories["security_antivirus"] = {
        "metadata": {
            "priority": 4,
            "tags": ["security", "antivirus", "malware", "protection"],
            "difficulty": "beginner",
            "description": "Antivirus software, malware protection, and security best practices"
        },
        "tips": [
            {"content": "Windows Defender: Built-in Windows 10/11, adequate protection 2024, real-time scanning, cloud-delivered protection, automatic updates, free, low performance impact", "keywords": ["windows defender", "built-in", "real-time"], "difficulty": "beginner", "tags": ["windows"], "related_tools": ["Windows Defender"]},
            {"content": "Malwarebytes: Anti-malware supplement, excellent adware/PUP detection, free scanner (manual), Premium $40/yr (real-time), run alongside Defender no conflicts", "keywords": ["malwarebytes", "anti-malware", "pup"], "difficulty": "beginner", "tags": ["malware"], "related_tools": ["Malwarebytes"]},
            {"content": "Real-time protection: On-Access scanning, monitors file opens/executes, slight performance cost (5-10% CPU games), disable temporarily benchmarking (re-enable after), exclusions for false positives", "keywords": ["real-time", "on-access", "performance"], "difficulty": "beginner", "tags": ["performance"], "related_tools": []},
            {"content": "Exclusions for performance: Exclude game folders, compiler directories (Visual Studio), mining software (flagged as malware), reduces scanning overhead, only trusted paths", "keywords": ["exclusions", "false positive", "performance"], "difficulty": "intermediate", "tags": ["optimization"], "related_tools": ["Windows Defender"]},
            {"content": "Scheduled scans: Weekly full scan (overnight), Quick scan daily, Offline scan if infected (Windows Defender Offline), don't disable real-time for scheduled only", "keywords": ["scheduled scan", "full scan", "offline scan"], "difficulty": "beginner", "tags": ["maintenance"], "related_tools": []},
            {"content": "Third-party AV (avoid): Norton, McAfee, Avast = bloatware 2024, performance impact high, intrusive ads, difficult uninstall, Defender + Malwarebytes sufficient most users", "keywords": ["norton", "mcafee", "avast", "bloatware"], "difficulty": "beginner", "tags": ["avoid"], "related_tools": []},
            {"content": "Browser security: uBlock Origin (ad blocker), blocks malicious ads, phishing protection Chrome/Edge built-in, HTTPS Everywhere, avoid extensions from unknown sources", "keywords": ["ublock origin", "browser", "phishing"], "difficulty": "beginner", "tags": ["browser"], "related_tools": ["uBlock Origin"]},
            {"content": "Email security: Don't open attachments unknown senders, Office macros disabled default (good), .exe .scr .zip attachments suspicious, verify sender address (spoofing common)", "keywords": ["email", "phishing", "attachments"], "difficulty": "beginner", "tags": ["email"], "related_tools": []},
            {"content": "Ransomware protection: Defender Controlled Folder Access (blocks unauthorized changes), backup 3-2-1 rule (offline copy), avoid pirated software (common vector), UAC prompts seriously", "keywords": ["ransomware", "controlled folder access", "backup"], "difficulty": "intermediate", "tags": ["ransomware"], "related_tools": ["Windows Defender"]},
            {"content": "Portable scanners: ESET Online Scanner, Kaspersky Virus Removal Tool, second opinion if infection suspected, no installation needed, complements primary AV", "keywords": ["portable", "eset", "kaspersky", "second opinion"], "difficulty": "intermediate", "tags": ["tools"], "related_tools": ["ESET Online Scanner"]},
        ]
    }

    # =============================================================================
    # 9. SECURITY FIREWALL
    # =============================================================================
    categories["security_firewall"] = {
        "metadata": {
            "priority": 3,
            "tags": ["security", "firewall", "network", "privacy"],
            "difficulty": "intermediate",
            "description": "Firewall configuration, outbound blocking, and network security"
        },
        "tips": [
            {"content": "Windows Firewall: Built-in stateful firewall, blocks inbound by default (good), allows outbound by default (bad), advanced settings for granular control, adequate for most users", "keywords": ["windows firewall", "stateful", "inbound", "outbound"], "difficulty": "beginner", "tags": ["windows"], "related_tools": ["Windows Firewall"]},
            {"content": "Outbound blocking: Block all outbound, allow per-application (whitelist approach), stops malware exfiltration/C2, requires manual rules (annoying), privacy-focused users only", "keywords": ["outbound", "blocking", "whitelist", "privacy"], "difficulty": "advanced", "tags": ["privacy"], "related_tools": []},
            {"content": "Simplewall: Free Windows firewall manager, blocks outbound default, easy allow/deny GUI, shows connection attempts live, filtering mode (whitelist/blacklist), replaces complex Windows UI", "keywords": ["simplewall", "firewall", "outbound", "gui"], "difficulty": "intermediate", "tags": ["tools"], "related_tools": ["Simplewall"]},
            {"content": "Firewall rule creation: Inbound rule (block port 445 SMB outside LAN), Outbound rule (block telemetry), Program rules (block app internet), IP rules (block country ranges), test rules after", "keywords": ["rules", "inbound", "outbound", "program"], "difficulty": "intermediate", "tags": ["configuration"], "related_tools": ["Windows Firewall"]},
            {"content": "Port security: Close unused ports (netstat -an shows listening), Port 445 (SMB) WAN-exposed = ransomware risk, 3389 (RDP) brute-force target, 80/443 (web) OK if hosting", "keywords": ["ports", "smb", "rdp", "netstat"], "difficulty": "intermediate", "tags": ["ports"], "related_tools": []},
            {"content": "Gaming firewall issues: Port forwarding for P2P games, UPnP (Universal Plug and Play) auto-opens ports, disable UPnP security (manual port forward instead), check game server requirements", "keywords": ["gaming", "port forwarding", "upnp"], "difficulty": "intermediate", "tags": ["gaming"], "related_tools": []},
            {"content": "Firewall logging: Enable logging (audit), logs in C:\\Windows\\System32\\LogFiles\\Firewall, analyze dropped packets, troubleshoot connectivity, log size limit 4096 KB default", "keywords": ["logging", "audit", "dropped packets"], "difficulty": "advanced", "tags": ["troubleshooting"], "related_tools": []},
            {"content": "Third-party firewalls: GlassWire (network monitoring + firewall), ZoneAlarm (legacy), NOT needed if Simplewall/Windows Firewall configured, avoid Suite bloatware (Norton, McAfee)", "keywords": ["glasswire", "zonealarm", "third-party"], "difficulty": "intermediate", "tags": ["tools"], "related_tools": ["GlassWire"]},
            {"content": "Network profiles: Public (restrictive, coffee shop), Private (trusted, home), Domain (work), Windows changes firewall rules per profile, ensure home = Private not Public", "keywords": ["network profiles", "public", "private", "domain"], "difficulty": "beginner", "tags": ["configuration"], "related_tools": []},
            {"content": "DMZ and router firewall: Router firewall first line defense (NAT = basic firewall), DMZ exposes device to internet (gaming/hosting), disable DMZ use port forward instead (safer)", "keywords": ["dmz", "router", "nat", "port forward"], "difficulty": "advanced", "tags": ["router"], "related_tools": []},
        ]
    }

    # =============================================================================
    # 10. DIAGNOSTICS BSOD ANALYSIS
    # =============================================================================
    categories["diagnostics_bsod_analysis"] = {
        "metadata": {
            "priority": 5,
            "tags": ["diagnostics", "bsod", "crash", "troubleshooting", "debugging"],
            "difficulty": "advanced",
            "description": "Blue Screen of Death analysis, dump file debugging, and crash troubleshooting"
        },
        "tips": [
            {"content": "Common BSOD codes: MEMORY_MANAGEMENT (RAM/XMP), SYSTEM_SERVICE_EXCEPTION (driver), IRQL_NOT_LESS_OR_EQUAL (driver/OC), WHEA_UNCORRECTABLE_ERROR (hardware/OC), DPC_WATCHDOG_VIOLATION (storage driver)", "keywords": ["bsod", "error codes", "memory management", "whea"], "difficulty": "intermediate", "tags": ["errors"], "related_tools": []},
            {"content": "BlueScreenView: Free tool reads minidump files, shows crash details (driver, error code, parameters), C:\\Windows\\Minidump location, sort by date, pattern analysis multiple crashes", "keywords": ["bluescreenview", "minidump", "analysis"], "difficulty": "intermediate", "tags": ["tools"], "related_tools": ["BlueScreenView"]},
            {"content": "WinDbg: Microsoft debugger, advanced analysis, !analyze -v command auto-analyzes dump, shows call stack, identifies faulting driver, steep learning curve, expert troubleshooting", "keywords": ["windbg", "debugger", "call stack"], "difficulty": "expert", "tags": ["debugging"], "related_tools": ["WinDbg"]},
            {"content": "Memory dump settings: Small (256 KB, error code only), Kernel (kernel memory, good balance), Complete (full RAM, huge file), set in Advanced System > Startup and Recovery", "keywords": ["memory dump", "kernel dump", "minidump"], "difficulty": "intermediate", "tags": ["configuration"], "related_tools": []},
            {"content": "MEMORY_MANAGEMENT fix: Test RAM (MemTest86 8 passes), disable XMP, increase VCCSA +0.05V, reseat RAM sticks, try one stick at a time (isolate bad module)", "keywords": ["memory management", "ram", "memtest86", "xmp"], "difficulty": "intermediate", "tags": ["troubleshooting"], "related_tools": ["MemTest86"]},
            {"content": "WHEA_UNCORRECTABLE_ERROR fix: CPU/RAM overclock unstable, increase VCore +0.05V, reduce frequency -100 MHz, check Event Viewer WHEA errors (ID 18/19), thermal throttling possible", "keywords": ["whea", "overclock", "vcore", "event viewer"], "difficulty": "advanced", "tags": ["overclocking"], "related_tools": ["Event Viewer", "HWiNFO64"]},
            {"content": "Driver BSOD troubleshooting: Note .sys file in BlueScreenView, update driver (GPU, chipset, network), rollback if started after update, DDU safe mode GPU drivers, disable driver signing (testing only)", "keywords": ["driver", "sys file", "ddu", "update"], "difficulty": "intermediate", "tags": ["drivers"], "related_tools": ["DDU", "BlueScreenView"]},
            {"content": "IRQL_NOT_LESS_OR_EQUAL: Driver accessing wrong memory, often network/audio drivers, update drivers first, disable device Device Manager (isolate), check for conflicting software", "keywords": ["irql", "driver conflict", "network driver"], "difficulty": "advanced", "tags": ["drivers"], "related_tools": []},
            {"content": "DPC_WATCHDOG_VIOLATION: Storage driver timeout, update NVMe/SATA drivers, disable VMware/VirtualBox if not using, check SSD health (CrystalDiskInfo), SATA cable reseat", "keywords": ["dpc watchdog", "storage", "nvme", "sata"], "difficulty": "intermediate", "tags": ["storage"], "related_tools": ["CrystalDiskInfo"]},
            {"content": "Crash pattern analysis: Random crashes = hardware (RAM/PSU), specific app crashes = software/driver, boot loop = corrupted system files (SFC /scannow), game-only crashes = GPU/OC", "keywords": ["pattern", "analysis", "diagnosis"], "difficulty": "advanced", "tags": ["methodology"], "related_tools": []},
            {"content": "Preventing BSOD: Keep drivers updated, validate overclocks thoroughly, quality PSU (avoid cheap brands), monitor temperatures, backup before major changes, Windows updates (defer 1 week test)", "keywords": ["prevention", "stability", "best practices"], "difficulty": "intermediate", "tags": ["best practices"], "related_tools": []},
        ]
    }

    # =============================================================================
    # 11. DIAGNOSTICS EVENT VIEWER
    # =============================================================================
    categories["diagnostics_event_viewer"] = {
        "metadata": {
            "priority": 4,
            "tags": ["diagnostics", "event viewer", "logs", "troubleshooting", "windows"],
            "difficulty": "intermediate",
            "description": "Windows Event Viewer navigation, log analysis, and troubleshooting"
        },
        "tips": [
            {"content": "Event Viewer location: eventvwr.msc (Run dialog), Windows Logs > System (hardware/drivers), Application (software), Security (logins/permissions), expand for details", "keywords": ["event viewer", "eventvwr", "windows logs"], "difficulty": "beginner", "tags": ["windows"], "related_tools": ["Event Viewer"]},
            {"content": "Event levels: Critical (system crash/data loss), Error (problem occurred), Warning (potential issue), Information (normal operation), filter by level for troubleshooting", "keywords": ["critical", "error", "warning", "information"], "difficulty": "beginner", "tags": ["logs"], "related_tools": []},
            {"content": "System log critical events: Kernel-Power 41 (unexpected shutdown/crash), DistributedCOM 10016 (benign, ignore), WHEA-Logger 18/19 (hardware errors OC), EventLog 6008 (improper shutdown)", "keywords": ["system log", "kernel-power", "whea", "critical"], "difficulty": "intermediate", "tags": ["errors"], "related_tools": []},
            {"content": "Application log errors: Application crashes (.NET, faulting module), Windows Update errors (0x8007...), .NET Framework issues, helps identify problematic software", "keywords": ["application log", "crashes", "windows update"], "difficulty": "intermediate", "tags": ["software"], "related_tools": []},
            {"content": "Kernel-Power 41: Unexpected power loss (PSU, OC instability, overheat), BugCheckCode 0 = hard power loss, not BSOD, check PSU cables, power settings, OC stability", "keywords": ["kernel-power 41", "power loss", "psu"], "difficulty": "intermediate", "tags": ["hardware"], "related_tools": []},
            {"content": "WHEA errors (Event ID 18/19): Hardware Error Architecture, Cache Hierarchy errors (CPU), Bus/Interconnect errors (RAM/IMC), Memory errors (RAM), indicates OC instability or failing hardware", "keywords": ["whea", "hardware errors", "cache", "memory"], "difficulty": "advanced", "tags": ["hardware"], "related_tools": ["HWiNFO64"]},
            {"content": "Custom views: Create custom filter (Critical + Error only), specific Event IDs, date range, save view for quick access, 'Administrative Events' pre-made view useful", "keywords": ["custom views", "filter", "administrative events"], "difficulty": "intermediate", "tags": ["workflow"], "related_tools": []},
            {"content": "Event log size: Default 20 MB (rolls over), increase to 100-200 MB (Properties > Maximum log size), 'Archive when full' vs 'Overwrite', larger = better history", "keywords": ["log size", "archive", "retention"], "difficulty": "intermediate", "tags": ["configuration"], "related_tools": []},
            {"content": "Security log: Event ID 4625 (failed login, brute force?), 4624 (successful login), 4672 (admin privileges), 4720 (user account created), audit security incidents", "keywords": ["security log", "login", "audit"], "difficulty": "advanced", "tags": ["security"], "related_tools": []},
            {"content": "Troubleshooting workflow: 1) Note error time, 2) Event Viewer > System/Application at that time, 3) Red (Error) and yellow (Warning) events, 4) Google Event ID + description, 5) Apply fix, 6) Verify cleared", "keywords": ["troubleshooting", "workflow", "methodology"], "difficulty": "intermediate", "tags": ["methodology"], "related_tools": []},
        ]
    }

    # =============================================================================
    # 12. DIAGNOSTICS RELIABILITY MONITOR
    # =============================================================================
    categories["diagnostics_reliability_monitor"] = {
        "metadata": {
            "priority": 3,
            "tags": ["diagnostics", "reliability", "stability", "monitoring", "windows"],
            "difficulty": "beginner",
            "description": "Windows Reliability Monitor for system stability tracking and problem identification"
        },
        "tips": [
            {"content": "Reliability Monitor: perfmon /rel (Run dialog), graphs stability index 1-10 over time, shows crashes/errors/warnings in calendar view, easier than Event Viewer for beginners", "keywords": ["reliability monitor", "perfmon", "stability index"], "difficulty": "beginner", "tags": ["windows"], "related_tools": ["Reliability Monitor"]},
            {"content": "Stability index: 1 = frequent crashes, 10 = rock stable, dips indicate problems, correlate dips with software installs/updates, goal = consistent 9-10 rating", "keywords": ["stability index", "rating", "crashes"], "difficulty": "beginner", "tags": ["monitoring"], "related_tools": []},
            {"content": "Critical events: Red X icons, application crashes, Windows failures, hardware errors, click event for details (links to Event Viewer), identifies problem apps/drivers", "keywords": ["critical events", "crashes", "failures"], "difficulty": "beginner", "tags": ["errors"], "related_tools": []},
            {"content": "Warning events: Yellow ! icons, non-critical issues, Windows updates installed, driver warnings, configuration changes, helps identify patterns", "keywords": ["warnings", "updates", "configuration"], "difficulty": "beginner", "tags": ["logs"], "related_tools": []},
            {"content": "Informational events: Blue i icons, successful operations, software installs/uninstalls, Windows updates, tracks system changes chronologically", "keywords": ["informational", "changes", "history"], "difficulty": "beginner", "tags": ["tracking"], "related_tools": []},
            {"content": "Problem reports: Click 'View technical details', shows crash dump info, faulting module, exception code, can save report, share for troubleshooting help", "keywords": ["problem reports", "crash dump", "technical details"], "difficulty": "intermediate", "tags": ["diagnostics"], "related_tools": []},
            {"content": "History navigation: Calendar view (day-by-day), timeline scrolls back years, identify when stability changed, correlate with hardware changes, driver updates, new software", "keywords": ["history", "calendar", "timeline"], "difficulty": "beginner", "tags": ["analysis"], "related_tools": []},
            {"content": "Common crash patterns: Daily crashes same app = software bug/incompatibility, random crashes = hardware (RAM/PSU), crashes after update = driver regression, new hardware = driver/compatibility", "keywords": ["patterns", "diagnosis", "troubleshooting"], "difficulty": "intermediate", "tags": ["methodology"], "related_tools": []},
            {"content": "Post-crash investigation: Reliability Monitor first (quick overview), Event Viewer second (detailed logs), BlueScreenView if BSOD, cross-reference all three tools", "keywords": ["investigation", "workflow", "multi-tool"], "difficulty": "intermediate", "tags": ["methodology"], "related_tools": ["Event Viewer", "BlueScreenView"]},
            {"content": "Baseline stability: After fresh Windows install + updates, should reach index 10 within days, persistent <8 = investigate, <5 = serious issues (hardware/drivers)", "keywords": ["baseline", "fresh install", "target"], "difficulty": "beginner", "tags": ["benchmarking"], "related_tools": []},
        ]
    }

    # =============================================================================
    # 13. AUDIO DAC AMP
    # =============================================================================
    categories["audio_dac_amp"] = {
        "metadata": {
            "priority": 3,
            "tags": ["audio", "dac", "amp", "headphone", "sound quality"],
            "difficulty": "intermediate",
            "description": "DAC/AMP basics, impedance matching, and audio quality optimization"
        },
        "tips": [
            {"content": "DAC (Digital-to-Analog Converter): Converts digital audio (0s/1s) to analog signal (voltage), better DAC = cleaner signal, ESS Sabre/AKM chips high-end, motherboard DAC adequate <$100 headphones", "keywords": ["dac", "digital", "analog", "ess sabre", "akm"], "difficulty": "intermediate", "tags": ["hardware"], "related_tools": []},
            {"content": "Amp (Amplifier): Increases voltage to drive headphones, high impedance (250Ω+) requires amp, low impedance (<32Ω) works phone/motherboard, power (mW) must exceed headphone requirement", "keywords": ["amp", "amplifier", "impedance", "power"], "difficulty": "intermediate", "tags": ["hardware"], "related_tools": []},
            {"content": "Impedance matching: 32Ω headphones = phone OK, 80-150Ω = desktop/DAC, 250-600Ω = dedicated amp required, mismatched = quiet volume or distortion, check headphone specs", "keywords": ["impedance", "matching", "ohm", "32", "250"], "difficulty": "intermediate", "tags": ["compatibility"], "related_tools": []},
            {"content": "THD (Total Harmonic Distortion): <0.1% good, <0.01% excellent, <0.001% inaudible, measures signal purity, lower = cleaner sound, high THD = muddy/distorted audio", "keywords": ["thd", "distortion", "signal purity"], "difficulty": "advanced", "tags": ["specs"], "related_tools": []},
            {"content": "SNR (Signal-to-Noise Ratio): >100dB good, >110dB excellent, >120dB flagship, measures noise floor, higher = quieter background, important sensitive IEMs", "keywords": ["snr", "signal to noise", "noise floor"], "difficulty": "advanced", "tags": ["specs"], "related_tools": []},
            {"content": "USB DAC vs Optical: USB = easier setup, carries power + data, optical = immune to electrical interference (no ground loop hum), USB preferred modern systems (UAC2 standard)", "keywords": ["usb", "optical", "toslink", "ground loop"], "difficulty": "intermediate", "tags": ["connectivity"], "related_tools": []},
            {"content": "Popular DAC/AMPs: FiiO K5 Pro ($150, 250Ω capable), Schiit Modi/Magni stack ($200, modular), iFi Zen DAC V2 ($160, bass boost), Sound BlasterX G6 ($120, gaming features)", "keywords": ["fiio", "schiit", "ifi", "sound blaster"], "difficulty": "intermediate", "tags": ["products"], "related_tools": []},
            {"content": "Balanced vs Unbalanced: Balanced (XLR, 4.4mm) = dual amp circuits (better separation, more power), Unbalanced (3.5mm, 6.35mm) = standard, balanced matters high-impedance only", "keywords": ["balanced", "xlr", "4.4mm", "unbalanced"], "difficulty": "advanced", "tags": ["advanced"], "related_tools": []},
            {"content": "Sample rate: 44.1kHz (CD quality, sufficient), 96kHz/192kHz (hi-res, inaudible difference blind test), 16-bit vs 24-bit (dynamic range), don't overspend for numbers", "keywords": ["sample rate", "44.1khz", "hi-res", "bit depth"], "difficulty": "intermediate", "tags": ["specs"], "related_tools": []},
            {"content": "Motherboard audio sufficiency: Modern ALC1220 codec good for <$150 headphones, dedicated DAC/AMP worth it for $200+ headphones or EMI noise issues, law of diminishing returns", "keywords": ["motherboard audio", "alc1220", "diminishing returns"], "difficulty": "intermediate", "tags": ["value"], "related_tools": []},
            {"content": "Ground loop hum: 60Hz/120Hz buzzing (AC interference), USB isolator fixes ($30), separate PSU for DAC, optical connection immune, avoid daisy-chaining power strips", "keywords": ["ground loop", "hum", "buzzing", "usb isolator"], "difficulty": "advanced", "tags": ["troubleshooting"], "related_tools": []},
        ]
    }

    # =============================================================================
    # 14. LAPTOP UNDERVOLTING
    # =============================================================================
    categories["laptop_undervolting"] = {
        "metadata": {
            "priority": 4,
            "tags": ["laptop", "undervolting", "temperature", "battery", "throttling"],
            "difficulty": "advanced",
            "description": "Laptop undervolting with Intel XTU and ThrottleStop for temperature and battery improvement"
        },
        "tips": [
            {"content": "Undervolting basics: Reduce CPU voltage at same frequency, 10-15°C temperature drop typical, 0-5% performance loss (or gain from less throttling), better battery life, no hardware risk", "keywords": ["undervolting", "voltage", "temperature", "battery"], "difficulty": "intermediate", "tags": ["laptop"], "related_tools": []},
            {"content": "Intel XTU (Extreme Tuning Utility): Official Intel tool, voltage offset slider, stress test built-in, -100mV typical start, -150mV good silicon, -200mV rare, test stability incremental", "keywords": ["intel xtu", "voltage offset", "stress test"], "difficulty": "intermediate", "tags": ["intel"], "related_tools": ["Intel XTU"]},
            {"content": "ThrottleStop: Advanced alternative to XTU, more features, FIVR (Fully Integrated Voltage Regulator) section, CPU Core/Cache/GPU offset, disable turbo on battery, per-profile settings", "keywords": ["throttlestop", "fivr", "profiles"], "difficulty": "advanced", "tags": ["advanced"], "related_tools": ["ThrottleStop"]},
            {"content": "Voltage offset procedure: Start -50mV, stress test (XTU 30min or Cinebench 5 runs), stable = -75mV, repeat, unstable = rollback +25mV, find sweet spot, CPU + Cache same offset usually", "keywords": ["voltage offset", "procedure", "stability"], "difficulty": "advanced", "tags": ["methodology"], "related_tools": []},
            {"content": "Cache (Ring) undervolting: Cache offset = CPU Core offset usually, separate testing possible, Cache instability = crashes, Core instability = hangs/BSOD, adjust independently if needed", "keywords": ["cache", "ring", "uncore", "stability"], "difficulty": "advanced", "tags": ["advanced"], "related_tools": []},
            {"content": "GPU undervolting: Intel iGPU undervolt possible (ThrottleStop), -50mV to -100mV typical, helps dual graphics laptops, NVIDIA/AMD discrete GPUs = use MSI Afterburner instead", "keywords": ["gpu", "igpu", "undervolt"], "difficulty": "advanced", "tags": ["gpu"], "related_tools": ["ThrottleStop", "MSI Afterburner"]},
            {"content": "Battery savings: Undervolting + lower turbo limits = 20-30% battery life increase, 'On Battery' profile ThrottleStop (disable turbo, lower PL), 'Plugged In' profile (full performance)", "keywords": ["battery", "savings", "profiles", "turbo"], "difficulty": "intermediate", "tags": ["battery"], "related_tools": ["ThrottleStop"]},
            {"content": "Thermal throttling fix: Laptops throttle 90-100°C (TjMax), undervolting shifts throttle point higher, repaste + undervolting = 20-25°C drop, sustains boost clocks longer", "keywords": ["thermal throttling", "tjmax", "repaste"], "difficulty": "advanced", "tags": ["cooling"], "related_tools": []},
            {"content": "BIOS locked undervolting: Some manufacturers (Dell, HP) lock voltage controls BIOS, Plundervolt patch (2019+) disabled undervolting security, research model-specific unlocks or downgrade BIOS (risk)", "keywords": ["bios lock", "plundervolt", "security"], "difficulty": "expert", "tags": ["limitations"], "related_tools": []},
            {"content": "Start with Windows: XTU/ThrottleStop must auto-start (Task Scheduler), 'Run at startup' option, verify active after reboot, undervolt resets on cold boot if not persistent", "keywords": ["startup", "task scheduler", "auto-start"], "difficulty": "intermediate", "tags": ["configuration"], "related_tools": []},
            {"content": "AMD Ryzen laptops: Ryzen Controller (unofficial tool), cTDP limits, Curve Optimizer (BIOS if available), less dramatic than Intel undervolting, 5-10°C improvement typical", "keywords": ["amd", "ryzen", "ryzen controller", "ctdp"], "difficulty": "advanced", "tags": ["amd"], "related_tools": ["Ryzen Controller"]},
        ]
    }

    # =============================================================================
    # 15. LAPTOP BATTERY OPTIMIZATION
    # =============================================================================
    categories["laptop_battery_optimization"] = {
        "metadata": {
            "priority": 4,
            "tags": ["laptop", "battery", "longevity", "charging", "power"],
            "difficulty": "intermediate",
            "description": "Laptop battery care, charge limits, calibration, and longevity optimization"
        },
        "tips": [
            {"content": "Charge limits: 80% max charge extends lifespan (reduces stress), 40-80% sweet spot, ASUS Battery Health Charging, Lenovo Conservation Mode, Dell BIOS charge limit, 100% OK if unplugging daily", "keywords": ["charge limit", "80%", "battery health", "longevity"], "difficulty": "intermediate", "tags": ["battery"], "related_tools": []},
            {"content": "Battery calibration: Fully charge 100%, discharge to 5% (no sleep), recharge 100% uninterrupted, quarterly calibration, resets battery gauge (Windows % accuracy), doesn't restore capacity", "keywords": ["calibration", "battery gauge", "discharge"], "difficulty": "intermediate", "tags": ["maintenance"], "related_tools": []},
            {"content": "Power profiles: Balanced (default), Power Saver (dim screen, low CPU), High Performance (no throttling, more battery drain), Windows 11 'Best power efficiency' better than Power Saver", "keywords": ["power profile", "balanced", "power saver"], "difficulty": "beginner", "tags": ["windows"], "related_tools": []},
            {"content": "Battery report: powercfg /batteryreport (cmd), generates HTML report, design capacity vs full charge capacity, cycle count, recent usage, C:\\Windows\\System32\\battery-report.html", "keywords": ["battery report", "powercfg", "capacity", "cycle count"], "difficulty": "intermediate", "tags": ["diagnostics"], "related_tools": []},
            {"content": "Storage voltage: Long-term storage (1+ months), charge to 50-60%, power off completely (not sleep), cool dry place, prevents deep discharge (unrecoverable) and high voltage stress", "keywords": ["storage", "50%", "long-term", "deep discharge"], "difficulty": "intermediate", "tags": ["storage"], "related_tools": []},
            {"content": "Heat and battery life: >35°C accelerates degradation, avoid gaming on battery (high heat), cooling pad helps, keep vents clear, avoid sun/closed car, heat > charge cycles for degradation", "keywords": ["heat", "temperature", "degradation", "cooling"], "difficulty": "intermediate", "tags": ["longevity"], "related_tools": []},
            {"content": "Fast charging trade-off: 0-80% fast (30-45 min), 80-100% slow (trickle), fast charging generates heat (degrades faster), slow charging better longevity, balance convenience vs lifespan", "keywords": ["fast charging", "slow charging", "heat", "trade-off"], "difficulty": "intermediate", "tags": ["charging"], "related_tools": []},
            {"content": "Cycle count: 1 cycle = 100% discharge (two 50% discharges = 1 cycle), 300-500 cycles typical lifespan (80% capacity), modern batteries 1000+ cycles possible, check battery report", "keywords": ["cycle count", "lifespan", "discharge"], "difficulty": "intermediate", "tags": ["longevity"], "related_tools": []},
            {"content": "Always plugged in: NOT harmful if charge limit 80% enabled, without limit = 100% stress, battery trickle discharge/recharge cycles (micro-cycles), hibernate if unused 2+ days", "keywords": ["always plugged", "desktop replacement", "charge limit"], "difficulty": "intermediate", "tags": ["usage"], "related_tools": []},
            {"content": "Battery saver mode: Windows 10/11 feature, auto-enable <20%, limits background apps, reduces brightness, disables sync, extends emergency battery, customizable threshold Settings > Battery", "keywords": ["battery saver", "windows", "background apps"], "difficulty": "beginner", "tags": ["windows"], "related_tools": []},
            {"content": "Third-party tools: BatteryBar (detailed stats), HWiNFO64 (wear level), BatteryCare (discharge cycles tracking), redundant if using built-in powercfg report, useful for old Windows versions", "keywords": ["batterybar", "hwinfo64", "batterycare"], "difficulty": "intermediate", "tags": ["tools"], "related_tools": ["HWiNFO64", "BatteryBar"]},
        ]
    }

    return categories


def insert_batch_3_into_file(kb_file_path, categories):
    """Insère les catégories Batch 3 avant 'return kb'"""

    print(f"Lecture du fichier: {kb_file_path}")
    with open(kb_file_path, 'r', encoding='utf-8') as f:
        lines = f.readlines()

    # Trouver la ligne "return kb"
    return_kb_index = None
    for i, line in enumerate(lines):
        if line.strip() == "return kb":
            return_kb_index = i
            break

    if return_kb_index is None:
        raise ValueError("Ligne 'return kb' non trouvée dans le fichier!")

    print(f"Ligne 'return kb' trouvée à l'index: {return_kb_index}")

    # Construire le texte des nouvelles catégories
    insertion_text = []
    insertion_text.append("\n")
    insertion_text.append("        # " + "=" * 77 + "\n")
    insertion_text.append("        # BATCH 3 - BENCHMARKING, OVERCLOCKING AVANCÉ, DIAGNOSTICS, SÉCURITÉ\n")
    insertion_text.append("        # (15 catégories - ~150 conseils)\n")
    insertion_text.append("        # " + "=" * 77 + "\n")
    insertion_text.append("\n")

    for cat_name, cat_data in categories.items():
        # Commentaire de catégorie
        insertion_text.append(f"        # {cat_name.upper()}\n")
        insertion_text.append(f"        kb[\"{cat_name}\"] = {{\n")

        # Metadata
        insertion_text.append(f"            \"metadata\": {{\n")
        insertion_text.append(f"                \"priority\": {cat_data['metadata']['priority']},\n")
        insertion_text.append(f"                \"tags\": {cat_data['metadata']['tags']},\n")
        insertion_text.append(f"                \"difficulty\": \"{cat_data['metadata']['difficulty']}\",\n")
        insertion_text.append(f"                \"description\": \"{cat_data['metadata']['description']}\"\n")
        insertion_text.append(f"            }},\n")

        # Tips
        insertion_text.append(f"            \"tips\": [\n")
        for i, tip in enumerate(cat_data['tips']):
            insertion_text.append(f"                {tip}")
            if i < len(cat_data['tips']) - 1:
                insertion_text.append(",\n")
            else:
                insertion_text.append("\n")
        insertion_text.append(f"            ]\n")
        insertion_text.append(f"        }}\n")
        insertion_text.append("\n")

    # Insérer avant "return kb"
    lines[return_kb_index:return_kb_index] = insertion_text

    # Écrire le fichier modifié
    print(f"Écriture du fichier modifié...")
    with open(kb_file_path, 'w', encoding='utf-8') as f:
        f.writelines(lines)

    print("Insertion terminée avec succès!")


def test_import_and_stats(kb_file_path):
    """Teste l'import et affiche les statistiques"""

    print("\n" + "=" * 80)
    print("TEST D'IMPORT ET STATISTIQUES")
    print("=" * 80)

    # Ajouter le répertoire au path pour import
    import sys
    import os
    sys.path.insert(0, os.path.dirname(kb_file_path))

    try:
        # Import du module
        from ai_knowledge_unified import UnifiedKnowledgeBase

        # Initialisation
        print("\nInitialisation de la Knowledge Base...")
        kb_instance = UnifiedKnowledgeBase()

        # Statistiques globales
        all_categories = kb_instance.get_all_categories()
        total_categories = len(all_categories)

        total_tips = 0
        for cat_name in all_categories:
            cat = kb_instance.get_category(cat_name)
            if cat and 'tips' in cat:
                total_tips += len(cat['tips'])

        print(f"\n{'=' * 80}")
        print(f"STATISTIQUES GLOBALES")
        print(f"{'=' * 80}")
        print(f"Nombre total de catégories: {total_categories}")
        print(f"Nombre total de conseils: {total_tips}")
        print(f"Moyenne conseils/catégorie: {total_tips/total_categories:.1f}")
        print(f"Progrès vers objectif 143 catégories: {total_categories}/143 ({total_categories/143*100:.1f}%)")
        print(f"Progrès vers objectif 5000 conseils: {total_tips}/5000 ({total_tips/5000*100:.1f}%)")

        # Statistiques Batch 3 spécifiques
        batch_3_categories = [
            "benchmarking_tools",
            "cpu_overclocking_advanced",
            "ram_overclocking_tightening",
            "gpu_overclocking_curves",
            "bios_uefi_settings",
            "storage_raid_configurations",
            "backup_strategies",
            "security_antivirus",
            "security_firewall",
            "diagnostics_bsod_analysis",
            "diagnostics_event_viewer",
            "diagnostics_reliability_monitor",
            "audio_dac_amp",
            "laptop_undervolting",
            "laptop_battery_optimization"
        ]

        print(f"\n{'=' * 80}")
        print(f"STATISTIQUES BATCH 3 (15 NOUVELLES CATÉGORIES)")
        print(f"{'=' * 80}")

        batch_3_tips = 0
        for cat_name in batch_3_categories:
            cat = kb_instance.get_category(cat_name)
            if cat and 'tips' in cat:
                tips_count = len(cat['tips'])
                batch_3_tips += tips_count
                priority = cat['metadata']['priority']
                difficulty = cat['metadata']['difficulty']
                print(f"  {cat_name:40} | {tips_count:2} conseils | P{priority} | {difficulty:12}")

        print(f"\nTotal Batch 3: {len(batch_3_categories)} catégories, {batch_3_tips} conseils")

        # Vérification que toutes les catégories existent
        missing = []
        for cat_name in batch_3_categories:
            if cat_name not in all_categories:
                missing.append(cat_name)

        if missing:
            print(f"\n[WARNING] Categories manquantes: {missing}")
        else:
            print(f"\n[OK] Toutes les categories du Batch 3 ont ete ajoutees avec succes!")

        print(f"\n{'=' * 80}")
        print("TEST D'IMPORT REUSSI!")
        print(f"{'=' * 80}\n")

        return True

    except Exception as e:
        print(f"\n[ERROR] Erreur lors de l'import: {e}")
        import traceback
        traceback.print_exc()
        return False


def main():
    """Fonction principale"""

    print("=" * 80)
    print("ENRICHISSEMENT KNOWLEDGE BASE - BATCH 3")
    print("15 nouvelles catégories: Benchmarking, OC avancé, Diagnostics, Sécurité")
    print("=" * 80)

    # Chemin du fichier cible
    kb_file_path = r"C:\Users\Utilisateur\Downloads\Nitrite-V18.5\src\v14_mvp\ai_knowledge_unified.py"

    # Créer les catégories
    print("\nCreation des 15 categories Batch 3...")
    categories = create_batch_3_categories()
    print(f"[OK] {len(categories)} categories creees")

    # Compter les tips
    total_tips = sum(len(cat['tips']) for cat in categories.values())
    print(f"[OK] {total_tips} conseils generes")

    # Insérer dans le fichier
    print(f"\nInsertion dans {kb_file_path}...")
    insert_batch_3_into_file(kb_file_path, categories)

    # Test d'import et stats
    test_import_and_stats(kb_file_path)


if __name__ == "__main__":
    main()
