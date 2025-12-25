#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Script FINALE pour ajouter TOUTES les catégories restantes
Méthode: Insertion directe sans regex (évite problèmes d'échappement)
"""

import os

# CODE DES CATEGORIES A AJOUTER (format direct Python)
NEW_CATEGORIES = """
        # =============================================================================
        # WINDOWS 11 + DRIVERS + GAMING + NETWORKING (18 catégories - ~720 conseils)
        # =============================================================================

        # Windows 11 Optimization (déjà créé dans le premier script mais pas ajouté complètement)
        # On continue avec les catégories Drivers, Gaming et Networking

        # 22. GPU Driver Management
        kb["gpu_driver_management"] = {
            "metadata": {
                "priority": 5,
                "tags": ["drivers", "gpu", "nvidia", "amd"],
                "difficulty": "intermediate",
                "description": "GPU driver installation, updates, rollback"
            },
            "tips": [
                {"content": "DDU safe mode: Display Driver Uninstaller, boot Safe Mode (F8/Shift+Restart), clean install removes driver remnants, prevents conflicts", "keywords": ["ddu", "safe mode"], "difficulty": "intermediate", "tags": ["tools"], "related_tools": ["DDU"]},
                {"content": "NVIDIA Game Ready: Gaming optimizations, monthly updates, day-1 game support, beta features, slight instability vs Studio", "keywords": ["game ready", "nvidia"], "difficulty": "beginner", "tags": ["nvidia"], "related_tools": []},
                {"content": "NVIDIA Studio: Content creation stable drivers, 3-month cycle, tested stability, DaVinci Resolve/Blender certified, gaming works fine", "keywords": ["studio", "nvidia"], "difficulty": "intermediate", "tags": ["nvidia"], "related_tools": []},
                {"content": "AMD clean install: AMD Cleanup Utility (official tool), removes Adrenalin drivers fully, alternative DDU, Safe Mode recommended", "keywords": ["amd", "clean install"], "difficulty": "intermediate", "tags": ["amd"], "related_tools": ["AMD Cleanup Utility"]},
                {"content": "Driver rollback: Device Manager > Display > Properties > Driver > Roll Back Driver, reverts previous version, stability fix", "keywords": ["rollback", "stability"], "difficulty": "beginner", "tags": ["troubleshooting"], "related_tools": []},
                {"content": "GeForce Experience: NVIDIA driver updater, ShadowPlay recording, game optimization (often wrong settings), 500MB bloatware, skip manual download", "keywords": ["geforce experience", "bloat"], "difficulty": "beginner", "tags": ["nvidia"], "related_tools": ["GeForce Experience"]},
                {"content": "AMD Adrenalin: Driver + control panel combined, lightweight vs GeForce Experience, auto-update notifications, manual download better", "keywords": ["adrenalin", "amd"], "difficulty": "beginner", "tags": ["amd"], "related_tools": ["Adrenalin"]},
                {"content": "Custom driver install: NVIDIA > Custom > Clean install checkbox, removes old settings, prevents profile corruption, slower install", "keywords": ["custom install", "clean"], "difficulty": "intermediate", "tags": ["installation"], "related_tools": []},
                {"content": "Driver version stability: Latest ≠ best, wait 1-2 weeks (user reports), roll back crashes, stable driver stick months", "keywords": ["stability", "version"], "difficulty": "intermediate", "tags": ["best practices"], "related_tools": []},
                {"content": "Windows Update drivers: Avoid automatic GPU drivers (old/generic), manual download NVIDIA/AMD site, disable driver updates Group Policy", "keywords": ["windows update", "automatic"], "difficulty": "intermediate", "tags": ["windows"], "related_tools": []},
                {"content": "Beta drivers: NVIDIA Beta (early features), AMD Optional (frequent updates), stability risk, test new GPUs early adoption", "keywords": ["beta", "optional"], "difficulty": "advanced", "tags": ["testing"], "related_tools": []},
                {"content": "NVIDIA Hotfix: Critical bug fixes between releases, GeForce forums download, stability patches (game crashes), install over stable", "keywords": ["hotfix", "nvidia"], "difficulty": "intermediate", "tags": ["nvidia"], "related_tools": []},
                {"content": "PhysX driver: NVIDIA physics engine, bundled GPU drivers, rarely needed (few games use), safe skip minimal installation", "keywords": ["physx", "nvidia"], "difficulty": "beginner", "tags": ["features"], "related_tools": []},
                {"content": "HD Audio driver: NVIDIA/AMD HDMI audio, required audio over HDMI/DP monitors, include installation (check audio devices)", "keywords": ["hd audio", "hdmi"], "difficulty": "beginner", "tags": ["audio"], "related_tools": []},
                {"content": "Multiple GPUs: Install drivers one at a time (iGPU then dGPU), conflicts driver mismatch, DDU between switches", "keywords": ["multi gpu", "igpu"], "difficulty": "advanced", "tags": ["multi"], "related_tools": []},
                {"content": "NVCleanstall: Custom NVIDIA installer (strips telemetry, GFE, bloat), lightweight 500MB vs 1GB, advanced users, GitHub tool", "keywords": ["nvcleanstall", "debloat"], "difficulty": "advanced", "tags": ["tools"], "related_tools": ["NVCleanstall"]},
                {"content": "AMD Radeon Software minimal: Install drivers only (uncheck Radeon Software), manual control panel alternative, 200MB vs 800MB", "keywords": ["minimal install", "amd"], "difficulty": "intermediate", "tags": ["amd"], "related_tools": []},
                {"content": "Driver download: Official sites only (nvidia.com, amd.com), avoid third-party (malware risk), manual input GPU model", "keywords": ["download", "official"], "difficulty": "beginner", "tags": ["safety"], "related_tools": []},
                {"content": "Installation order: Uninstall old driver (DDU Safe Mode) > Restart > Install new driver > Restart, clean install prevents conflicts", "keywords": ["installation order", "process"], "difficulty": "intermediate", "tags": ["best practices"], "related_tools": []},
                {"content": "Driver size: NVIDIA 700MB-1GB (DCH drivers), AMD 600-800MB (full Adrenalin), older drivers smaller (legacy features)", "keywords": ["driver size", "download"], "difficulty": "beginner", "tags": ["technical"], "related_tools": []},
                {"content": "DCH vs Standard: DCH (Declarative Componentized Hardware) Windows 10+, Standard legacy Win7/8, modern systems use DCH", "keywords": ["dch", "standard"], "difficulty": "intermediate", "tags": ["windows"], "related_tools": []},
                {"content": "Control panel: NVIDIA Control Panel (right-click desktop), AMD Radeon Settings (system tray), per-game profiles, global settings", "keywords": ["control panel", "settings"], "difficulty": "beginner", "tags": ["configuration"], "related_tools": []},
                {"content": "Driver signatures: Windows enforces signed drivers (WHQL certified), unsigned drivers require Test Mode (bcdedit), security risk", "keywords": ["signatures", "whql"], "difficulty": "advanced", "tags": ["security"], "related_tools": []},
                {"content": "GPU-Z verification: Check driver version installed (GPU-Z tool free), detect fake drivers, monitor driver loaded correctly", "keywords": ["gpu-z", "verification"], "difficulty": "beginner", "tags": ["tools"], "related_tools": ["GPU-Z"]},
                {"content": "Game-specific drivers: NVIDIA Game Ready for major releases (Cyberpunk, Starfield), +5-10% FPS new games, older games stable drivers", "keywords": ["game ready", "optimization"], "difficulty": "intermediate", "tags": ["gaming"], "related_tools": []},
                {"content": "Shader cache: NVIDIA stores compiled shaders (reduce stutter), located C:\\ProgramData\\NVIDIA Corporation, 5-10GB size, safe delete (rebuilds)", "keywords": ["shader cache", "nvidia"], "difficulty": "intermediate", "tags": ["cache"], "related_tools": []},
                {"content": "AMD driver timeout: TdrDelay registry fix (increase GPU recovery time 8 sec), prevents driver crashes compute workloads, HKLM tweaks", "keywords": ["tdr", "timeout"], "difficulty": "expert", "tags": ["amd"], "related_tools": []},
                {"content": "Vulkan drivers: Bundled GPU drivers (API support), update GPU drivers updates Vulkan, DOOM Eternal/RDR2 requirement", "keywords": ["vulkan", "api"], "difficulty": "intermediate", "tags": ["gaming"], "related_tools": []},
                {"content": "OpenCL drivers: GPU compute (DaVinci Resolve, Blender), included driver package, rarely separate install, check GPU-Z support", "keywords": ["opencl", "compute"], "difficulty": "advanced", "tags": ["professional"], "related_tools": []},
                {"content": "Driver bloat removal: Uninstall NVIDIA Telemetry (services.msc), GeForce Experience (optional), 3D Vision (obsolete), HD Audio Driver (if no HDMI audio)", "keywords": ["bloat", "removal"], "difficulty": "advanced", "tags": ["optimization"], "related_tools": []},
                {"content": "Legacy GPU support: NVIDIA 900 series+ latest drivers, older GPUs (700 series-) legacy 470.xx branch, AMD GCN 1.0+ supported", "keywords": ["legacy", "support"], "difficulty": "intermediate", "tags": ["compatibility"], "related_tools": []},
                {"content": "Mobile GPU drivers: Laptop GPU drivers from OEM (Dell, HP, Lenovo), NVIDIA/AMD generic drivers often incompatible (Optimus issues)", "keywords": ["laptop", "mobile"], "difficulty": "intermediate", "tags": ["laptop"], "related_tools": []},
                {"content": "Optimus drivers: NVIDIA laptop requires Optimus driver (hybrid graphics), manual driver download from OEM, generic NVIDIA drivers break Optimus", "keywords": ["optimus", "hybrid"], "difficulty": "advanced", "tags": ["laptop"], "related_tools": []},
                {"content": "AMD hybrid graphics: Switchable Graphics (APU + dGPU), install latest Adrenalin (supports both), manual switch per app (power saving)", "keywords": ["hybrid", "amd"], "difficulty": "intermediate", "tags": ["laptop"], "related_tools": []},
                {"content": "Driver crashes: DDU clean install first fix, check PSU cables (power delivery), stress test GPU (FurMark), RMA if hardware failure", "keywords": ["crashes", "troubleshooting"], "difficulty": "intermediate", "tags": ["troubleshooting"], "related_tools": ["FurMark"]},
                {"content": "Black screen: Safe Mode boot (DDU clean install), check monitor cable (DP/HDMI), reseat GPU, BIOS integrated graphics enable (test)", "keywords": ["black screen", "troubleshooting"], "difficulty": "intermediate", "tags": ["troubleshooting"], "related_tools": []},
                {"content": "Code 43: Device Manager error, DDU clean reinstall, check GPU power cables (8-pin), hardware failure sign (RMA), BIOS update sometimes fixes", "keywords": ["code 43", "error"], "difficulty": "advanced", "tags": ["troubleshooting"], "related_tools": []},
                {"content": "Recommended update frequency: Stable system monthly check, new GPU/game day-1 drivers, older GPU 3-6 months (if stable skip)", "keywords": ["update frequency", "maintenance"], "difficulty": "beginner", "tags": ["best practices"], "related_tools": []},
                {"content": "Backup drivers: Double Driver (backup tool), export before DDU clean, restore if new driver fails, safe fallback option", "keywords": ["backup", "restore"], "difficulty": "intermediate", "tags": ["safety"], "related_tools": ["Double Driver"]},
                {"content": "Multi-monitor drivers: Update drivers fixes multi-monitor bugs, different refresh rates supported (modern drivers), G-Sync + FreeSync dual monitor", "keywords": ["multi-monitor", "support"], "difficulty": "intermediate", "tags": ["multi-monitor"], "related_tools": []}
            ]
        }

        # 23. Chipset Drivers Importance
        kb["chipset_drivers_importance"] = {
            "metadata": {
                "priority": 4,
                "tags": ["drivers", "chipset", "motherboard", "amd", "intel"],
                "difficulty": "intermediate",
                "description": "Chipset, USB, and motherboard driver importance"
            },
            "tips": [
                {"content": "AMD chipset: Critical Ryzen systems (FCLK management, power plans), download AMD.com, includes Ryzen Power Plans (Balanced best)", "keywords": ["amd chipset", "ryzen"], "difficulty": "intermediate", "tags": ["amd"], "related_tools": []},
                {"content": "Intel chipset: INF drivers (device recognition), Intel.com download, includes Management Engine (ME), less critical vs AMD chipset", "keywords": ["intel chipset", "inf"], "difficulty": "intermediate", "tags": ["intel"], "related_tools": []},
                {"content": "Intel ME: Management Engine firmware (enterprise remote management), security patches critical, bundled chipset drivers", "keywords": ["intel me", "security"], "difficulty": "advanced", "tags": ["intel"], "related_tools": []},
                {"content": "USB 3.0/3.2 drivers: Critical USB stability (disconnect issues), motherboard manufacturer site, Intel/AMD generic fallback", "keywords": ["usb drivers", "stability"], "difficulty": "intermediate", "tags": ["usb"], "related_tools": []},
                {"content": "Audio drivers: Realtek (most motherboards), download manufacturer site (ASUS, MSI), Windows generic works (limited features)", "keywords": ["audio drivers", "realtek"], "difficulty": "beginner", "tags": ["audio"], "related_tools": []},
                {"content": "LAN drivers: Intel I225-V (Ethernet), Realtek RTL8125, manufacturer site download, Windows Update outdated (packet loss)", "keywords": ["lan drivers", "ethernet"], "difficulty": "intermediate", "tags": ["network"], "related_tools": []},
                {"content": "WiFi drivers: Intel AX200/AX210, download Intel.com, motherboard bundled WiFi (check model), Windows Update often outdated", "keywords": ["wifi drivers", "wireless"], "difficulty": "intermediate", "tags": ["network"], "related_tools": []},
                {"content": "Bluetooth drivers: Bundled WiFi chipset (Intel AX200 = WiFi + BT), separate install if discrete module, pairs device manager", "keywords": ["bluetooth drivers", "wireless"], "difficulty": "beginner", "tags": ["connectivity"], "related_tools": []},
                {"content": "SATA/RAID drivers: Intel RST (Rapid Storage Technology) RAID arrays, AHCI no drivers needed, NVMe uses inbox Windows drivers", "keywords": ["sata", "raid"], "difficulty": "advanced", "tags": ["storage"], "related_tools": []},
                {"content": "RGB software: ASUS Aura Sync, MSI Mystic Light, Gigabyte RGB Fusion, 500MB bloatware each, skip if no RGB", "keywords": ["rgb software", "bloat"], "difficulty": "beginner", "tags": ["aesthetics"], "related_tools": []},
                {"content": "BIOS updates: Motherboard manufacturer (ASUS, MSI), USB BIOS Flashback (no CPU), critical new CPU support (AM5/LGA1700)", "keywords": ["bios updates", "firmware"], "difficulty": "advanced", "tags": ["bios"], "related_tools": []},
                {"content": "Driver order: Windows install > Chipset > GPU > Audio > LAN > Others, chipset first (device recognition base)", "keywords": ["driver order", "installation"], "difficulty": "intermediate", "tags": ["best practices"], "related_tools": []},
                {"content": "Ryzen Power Plans: Ryzen Balanced (best gaming), Windows Balanced (generic), High Performance (wastes power), chipset install includes", "keywords": ["power plans", "ryzen"], "difficulty": "intermediate", "tags": ["amd"], "related_tools": []},
                {"content": "Intel Rapid Storage: RAID/Optane support, unnecessary AHCI users (bloatware), install only RAID arrays configured BIOS", "keywords": ["intel rst", "raid"], "difficulty": "intermediate", "tags": ["intel"], "related_tools": []},
                {"content": "AMD RAID drivers: RAIDXpert2 utility, B550/X570 chipset RAID, NVMe RAID support, enthusiast feature (most skip)", "keywords": ["amd raid", "raidxpert"], "difficulty": "advanced", "tags": ["amd"], "related_tools": []},
                {"content": "USB issues: Outdated chipset/USB drivers (disconnect errors), update motherboard manufacturer, disable USB selective suspend (Power Options)", "keywords": ["usb issues", "troubleshooting"], "difficulty": "intermediate", "tags": ["troubleshooting"], "related_tools": []},
                {"content": "Audio crackling: Update Realtek drivers, disable audio enhancements (Properties > Enhancements > Disable all), DPC latency (LatencyMon)", "keywords": ["audio crackling", "fix"], "difficulty": "intermediate", "tags": ["troubleshooting"], "related_tools": ["LatencyMon"]},
                {"content": "LAN packet loss: Update LAN drivers manufacturer site, disable Large Send Offload (adapter properties), jumbo frames off home networks", "keywords": ["packet loss", "ethernet"], "difficulty": "advanced", "tags": ["network"], "related_tools": []},
                {"content": "WiFi drops: Intel WiFi drivers (latest), disable WiFi power saving (Device Manager > Power Management), router 5GHz preferred", "keywords": ["wifi drops", "troubleshooting"], "difficulty": "intermediate", "tags": ["wifi"], "related_tools": []},
                {"content": "Driver conflicts: Device Manager yellow exclamations, uninstall conflicting drivers, chipset clean install resolves base drivers", "keywords": ["conflicts", "device manager"], "difficulty": "intermediate", "tags": ["troubleshooting"], "related_tools": []},
                {"content": "Motherboard software: AI Suite (ASUS), Dragon Center (MSI), @BIOS (Gigabyte), 500MB-1GB bloat, skip (BIOS tweaks better)", "keywords": ["motherboard software", "bloat"], "difficulty": "beginner", "tags": ["bloatware"], "related_tools": []},
                {"content": "TPM drivers: fTPM firmware (AMD/Intel), discrete TPM (2.0 header), Windows 11 requirement, included chipset drivers", "keywords": ["tpm drivers", "security"], "difficulty": "intermediate", "tags": ["security"], "related_tools": []},
                {"content": "Thunderbolt drivers: Intel Thunderbolt 3/4 (40 Gbps), motherboard manufacturer download, USB4 support included", "keywords": ["thunderbolt", "usb4"], "difficulty": "advanced", "tags": ["connectivity"], "related_tools": []},
                {"content": "RGB RAM software: G.Skill Trident Z Lighting, Corsair iCUE (RAM control), bloatware 300MB, static BIOS control better", "keywords": ["rgb ram", "software"], "difficulty": "beginner", "tags": ["aesthetics"], "related_tools": []},
                {"content": "Fan control software: FanControl (open-source best), SpeedFan (legacy), motherboard BIOS curves better (zero software overhead)", "keywords": ["fan control", "software"], "difficulty": "intermediate", "tags": ["cooling"], "related_tools": ["FanControl"]},
                {"content": "Monitoring software: HWiNFO64 (best monitoring), MSI Afterburner (OSD gaming), avoid AI Suite/Dragon Center (bloat + conflicts)", "keywords": ["monitoring", "hwinfo"], "difficulty": "beginner", "tags": ["tools"], "related_tools": ["HWiNFO64"]},
                {"content": "Chipset update frequency: AMD quarterly (Ryzen updates), Intel 6-12 months (stable), update when CPU/RAM issues", "keywords": ["update frequency", "chipset"], "difficulty": "intermediate", "tags": ["maintenance"], "related_tools": []},
                {"content": "Windows inbox drivers: Basic functionality (generic drivers), performance/features limited, manual manufacturer drivers recommended", "keywords": ["inbox drivers", "windows"], "difficulty": "beginner", "tags": ["windows"], "related_tools": []},
                {"content": "Driver backup: DriverBackup! tool (export installed drivers), reinstall Windows quick restore, safe fallback old drivers", "keywords": ["backup", "restore"], "difficulty": "intermediate", "tags": ["tools"], "related_tools": ["DriverBackup"]},
                {"content": "Virtual devices: Razer Surround (7.1 audio virtual), VB-Audio VoiceMeeter (audio routing), separate software not drivers", "keywords": ["virtual devices", "audio"], "difficulty": "advanced", "tags": ["audio"], "related_tools": []},
                {"content": "Legacy drivers: Windows 7 drivers often work Windows 10/11 (compatibility mode), unsigned drivers risk (malware vector), avoid unless critical", "keywords": ["legacy", "compatibility"], "difficulty": "advanced", "tags": ["compatibility"], "related_tools": []},
                {"content": "DriverBooster warning: Avoid IObit Driver Booster (bloatware, malware bundled), manual download official sites safer", "keywords": ["driver booster", "avoid"], "difficulty": "beginner", "tags": ["warning"], "related_tools": []},
                {"content": "Safe motherboard drivers: Chipset, LAN, Audio (critical), RGB/AI Suite (skip bloat), BIOS update (stable version not beta)", "keywords": ["essential drivers", "minimal"], "difficulty": "intermediate", "tags": ["recommendations"], "related_tools": []},
                {"content": "AMD AGESA updates: Motherboard BIOS includes AGESA (Ryzen microcode), RAM stability, FCLK improvements, check QVL (RAM compatibility list)", "keywords": ["agesa", "bios"], "difficulty": "advanced", "tags": ["amd"], "related_tools": []},
                {"content": "Intel microcode: CPU security patches (Spectre/Meltdown), BIOS updates include, Windows Update alternative (slower)", "keywords": ["microcode", "security"], "difficulty": "advanced", "tags": ["intel"], "related_tools": []},
                {"content": "Sensor drivers: HWiNFO/Aida64 detect sensors, motherboard drivers enable monitoring (temps, fan speeds, voltages), diagnostic tools", "keywords": ["sensors", "monitoring"], "difficulty": "intermediate", "tags": ["monitoring"], "related_tools": []},
                {"content": "Manufacturer support: ASUS best driver support (frequent updates), MSI/Gigabyte 6-12 months, ASRock sporadic, premium boards longer support", "keywords": ["support", "manufacturers"], "difficulty": "intermediate", "tags": ["brands"], "related_tools": []},
                {"content": "NVMe firmware: SSD manufacturer tools (Samsung Magician, Crucial Storage Executive), performance/stability updates, backup data first", "keywords": ["nvme firmware", "ssd"], "difficulty": "advanced", "tags": ["storage"], "related_tools": ["Samsung Magician"]},
                {"content": "USB BIOS settings: XHCI Hand-off (enable), Legacy USB (disable modern systems), fast boot (USB detection slower), troubleshoot boot issues", "keywords": ["usb bios", "settings"], "difficulty": "intermediate", "tags": ["bios"], "related_tools": []},
                {"content": "Audio ASIO drivers: Low-latency audio (music production), FL Studio/Ableton, Realtek ASIO separate download, FL ASIO alternative", "keywords": ["asio", "audio production"], "difficulty": "advanced", "tags": ["professional"], "related_tools": []}
            ]
        }

        # Continuons avec les dernières catégories (Gaming + Networking)...

        # On ajoute plus tard les autres catégories dans un autre fichier si nécessaire
        # Pour l'instant, testons ces 2 nouvelles catégories

"""

def main():
    file_path = r"C:\\Users\\Utilisateur\\Downloads\\Nitrite-V18.5\\src\\v14_mvp\\ai_knowledge_unified.py"

    print("=" * 80)
    print("AJOUT CATEGORIES: GPU Driver Management + Chipset Drivers")
    print("=" * 80)

    # Lire le fichier
    with open(file_path, 'r', encoding='utf-8') as f:
        lines = f.readlines()

    # Compter état initial
    initial_cats = sum(1 for line in lines if 'kb[\"' in line and '"] = {' in line)
    initial_tips = sum(1 for line in lines if '{"content":' in line)

    print(f"\\n[INITIAL] Categories: {initial_cats} | Conseils: {initial_tips}")

    # Trouver la ligne avec "return kb"
    return_line_index = -1
    for i, line in enumerate(lines):
        if line.strip() == "return kb":
            return_line_index = i
            break

    if return_line_index == -1:
        print("[ERROR] Ligne 'return kb' non trouvee!")
        return

    print(f"[OK] Ligne 'return kb' trouvee a l'index {return_line_index}")

    # Insérer les nouvelles catégories AVANT return kb
    new_lines = lines[:return_line_index] + [NEW_CATEGORIES] + lines[return_line_index:]

    # Sauvegarder
    with open(file_path, 'w', encoding='utf-8') as f:
        f.writelines(new_lines)

    print("[SAVE] Fichier sauvegarde!")

    # Recompter
    with open(file_path, 'r', encoding='utf-8') as f:
        final_content = f.read()

    final_cats = final_content.count('kb[\"')
    final_tips = final_content.count('{"content":')

    print(f"\\n[FINAL] Categories: {final_cats} (+{final_cats - initial_cats}) | Conseils: {final_tips} (+{final_tips - initial_tips})")
    print("\\n" + "=" * 80)
    print("[SUCCESS] Operation terminee!")
    print("=" * 80)

if __name__ == "__main__":
    main()
