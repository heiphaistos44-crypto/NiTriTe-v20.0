#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Script batch pour ajouter des catégories massives à ai_knowledge_unified.py
Mode silencieux pour éviter les problèmes d'encodage console
"""

import os
import sys


def add_storage_and_motherboard_categories():
    """
    Ajoute 4 catégories Storage + Motherboard/PSU
    Chaque catégorie a 25-30 conseils RÉELS et TECHNIQUES
    """

    file_path = r"C:\Users\Utilisateur\Downloads\Nitrite-V18.5\src\v14_mvp\ai_knowledge_unified.py"

    # Lire le fichier
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # Trouver le point d'insertion (avant "return kb")
    marker = "        return kb"
    insertion_point = content.rfind(marker)

    if insertion_point == -1:
        print("ERROR: Marker not found")
        return False

    # Générer les 4 catégories (Storage × 2, Motherboard/PSU × 2)
    new_code = '''
        # =============================================================================
        # STORAGE (2 categories)
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
                {"content": "PCIe Gen4 speeds: 7000-7450 MB/s read typical (Samsung 980 Pro, WD SN850X), 5000-6800 MB/s write, 4x faster than SATA SSD", "keywords": ["gen4", "7000 mbs", "nvme"], "difficulty": "intermediate", "tags": ["performance"], "related_tools": ["CrystalDiskMark"]},
                {"content": "PCIe Gen5 speeds: 10000-12400 MB/s read (Crucial T700), real-world gaming benefit minimal 2024, future-proofing only", "keywords": ["gen5", "12000 mbs"], "difficulty": "advanced", "tags": ["future"], "related_tools": ["CrystalDiskMark"]},
                {"content": "Samsung 980 Pro: PCIe 4.0, 7000 MB/s, TLC NAND, 1200 TBW for 2TB, industry reliability standard, 130-150 euros/TB", "keywords": ["980 pro", "samsung", "reliable"], "difficulty": "intermediate", "tags": ["recommendation"], "related_tools": ["Samsung Magician"]},
                {"content": "WD Black SN850X: 7300 MB/s, Game Mode 2.0, excellent random IOPS, PS5 compatible, 120-140 euros/TB competitive", "keywords": ["sn850x", "western digital"], "difficulty": "intermediate", "tags": ["gaming"], "related_tools": ["WD Dashboard"]},
                {"content": "SK Hynix Platinum P41: 7000 MB/s, excellent efficiency, low temps, 176-layer NAND, underrated gem 110-130 euros/TB", "keywords": ["p41", "hynix", "efficient"], "difficulty": "intermediate", "tags": ["value"], "related_tools": []},
                {"content": "TBW (Total Bytes Written): 600 TBW for 1TB typical, 1200 TBW for 2TB, 10-year warranty most brands, endurance rating", "keywords": ["tbw", "endurance", "warranty"], "difficulty": "intermediate", "tags": ["reliability"], "related_tools": ["CrystalDiskInfo"]},
                {"content": "DRAM cache importance: Dedicated DRAM buffer improves sustained writes, DRAMless OK for budget, DRAM mandatory for OS drive", "keywords": ["dram cache", "buffer"], "difficulty": "advanced", "tags": ["architecture"], "related_tools": []},
                {"content": "SLC cache: Pseudo-SLC mode for burst writes, 100-200 GB cache typical, saturates after 50GB+ transfers, TLC converts back", "keywords": ["slc cache", "write cache"], "difficulty": "advanced", "tags": ["architecture"], "related_tools": []},
                {"content": "DirectStorage Windows 11: GPU decompression for gaming, requires Gen4+ NVMe and RTX/RX GPU, 2-3x faster load times supported games", "keywords": ["directstorage", "windows 11", "gpu"], "difficulty": "intermediate", "tags": ["gaming"], "related_tools": []},
                {"content": "4K random IOPS: More important than sequential for OS responsiveness, 500K+ IOPS read typical Gen4, snappier feel", "keywords": ["4k iops", "random", "responsiveness"], "difficulty": "advanced", "tags": ["performance"], "related_tools": ["CrystalDiskMark"]},
                {"content": "Thermal throttling NVMe: 70-80C typical load, 85C+ throttles to 50% speed, Gen5 requires heatsink mandatory, Gen4 recommended", "keywords": ["thermal throttling", "temperature"], "difficulty": "intermediate", "tags": ["cooling"], "related_tools": ["HWiNFO64"]},
                {"content": "M.2 heatsinks: Motherboard integrated best (metal contact), adhesive aftermarket OK, thermal pads 1-2mm, Gen5 needs active", "keywords": ["heatsink", "m.2", "cooling"], "difficulty": "intermediate", "tags": ["cooling"], "related_tools": []},
                {"content": "NVMe form factors: M.2 2280 (80mm) standard desktop, 2242/2260 for laptops, U.2 enterprise, verify motherboard slot compatibility", "keywords": ["m.2 2280", "form factor"], "difficulty": "beginner", "tags": ["hardware"], "related_tools": []},
                {"content": "PCIe lane sharing: M.2 slot may disable SATA ports or share GPU lanes, check motherboard manual, Gen5 CPU lanes only typically", "keywords": ["pcie lanes", "sharing", "sata"], "difficulty": "intermediate", "tags": ["compatibility"], "related_tools": []},
                {"content": "Boot drive sizing: 500GB minimum OS + apps, 1TB sweet spot gaming, 2TB future-proof, separate data drive optional", "keywords": ["capacity", "500gb", "1tb"], "difficulty": "beginner", "tags": ["buying"], "related_tools": []},
                {"content": "Real-world gaming: Gen4 vs SATA load times 1-3s faster, Gen5 vs Gen4 marginal 0.5s, DirectStorage future benefit", "keywords": ["gaming", "load times", "real world"], "difficulty": "intermediate", "tags": ["gaming"], "related_tools": []},
                {"content": "Productivity workloads: Video editing 4K+ benefits from Gen4 speed, photo editing minimal difference, 3D asset streaming uses bandwidth", "keywords": ["productivity", "video editing"], "difficulty": "intermediate", "tags": ["productivity"], "related_tools": []},
                {"content": "QLC vs TLC NAND: TLC (3-bit) faster writes and endurance, QLC (4-bit) cheaper but slower sustained, TLC for boot drive", "keywords": ["qlc", "tlc", "nand"], "difficulty": "advanced", "tags": ["architecture"], "related_tools": []},
                {"content": "Controller importance: Phison E18/E26, Samsung Elpis, WD in-house controllers, firmware updates fix bugs, check brand software", "keywords": ["controller", "phison", "firmware"], "difficulty": "advanced", "tags": ["technical"], "related_tools": []},
                {"content": "CrystalDiskMark benchmark: Sequential Q32T1 tests queue depth, 4K Q1T1 real-world responsiveness, run 5 passes consistency", "keywords": ["crystaldiskmark", "benchmark"], "difficulty": "intermediate", "tags": ["benchmark"], "related_tools": ["CrystalDiskMark"]},
                {"content": "Health monitoring: SMART attributes track TBW usage, Power-On Hours, wear leveling, CrystalDiskInfo shows health %, replace <10%", "keywords": ["smart", "health", "monitoring"], "difficulty": "intermediate", "tags": ["maintenance"], "related_tools": ["CrystalDiskInfo"]},
                {"content": "Secure Erase: Returns SSD to factory state, improves performance degraded drive, use manufacturer tool (Samsung Magician), backup first", "keywords": ["secure erase", "factory reset"], "difficulty": "advanced", "tags": ["maintenance"], "related_tools": ["Samsung Magician"]},
                {"content": "Over-provisioning: Reserve 10% unallocated space for wear leveling, improves longevity 20-30%, manual setup or manufacturer tool", "keywords": ["over-provisioning", "wear leveling"], "difficulty": "advanced", "tags": ["optimization"], "related_tools": []},
                {"content": "RAID 0 NVMe: Doubles sequential speed theoretically, complexity not worth it, single large SSD better, RAID controller overhead", "keywords": ["raid 0", "striping"], "difficulty": "expert", "tags": ["advanced"], "related_tools": []},
                {"content": "Best value Gen4 2024: WD SN850X 1TB 100 euros, Samsung 980 Pro 1TB 110 euros, SK Hynix P41 1TB 95 euros, avoid DRAMless for OS", "keywords": ["value", "recommendation"], "difficulty": "beginner", "tags": ["buying"], "related_tools": []}
            ]
        }

        # 8. SSD Optimization Windows
        kb["ssd_optimization_windows"] = {
            "metadata": {
                "priority": 4,
                "tags": ["ssd", "windows", "optimization"],
                "difficulty": "intermediate",
                "description": "Windows SSD optimization and maintenance"
            },
            "tips": [
                {"content": "TRIM support: Enabled by default Windows 10/11, verify 'fsutil behavior query DisableDeleteNotify' (0 = enabled), maintains performance", "keywords": ["trim", "fsutil"], "difficulty": "intermediate", "tags": ["windows"], "related_tools": []},
                {"content": "Disable defragmentation: Windows auto-detects SSD and runs TRIM instead, verify Optimize Drives shows 'Optimize' not 'Defragment'", "keywords": ["defrag", "disable"], "difficulty": "beginner", "tags": ["windows"], "related_tools": []},
                {"content": "AHCI mode: Enable in BIOS before Windows install, 20-30% better performance than IDE mode, changing post-install requires registry", "keywords": ["ahci", "bios"], "difficulty": "intermediate", "tags": ["bios"], "related_tools": []},
                {"content": "4K alignment: Modern Windows auto-aligns at 1MB, check with AS SSD Benchmark, misalignment causes 50% performance loss", "keywords": ["4k alignment", "partition"], "difficulty": "advanced", "tags": ["partition"], "related_tools": ["AS SSD Benchmark"]},
                {"content": "Over-provisioning setup: Leave 10% unallocated after last partition, improves write endurance and sustained performance, free boost", "keywords": ["over-provisioning", "unallocated"], "difficulty": "advanced", "tags": ["optimization"], "related_tools": []},
                {"content": "Disable Superfetch/Prefetch: Not needed for SSD (instant access), Windows auto-disables Superfetch, manually disable Prefetch in services", "keywords": ["superfetch", "prefetch"], "difficulty": "intermediate", "tags": ["windows"], "related_tools": []},
                {"content": "Hibernation file: hiberfil.sys equals RAM size, delete with 'powercfg -h off' if tight space, re-enable 'powercfg -h on'", "keywords": ["hibernation", "hiberfil.sys"], "difficulty": "intermediate", "tags": ["windows"], "related_tools": []},
                {"content": "Page file optimization: Set fixed size (initial = max) less fragmentation, 8-16GB sufficient gaming, or disable if 32GB+ RAM (risky)", "keywords": ["page file", "pagefile.sys"], "difficulty": "advanced", "tags": ["windows"], "related_tools": []},
                {"content": "System Restore points: Disable to save 10-20GB if doing regular backups, keep enabled if no backup solution, adjust max 2-5%", "keywords": ["system restore", "space"], "difficulty": "beginner", "tags": ["windows"], "related_tools": []},
                {"content": "Write caching: Enable in Device Manager > Disk Properties > Policies > 'Enable write caching', improves write performance 10-15%", "keywords": ["write caching", "device manager"], "difficulty": "intermediate", "tags": ["windows"], "related_tools": []},
                {"content": "Disable indexing: Right-click drive > Properties > uncheck 'Allow files to be indexed', saves writes, search slower (negligible SSD)", "keywords": ["indexing", "search"], "difficulty": "intermediate", "tags": ["windows"], "related_tools": []},
                {"content": "Temp file cleanup: Use Disk Cleanup (cleanmgr) or Storage Sense, auto-clean temp files monthly, saves 5-20GB", "keywords": ["temp files", "cleanup"], "difficulty": "beginner", "tags": ["maintenance"], "related_tools": ["Disk Cleanup"]},
                {"content": "Move downloads/documents: Relocate user folders to secondary drive, saves SSD writes, Properties > Location tab > Move", "keywords": ["move folders", "documents"], "difficulty": "intermediate", "tags": ["configuration"], "related_tools": []},
                {"content": "Windows Update cleanup: Run Disk Cleanup > Clean up system files, deletes old updates, recovers 2-10GB after major updates", "keywords": ["windows update", "cleanup"], "difficulty": "beginner", "tags": ["maintenance"], "related_tools": ["Disk Cleanup"]},
                {"content": "Disable System Protection: If using external backup, turn off per-drive saves writes and space, System Properties > System Protection", "keywords": ["system protection", "disable"], "difficulty": "intermediate", "tags": ["windows"], "related_tools": []},
                {"content": "Browser cache location: Move Chrome/Firefox cache to RAM disk or secondary drive, reduces SSD writes 2-5GB daily heavy browsing", "keywords": ["browser cache", "chrome"], "difficulty": "advanced", "tags": ["browser"], "related_tools": []},
                {"content": "WinDirStat analysis: Visualize disk usage, find large files, free portable tool, run monthly to identify waste", "keywords": ["windirstat", "disk usage"], "difficulty": "beginner", "tags": ["tool"], "related_tools": ["WinDirStat"]},
                {"content": "TreeSize alternative: Faster than WinDirStat, free version sufficient, sorts by size, identifies duplicates", "keywords": ["treesize", "disk analysis"], "difficulty": "beginner", "tags": ["tool"], "related_tools": ["TreeSize"]},
                {"content": "Partition alignment check: CMD 'msinfo32' > Components > Storage > Disks, Partition Starting Offset divisible by 4096 = aligned", "keywords": ["partition alignment", "msinfo32"], "difficulty": "advanced", "tags": ["diagnostic"], "related_tools": []},
                {"content": "Storage Spaces warning: Windows RAID alternative adds overhead, single fast SSD better than Storage Spaces pool, enterprise feature", "keywords": ["storage spaces", "raid"], "difficulty": "advanced", "tags": ["windows"], "related_tools": []},
                {"content": "Fast Startup disable: Hybrid hibernate/shutdown can cause issues, disable in Power Options > Choose what power buttons do", "keywords": ["fast startup", "disable"], "difficulty": "intermediate", "tags": ["windows"], "related_tools": []},
                {"content": "Game install location: AAA games 100GB+ each, install on secondary SSD/HDD if limited boot space, load time difference minimal Gen4", "keywords": ["games", "install location"], "difficulty": "beginner", "tags": ["gaming"], "related_tools": []},
                {"content": "Symbolic links: mklink command to fake game location on other drive, appears in original location, advanced capacity management", "keywords": ["symbolic links", "mklink"], "difficulty": "expert", "tags": ["advanced"], "related_tools": []},
                {"content": "UEFI vs MBR: Use GPT/UEFI for modern systems, MBR legacy, UEFI required for Secure Boot and >2TB drives, convert mbr2gpt", "keywords": ["uefi", "gpt", "mbr"], "difficulty": "intermediate", "tags": ["partition"], "related_tools": []},
                {"content": "Windows 11 DirectStorage: Requires NVMe (Gen4+), RTX/RX GPU, game support needed, future-proofs for 2025+ titles", "keywords": ["directstorage", "windows 11"], "difficulty": "intermediate", "tags": ["windows"], "related_tools": []}
            ]
        }

        # =============================================================================
        # MOTHERBOARD & PSU (2 categories)
        # =============================================================================

        # 9. Motherboard Features Comparison
        kb["motherboard_features_comparison"] = {
            "metadata": {
                "priority": 4,
                "tags": ["motherboard", "hardware", "features"],
                "difficulty": "intermediate",
                "description": "Motherboard features and chipset comparison"
            },
            "tips": [
                {"content": "VRM phases importance: 10+ phases sufficient mid-range CPUs (i5/R5), 14-20 phases high-end (i9/R9), overkill costs more", "keywords": ["vrm", "phases"], "difficulty": "advanced", "tags": ["power"], "related_tools": []},
                {"content": "VRM heatsinks: Mandatory for K/X-series CPUs, passive sufficient 95% cases, active fan extreme boards, direct MOSFETs cooling", "keywords": ["vrm heatsinks", "cooling"], "difficulty": "intermediate", "tags": ["cooling"], "related_tools": []},
                {"content": "PCIe 5.0 GPU slot: x16 Gen5 on high-end (Z790, X670E), current GPUs Gen4, future RTX 5000 may use Gen5, backward compatible", "keywords": ["pcie 5.0", "gpu slot"], "difficulty": "intermediate", "tags": ["expansion"], "related_tools": []},
                {"content": "PCIe 5.0 M.2 slot: One Gen5 M.2 typical high-end, shares CPU lanes, Gen5 SSD overkill 2024, Gen4 sufficient gaming", "keywords": ["pcie 5.0", "m.2"], "difficulty": "intermediate", "tags": ["storage"], "related_tools": []},
                {"content": "DDR5 support: Z790/Z690 Intel dual DDR5/DDR4, AM5 DDR5 only, verify board spec, DDR5 default 4800 MT/s (enable XMP for rated)", "keywords": ["ddr5", "support"], "difficulty": "beginner", "tags": ["memory"], "related_tools": []},
                {"content": "WiFi 6E (802.11ax): 6 GHz band support, less congestion than WiFi 6, built-in on high-end, PCIe card alternative 30-50 euros", "keywords": ["wifi 6e", "wireless"], "difficulty": "intermediate", "tags": ["networking"], "related_tools": []},
                {"content": "Bluetooth 5.3: Latest version on modern boards, backward compatible, 2x speed vs BT 5.0, lower latency for peripherals", "keywords": ["bluetooth", "5.3"], "difficulty": "beginner", "tags": ["connectivity"], "related_tools": []},
                {"content": "USB 4.0 support: 40 Gbps bandwidth, Thunderbolt 3/4 compatible, rare on AM5 (Intel only typically), USB-C connector, docks/eGPU", "keywords": ["usb 4.0", "40gbps"], "difficulty": "advanced", "tags": ["connectivity"], "related_tools": []},
                {"content": "2.5G Ethernet: Standard on mid-range+, Intel i225-V or Realtek 8125B controller, 2.5x faster than 1G, sufficient home", "keywords": ["2.5g ethernet", "lan"], "difficulty": "intermediate", "tags": ["networking"], "related_tools": []},
                {"content": "10G Ethernet: Enthusiast/workstation feature, requires 10G switch (expensive), Intel X550, overkill consumer, NAS/server use", "keywords": ["10g ethernet", "x550"], "difficulty": "advanced", "tags": ["networking"], "related_tools": []},
                {"content": "BIOS Flashback: Update BIOS without CPU/RAM/GPU, button on I/O panel, USB with renamed file, essential for new CPU compat", "keywords": ["bios flashback", "q-flash"], "difficulty": "intermediate", "tags": ["bios"], "related_tools": []},
                {"content": "Clear CMOS button: External I/O button convenient, internal jumper alternative, resets BIOS to defaults (bad OC recovery)", "keywords": ["clear cmos", "reset"], "difficulty": "beginner", "tags": ["troubleshooting"], "related_tools": []},
                {"content": "POST code display: Debug LED shows boot error codes, premium boards, identifies failures (RAM, CPU, GPU, Boot device)", "keywords": ["post code", "debug"], "difficulty": "intermediate", "tags": ["troubleshooting"], "related_tools": []},
                {"content": "M.2 slot count: 2-3 slots budget, 4-5 high-end, verify Gen4 vs Gen3, check SATA sharing (manual), heatsinks included mid+", "keywords": ["m.2 slots", "nvme"], "difficulty": "intermediate", "tags": ["storage"], "related_tools": []},
                {"content": "SATA ports: 4-6 ports typical, SATA 3 (6 Gbps), M.2 usage may disable some ports (check manual), legacy HDD/SSD/optical", "keywords": ["sata", "ports"], "difficulty": "beginner", "tags": ["storage"], "related_tools": []},
                {"content": "Audio codec: Realtek ALC1220 budget/mid, ALC4080 high-end, ESS Sabre DAC enthusiast, onboard sufficient 95%, external DAC audiophile", "keywords": ["audio", "codec"], "difficulty": "intermediate", "tags": ["audio"], "related_tools": []},
                {"content": "RGB headers: 12V RGB and 5V ARGB headers, verify count and amperage for strips/fans, software control (ASUS Aura, MSI Mystic Light)", "keywords": ["rgb", "argb"], "difficulty": "intermediate", "tags": ["rgb"], "related_tools": []},
                {"content": "Fan headers: 6+ headers ideal (CPU, AIO pump, chassis fans), PWM 4-pin preferred, DC 3-pin legacy, 1A per header typical", "keywords": ["fan headers", "pwm"], "difficulty": "intermediate", "tags": ["cooling"], "related_tools": []},
                {"content": "Chipset Z790 vs B760: Z790 has CPU OC, more PCIe lanes, better VRM, B760 locked CPU (memory OC OK), sufficient gaming", "keywords": ["z790", "b760"], "difficulty": "intermediate", "tags": ["intel"], "related_tools": []},
                {"content": "Chipset X670E vs B650: X670E dual PCIe 5.0, more I/O, B650 single PCIe 5.0, both allow CPU/RAM OC, B650 value", "keywords": ["x670e", "b650"], "difficulty": "intermediate", "tags": ["amd"], "related_tools": []},
                {"content": "Form factors: ATX (305x244mm) standard, Micro-ATX (244x244mm) compact, Mini-ITX (170x170mm) SFF, verify case compatibility", "keywords": ["form factor", "atx"], "difficulty": "beginner", "tags": ["size"], "related_tools": []},
                {"content": "CPU socket compatibility: LGA1700 (Intel 12th-14th), AM5 (Ryzen 7000+), verify physical fit, BIOS update may needed newer CPUs", "keywords": ["socket", "lga1700"], "difficulty": "beginner", "tags": ["compatibility"], "related_tools": []},
                {"content": "Reinforced PCIe slots: Metal shielding prevents GPU sag damage, standard mid-range+, aesthetics + structural integrity", "keywords": ["reinforced slot", "gpu sag"], "difficulty": "intermediate", "tags": ["durability"], "related_tools": []},
                {"content": "TPM 2.0: Windows 11 requirement, fTPM in BIOS (firmware) or discrete TPM header, enable in BIOS Security settings", "keywords": ["tpm", "tpm 2.0"], "difficulty": "intermediate", "tags": ["windows"], "related_tools": []},
                {"content": "Best value boards 2024: MSI PRO B650-P (AM5 100 euros), ASUS TUF B760 (LGA1700 150 euros), avoid cheapest sub-100", "keywords": ["value", "recommendation"], "difficulty": "beginner", "tags": ["buying"], "related_tools": []}
            ]
        }

        # 10. PSU Selection Guide
        kb["psu_selection_guide"] = {
            "metadata": {
                "priority": 5,
                "tags": ["psu", "power", "hardware"],
                "difficulty": "intermediate",
                "description": "Power supply selection and efficiency ratings"
            },
            "tips": [
                {"content": "80+ Bronze: 82-85% efficiency, budget PSUs 50-80 euros, sufficient low-power builds (300W), semi-modular typical", "keywords": ["80+ bronze", "efficiency"], "difficulty": "beginner", "tags": ["budget"], "related_tools": []},
                {"content": "80+ Gold: 87-90% efficiency, sweet spot value 80-150 euros, mid-range builds, fully modular available, 10-year warranty brands", "keywords": ["80+ gold", "efficiency"], "difficulty": "intermediate", "tags": ["value"], "related_tools": []},
                {"content": "80+ Platinum: 89-92% efficiency, high-end 150-250 euros, diminishing returns vs Gold, silent operation, 12-year warranty", "keywords": ["80+ platinum", "efficiency"], "difficulty": "intermediate", "tags": ["high-end"], "related_tools": []},
                {"content": "80+ Titanium: 90-94% efficiency, enthusiast/server 250+ euros, marginal gains over Platinum, silent premium, 12-15 year warranty", "keywords": ["80+ titanium", "efficiency"], "difficulty": "advanced", "tags": ["enthusiast"], "related_tools": []},
                {"content": "ATX 3.0 standard: New spec for RTX 40 series, 12VHPWR native cable, transient power spike handling 200%+ rated, backward compatible", "keywords": ["atx 3.0", "12vhpwr"], "difficulty": "intermediate", "tags": ["standard"], "related_tools": []},
                {"content": "12VHPWR cable: 600W capable single cable, 16-pin (12+4), used RTX 4070 Ti+, proper seating critical (melting risk), 35mm bend radius min", "keywords": ["12vhpwr", "600w"], "difficulty": "intermediate", "tags": ["cables"], "related_tools": []},
                {"content": "PCIe 5.0 ready: Handles GPU transient spikes (RTX 4090 600W peaks), ATX 3.0 PSUs recommended RTX 40, ATX 2.x works with adapters", "keywords": ["pcie 5.0", "transient"], "difficulty": "advanced", "tags": ["compatibility"], "related_tools": []},
                {"content": "Modular vs semi-modular: Fully modular detaches all cables (clean builds), semi-modular 24-pin + 8-pin fixed, non-modular budget mess", "keywords": ["modular", "semi-modular"], "difficulty": "beginner", "tags": ["aesthetics"], "related_tools": []},
                {"content": "Wattage calculation: Add CPU TDP + GPU TDP + 100W overhead, 20-30% headroom for efficiency sweet spot (50-80% load optimal)", "keywords": ["wattage", "calculation"], "difficulty": "intermediate", "tags": ["sizing"], "related_tools": []},
                {"content": "RTX 4090 system: 850W minimum (1000W recommended), i9-14900K + 4090 peak 700W, transient spikes 800W+, 1000W safe overhead", "keywords": ["rtx 4090", "850w"], "difficulty": "intermediate", "tags": ["high-end"], "related_tools": []},
                {"content": "RTX 4070 Ti system: 650W sufficient, 750W recommended overhead, i5/R5 + 4070 Ti peak 450W, 750W sweet spot efficiency", "keywords": ["rtx 4070", "650w"], "difficulty": "intermediate", "tags": ["mid-range"], "related_tools": []},
                {"content": "Budget gaming build: 550-650W for RTX 4060/RX 7600 + mid CPU, 80+ Bronze minimum, semi-modular preferred, 50-80 euros", "keywords": ["budget", "550w"], "difficulty": "beginner", "tags": ["budget"], "related_tools": []},
                {"content": "Single rail vs multi-rail: Single rail simplifies high-power GPUs (no OCP trips), multi-rail safer component protection, modern PSUs single", "keywords": ["single rail", "multi-rail"], "difficulty": "advanced", "tags": ["technical"], "related_tools": []},
                {"content": "OCP/OVP/UVP protections: Overcurrent, overvoltage, undervoltage protection mandatory, OTP (temperature) preferred, SCP (short circuit) critical", "keywords": ["ocp", "ovp"], "difficulty": "advanced", "tags": ["safety"], "related_tools": []},
                {"content": "Fan noise: 120mm fan quieter than 140mm (lower RPM), semi-passive (0 RPM idle) on quality PSUs, fan replacement voids warranty", "keywords": ["fan noise", "120mm"], "difficulty": "intermediate", "tags": ["noise"], "related_tools": []},
                {"content": "Cable length: Verify 24-pin ATX and PCIe cables reach in large cases, extension cables available, custom cables aesthetics (CableMod)", "keywords": ["cable length", "extension"], "difficulty": "intermediate", "tags": ["compatibility"], "related_tools": []},
                {"content": "Warranty period: 5 years minimum, 7-10 years mid-range, 12 years high-end (Corsair RMx, SeaSonic), warranty indicates confidence", "keywords": ["warranty", "5 years"], "difficulty": "intermediate", "tags": ["reliability"], "related_tools": []},
                {"content": "Brands tier list: Tier A (SeaSonic, Corsair RMx, EVGA G6), Tier B (Corsair CX, EVGA BQ), Tier C+ (budget), avoid Tier D (fire hazard)", "keywords": ["brands", "tier list"], "difficulty": "beginner", "tags": ["buying"], "related_tools": []},
                {"content": "OEM manufacturers: SeaSonic, CWT, FSP, HEC make PSUs for brands, same OEM different quality tiers, check PSU review sites (Tom's Hardware)", "keywords": ["oem", "seasonic"], "difficulty": "advanced", "tags": ["technical"], "related_tools": []},
                {"content": "ATX vs SFX: ATX (150mm) standard desktop, SFX (125mm) compact ITX cases, SFX-L (130mm) hybrid, ATX cheaper and quieter", "keywords": ["atx", "sfx"], "difficulty": "intermediate", "tags": ["form factor"], "related_tools": []},
                {"content": "Efficiency curve: 50-80% load most efficient, avoid <20% or >90% load (reduced efficiency), size PSU for typical usage not peak", "keywords": ["efficiency curve", "load"], "difficulty": "advanced", "tags": ["efficiency"], "related_tools": []},
                {"content": "Ripple and noise: <50mV good quality, <30mV excellent, <20mV enthusiast, affects component longevity, check professional reviews", "keywords": ["ripple", "noise"], "difficulty": "expert", "tags": ["quality"], "related_tools": []},
                {"content": "Voltage regulation: ±3% tolerance acceptable, ±1% excellent, stable rails critical for OC stability, budget PSUs ±5% (avoid)", "keywords": ["voltage regulation", "tolerance"], "difficulty": "advanced", "tags": ["quality"], "related_tools": []},
                {"content": "Best value 2024: Corsair RM750e (80+ Gold 750W ATX 3.0) 100 euros, SeaSonic Focus GX-850 90 euros, EVGA SuperNOVA 850 G6 110 euros", "keywords": ["value", "2024"], "difficulty": "beginner", "tags": ["buying"], "related_tools": []},
                {"content": "Never cheap out PSU: Failed PSU can destroy entire system (surge/fire), invest 100-150 euros mid-range minimum, 10% total budget", "keywords": ["importance", "safety"], "difficulty": "beginner", "tags": ["safety"], "related_tools": []}
            ]
        }

'''

    # Insérer le nouveau code
    new_content = content[:insertion_point] + new_code + "\n" + content[insertion_point:]

    # Sauvegarder
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(new_content)

    return True


if __name__ == "__main__":
    print("Batch adding 4 categories (Storage × 2, Motherboard/PSU × 2)...")
    print()

    try:
        success = add_storage_and_motherboard_categories()

        if success:
            # Vérifier le résultat
            sys.path.insert(0, r"C:\Users\Utilisateur\Downloads\Nitrite-V18.5\src\v14_mvp")
            from ai_knowledge_unified import UnifiedKnowledgeBase

            kb = UnifiedKnowledgeBase()
            stats = kb.get_stats()

            print()
            print("SUCCESS!")
            print(f"  Categories: {stats['categories']}")
            print(f"  Total Tips: {stats['tips']}")
            print(f"  Avg Tips/Cat: {stats['avg_tips_per_category']:.1f}")
            print()
            print("Added categories:")
            print("  - ssd_nvme_gen4_gen5 (25 tips)")
            print("  - ssd_optimization_windows (25 tips)")
            print("  - motherboard_features_comparison (25 tips)")
            print("  - psu_selection_guide (25 tips)")
        else:
            print("ERROR during insertion")

    except Exception as e:
        print(f"ERROR: {e}")
