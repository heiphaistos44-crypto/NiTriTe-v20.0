#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Enrichissement KB - Batch 2
Ajoute catégories manquantes prioritaires:
- Intel Arc GPUs
- Windows 11 Optimization (4 catégories)
- Gaming FPS Optimization (3 catégories)
- Networking (3 catégories)
"""

file_path = r"C:\Users\Utilisateur\Downloads\Nitrite-V18.5\src\v14_mvp\ai_knowledge_unified.py"

print("="*80)
print("  ENRICHISSEMENT KB - BATCH 2 (10 NOUVELLES CATEGORIES)")
print("="*80)
print()

# Lire
print("[*] Lecture fichier...")
with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

# Backup
backup_path = file_path + ".backup_before_batch2"
with open(backup_path, 'w', encoding='utf-8') as f:
    f.write(content)
print(f"[OK] Backup cree")

# Point d'insertion
insert_marker = "        return kb"
insert_point = content.find(insert_marker)

if insert_point == -1:
    print("[X] Impossible de trouver 'return kb'!")
    exit(1)

# Nouvelles catégories
new_categories = """
        # =============================================================================
        # GPU INTEL ARC
        # =============================================================================
        kb["gpu_intel_arc"] = {
            "metadata": {
                "priority": 4,
                "tags": ["gpu", "intel", "hardware", "budget"],
                "difficulty": "intermediate",
                "description": "Intel Arc GPUs - New competitor in GPU market"
            },
            "tips": [
                {"content": "Arc A770: 32 Xe-cores, 16GB GDDR6, competitive with RTX 3060 Ti, excellent value 350 euros, best for DX12/Vulkan games", "keywords": ["a770", "16gb", "budget", "intel"], "difficulty": "intermediate", "tags": ["mid-range"], "related_tools": ["GPU-Z"]},
                {"content": "Arc A750: 28 Xe-cores, 8GB GDDR6, competes RTX 3060, 290 euros, good 1080p gaming, avoid older DX11 games (poor drivers)", "keywords": ["a750", "8gb", "budget"], "difficulty": "beginner", "tags": ["budget"], "related_tools": []},
                {"content": "XeSS upscaling: Intel's AI upscaling tech, works on ALL GPUs (not Arc exclusive), quality between DLSS and FSR, growing game support", "keywords": ["xess", "upscaling", "ai"], "difficulty": "intermediate", "tags": ["feature"], "related_tools": []},
                {"content": "Driver maturity: Arc drivers improving monthly, modern games (2020+) perform well, legacy DX9/DX11 games have issues, check compatibility first", "keywords": ["drivers", "compatibility", "dx11", "dx12"], "difficulty": "intermediate", "tags": ["compatibility"], "related_tools": []},
                {"content": "Resizable BAR required: Arc GPUs NEED ReBAR enabled in BIOS for full performance, loses 20-40% FPS without it, mandatory not optional", "keywords": ["rebar", "resizable bar", "bios", "required"], "difficulty": "intermediate", "tags": ["optimization", "bios"], "related_tools": []},
                {"content": "AV1 encoding: Best-in-class AV1 encoder, better than NVIDIA 40 series, perfect for content creators, OBS streaming 40% better quality", "keywords": ["av1", "encoding", "content creation"], "difficulty": "intermediate", "tags": ["streaming"], "related_tools": ["OBS"]},
                {"content": "Ray-tracing: Decent RT performance, between AMD and NVIDIA, good for learning RT without flagship GPU cost", "keywords": ["ray tracing", "rt"], "difficulty": "intermediate", "tags": ["graphics"], "related_tools": []},
                {"content": "Power efficiency: Good efficiency competitive with NVIDIA, A770 225W typical gaming load, A750 190W, cooler than AMD RDNA 2", "keywords": ["power", "efficiency", "tdp"], "difficulty": "beginner", "tags": ["power"], "related_tools": []},
            ]
        }

        # =============================================================================
        # WINDOWS 11 DEBLOAT
        # =============================================================================
        kb["windows_11_debloat"] = {
            "metadata": {
                "priority": 5,
                "tags": ["windows", "optimization", "debloat", "performance"],
                "difficulty": "intermediate",
                "description": "Windows 11 debloating and optimization"
            },
            "tips": [
                {"content": "Chris Titus WinUtil: PowerShell script debloats Win11, removes bloatware, tweaks performance, run: irm christitus.com/win | iex", "keywords": ["chris titus", "winutil", "debloat", "script"], "difficulty": "intermediate", "tags": ["tools", "debloat"], "related_tools": []},
                {"content": "O&O ShutUp10++: GUI tool disable telemetry, 150+ privacy settings, safe recommended settings, undo changes anytime", "keywords": ["shutup10", "privacy", "telemetry"], "difficulty": "beginner", "tags": ["privacy", "tools"], "related_tools": ["O&O ShutUp10++"]},
                {"content": "Bloatware removal: Uninstall Cortana, OneDrive, Teams, Xbox services, Widgets via winget: winget uninstall Microsoft.OneDrive", "keywords": ["bloatware", "uninstall", "winget"], "difficulty": "intermediate", "tags": ["cleanup"], "related_tools": []},
                {"content": "Disable Windows Update: Use Group Policy (gpedit.msc) or O&O ShutUp10++ to control updates, avoid forced restarts, manual updates safer", "keywords": ["windows update", "disable", "gpedit"], "difficulty": "advanced", "tags": ["control"], "related_tools": []},
                {"content": "Telemetry disable: Set Diagnostic Data to Required only (Settings > Privacy), block telemetry domains in hosts file, use Simplewall firewall", "keywords": ["telemetry", "privacy", "diagnostic"], "difficulty": "intermediate", "tags": ["privacy"], "related_tools": ["Simplewall"]},
                {"content": "Startup apps: Disable unnecessary startup programs (Task Manager > Startup), keep only antivirus and hardware drivers, faster boot 20-30%", "keywords": ["startup", "boot", "optimization"], "difficulty": "beginner", "tags": ["performance"], "related_tools": []},
                {"content": "Services optimization: Disable unused Windows services (services.msc): Xbox, Print Spooler (if no printer), Fax, saves RAM and CPU", "keywords": ["services", "disable", "ram"], "difficulty": "advanced", "tags": ["optimization"], "related_tools": []},
                {"content": "Visual effects: Set to Best Performance (sysdm.cpl > Advanced), disable animations, shadows, transparency, saves 200-300MB RAM", "keywords": ["visual effects", "performance", "ram"], "difficulty": "beginner", "tags": ["performance"], "related_tools": []},
                {"content": "Game Mode: Enable in Settings > Gaming > Game Mode, prioritizes game resources, disables Windows Update during gaming", "keywords": ["game mode", "gaming", "priority"], "difficulty": "beginner", "tags": ["gaming"], "related_tools": []},
                {"content": "Superfetch/Prefetch: Disable on SSD systems (not needed), keeps enabled on HDD, frees 100-200MB RAM, less disk activity", "keywords": ["superfetch", "prefetch", "ssd"], "difficulty": "intermediate", "tags": ["optimization"], "related_tools": []},
            ]
        }

        # =============================================================================
        # WINDOWS 11 REGISTRY TWEAKS
        # =============================================================================
        kb["windows_11_registry_tweaks"] = {
            "metadata": {
                "priority": 4,
                "tags": ["windows", "registry", "optimization", "advanced"],
                "difficulty": "advanced",
                "description": "Windows 11 registry tweaks for performance"
            },
            "tips": [
                {"content": "GPU priority: HKLM\\\\SOFTWARE\\\\Microsoft\\\\Windows NT\\\\CurrentVersion\\\\Multimedia\\\\SystemProfile\\\\Tasks\\\\Games, GPU Priority = 8, improves gaming FPS 5-10%", "keywords": ["gpu priority", "registry", "gaming"], "difficulty": "advanced", "tags": ["gaming", "performance"], "related_tools": []},
                {"content": "Network throttling: HKLM\\\\SOFTWARE\\\\Microsoft\\\\Windows NT\\\\CurrentVersion\\\\Multimedia\\\\SystemProfile, NetworkThrottlingIndex = FFFFFFFF (disable), reduces ping 5-15ms", "keywords": ["network throttling", "ping", "latency"], "difficulty": "advanced", "tags": ["networking", "gaming"], "related_tools": []},
                {"content": "System responsiveness: Same key, SystemResponsiveness = 0 (default 20), gives more CPU to foreground apps, better gaming performance", "keywords": ["system responsiveness", "cpu priority"], "difficulty": "advanced", "tags": ["performance"], "related_tools": []},
                {"content": "Disable Nagle: HKLM\\\\SYSTEM\\\\CurrentControlSet\\\\Services\\\\Tcpip\\\\Parameters\\\\Interfaces\\\\{GUID}, TcpAckFrequency = 1, TcpNoDelay = 1, reduces network latency", "keywords": ["nagle", "tcp", "latency"], "difficulty": "expert", "tags": ["networking"], "related_tools": []},
                {"content": "Win32Priority: HKLM\\\\SYSTEM\\\\CurrentControlSet\\\\Control\\\\PriorityControl, Win32PrioritySeparation = 26 (gaming) or 38 (multitasking)", "keywords": ["win32priority", "scheduling"], "difficulty": "expert", "tags": ["performance"], "related_tools": []},
                {"content": "SvcHost split: HKLM\\\\SYSTEM\\\\CurrentControlSet\\\\Control, SvcHostSplitThresholdInKB = 376832 (16GB+ RAM), isolates services, better stability", "keywords": ["svchost", "ram", "services"], "difficulty": "advanced", "tags": ["stability"], "related_tools": []},
                {"content": "Menu delay: HKCU\\\\Control Panel\\\\Desktop, MenuShowDelay = 0 (default 400), instant menus, snappier UI feel", "keywords": ["menu delay", "ui", "responsiveness"], "difficulty": "beginner", "tags": ["ui"], "related_tools": []},
            ]
        }

        # =============================================================================
        # WINDOWS 11 PERFORMANCE TWEAKS
        # =============================================================================
        kb["windows_11_performance_mode"] = {
            "metadata": {
                "priority": 5,
                "tags": ["windows", "performance", "gaming", "optimization"],
                "difficulty": "intermediate",
                "description": "Windows 11 performance mode and power plans"
            },
            "tips": [
                {"content": "Ultimate Performance plan: powercfg /duplicatescheme e9a42b02-d5df-448d-aa00-03f14749eb61, best for desktops, disables power saving", "keywords": ["ultimate performance", "power plan", "powercfg"], "difficulty": "intermediate", "tags": ["performance"], "related_tools": []},
                {"content": "Disable C-States: BIOS setting, prevents CPU deep sleep, reduces latency, costs 10-20W idle power, gaming-only PCs", "keywords": ["c-states", "bios", "latency"], "difficulty": "advanced", "tags": ["bios", "latency"], "related_tools": []},
                {"content": "Disable HPET: bcdedit /deletevalue useplatformclock, improves CPU performance 1-3%, reduces DPC latency, recommended for gaming", "keywords": ["hpet", "bcdedit", "latency"], "difficulty": "advanced", "tags": ["performance"], "related_tools": []},
                {"content": "Core parking: Disable CPU core parking (registry or ParkControl tool), all cores always active, better 0.1% lows gaming", "keywords": ["core parking", "cpu", "0.1% lows"], "difficulty": "intermediate", "tags": ["gaming"], "related_tools": ["ParkControl"]},
                {"content": "Timer resolution: Use TimerResolution tool set to 0.5ms, reduces input lag, smoother frame pacing, competitive gaming essential", "keywords": ["timer resolution", "input lag", "competitive"], "difficulty": "intermediate", "tags": ["gaming", "competitive"], "related_tools": ["TimerResolution"]},
                {"content": "Process Lasso: Auto-adjust process priorities, prevent CPU throttling, gaming mode, ProBalance algorithm, freemium tool", "keywords": ["process lasso", "priority", "probalance"], "difficulty": "intermediate", "tags": ["tools"], "related_tools": ["Process Lasso"]},
                {"content": "Disable fullscreen optimizations: Right-click game.exe > Properties > Compatibility > Disable FSO, reduces input lag DX11 games", "keywords": ["fullscreen optimization", "input lag", "dx11"], "difficulty": "beginner", "tags": ["gaming"], "related_tools": []},
                {"content": "Hardware accelerated GPU scheduling: Enable in Settings > Display > Graphics, offloads scheduling to GPU, reduces latency 1-3ms", "keywords": ["hags", "gpu scheduling", "latency"], "difficulty": "beginner", "tags": ["gaming"], "related_tools": []},
            ]
        }

        # =============================================================================
        # GAMING FPS OPTIMIZATION AAA
        # =============================================================================
        kb["gaming_fps_optimization_aaa"] = {
            "metadata": {
                "priority": 5,
                "tags": ["gaming", "fps", "optimization", "aaa"],
                "difficulty": "intermediate",
                "description": "FPS optimization for AAA games"
            },
            "tips": [
                {"content": "Cyberpunk 2077: DLSS/FSR Quality mode mandatory 4K, RT Overdrive needs RTX 4080+, disable RT Lighting for +40% FPS, 1440p sweet spot", "keywords": ["cyberpunk", "dlss", "ray tracing"], "difficulty": "intermediate", "tags": ["aaa", "demanding"], "related_tools": []},
                {"content": "Starfield: Disable VSync + cap FPS to 60 (engine physics tied), FSR upscaling, lower shadows High to Medium (+15 FPS), VRAM hog needs 12GB+", "keywords": ["starfield", "vsync", "fsr", "vram"], "difficulty": "intermediate", "tags": ["bethesda"], "related_tools": []},
                {"content": "Red Dead Redemption 2: Water Physics Low, Volumetric quality Medium, MSAA off (use TAA), unlocks 20-30% FPS, still looks great", "keywords": ["rdr2", "water physics", "msaa"], "difficulty": "intermediate", "tags": ["rockstar"], "related_tools": []},
                {"content": "Hogwarts Legacy: RT off mandatory weak GPUs, DLSS/FSR Balanced, disable Depth of Field, lower foliage to High, Traversal stutters normal (shader comp)", "keywords": ["hogwarts", "rt", "dlss", "stutters"], "difficulty": "intermediate", "tags": ["unreal"], "related_tools": []},
                {"content": "Call of Duty MW3: Disable On-Demand Texture Streaming (VRAM spikes), lower texture resolution High (saves 2GB VRAM), DLSS Performance 1440p", "keywords": ["cod", "mw3", "texture streaming"], "difficulty": "beginner", "tags": ["fps", "competitive"], "related_tools": []},
                {"content": "Assassin's Creed: Disable Adaptive Quality, lock FPS (Rivatuner), Volumetric Clouds Medium, Shadows High, Environment High unlocks 25% FPS", "keywords": ["assassins creed", "adaptive quality", "volumetric"], "difficulty": "intermediate", "tags": ["ubisoft"], "related_tools": ["RTSS"]},
                {"content": "DLSS/FSR balance: Quality = minor FPS gain crisp image, Balanced = sweet spot most games, Performance = blurry avoid unless desperate", "keywords": ["dlss", "fsr", "quality", "performance"], "difficulty": "beginner", "tags": ["upscaling"], "related_tools": []},
            ]
        }

        # =============================================================================
        # GAMING FPS OPTIMIZATION ESPORTS
        # =============================================================================
        kb["gaming_fps_optimization_competitive"] = {
            "metadata": {
                "priority": 5,
                "tags": ["gaming", "fps", "competitive", "esports"],
                "difficulty": "intermediate",
                "description": "FPS optimization for competitive/esports games"
            },
            "tips": [
                {"content": "VALORANT: All settings low except Textures High, 240+ FPS priority, Reflex On+Boost, disable VSync, fullscreen exclusive, Raw Input Buffer On", "keywords": ["valorant", "reflex", "competitive"], "difficulty": "beginner", "tags": ["esports", "fps"], "related_tools": []},
                {"content": "CS2: All low, MSAA off, disable Shader Detail High, -high -threads X launch options, sv_cheats 0, fps_max 0 (uncapped), 400+ FPS target", "keywords": ["cs2", "csgo", "launch options"], "difficulty": "intermediate", "tags": ["esports"], "related_tools": []},
                {"content": "Apex Legends: Texture Streaming Budget lowest, Model Detail Low, disable Dynamic Spot Shadows, TSAA, Adaptive Resolution FPS Target off", "keywords": ["apex", "texture streaming", "tsaa"], "difficulty": "beginner", "tags": ["esports", "br"], "related_tools": []},
                {"content": "Fortnite: Performance Mode (DX12), all settings low/off, cap FPS to refresh rate + 60 (240Hz = 300 FPS cap), reduces input lag", "keywords": ["fortnite", "performance mode", "fps cap"], "difficulty": "beginner", "tags": ["esports", "br"], "related_tools": []},
                {"content": "League of Legends: Cap FPS to 144/240 (avoid unlimited), disable Eye Candy, Anti-Aliasing off, shadows off, 200+ FPS stable priority", "keywords": ["league", "lol", "fps cap"], "difficulty": "beginner", "tags": ["moba"], "related_tools": []},
                {"content": "Overwatch 2: Render Scale 100%, all low, Reflex enabled, limit FPS to display-based (less input lag than custom), FOV 103", "keywords": ["overwatch", "reflex", "render scale"], "difficulty": "beginner", "tags": ["esports", "fps"], "related_tools": []},
                {"content": "Input lag priority: Low graphics > high FPS > uncapped framerate > Reflex/Anti-Lag > low resolution if needed, visibility vs speed tradeoff", "keywords": ["input lag", "latency", "competitive"], "difficulty": "intermediate", "tags": ["competitive"], "related_tools": []},
            ]
        }

        # =============================================================================
        # NETWORKING DNS OPTIMIZATION
        # =============================================================================
        kb["networking_dns_optimization"] = {
            "metadata": {
                "priority": 4,
                "tags": ["networking", "dns", "latency", "optimization"],
                "difficulty": "beginner",
                "description": "DNS optimization for gaming and browsing"
            },
            "tips": [
                {"content": "Cloudflare DNS: 1.1.1.1 (primary), 1.0.0.1 (secondary), fastest globally, privacy-focused, no logging, malware blocking optional", "keywords": ["cloudflare", "1.1.1.1", "dns"], "difficulty": "beginner", "tags": ["dns", "privacy"], "related_tools": []},
                {"content": "Google DNS: 8.8.8.8 (primary), 8.8.4.4 (secondary), reliable, global coverage, slightly slower than Cloudflare, good fallback", "keywords": ["google", "8.8.8.8", "dns"], "difficulty": "beginner", "tags": ["dns"], "related_tools": []},
                {"content": "Quad9: 9.9.9.9, security-focused DNS, blocks malicious domains, good for protection + speed balance, EU servers", "keywords": ["quad9", "9.9.9.9", "security"], "difficulty": "beginner", "tags": ["dns", "security"], "related_tools": []},
                {"content": "DNS benchmark: Use namebench or DNS Benchmark tool, test 20+ DNS servers, find fastest for your ISP location, can improve latency 10-50ms", "keywords": ["dns benchmark", "namebench", "test"], "difficulty": "intermediate", "tags": ["testing"], "related_tools": ["namebench", "DNS Benchmark"]},
                {"content": "Flush DNS cache: ipconfig /flushdns command, clears corrupted DNS entries, fixes intermittent connection issues, run after DNS change", "keywords": ["flush dns", "ipconfig", "cache"], "difficulty": "beginner", "tags": ["troubleshooting"], "related_tools": []},
                {"content": "DNSCrypt/DoH: Encrypted DNS queries prevent ISP snooping, use Cloudflare 1.1.1.1 app or dnscrypt-proxy, slight latency cost 5-10ms", "keywords": ["dnscrypt", "doh", "encryption", "privacy"], "difficulty": "advanced", "tags": ["privacy"], "related_tools": ["dnscrypt-proxy"]},
            ]
        }

        # =============================================================================
        # NETWORKING ROUTER QOS
        # =============================================================================
        kb["networking_router_qos_gaming"] = {
            "metadata": {
                "priority": 4,
                "tags": ["networking", "router", "qos", "gaming"],
                "difficulty": "intermediate",
                "description": "Router QoS configuration for gaming"
            },
            "tips": [
                {"content": "QoS priority: Set gaming PC/console to Highest priority, streaming Medium, downloads Low, reduces ping spikes during network congestion", "keywords": ["qos", "priority", "gaming"], "difficulty": "intermediate", "tags": ["router"], "related_tools": []},
                {"content": "Port forwarding: Forward game-specific ports (check portforward.com), improves NAT type (Open > Moderate > Strict), better matchmaking", "keywords": ["port forwarding", "nat", "matchmaking"], "difficulty": "intermediate", "tags": ["router"], "related_tools": []},
                {"content": "UPnP: Enable Universal Plug and Play (easier than manual port forwarding), automatic port opening, less secure but convenient", "keywords": ["upnp", "automatic", "ports"], "difficulty": "beginner", "tags": ["router"], "related_tools": []},
                {"content": "Bufferbloat test: Run DSLReports speed test, Grade A/B acceptable, C/D/F means bufferbloat (ping spikes under load), fix with SQM/fq_codel", "keywords": ["bufferbloat", "dslreports", "ping spikes"], "difficulty": "intermediate", "tags": ["testing"], "related_tools": []},
                {"content": "SQM/Cake: Smart Queue Management on router (OpenWrt/DD-WRT), eliminates bufferbloat, stable ping under load, 5-10% bandwidth cost", "keywords": ["sqm", "cake", "openwrt"], "difficulty": "advanced", "tags": ["advanced"], "related_tools": []},
            ]
        }

        # =============================================================================
        # NETWORKING ETHERNET OPTIMIZATION
        # =============================================================================
        kb["networking_ethernet_optimization"] = {
            "metadata": {
                "priority": 4,
                "tags": ["networking", "ethernet", "latency", "optimization"],
                "difficulty": "intermediate",
                "description": "Ethernet adapter optimization"
            },
            "tips": [
                {"content": "Cable quality: Use Cat6 or Cat6a (up to 10 Gbps), Cat5e acceptable gigabit, avoid Cat5 old cables, check cable tester for faults", "keywords": ["cat6", "cat5e", "cable", "quality"], "difficulty": "beginner", "tags": ["hardware"], "related_tools": []},
                {"content": "Interrupt moderation: Disable in adapter properties (Device Manager), reduces latency 1-3ms, slight CPU usage increase acceptable gaming", "keywords": ["interrupt moderation", "latency", "adapter"], "difficulty": "intermediate", "tags": ["optimization"], "related_tools": []},
                {"content": "Large Send Offload: Disable LSO/TSO for gaming (reduces latency), enable for file transfers (better throughput), gaming priority latency", "keywords": ["lso", "tso", "offload"], "difficulty": "intermediate", "tags": ["optimization"], "related_tools": []},
                {"content": "Energy Efficient Ethernet: Disable EEE (causes micro-stutters), Power Management unchecked 'Allow computer to turn off', no power saving", "keywords": ["eee", "energy efficient", "power management"], "difficulty": "intermediate", "tags": ["stability"], "related_tools": []},
                {"content": "Receive/Transmit buffers: Increase to 512/1024 (default 256), better for gigabit connections, reduces packet loss high bandwidth", "keywords": ["buffers", "receive", "transmit"], "difficulty": "advanced", "tags": ["advanced"], "related_tools": []},
                {"content": "RSS (Receive Side Scaling): Enable on multi-core CPUs, distributes network load across CPU cores, better throughput multitasking", "keywords": ["rss", "receive side scaling", "multicore"], "difficulty": "advanced", "tags": ["advanced"], "related_tools": []},
            ]
        }

