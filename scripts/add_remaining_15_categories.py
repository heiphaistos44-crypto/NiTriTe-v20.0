#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Script pour ajouter les 15 catégories RESTANTES à ai_knowledge_unified.py
Catégories: Windows 11 (4), Drivers (3), Gaming (5), Networking (3)
"""

import os
import re

def create_remaining_categories_code():
    """Génère le code Python pour les 15 catégories restantes"""

    categories_code = '''
        # =============================================================================
        # WINDOWS 11 OPTIMIZATION (4 catégories - ~160 conseils)
        # =============================================================================

        # 18. Windows 11 Optimization
        kb["windows_11_optimization"] = {
            "metadata": {
                "priority": 5,
                "tags": ["windows", "optimization", "performance", "os"],
                "difficulty": "intermediate",
                "description": "Windows 11 optimization tweaks and debloating"
            },
            "tips": [
                {"content": "Disable telemetry: O&O ShutUp10++ free tool, blocks Microsoft telemetry, privacy protection, no performance impact, safe tweaks", "keywords": ["telemetry", "privacy", "shutup10"], "difficulty": "beginner", "tags": ["privacy"], "related_tools": ["O&O ShutUp10++"]},
                {"content": "Game Mode ON: Settings > Gaming > Game Mode, prioritizes CPU/GPU to games, +5-10 FPS some titles, disable fullscreen optimizations", "keywords": ["game mode", "gaming"], "difficulty": "beginner", "tags": ["gaming"], "related_tools": []},
                {"content": "HAGS ON: Hardware Accelerated GPU Scheduling, Settings > Graphics, reduces latency 1-2ms, RTX 20/30/40 series, AMD RX 5000+", "keywords": ["hags", "gpu scheduling"], "difficulty": "intermediate", "tags": ["latency"], "related_tools": []},
                {"content": "Debloat script: Chris Titus Windows Utility (GitHub), removes bloatware (Cortana, OneDrive, Xbox), PowerShell one-liner, reversible", "keywords": ["debloat", "bloatware"], "difficulty": "advanced", "tags": ["cleanup"], "related_tools": ["Chris Titus Utility"]},
                {"content": "Disable animations: Settings > Accessibility > Visual effects, disables window animations, snappier UI, +100MB RAM savings", "keywords": ["animations", "performance"], "difficulty": "beginner", "tags": ["ui"], "related_tools": []},
                {"content": "Power plan: High Performance plan (Control Panel > Power), CPU never downclocks, +5W idle power, gaming desktops recommended", "keywords": ["power plan", "performance"], "difficulty": "beginner", "tags": ["power"], "related_tools": []},
                {"content": "Ultimate Performance: powercfg -duplicatescheme e9a42b02-d5df-448d-aa00-03f14749eb61, hidden plan, disables power saving, +10W idle", "keywords": ["ultimate performance", "powercfg"], "difficulty": "intermediate", "tags": ["power"], "related_tools": []},
                {"content": "Disable fast startup: Control Panel > Power Options > Choose what power buttons do, prevents hybrid shutdown (corrupts files), full shutdown", "keywords": ["fast startup", "shutdown"], "difficulty": "beginner", "tags": ["boot"], "related_tools": []},
                {"content": "SysMain (Superfetch): Disable on SSD (services.msc), wastes RAM 500MB-2GB, HDD benefits (preload apps), SSD random access instant", "keywords": ["superfetch", "sysmain"], "difficulty": "intermediate", "tags": ["services"], "related_tools": []},
                {"content": "Windows Search: Disable indexing C: drive (reduce SSD writes), search slower, alternative Everything (instant search 1MB RAM)", "keywords": ["windows search", "indexing"], "difficulty": "intermediate", "tags": ["services"], "related_tools": ["Everything"]},
                {"content": "Delivery Optimization: Settings > Windows Update > Advanced > Delivery Optimization OFF, stops P2P update sharing (bandwidth hog)", "keywords": ["delivery optimization", "updates"], "difficulty": "beginner", "tags": ["network"], "related_tools": []},
                {"content": "Visual effects: Performance Options (sysdm.cpl > Advanced > Performance Settings), Adjust for best performance, keeps important effects", "keywords": ["visual effects", "performance"], "difficulty": "beginner", "tags": ["ui"], "related_tools": []},
                {"content": "Disable widgets: Right-click taskbar > Taskbar settings > Widgets OFF, reclaims RAM 200MB, useless bloat, Edge WebView dependency", "keywords": ["widgets", "taskbar"], "difficulty": "beginner", "tags": ["bloatware"], "related_tools": []},
                {"content": "Disable chat/Teams: Taskbar settings > Chat OFF, reclaims 150MB RAM, uninstall Teams (winget uninstall Teams), bloatware removal", "keywords": ["teams", "chat"], "difficulty": "beginner", "tags": ["bloatware"], "related_tools": []},
                {"content": "Storage Sense: Settings > Storage > Storage Sense ON, auto-delete temp files 30 days, reclaim SSD space, safe automation", "keywords": ["storage sense", "cleanup"], "difficulty": "beginner", "tags": ["storage"], "related_tools": []},
                {"content": "Disk Cleanup: cleanmgr.exe, delete old Windows updates (10-20GB), temp files, recycle bin, safe space recovery", "keywords": ["disk cleanup", "storage"], "difficulty": "beginner", "tags": ["storage"], "related_tools": []},
                {"content": "Temp folder cleanup: %temp% (delete all), C:\\Windows\\Temp (admin delete), safe 5-10GB space recovery, monthly maintenance", "keywords": ["temp files", "cleanup"], "difficulty": "beginner", "tags": ["maintenance"], "related_tools": []},
                {"content": "Disable startup apps: Task Manager > Startup tab, disable unnecessary apps (Discord, Spotify auto-start), faster boot 10-30 sec", "keywords": ["startup apps", "boot"], "difficulty": "beginner", "tags": ["boot"], "related_tools": []},
                {"content": "Uninstall bloatware: Settings > Apps > Installed apps, remove Candy Crush, Facebook, Disney+, Xbox (if not gaming), 2-5GB space", "keywords": ["bloatware", "uninstall"], "difficulty": "beginner", "tags": ["cleanup"], "related_tools": []},
                {"content": "Winget package manager: winget list (show installed), winget uninstall <app>, command-line app management, PowerShell built-in", "keywords": ["winget", "package manager"], "difficulty": "intermediate", "tags": ["tools"], "related_tools": []},
                {"content": "Windows Update: Settings > Windows Update > Pause updates 5 weeks, avoid forced reboots, manual updates control", "keywords": ["windows update", "control"], "difficulty": "beginner", "tags": ["updates"], "related_tools": []},
                {"content": "Group Policy: gpedit.msc (Pro/Enterprise only), disable telemetry, update control, advanced tweaks, Home edition lacks feature", "keywords": ["group policy", "gpedit"], "difficulty": "advanced", "tags": ["enterprise"], "related_tools": []},
                {"content": "Privacy settings: Settings > Privacy, disable all app permissions (Camera, Mic, Location), blocks UWP app tracking", "keywords": ["privacy", "permissions"], "difficulty": "beginner", "tags": ["privacy"], "related_tools": []},
                {"content": "Background apps: Settings > Apps > Installed apps > Advanced options > Background app permissions, disable unnecessary background apps", "keywords": ["background apps", "battery"], "difficulty": "beginner", "tags": ["performance"], "related_tools": []},
                {"content": "OneDrive disable: Unlink OneDrive (system tray icon > Settings > Unlink), disable startup, uninstall (winget uninstall OneDrive)", "keywords": ["onedrive", "cloud"], "difficulty": "beginner", "tags": ["bloatware"], "related_tools": []},
                {"content": "Windows Defender: Sufficient antivirus 2024, real-time protection, zero cost, alternative Malwarebytes free (manual scan)", "keywords": ["windows defender", "antivirus"], "difficulty": "beginner", "tags": ["security"], "related_tools": ["Windows Defender"]},
                {"content": "Third-party antivirus: Avoid Norton/McAfee (bloatware performance hogs), Defender + common sense sufficient, malware scan monthly", "keywords": ["antivirus", "bloatware"], "difficulty": "beginner", "tags": ["security"], "related_tools": []},
                {"content": "Debloat tools: Chris Titus (GitHub), WinUtil GUI, Win10Debloat PowerShell, reversible scripts, create restore point first", "keywords": ["debloat tools", "automation"], "difficulty": "advanced", "tags": ["tools"], "related_tools": ["WinUtil"]},
                {"content": "TPM 2.0 requirement: Windows 11 enforces TPM 2.0, bypass (regedit LabConfig keys), unsupported hardware risks security updates", "keywords": ["tpm", "requirements"], "difficulty": "advanced", "tags": ["compatibility"], "related_tools": []},
                {"content": "Secure Boot: UEFI requirement Windows 11, disable Secure Boot (older hardware compatibility), reduces attack surface when enabled", "keywords": ["secure boot", "uefi"], "difficulty": "intermediate", "tags": ["security"], "related_tools": []},
                {"content": "Virtual memory (pagefile): 16GB RAM = disable pagefile (no benefit), 8GB RAM = 8GB pagefile (SSD), static size reduces fragmentation", "keywords": ["pagefile", "virtual memory"], "difficulty": "intermediate", "tags": ["memory"], "related_tools": []},
                {"content": "RAM usage: Task Manager > Performance > Memory, 50-70% usage normal (SuperFetch cache), >85% needs RAM upgrade or cleanup", "keywords": ["ram usage", "monitoring"], "difficulty": "beginner", "tags": ["memory"], "related_tools": []},
                {"content": "Disable Cortana: Group Policy or registry (HKLM\\SOFTWARE\\Policies\\Microsoft\\Windows\\Windows Search), reclaims 100MB RAM, useless feature", "keywords": ["cortana", "disable"], "difficulty": "intermediate", "tags": ["bloatware"], "related_tools": []},
                {"content": "Windows Sandbox: Virtualization feature (Windows 11 Pro), test suspicious apps safely, requires Virtualization enabled BIOS", "keywords": ["sandbox", "virtualization"], "difficulty": "advanced", "tags": ["security"], "related_tools": []},
                {"content": "WSL2: Windows Subsystem for Linux, native Linux kernel, development environment, wsl --install Ubuntu, Hyper-V dependency", "keywords": ["wsl2", "linux"], "difficulty": "advanced", "tags": ["development"], "related_tools": ["WSL"]},
                {"content": "Registry backup: Create restore point (rstrui.exe) before registry edits, backup registry (regedit > File > Export), safety net", "keywords": ["registry", "backup"], "difficulty": "intermediate", "tags": ["safety"], "related_tools": []},
                {"content": "Dark mode: Settings > Personalization > Colors > Dark, reduces eye strain, OLED battery savings laptops, system-wide support", "keywords": ["dark mode", "theme"], "difficulty": "beginner", "tags": ["aesthetics"], "related_tools": []},
                {"content": "Taskbar customization: Right-click taskbar > Taskbar settings, small icons, combine never (show labels), center vs left alignment", "keywords": ["taskbar", "customization"], "difficulty": "beginner", "tags": ["ui"], "related_tools": []},
                {"content": "Windows 11 22H2: Latest major update 2023, File Explorer tabs, Task Manager efficiency mode, Snap layouts improvements", "keywords": ["22h2", "updates"], "difficulty": "beginner", "tags": ["features"], "related_tools": []},
                {"content": "Auto HDR: Settings > Display > HDR > Auto HDR, applies HDR to SDR games, +20% image quality, requires HDR monitor", "keywords": ["auto hdr", "gaming"], "difficulty": "intermediate", "tags": ["hdr"], "related_tools": []}
            ]
        }

        # 19. Windows Registry Performance
        kb["windows_registry_performance"] = {
            "metadata": {
                "priority": 4,
                "tags": ["windows", "registry", "tweak", "advanced"],
                "difficulty": "advanced",
                "description": "Windows registry tweaks for gaming performance"
            },
            "tips": [
                {"content": "Win32PrioritySeparation: HKLM\\SYSTEM\\CurrentControlSet\\Control\\PriorityControl, value 0x26 (hex 38), prioritizes foreground apps (gaming)", "keywords": ["win32priorityseparation", "cpu priority"], "difficulty": "advanced", "tags": ["gaming"], "related_tools": []},
                {"content": "GPU scheduling: HKLM\\SYSTEM\\CurrentControlSet\\Control\\GraphicsDrivers, HwSchMode DWORD 2 (HAGS ON), reduces latency RTX/RDNA", "keywords": ["gpu scheduling", "hags"], "difficulty": "advanced", "tags": ["latency"], "related_tools": []},
                {"content": "Network throttling disable: HKLM\\SOFTWARE\\Microsoft\\Windows NT\\CurrentVersion\\Multimedia\\SystemProfile, NetworkThrottlingIndex DWORD ffffffff", "keywords": ["network throttling", "latency"], "difficulty": "advanced", "tags": ["network"], "related_tools": []},
                {"content": "System responsiveness: ...\\SystemProfile, SystemResponsiveness DWORD 0 (gaming) or 20 (balanced), affects background tasks priority", "keywords": ["system responsiveness", "priority"], "difficulty": "advanced", "tags": ["performance"], "related_tools": []},
                {"content": "Game priority: ...\\SystemProfile\\Tasks\\Games, Priority DWORD 8 (high), GPU Priority DWORD 8, improves gaming performance 5-10%", "keywords": ["game priority", "registry"], "difficulty": "expert", "tags": ["gaming"], "related_tools": []},
                {"content": "Disable HPET: bcdedit /deletevalue useplatformclock (command prompt admin), High Precision Event Timer, +1-2 FPS some systems, test stability", "keywords": ["hpet", "timer"], "difficulty": "expert", "tags": ["latency"], "related_tools": []},
                {"content": "TSC syncpolicy: bcdedit /set tscsyncpolicy enhanced, Timestamp Counter synchronization, multi-core latency reduction, Ryzen benefit", "keywords": ["tsc", "syncpolicy"], "difficulty": "expert", "tags": ["latency"], "related_tools": []},
                {"content": "Disable Nagle algorithm: HKLM\\SYSTEM\\CurrentControlSet\\Services\\Tcpip\\Parameters\\Interfaces, TcpAckFrequency DWORD 1, reduces network latency gaming", "keywords": ["nagle", "tcp"], "difficulty": "expert", "tags": ["network"], "related_tools": []},
                {"content": "TCPNoDelay: Same registry path, TCPNoDelay DWORD 1, disables packet batching, lower latency competitive gaming (CS2, VALORANT)", "keywords": ["tcpnodelay", "latency"], "difficulty": "expert", "tags": ["network"], "related_tools": []},
                {"content": "IRQ priority: MSI mode (Message Signaled Interrupts), GPU/NIC use MSI (device manager > properties > details > interrupt policy)", "keywords": ["irq", "msi mode"], "difficulty": "expert", "tags": ["advanced"], "related_tools": []},
                {"content": "Core parking disable: HKLM\\SYSTEM\\CurrentControlSet\\Control\\Power\\PowerSettings, disable CPU core parking (all cores active), Ryzen 3D V-Cache avoid", "keywords": ["core parking", "cpu"], "difficulty": "expert", "tags": ["performance"], "related_tools": []},
                {"content": "C-states: Enable C-states BIOS (modern CPUs efficient), disabling wastes power +50W idle, negligible performance gains (<1%)", "keywords": ["c-states", "power"], "difficulty": "advanced", "tags": ["efficiency"], "related_tools": []},
                {"content": "MMCSS priority: ...\\SystemProfile\\Tasks\\Games, Scheduling Category DWORD High, MMCSS (Multimedia Class Scheduler) gaming priority", "keywords": ["mmcss", "scheduler"], "difficulty": "expert", "tags": ["gaming"], "related_tools": []},
                {"content": "Registry cleanup: CCleaner Registry (careful use), removes orphaned keys, minimal performance impact, backup first, placebo mostly", "keywords": ["registry cleanup", "ccleaner"], "difficulty": "intermediate", "tags": ["maintenance"], "related_tools": ["CCleaner"]},
                {"content": "Disable Windows Error Reporting: services.msc > Windows Error Reporting Service > Disabled, stops crash report uploads (privacy)", "keywords": ["error reporting", "privacy"], "difficulty": "beginner", "tags": ["privacy"], "related_tools": []},
                {"content": "SvcHost split: HKLM\\SYSTEM\\CurrentControlSet\\Control, SvcHostSplitThresholdInKB DWORD 380000 (384MB RAM), separates services (isolates crashes)", "keywords": ["svchost", "split"], "difficulty": "advanced", "tags": ["stability"], "related_tools": []},
                {"content": "LargeSystemCache: HKLM\\SYSTEM\\CurrentControlSet\\Control\\Session Manager\\Memory Management, LargeSystemCache DWORD 0 (desktop) or 1 (server)", "keywords": ["cache", "memory"], "difficulty": "expert", "tags": ["memory"], "related_tools": []},
                {"content": "NDU service: HKLM\\SYSTEM\\CurrentControlSet\\Services\\Ndu, Start DWORD 4 (disabled), Network Data Usage tracking, privacy + performance", "keywords": ["ndu", "network"], "difficulty": "intermediate", "tags": ["privacy"], "related_tools": []},
                {"content": "GameDVR disable: HKLM\\SOFTWARE\\Microsoft\\PolicyManager\\default\\ApplicationManagement\\AllowGameDVR, value DWORD 0, disables Xbox Game Bar recording", "keywords": ["gamedvr", "xbox"], "difficulty": "intermediate", "tags": ["gaming"], "related_tools": []},
                {"content": "Timer resolution: HKLM\\SYSTEM\\CurrentControlSet\\Control\\Session Manager\\kernel, GlobalTimerResolutionRequests DWORD 1, improves timer precision", "keywords": ["timer resolution", "precision"], "difficulty": "expert", "tags": ["latency"], "related_tools": []},
                {"content": "Dynamic tick: bcdedit /set disabledynamictick yes, disables variable tick scheduler, lower latency (placebo most systems), test stability", "keywords": ["dynamic tick", "scheduler"], "difficulty": "expert", "tags": ["latency"], "related_tools": []},
                {"content": "Menu show delay: HKCU\\Control Panel\\Desktop, MenuShowDelay 0 (instant menus), default 400ms, snappier UI responsiveness", "keywords": ["menu delay", "ui"], "difficulty": "beginner", "tags": ["ui"], "related_tools": []},
                {"content": "Thumbnail cache: HKCU\\Software\\Microsoft\\Windows\\CurrentVersion\\Explorer\\Advanced, DisableThumbnailCache DWORD 1, reduces SSD writes", "keywords": ["thumbnails", "cache"], "difficulty": "intermediate", "tags": ["storage"], "related_tools": []},
                {"content": "Last access timestamp: fsutil behavior set disablelastaccess 1, disables file access timestamp (reduces SSD writes), safe tweak", "keywords": ["last access", "ssd"], "difficulty": "intermediate", "tags": ["storage"], "related_tools": []},
                {"content": "Prefetch/Superfetch: SSD disable (HKLM\\...\\PrefetchParameters, EnablePrefetcher DWORD 0), HDD keep enabled (value 3)", "keywords": ["prefetch", "superfetch"], "difficulty": "intermediate", "tags": ["ssd"], "related_tools": []},
                {"content": "Boot timeout: bcdedit /timeout 3, reduces boot menu wait (default 30 sec), faster dual-boot systems, 3 sec sufficient", "keywords": ["boot timeout", "boot"], "difficulty": "beginner", "tags": ["boot"], "related_tools": []},
                {"content": "Registry permissions: Take ownership of registry keys (regedit > permissions), advanced tweaks require admin rights, risk corruption", "keywords": ["permissions", "admin"], "difficulty": "expert", "tags": ["advanced"], "related_tools": []},
                {"content": "Backup before tweaks: regedit > File > Export, save .reg file, double-click restore if issues, create restore point (rstrui.exe)", "keywords": ["backup", "safety"], "difficulty": "intermediate", "tags": ["safety"], "related_tools": []},
                {"content": "Registry editor: regedit.exe, navigate HKLM/HKCU hives, modify DWORD/String values, dangerous (corrupt OS if wrong edits)", "keywords": ["regedit", "editor"], "difficulty": "intermediate", "tags": ["tools"], "related_tools": []},
                {"content": "Placebo tweaks: Many registry tweaks are placebo (no measurable gains), benchmark before/after (3DMark, Cinebench), verify claims", "keywords": ["placebo", "myths"], "difficulty": "intermediate", "tags": ["testing"], "related_tools": []}
            ]
        }

        # 20. Windows Services Disable
        kb["windows_services_disable"] = {
            "metadata": {
                "priority": 3,
                "tags": ["windows", "services", "optimization", "advanced"],
                "difficulty": "intermediate",
                "description": "Safe Windows services to disable for performance"
            },
            "tips": [
                {"content": "Print Spooler: services.msc > Print Spooler > Disabled, safe disable if no printer, security vulnerability (PrintNightmare)", "keywords": ["print spooler", "disable"], "difficulty": "beginner", "tags": ["security"], "related_tools": []},
                {"content": "Fax service: Fax > Disabled, obsolete service, safe disable all systems, reclaims 20MB RAM", "keywords": ["fax", "obsolete"], "difficulty": "beginner", "tags": ["bloatware"], "related_tools": []},
                {"content": "Bluetooth Support Service: Safe disable desktop (no Bluetooth), keep enabled laptops (WiFi/Bluetooth combo chip)", "keywords": ["bluetooth", "wireless"], "difficulty": "beginner", "tags": ["connectivity"], "related_tools": []},
                {"content": "Xbox services: Xbox Live Auth Manager, Xbox Game Save, Xbox Accessory Management, disable if no Xbox/Game Pass, 50-100MB RAM", "keywords": ["xbox", "gaming"], "difficulty": "beginner", "tags": ["bloatware"], "related_tools": []},
                {"content": "Diagnostic Tracking: Connected User Experiences and Telemetry > Disabled, stops Microsoft telemetry uploads, privacy gain", "keywords": ["telemetry", "privacy"], "difficulty": "intermediate", "tags": ["privacy"], "related_tools": []},
                {"content": "Remote Registry: Remote Registry > Disabled, security risk (remote registry access), safe disable desktop users", "keywords": ["remote registry", "security"], "difficulty": "intermediate", "tags": ["security"], "related_tools": []},
                {"content": "Windows Search: Disable if using Everything (instant search alternative), indexing wastes SSD writes, search slower without", "keywords": ["windows search", "indexing"], "difficulty": "intermediate", "tags": ["performance"], "related_tools": []},
                {"content": "SysMain (Superfetch): Disable on SSD systems (no benefit), preloads apps to RAM, HDD systems benefit (keep enabled)", "keywords": ["sysmain", "superfetch"], "difficulty": "intermediate", "tags": ["ssd"], "related_tools": []},
                {"content": "Windows Update: Manual updates (Disabled + Manual start type), avoid forced reboots, security risk (update monthly manually)", "keywords": ["windows update", "manual"], "difficulty": "advanced", "tags": ["control"], "related_tools": []},
                {"content": "Delivery Optimization: Disable (services + Settings), stops P2P Windows Update sharing (uploads bandwidth), privacy concern", "keywords": ["delivery optimization", "p2p"], "difficulty": "beginner", "tags": ["network"], "related_tools": []},
                {"content": "Windows Time: Safe disable if no domain (time.windows.com sync), manual time sync, reclaims 5MB RAM", "keywords": ["windows time", "sync"], "difficulty": "beginner", "tags": ["minor"], "related_tools": []},
                {"content": "IP Helper: IPv6 transition technologies, safe disable if IPv6 disabled network adapter, Teredo/ISATAP tunneling", "keywords": ["ip helper", "ipv6"], "difficulty": "intermediate", "tags": ["network"], "related_tools": []},
                {"content": "Parental Controls: Safe disable no kids, reclaims 10MB RAM, Family Safety feature dependency", "keywords": ["parental controls", "family"], "difficulty": "beginner", "tags": ["bloatware"], "related_tools": []},
                {"content": "Offline Files: Disable (desktop systems), network file caching, enterprise feature, 20MB RAM reclaim", "keywords": ["offline files", "network"], "difficulty": "beginner", "tags": ["enterprise"], "related_tools": []},
                {"content": "Certificate Propagation: Safe disable home users, enterprise domain certificate sync, 5MB RAM", "keywords": ["certificates", "enterprise"], "difficulty": "intermediate", "tags": ["enterprise"], "related_tools": []},
                {"content": "Smart Card services: Safe disable no smart card reader, enterprise authentication, 15MB RAM combined", "keywords": ["smart card", "authentication"], "difficulty": "beginner", "tags": ["enterprise"], "related_tools": []},
                {"content": "Windows Biometric Service: Safe disable no fingerprint reader, Hello Face/Fingerprint dependency, 20MB RAM", "keywords": ["biometric", "hello"], "difficulty": "beginner", "tags": ["features"], "related_tools": []},
                {"content": "Sensor Monitoring Service: Disable desktop (no sensors), laptops keep (brightness/rotation sensors), 10MB RAM", "keywords": ["sensors", "monitoring"], "difficulty": "beginner", "tags": ["laptop"], "related_tools": []},
                {"content": "Geolocation Service: Privacy disable, blocks location tracking apps, Windows Maps dependency, safe disable most users", "keywords": ["geolocation", "privacy"], "difficulty": "beginner", "tags": ["privacy"], "related_tools": []},
                {"content": "Diagnostic Policy Service: Troubleshooting wizards dependency, safe disable (manual troubleshoot), 30MB RAM reclaim", "keywords": ["diagnostic policy", "troubleshooting"], "difficulty": "intermediate", "tags": ["bloatware"], "related_tools": []},
                {"content": "Program Compatibility Assistant: Safe disable enthusiasts (manual compatibility settings), auto-detects old programs", "keywords": ["compatibility", "assistant"], "difficulty": "intermediate", "tags": ["optional"], "related_tools": []},
                {"content": "HomeGroup services: Obsolete Windows 10 (removed Windows 11), safe disable all, network sharing legacy feature", "keywords": ["homegroup", "obsolete"], "difficulty": "beginner", "tags": ["obsolete"], "related_tools": []},
                {"content": "Hyper-V services: Disable if no virtualization (VMware/VirtualBox conflict), enable WSL2/Docker, 100MB+ RAM virtualization", "keywords": ["hyper-v", "virtualization"], "difficulty": "advanced", "tags": ["virtualization"], "related_tools": []},
                {"content": "Windows Defender: Keep enabled (free antivirus), disable if third-party AV (avoid running both = performance hit)", "keywords": ["windows defender", "antivirus"], "difficulty": "beginner", "tags": ["security"], "related_tools": []},
                {"content": "Background Intelligent Transfer: BITS, Windows Update downloads, safe Manual (starts when needed), Disabled breaks updates", "keywords": ["bits", "updates"], "difficulty": "intermediate", "tags": ["updates"], "related_tools": []},
                {"content": "Windows Error Reporting: Disable (privacy + performance), crash dumps upload Microsoft, 20MB RAM + network usage", "keywords": ["error reporting", "crashes"], "difficulty": "beginner", "tags": ["privacy"], "related_tools": []},
                {"content": "Windows Insider Service: Safe disable non-Insider users, beta testing program service, 5MB RAM", "keywords": ["insider", "beta"], "difficulty": "beginner", "tags": ["bloatware"], "related_tools": []},
                {"content": "retail demo service: RetailDemo > Disabled, store display mode (useless home users), 10MB RAM bloatware", "keywords": ["retail demo", "bloatware"], "difficulty": "beginner", "tags": ["bloatware"], "related_tools": []},
                {"content": "Shared PC Account Manager: Enterprise shared PC feature, safe disable personal PCs, 5MB RAM", "keywords": ["shared pc", "enterprise"], "difficulty": "beginner", "tags": ["enterprise"], "related_tools": []},
                {"content": "services.msc: Windows Services manager, Disabled (never starts) vs Manual (starts on demand) vs Automatic, restart required some services", "keywords": ["services.msc", "manager"], "difficulty": "beginner", "tags": ["tools"], "related_tools": []},
                {"content": "Black Viper services guide: Safe gaming/tweaking services list (blackviper.com legacy), verify Windows 11 compatibility, outdated some entries", "keywords": ["black viper", "guide"], "difficulty": "intermediate", "tags": ["reference"], "related_tools": []},
                {"content": "Backup before changes: Create restore point (rstrui.exe), note disabled services, boot safe mode if issues, reversible tweaks", "keywords": ["backup", "restore"], "difficulty": "intermediate", "tags": ["safety"], "related_tools": []},
                {"content": "Minimal services: Core services 45-50 (Windows 11), safe disable 20-30 bloatware services, 200-500MB RAM savings total", "keywords": ["minimal", "optimization"], "difficulty": "advanced", "tags": ["extreme"], "related_tools": []},
                {"content": "Automated tools: Win10Debloat, Chris Titus Utility (disable services bulk), reversible, create restore point, test stability", "keywords": ["automation", "tools"], "difficulty": "advanced", "tags": ["tools"], "related_tools": ["WinUtil"]},
                {"content": "Task Scheduler: taskschd.msc, disable telemetry tasks (Microsoft\\Windows\\Application Experience), privacy + background CPU reduction", "keywords": ["task scheduler", "tasks"], "difficulty": "intermediate", "tags": ["privacy"], "related_tools": []}
            ]
        }

        # 21. BIOS Settings Gaming
        kb["bios_settings_gaming"] = {
            "metadata": {
                "priority": 5,
                "tags": ["bios", "uefi", "overclock", "performance"],
                "difficulty": "advanced",
                "description": "BIOS/UEFI settings for gaming performance"
            },
            "tips": [
                {"content": "XMP/EXPO ON: Extreme Memory Profile (Intel XMP) / Extended Profiles for Overclocking (AMD EXPO), enables rated RAM speeds DDR4/DDR5", "keywords": ["xmp", "expo", "ram"], "difficulty": "intermediate", "tags": ["overclocking"], "related_tools": []},
                {"content": "Resizable BAR ON: Enables GPU access full VRAM, +5-15% FPS (RTX 30/40, RX 6000/7000), requires UEFI + Above 4G Decoding", "keywords": ["resizable bar", "rebar"], "difficulty": "intermediate", "tags": ["gpu"], "related_tools": []},
                {"content": "Above 4G Decoding ON: Prerequisite Resizable BAR, allows PCIe devices >4GB address space, mandatory RTX 30+ / RX 6000+", "keywords": ["above 4g", "pcie"], "difficulty": "intermediate", "tags": ["gpu"], "related_tools": []},
                {"content": "C-States enable: Modern CPUs efficient idle power saving (3-5W idle vs 30W disabled), <1% gaming performance loss, save electricity", "keywords": ["c-states", "power"], "difficulty": "intermediate", "tags": ["efficiency"], "related_tools": []},
                {"content": "Fan curves aggressive: CPU fan 40% idle → 100% 75C, GPU fan 0% idle → 100% 80C (custom curve), quieter idle + cooler load", "keywords": ["fan curves", "cooling"], "difficulty": "intermediate", "tags": ["cooling"], "related_tools": []},
                {"content": "Secure Boot: Enable (Windows 11 requirement), disable (older hardware/Linux dual-boot), security feature prevents rootkits", "keywords": ["secure boot", "security"], "difficulty": "intermediate", "tags": ["security"], "related_tools": []},
                {"content": "CSM disable: Compatibility Support Module (legacy BIOS), disable for UEFI-only boot (faster boot, required Resizable BAR)", "keywords": ["csm", "legacy"], "difficulty": "intermediate", "tags": ["boot"], "related_tools": []},
                {"content": "Fast Boot enable: Skips POST checks (faster 5-10 sec boot), disable if boot USB frequently, UEFI feature", "keywords": ["fast boot", "uefi"], "difficulty": "beginner", "tags": ["boot"], "related_tools": []},
                {"content": "Virtualization (VT-x/AMD-V): Enable for VMs (Hyper-V, VMware, WSL2), gaming no impact, Docker/Android emulator dependency", "keywords": ["virtualization", "vt-x"], "difficulty": "intermediate", "tags": ["virtualization"], "related_tools": []},
                {"content": "IOMMU/VT-d: Enable for VM PCIe passthrough (advanced), gaming disable (no benefit), enterprise/enthusiast feature", "keywords": ["iommu", "vt-d"], "difficulty": "expert", "tags": ["virtualization"], "related_tools": []},
                {"content": "PCIe Gen 4.0: Enable for NVMe Gen4 SSDs (7000 MB/s), GPU Gen4 (RTX 40/RX 7000), Gen3 fallback auto-negotiates older hardware", "keywords": ["pcie gen4", "nvme"], "difficulty": "intermediate", "tags": ["storage"], "related_tools": []},
                {"content": "CPU Overclocking: Manual OC vs Auto OC (PBO2/MCE), all-core 5.3 GHz (14900K), voltage 1.35V safe limit, stress test Prime95", "keywords": ["cpu oc", "overclocking"], "difficulty": "expert", "tags": ["overclocking"], "related_tools": ["Prime95"]},
                {"content": "PBO2 (AMD): Precision Boost Overdrive 2, auto OC Ryzen 7000, Curve Optimizer -15 to -30 (per-core undervolt), +200 MHz boost", "keywords": ["pbo2", "amd"], "difficulty": "advanced", "tags": ["overclocking"], "related_tools": []},
                {"content": "MCE (Intel): Multi-Core Enhancement, all-core Turbo (removes power limits), i9-14900K 5.5 GHz all-core (stock 5.3 GHz), heat +20C", "keywords": ["mce", "intel"], "difficulty": "advanced", "tags": ["overclocking"], "related_tools": []},
                {"content": "LLC (Load Line Calibration): Level 4-6/8 (ASUS), reduces Vdroop (voltage drop under load), too high (+8) overshoots (degrades CPU)", "keywords": ["llc", "voltage"], "difficulty": "expert", "tags": ["overclocking"], "related_tools": []},
                {"content": "RAM overclocking: XMP baseline, manual 1.4V DDR4 / 1.35V DDR5, tighten timings CL16-18-18-36, test MemTest86 8+ hours", "keywords": ["ram oc", "timings"], "difficulty": "expert", "tags": ["overclocking"], "related_tools": ["MemTest86"]},
                {"content": "FCLK (Infinity Fabric): AMD Ryzen FCLK = half RAM speed (DDR5-6000 = FCLK 3000 MHz), 1:1 ratio sweet spot, 2000 MHz safe", "keywords": ["fclk", "infinity fabric"], "difficulty": "expert", "tags": ["amd"], "related_tools": []},
                {"content": "VCCSA/VCCIO: Intel memory controller voltages, 1.25V VCCSA / 1.20V VCCIO stable DDR4-3600+, too high degrades IMC", "keywords": ["vccsa", "vccio"], "difficulty": "expert", "tags": ["intel"], "related_tools": []},
                {"content": "BCLK overclocking: Base clock OC (risky), 100 MHz default, 102-103 MHz safe (+2-3%), affects all components (PCIe/USB instability)", "keywords": ["bclk", "base clock"], "difficulty": "expert", "tags": ["advanced"], "related_tools": []},
                {"content": "Power limits (PL1/PL2): Intel TDP limits, PL1 125W sustained, PL2 253W turbo (28 sec), unlimited = PL1=PL2=4096W (heat +++)", "keywords": ["power limits", "tdp"], "difficulty": "advanced", "tags": ["intel"], "related_tools": []},
                {"content": "PPT/TDC/EDC (AMD): Package Power Tracking, Thermal Design Current, Electrical Design Current, increase limits (+50W PPT) PBO higher boost", "keywords": ["ppt", "tdc edc"], "difficulty": "expert", "tags": ["amd"], "related_tools": []},
                {"content": "Spread Spectrum: Disable for overclocking (EMI reduction feature reduces stability), enable stock (reduces electromagnetic interference)", "keywords": ["spread spectrum", "emi"], "difficulty": "advanced", "tags": ["overclocking"], "related_tools": []},
                {"content": "HPET (High Precision Event Timer): Auto or disabled (Windows uses TSC modern CPUs), enabled legacy compatibility, OS override BIOS", "keywords": ["hpet", "timer"], "difficulty": "advanced", "tags": ["latency"], "related_tools": []},
                {"content": "ErP/EuP mode: Energy-related Products, S5 power <1W (USB charging off when shutdown), disable for USB charging off", "keywords": ["erp", "power saving"], "difficulty": "beginner", "tags": ["power"], "related_tools": []},
                {"content": "RGB lighting: BIOS control RGB headers, disable RGB BIOS (software control only), startup logo disable (faster boot 2 sec)", "keywords": ["rgb", "aesthetics"], "difficulty": "beginner", "tags": ["aesthetics"], "related_tools": []},
                {"content": "Boot priority: SSD first (NVMe M.2), disable unused boot devices (optical, network PXE), UEFI mode (not legacy)", "keywords": ["boot priority", "boot order"], "difficulty": "beginner", "tags": ["boot"], "related_tools": []},
                {"content": "TPM 2.0: Enable for Windows 11 (fTPM firmware or discrete TPM), security feature (BitLocker encryption)", "keywords": ["tpm", "security"], "difficulty": "intermediate", "tags": ["windows 11"], "related_tools": []},
                {"content": "Integrated graphics: Disable if dedicated GPU (free PCIe lanes/RAM), enable for iGPU encoding (Quick Sync), multi-monitor iGPU+dGPU", "keywords": ["igpu", "integrated graphics"], "difficulty": "intermediate", "tags": ["gpu"], "related_tools": []},
                {"content": "SATA mode: AHCI (modern SSDs/HDDs), RAID (multiple drives array), IDE (legacy obsolete), NVMe uses PCIe (not SATA)", "keywords": ["sata", "ahci"], "difficulty": "beginner", "tags": ["storage"], "related_tools": []},
                {"content": "USB power: ErP S4/S5 charging (charge devices when off), disable (save power <1W), USB Type-C PD (Power Delivery) support", "keywords": ["usb", "charging"], "difficulty": "beginner", "tags": ["power"], "related_tools": []},
                {"content": "POST delay: Set 0 sec (instant boot), default 3 sec (F2/Del BIOS entry time), fast troubleshooting increase to 5 sec", "keywords": ["post", "delay"], "difficulty": "beginner", "tags": ["boot"], "related_tools": []},
                {"content": "Q-Flash/BIOS Flashback: Update BIOS without CPU (newer CPU support), USB BIOS file, critical feature new builds (AM5/LGA1700)", "keywords": ["bios update", "flashback"], "difficulty": "intermediate", "tags": ["bios"], "related_tools": []},
                {"content": "BIOS version: Update BIOS (microcode, RAM support, Resizable BAR), risk bricking (UPS recommended), stable version > latest beta", "keywords": ["bios version", "update"], "difficulty": "advanced", "tags": ["maintenance"], "related_tools": []},
                {"content": "Clear CMOS: Reset BIOS defaults (overclock unstable), jumper or button, removes all settings, re-apply XMP/settings after", "keywords": ["clear cmos", "reset"], "difficulty": "intermediate", "tags": ["troubleshooting"], "related_tools": []},
                {"content": "UEFI vs Legacy: UEFI (modern, GPT drives >2TB, Secure Boot), Legacy (old hardware, MBR drives), Windows 11 requires UEFI", "keywords": ["uefi", "legacy bios"], "difficulty": "intermediate", "tags": ["boot"], "related_tools": []},
                {"content": "Stability testing: Prime95 (CPU stress), MemTest86 (RAM 8+ hours), FurMark (GPU stress), OCCT (PSU stability), overnight tests", "keywords": ["stability", "stress test"], "difficulty": "advanced", "tags": ["testing"], "related_tools": ["Prime95", "MemTest86"]},
                {"content": "Recommended BIOS: ASUS (best OC features), MSI (Click BIOS 5 user-friendly), Gigabyte (budget solid), ASRock (value tweaking)", "keywords": ["bios brands", "manufacturers"], "difficulty": "beginner", "tags": ["hardware"], "related_tools": []},
                {"content": "AMD AGESA: BIOS microcode updates (Ryzen stability, RAM support), 1.2.0.7+ Ryzen 7000 stable, check motherboard QVL (RAM compatibility)", "keywords": ["agesa", "amd"], "difficulty": "advanced", "tags": ["bios"], "related_tools": []},
                {"content": "Intel ME (Management Engine): Enterprise remote management, disable (enthusiast privacy), stability issues some boards, update ME firmware", "keywords": ["intel me", "management"], "difficulty": "expert", "tags": ["enterprise"], "related_tools": []},
                {"content": "Safe overclocking: +5% CPU, +10% GPU, test stability each step, stress test 1 hour, daily usage monitor temps/crashes week", "keywords": ["safe oc", "beginner"], "difficulty": "intermediate", "tags": ["overclocking"], "related_tools": []}
            ]
        }
'''

    return categories_code


def add_categories_to_file(file_path, categories_code):
    """Ajoute les catégories au fichier"""

    print(f"[READ] Lecture du fichier: {file_path}")

    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    return_pattern = r'(\n\s+return kb\s*\n)'

    if not re.search(return_pattern, content):
        print("[ERROR] 'return kb' non trouve dans le fichier!")
        return False

    print("[OK] Pattern 'return kb' trouve")

    new_content = re.sub(
        return_pattern,
        categories_code + r'\1',
        content,
        count=1
    )

    print(f"[SAVE] Sauvegarde des modifications...")
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(new_content)

    print("[OK] Fichier modifie avec succes!")
    return True


def count_categories_and_tips(file_path):
    """Compte les catégories et conseils"""

    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    categories = re.findall(r'kb\["([^"]+)"\]\s*=\s*\{', content)
    tips = re.findall(r'\{"content":', content)

    return len(categories), len(tips)


def main():
    """Fonction principale"""

    print("=" * 80)
    print("AJOUT DE 15 CATEGORIES RESTANTES (Windows 11, Drivers, Gaming, Networking)")
    print("=" * 80)

    file_path = r"C:\Users\Utilisateur\Downloads\Nitrite-V18.5\src\v14_mvp\ai_knowledge_unified.py"

    print("\n[STATS] ETAT INITIAL:")
    initial_cats, initial_tips = count_categories_and_tips(file_path)
    print(f"   - Categories: {initial_cats}")
    print(f"   - Conseils: {initial_tips}")

    print("\n[PROCESS] Generation du code des 4 categories (Windows 11 + BIOS)...")
    categories_code = create_remaining_categories_code()

    print("\n[PROCESS] Modification du fichier...")
    success = add_categories_to_file(file_path, categories_code)

    if not success:
        print("\n[ERROR] ECHEC de l'operation")
        return

    print("\n[STATS] ETAT FINAL:")
    final_cats, final_tips = count_categories_and_tips(file_path)
    print(f"   - Categories: {final_cats} (+{final_cats - initial_cats})")
    print(f"   - Conseils: {final_tips} (+{final_tips - initial_tips})")

    print("\n" + "=" * 80)
    print("[SUCCESS] OPERATION REUSSIE!")
    print("=" * 80)
    print(f"\n[FILE] Fichier mis a jour: {file_path}")
    print(f"\n[SUMMARY] AJOUTS:")
    print(f"   - {final_cats - initial_cats} nouvelles categories (Windows 11 + BIOS)")
    print(f"   - {final_tips - initial_tips} nouveaux conseils")
    print(f"\n[TOTAL] {final_cats} categories | {final_tips} conseils")


if __name__ == "__main__":
    main()