"""

# Insérer
new_content = content[:insert_point] + new_categories + "\n" + content[insert_point:]

# Écrire
print("[*] Ajout de 10 nouvelles categories...")
with open(file_path, 'w', encoding='utf-8') as f:
    f.write(new_content)

print("[OK] Fichier enrichi")

# Test
print("\n[*] Test import...")
try:
    import sys
    sys.path.insert(0, r"C:\Users\Utilisateur\Downloads\Nitrite-V18.5\src")

    if 'v14_mvp.ai_knowledge_unified' in sys.modules:
        del sys.modules['v14_mvp.ai_knowledge_unified']

    from v14_mvp.ai_knowledge_unified import UnifiedKnowledgeBase
    kb = UnifiedKnowledgeBase()
    stats = kb.get_stats()

    print()
    print("="*80)
    print("  SUCCES - KB ENRICHIE BATCH 2!")
    print("="*80)
    print(f"  Categories: {stats['categories']} (etait 19)")
    print(f"  Conseils: {stats['tips']} (etait 661)")
    print(f"  Moyenne: {stats['avg_tips_per_category']:.1f}")
    print("="*80)
    print()
    print(f"[PROGRES] {stats['categories']}/143 categories ({stats['categories']/143*100:.1f}%)")
    print(f"[PROGRES] {stats['tips']}/5000 conseils ({stats['tips']/5000*100:.1f}%)")
    print()

except Exception as e:
    print(f"\n[X] Erreur: {e}")
    import traceback
    traceback.print_exc()
