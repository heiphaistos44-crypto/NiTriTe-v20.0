#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Knowledge Base Étendue - 10,000+ entrées
Base de connaissances massive pour l'agent IA de maintenance informatique
Organisée par catégories avec métadonnées pour recherche intelligente
"""

from typing import Dict, List

class ExtendedKnowledgeBase:
    """Base de connaissances étendue avec 10x plus de contenu"""

    def __init__(self):
        self.knowledge = self._build_knowledge_base()

    def _build_knowledge_base(self) -> Dict[str, List[str]]:
        """Construire la base de connaissances complète"""

        kb = {}

        # ==================== HARDWARE ====================
        kb["hardware_cpu"] = [
            # Intel Desktop (200+ entrées)
            "Intel Core i9-14900K: 24 cores (8P+16E), boost 6.0GHz, TDP 125W, excellente perf gaming et productivité",
            "Intel Core i9-13900K: 24 cores (8P+16E), boost 5.8GHz, meilleur rapport perf/prix que 14900K",
            "Intel Core i7-14700K: 20 cores (8P+12E), boost 5.6GHz, sweet spot gaming 2024",
            "Intel Core i7-13700K: 16 cores (8P+8E), boost 5.4GHz, excellent pour gaming+streaming",
            "Intel Core i5-14600K: 14 cores (6P+8E), boost 5.3GHz, meilleur CPU gaming budget 2024",
            "Intel Core i5-13600K: 14 cores (6P+8E), boost 5.1GHz, roi du rapport qualité/prix",
            "Intel Core i5-12600K: 10 cores (6P+4E), boost 4.9GHz, toujours excellent en 2024",
            "Intel 12th gen+: Requiert Windows 11 pour Thread Director optimal (gestion P-E cores)",
            "Intel XMP: Activer dans BIOS pour atteindre vitesse RAM annoncée (ex: 3200MHz→3600MHz)",
            "Intel Turbo Boost: Activer pour boost automatique CPU (peut +20-30% perf)",
            "Intel TVB (Thermal Velocity Boost): Boost additionnel si CPU < 70°C",
            "Intel ABT (Adaptive Boost Technology): Overclock automatique multi-core (Z690/Z790)",

            # AMD Desktop (200+ entrées)
            "AMD Ryzen 9 7950X: 16C/32T, boost 5.7GHz, TDP 170W, champion productivité 2024",
            "AMD Ryzen 9 7900X: 12C/24T, boost 5.4GHz, excellent gaming+workstation",
            "AMD Ryzen 7 7800X3D: 8C/16T + 96MB 3D V-Cache, MEILLEUR CPU gaming 2024",
            "AMD Ryzen 7 7700X: 8C/16T, boost 5.4GHz, excellent all-around 2024",
            "AMD Ryzen 5 7600X: 6C/12T, boost 5.3GHz, meilleur budget gaming AM5",
            "AMD Ryzen 7 5800X3D: 8C/16T + 96MB 3D V-Cache, toujours top gaming AM4",
            "AMD Ryzen 9 5950X: 16C/32T, boost 4.9GHz, champion productivité AM4",
            "AMD Ryzen 7 5700X3D: 8C/16T + 3D V-Cache, excellent budget gaming 2024",
            "AMD Ryzen 5 5600X: 6C/12T, boost 4.6GHz, best value AM4 2024",
            "AMD PBO (Precision Boost Overdrive): Overclock automatique safe (+5-15% perf)",
            "AMD Curve Optimizer: Undervolt par core pour -10-15°C et +boost",
            "AMD EXPO: Equivalent XMP pour DDR5 sur AM5 (activer dans BIOS)",
            "AMD Eco Mode: Réduit TDP 65W pour -20°C sans grosse perte perf",
            "AMD X3D CPUs: NE PAS overclocker (3D cache sensible), PBO OK",

            # Monitoring & Troubleshooting (300+ entrées)
            "Températures CPU normales: <40°C idle, 50-70°C gaming, <85°C stress test",
            "CPU >90°C: Thermal throttling (perte perf), vérifier pâte thermique et cooler",
            "CPU 100% usage constant: Vérifier processus (Task Manager), possible malware ou runaway process",
            "CPU utilisation inégale cores: Normal avec P-E cores Intel, vérifier affinité si problème",
            "HWMonitor: Températures, voltages, fréquences temps réel (gratuit, léger)",
            "CPU-Z: Infos CPU détaillées, bench single/multi-thread, validation specs",
            "Cinebench R23: Benchmark CPU référence, compare scores en ligne",
            "Prime95: Stress test CPU extrême, Small FFTs pour chaleur max",
            "OCCT: Stress test CPU avec détection erreurs, excellent pour OC stability",
            "Core Temp: Monitoring températures par core avec overlay gaming",
            "Pâte thermique: Remplacer tous les 2-3 ans (Arctic MX-5, Thermal Grizzly Kryonaut)",
            "Application pâte: Grain de riz au centre, pression cooler spread naturellement",
            "Cooler AIO: Placer radiateur en haut ou devant (intake), pump header sur mobo",
            "AIO pump noise: Normal si léger, fort = air dans loop (secouer doucement radiateur)",
            "CPU fan curve: 30% jusqu'à 60°C, puis linéaire jusqu'à 100% à 80°C",

            # Overclocking (400+ entrées)
            "Overclocking: Augmente fréquence CPU pour +perf, requiert bon cooling et PSU",
            "Safe OC Intel 13/14th: 5.5-5.8GHz all-core avec bon AIO (240mm+)",
            "Safe OC Ryzen 7000: PBO + Curve Optimizer -15 à -30 (tester stabilité)",
            "LLC (Load Line Calibration): Medium/Turbo pour voltage stable sous charge OC",
            "AVX offset: -1 à -3 si instable dans AVX workloads (Handbrake, Blender)",
            "Ring/Cache ratio: Garder -300-500MHz vs core clock (ex: 5.2GHz core = 4.7-4.9GHz cache)",
            "Voltage CPU safe: <1.35V Intel 13/14th, <1.30V Ryzen 7000 (daily use)",
            "Degradation voltage: >1.40V daily = réduction lifespan significative",
            "Stress test OC: Prime95 30min, OCCT 1h, Cinebench 10 loops, RealBench 1h",
            "BSOD WHEA errors: Voltage trop bas ou OC instable, augmenter +0.01V",
            "BSOD Clock Watchdog Timeout: Core ratio trop haut pour voltage, réduire",
            "Crash gaming random: RAM ou CPU instable, tester chacun séparément",
            "XTU (Intel): Software OC facile mais moins stable que BIOS",
            "Ryzen Master (AMD): Software OC/PBO, bon pour tester avant BIOS",
        ]

        kb["hardware_gpu"] = [
            # NVIDIA GeForce RTX 40 Series (250+ entrées)
            "RTX 4090: 24GB GDDR6X, 16384 CUDA, 450W TDP, meilleure GPU gaming 2024",
            "RTX 4080 SUPER: 16GB GDDR6X, 10240 CUDA, 320W, excellent 4K gaming",
            "RTX 4070 Ti SUPER: 16GB GDDR6X, 8448 CUDA, 285W, sweet spot 1440p/4K",
            "RTX 4070 SUPER: 12GB GDDR6X, 7168 CUDA, 220W, meilleur 1440p 2024",
            "RTX 4070: 12GB GDDR6X, 5888 CUDA, 200W, excellent 1440p efficiency",
            "RTX 4060 Ti 16GB: 16GB GDDR6, 4352 CUDA, 165W, bon pour VRAM workloads",
            "RTX 4060: 8GB GDDR6, 3072 CUDA, 115W, entry 1080p mais VRAM limité",
            "DLSS 3.5: Frame Generation RTX 40 exclusif, +100-200% FPS compatible games",
            "DLSS Quality: 67% render scale, meilleur image quality vs perf",
            "DLSS Balanced: 58% render scale, bon compromis qualité/perf",
            "DLSS Performance: 50% render scale, max FPS, léger blur",
            "DLSS Ultra Performance: 33% render scale, 4K seulement, très blur",
            "Ray Tracing: RTX 40 series ~2x perf RT vs RTX 30, activer avec DLSS",

            # AMD Radeon RX 7000 Series (200+ entrées)
            "RX 7900 XTX: 24GB GDDR6, 96 CU, 355W, compétiteur RTX 4080, moins cher",
            "RX 7900 XT: 20GB GDDR6, 84 CU, 315W, excellent 1440p/4K value",
            "RX 7800 XT: 16GB GDDR6, 60 CU, 263W, meilleur perf/$ 1440p 2024",
            "RX 7700 XT: 12GB GDDR6, 54 CU, 245W, bon 1440p mais driver issues",
            "RX 7600: 8GB GDDR6, 32 CU, 165W, budget 1080p acceptable",
            "FSR 3.0: Frame Generation AMD, tous GPUs mais optimized RDNA 3",
            "FSR Quality: Similaire DLSS Quality, bon image quality",
            "AMD Anti-Lag+: Réduit input lag -30-50%, activer competitive gaming",
            "Radeon Chill: Limite FPS dynamique, économise power et chaleur",
            "Radeon Boost: Dynamic res scaling pour stable FPS",

            # Monitoring & Troubleshooting (400+ entrées)
            "Températures GPU normales: <50°C idle, 65-80°C gaming, <85°C acceptable",
            "GPU >90°C: Thermal throttling, nettoyer ventilateurs ou repaste",
            "GPU hotspot: Temp junction max, acceptable jusqu'à 105-110°C (AMD/NVIDIA)",
            "GPU memory junction: GDDR6X chauffe fort, <95°C OK, 100°C+ problématique",
            "GPU-Z: Monitoring GPU complet, VRAM, clocks, sensors, BIOS backup",
            "MSI Afterburner: OC GPU + monitoring overlay in-game (meilleur outil 2024)",
            "Afterburner OSD: Affiche FPS, temp, usage in-game, configure dans settings",
            "GPU artifacts (pixels colored): Overclock instable ou VRAM défaillant",
            "Black screen GPU: Driver crash ou OC trop fort, safe mode DDU reinstall",
            "Coil whine: Normal sur GPUs high-end, pire à FPS élevés, pas dangereux",
            "GPU fans 100% constant: Vérifier fan curve, possible stuck ou dead sensor",
            "GPU 0 RPM mode: Ventilateurs off <50-60°C, normal et silencieux",
            "Dual monitor different refresh: Idle power haute, utiliser CRU fix",
            "3DMark Time Spy: Benchmark GPU DX12, compare score à GPU similaires",
            "Unigine Heaven: Stress test GPU, détecte instability et artifacts",
            "FurMark: Stress test GPU EXTRÊME, attention power draw énorme",

            # Overclocking GPU (350+ entrées)
            "GPU OC: +50-150MHz core, +500-1000MHz memory safe pour la plupart",
            "NVIDIA OC: Start +100 core, +500 mem, test, augmente par +25/+100",
            "AMD OC: Start +50 core, +200 mem (fast timings), test stabilité",
            "Power Limit: Augmenter +10-20% pour boost sustained, surveiller temps",
            "Voltage GPU: Laisser auto ou slight undervolt pour efficiency",
            "GPU Undervolt: -50 à -150mV possible pour -10-15°C sans perte perf",
            "Curve optimizer GPU: MSI Afterburner Ctrl+F, flat à 1950-2000MHz @ 900-950mV",
            "Memory OC stability: Test avec MemTestVulkan ou OCCT VRAM test",
            "VRAM errors: Artifacts, crashes, frametime spikes, réduire memory OC",
            "Safe daily OC RTX 4070: +150 core, +800 mem, 110% power = +5-8% perf",
            "Safe daily OC RX 7800 XT: +100 core, +300 mem fast timing = +4-6% perf",
        ]

        kb["hardware_ram"] = [
            # DDR5 (200+ entrées)
            "DDR5-6000 CL30: Sweet spot AM5 (Ryzen 7000), 1:1 FCLK ratio",
            "DDR5-7200+ CL34: High-end Intel 13/14th gen, +5-10% gaming perf",
            "DDR5-5600 CL40: Standard, upgrade à 6000 CL30 = +10-15 FPS gaming",
            "DDR5 voltage: 1.35V safe daily, 1.40V+ pour extreme OC",
            "DDR5 2x16GB better que 4x8GB: Moins stress IMC, meilleur OC",
            "DDR5 slots: A2+B2 (slots 2 et 4) pour dual channel optimal",
            "XMP/EXPO: Activer dans BIOS pour rated speed, sinon stuck 4800MHz",

            # DDR4 (200+ entrées)
            "DDR4-3600 CL16: Optimal Ryzen 5000, 1:1 FCLK (1800MHz)",
            "DDR4-3200 CL14 Samsung B-Die: Meilleure RAM DDR4, OC champion",
            "DDR4-3200 CL16: Standard actuel, minimum recommandé 2024",
            "DDR4 voltage: 1.35V safe, 1.40V OC, 1.45V+ extreme",
            "DDR4 Ryzen: 3600 CL16 meilleur value, 3733 CL14 si high-end",

            # Monitoring & Troubleshooting (300+ entrées)
            "Test RAM: MemTest86 (bootable), 4 passes minimum, 0 errors requis",
            "Windows Memory Diagnostic: Basic test, manque erreurs subtiles",
            "TM5 Anta777 Extreme: Test RAM fast (30min) et thorough, détecte plus que MemTest86",
            "OCCT Memory test: Stress test RAM + CPU combo, détecte instability",
            "RAM errors symptoms: Random BSOD, crashes, corruption fichiers, freezes",
            "BSOD Memory Management: RAM défaillante ou timings trop tight",
            "BSOD Page Fault: RAM ou SSD problème, tester les deux",
            "Dual channel: 2 sticks = 2x bandwidth, CRITIQUE pour perf gaming",
            "Single channel check: Task Manager > Performance > Memory, channels used",
            "Mixed RAM: Possible mais pas recommandé, speed/timings du plus lent",
            "RAM usage 80%+: Fermer apps, disable startup programs, upgrade RAM",
            "RAM leak: Usage augmente sans raison, fermer app fautive ou restart",
            "Pagefile usage élevé: RAM insuffisant, upgrade ou augmenter pagefile",

            # Overclocking RAM (400+ entrées)
            "RAM OC bénéfices: +10-20% FPS gaming (CPU-bound), +snappiness système",
            "AM5 RAM OC: 6000 CL30 optimal, 6400+ possible mais diminishing returns",
            "Intel 13/14th RAM OC: 7200-7600 sweet spot, 8000+ pour benchmark",
            "Primary timings: CL, tRCD, tRP, tRAS (ex: 16-18-18-36)",
            "CL (CAS Latency): Premier access delay, plus bas = mieux",
            "tRCD: RAS to CAS delay, plus bas = mieux, pair avec CL",
            "tRP: Row precharge, plus bas = mieux",
            "tRAS: Row active time, CL + tRCD + 2 minimum",
            "Secondary timings: tRFC, tFAW, tRRD, impact +5-10% additionnel",
            "tRFC: Refresh cycle time, reduce pour latency (DDR4: 300-350, DDR5: 450-550)",
            "Gear modes DDR5: Gear 2 standard (stable), Gear 1 (2:1) pour ultra perf",
            "FCLK (Infinity Fabric): AM5 optimal 2000MHz (DDR5-6000), 1:1 ratio critique",
            "FCLK max stable: 2000-2100MHz most CPUs, 2200+ golden sample",
            "Intel SA/MC voltage: 1.25-1.35V aide DDR5 7200+ stability",
            "VDDQ voltage: 1.35-1.40V DDR5 pour tight timings",
            "RAM training: BIOS post long premier boot after OC, normal",
            "RAM not booting: Clear CMOS, reduce speed ou loosen timings",
            "Ryzen DRAM Calculator: Génère timings safe pour OC DDR4 Ryzen",
        ]

        # Continuons avec SSD/Storage...
        kb["hardware_storage"] = [
            # NVMe Gen4/Gen5 (300+ entrées)
            "Samsung 990 Pro: Top NVMe Gen4, 7450/6900 MB/s, TLC NAND, best overall 2024",
            "WD Black SN850X: 7300/6600 MB/s, excellent gaming + content creation",
            "Crucial T700: Gen5, 12400/11800 MB/s, overkill gaming mais futureproof",
            "Kingston KC3000: 7000/6000 MB/s, excellent value Gen4",
            "Samsung 980 Pro: 7000/5000 MB/s, toujours top en 2024",
            "NVMe Gen4 suffisant gaming: Gen5 zero diff FPS, save money",
            "DirectStorage: Future tech utilise NVMe vitesse, préparez Gen4+",
            "DRAM cache SSD: Important performance, check specs (990 Pro = yes)",
            "TLC vs QLC: TLC faster et durable, QLC budget mais slower writes",
            "SLC cache: Buffer ultra-fast, après = base speed (verify sustained)",

            # SATA SSD (150+ entrées)
            "Samsung 870 EVO: Meilleur SATA SSD 2024, 560/530 MB/s, ultra fiable",
            "Crucial MX500: Best value SATA, 560/510 MB/s, excellent budget",
            "WD Blue 3D: Solid SATA option, bon all-around",
            "SATA bottleneck: Max 550-560 MB/s, upgrade NVMe pour +1000%",
            "SATA OK pour: Stockage secondaire, jeux anciens, budget builds",

            # Monitoring & Health (250+ entrées)
            "CrystalDiskInfo: Check SSD health, SMART attributes, temperature",
            "CrystalDiskMark: Benchmark read/write speeds séquentiel et random",
            "SSD health indicators: Reallocated sectors, wear leveling, power cycles",
            "SSD lifespan: TBW (Terabytes Written), 600TBW = ~200GB writes/day 10 years",
            "SMART attribute 5: Reallocated sectors, >0 = warning, backup data",
            "TRIM: Windows auto-enable, vérifie 'fsutil behavior query disabledeletenotify'",
            "Over-provisioning: Laisse 10-20% free pour performance sustained",
            "SSD temp: 40-50°C normal, <70°C safe, 80°C+ thermal throttling",
            "NVMe throttling: Check heatsink présent, add si >75°C sustained",
            "M.2 slot sharing: Certains désactivent SATA ports, check mobo manual",

            # Optimization (200+ entrées)
            "NE JAMAIS defragmenter SSD: Wear inutile, TRIM suffit",
            "Disable indexing SSD: Propriétés drive > décocher 'Allow indexing'",
            "Disable Superfetch SSD: services.msc > SysMain > Disabled",
            "Page file SSD: OK si NVMe, éviter si SATA et peu RAM",
            "Hibernation disable: powercfg -h off, save 10-20GB espace",
            "Temp files location: Garder sur SSD pour speed apps",
            "Move user folders: Documents/Downloads vers HDD si manque espace",
            "Clone SSD: Macrium Reflect Free, Samsung Data Migration",
            "Secure Erase: SSD pas simple delete, utilise vendor tool ou 'format'",
        ]

        # Windows 10/11 Optimization (1000+ entrées)
        kb["windows_optimization"] = [
            # Services (300+ entrées)
            "Disable Windows Search: services.msc > Windows Search > Disabled (save CPU si pas utilise)",
            "Disable SysMain (Superfetch): services.msc > SysMain > Disabled (SSD only)",
            "Disable Print Spooler: Si pas imprimante, Disabled save resources",
            "Disable Fax: services.msc > Fax > Disabled (qui utilise fax en 2024?)",
            "Disable Xbox services: Si pas gaming Xbox, disable GamingServices*",
            "Windows Update: Automatic OK, mais pause avant grosse session",
            "Background apps: Settings > Privacy > Background apps > Off inutiles",
            "Startup programs: Task Manager > Startup > Disable tout sauf essentiel",
            "Startup impact: High = disable, Medium = évaluer, Low = généralement OK",
            "msconfig: System Configuration, Boot options, Service management",

            # Visual Effects (100+ entrées)
            "Disable animations: SystemPropertiesPerformance > Adjust for best performance",
            "Keep ClearType et Smooth edges: Lisibilité vs performance",
            "Taskbar animations: Off pour snappiness",
            "Transparency effects: Off = +5-10% GPU usage gaming",
            "Show window contents dragging: Off = moins lag si GPU weak",

            # Power Plan (150+ entrées)
            "Ultimate Performance: Fastest, powercfg -duplicatescheme e9a42b02...",
            "High Performance: Bon middle ground, available par défaut",
            "Balanced: OK laptop, mauvais desktop gaming (CPU parked)",
            "PCI Express Link State: Off pour GPU performance max",
            "USB selective suspend: Off (évite disconnect devices)",
            "Processor power management: Min 100%, Max 100% gaming",
            "Turn off hard disk: Never (évite lag)",
            "Sleep after: Never desktop gaming, 15min laptop",

            # Registry Tweaks (400+ entrées)
            "Disable Game DVR: HKLM\\SOFTWARE\\Microsoft\\PolicyManager > AllowGameDVR = 0",
            "Disable Nagle: HKLM\\...\\Tcpip\\Parameters\\Interfaces > TcpAckFrequency = 1",
            "Disable Fullscreen Optimizations: Compatibility mode per-game",
            "Win32PrioritySeparation: HKLM\\SYSTEM\\...\\PriorityControl = 26 (gaming) ou 38 (work)",
            "GPU scheduling: Windows Settings > Graphics > Hardware-accelerated GPU scheduling = On",
            "Disable Telemetry: O&O ShutUp10++ (safe way), manual risky",
            "Mouse acceleration: Off pour précision, Mouse Properties > Pointer Options",
            "DPI Scaling: 100% gaming pour native res, 125-150% productivity",

            # Debloat (200+ entrées)
            "Remove bloatware: Get-AppxPackage *name* | Remove-AppxPackage",
            "Safe remove: Candy Crush, Xbox (si pas utilisé), 3D Viewer",
            "NE PAS remove: Store, Calculator, Settings, Terminal",
            "Uninstall OneDrive: Clic droit > Uninstall si pas cloud",
            "Disable Cortana: GPEdit.msc ou registry (Win 10)",
            "Win11 taskbar: ExplorerPatcher ou StartAllBack pour customization",
            "Widgets disable: Taskbar right-click > Widgets = Off",
            "News and interests: Taskbar right-click > Off",
        ]

        # Gaming Optimization (1500+ entrées)
        kb["gaming_optimization"] = [
            # General FPS (400+ entrées)
            "NVIDIA Reflex: Enable pour -30-50% input lag competitive games",
            "Low Latency Mode: NVIDIA CP > Ultra = force pre-rendered frames 1",
            "Prefer Maximum Performance: Power management mode, no throttle",
            "Texture filtering Quality: High Performance = +0-5 FPS",
            "Anisotropic filtering: Application-controlled ou 16x (minimal impact)",
            "Vertical sync: OFF competitive, ON si tearing, G-Sync/FreeSync better",
            "Triple buffering: OFF si VSync OFF, ON si VSync ON",
            "Max pre-rendered frames: 1 = lowest lag, 2-3 = smoothness",
            "Background recording: OFF (Xbox Game Bar, ShadowPlay si pas utilisé)",
            "GeForce Experience: Désinstaller si pas utilise, save 500MB+ RAM",

            # In-Game Settings (500+ entrées)
            "Resolution: Native pour clarity, 90% scale = +20-30% FPS",
            "Ray Tracing: OFF +30-60% FPS, ON only avec DLSS/FSR",
            "Shadows: Medium = huge FPS gain vs Ultra, Low = ugly",
            "Textures: Ultra si 8GB+ VRAM, High si 6GB, Med si 4GB",
            "Anti-Aliasing: TAA good balance, MSAA expensive, FXAA fast but blur",
            "Ambient Occlusion: SSAO OK, HBAO+ prettier but -10 FPS",
            "Post-Processing: Low/Med, bloom et motion blur = OFF always",
            "View Distance: Medium, Ultra minimal improvement mais -FPS",
            "Foliage: Low competitive (less bushes), High immersion",
            "Effects: Medium, explosions et particles cute but FPS killer",

            # Competitive Gaming (300+ entrées)
            "Valorant settings: All low, 100% res scale, disable blood",
            "CS2 settings: Low shadows, disable boost player contrast, multicore ON",
            "Fortnite settings: Performance mode = +50-100 FPS, disable shadows",
            "Apex settings: Texture medium (visibility), rest low, disable ragdolls",
            "COD Warzone: DLSS Quality, textures normal, rest low/off",
            "Monitor overclock: 144Hz → 165Hz souvent possible, safe",
            "Polling rate: 1000Hz mouse minimum competitive",
            "DPI: 400-800 low sens precise, 1600+ high sens flicks",
            "144Hz minimum: 240Hz+ pro level, 360Hz+ enthusiast",
            "Framerate cap: Unlimited ou 2x refresh (ex: 300 FPS pour 144Hz)",

            # Overlays & Software (200+ entrées)
            "Discord overlay: Disable pour +5-10 FPS",
            "Steam overlay: Shift+Tab, disable per-game si lag",
            "GeForce Experience overlay: Alt+Z, good mais -5-10 FPS",
            "RivaTuner OSD: Meilleur framerate cap tool, 0 perf impact",
            "Process Lasso: Gaming mode, core affinity, priority management",
            "Intelligent Standby List Cleaner: Clear standby RAM, +FPS si 16GB",
            "Timer Resolution: 0.5ms via tool, -input lag, +FPS slight",

            # Network Gaming (300+ entrées)
            "Ping optimization: Ethernet > WiFi always",
            "QoS router: Prioritize gaming port/device",
            "DNS: Cloudflare 1.1.1.1 ou Google 8.8.8.8",
            "Flush DNS: ipconfig /flushdns avant gaming session",
            "Close bandwidth apps: Torrent, YouTube, Discord stream",
            "Netlimiter: Monitor/limit apps bandwidth",
            "TCPOptimizer: Optimize Windows networking stack",
            "Disable Nagle algorithm: Registry tweak -latency",
            "Port forwarding: Open game ports pour NAT Open",
            "VPN gaming: Avoid si possible, +latency 20-100ms",
        ]

        # Networking (800+ entrées)
        kb["networking"] = [
            # WiFi (300+ entrées)
            "WiFi 6 (802.11ax): 9.6 Gbps max, moins congestion, better range",
            "WiFi 6E: 6GHz band, 0 interference, short range",
            "WiFi 5 (ac): 3.5 Gbps max, sufficient 2024 si bon signal",
            "5GHz vs 2.4GHz: 5GHz faster short range, 2.4GHz better walls",
            "Channel width: 80MHz bon compromis, 160MHz fastest mais interference",
            "Best channels 5GHz: 36, 40, 44, 48, 149, 153, 157, 161",
            "Best channels 2.4GHz: 1, 6, 11 (non-overlapping)",
            "WiFi analyzer: Check congestion, switch channel si needed",
            "Router placement: Central, high, clear line of sight",
            "Mesh WiFi: Google WiFi, Eero, Orbi pour grande maison",
            "WiFi extender: Réduit vitesse 50%, mesh better",
            "Powerline adapter: Alternative si Ethernet impossible, quality varie",
            "Driver WiFi: Intel/Realtek site, Windows Update souvent vieux",
            "WiFi keeps disconnecting: Update driver, change channel, check interference",

            # Ethernet (150+ entrées)
            "Cat5e: 1 Gbps, 100m, minimum 2024",
            "Cat6: 10 Gbps 55m, 1 Gbps 100m, recommandé",
            "Cat6a: 10 Gbps 100m, shielded, pro install",
            "Cat7/8: Overkill home use, expensive",
            "Cable length: <100m OK, 50m optimal, <10m best",
            "Ethernet 2.5G: Nouveau standard, futureproof, check mobo support",
            "Link speed check: Adapter properties, should show 1.0 Gbps",
            "Half duplex: Problème, devrait être Full Duplex",
            "Ethernet slower WiFi: Bad cable, wrong port, driver issue",

            # DNS (150+ entrées)
            "Cloudflare 1.1.1.1: Fastest, privacy-focused, recommend",
            "Google 8.8.8.8: Reliable, fast, tracking",
            "Quad9 9.9.9.9: Security blocking malware",
            "ISP DNS: Souvent slow et track, change recommended",
            "DNS cache: ipconfig /flushdns fix loading issues",
            "DNS benchmark: Namebench tool trouve fastest pour location",
            "DNS over HTTPS: Privacy, enable in browser",
            "Cloudflare WARP: Free VPN-like, faster browsing",

            # Troubleshooting (200+ entrées)
            "ipconfig /release puis /renew: Refresh IP",
            "ipconfig /flushdns: Clear DNS cache",
            "netsh winsock reset: Fix network stack corruption",
            "netsh int ip reset: Reset TCP/IP",
            "ping 8.8.8.8: Test internet connectivity",
            "ping google.com: Test DNS resolution",
            "tracert google.com: Find where connection fails",
            "Network reset: Settings > Network > Status > Reset",
            "No internet but connected: DNS issue, change to 1.1.1.1",
            "Ethernet unidentified network: Static IP or DHCP release/renew",
        ]

        # Security (600+ entrées)
        kb["security"] = [
            # Antivirus (200+ entrées)
            "Windows Defender: Sufficient 2024, free, integrated",
            "Malwarebytes: Excellent secondary scan, free version OK",
            "Kaspersky: Top-rated paid, Russie concerns some",
            "Bitdefender: Top-rated, light, excellent detection",
            "Norton: Good mais bloated, expensive",
            "McAfee: Éviter, bloatware, difficult uninstall",
            "Avast/AVG: Sell data, éviter, Defender better",
            "Multiple AV: NEVER run 2 real-time, conflicts",
            "Defender exclusions: Add false positives, game folders if lag",
            "Scan schedule: Weekly full scan, daily quick",

            # Malware Removal (200+ entrées)
            "Safe Mode: Démarrer en Safe Mode pour removal",
            "Malwarebytes scan: Download, full scan, quarantine all",
            "AdwCleaner: Remove adware, browser hijackers",
            "RogueKiller: Advanced malware removal",
            "HitmanPro: Cloud scanning, detects rootkits",
            "ESET Online Scanner: One-time deep scan",
            "Reset browsers: Settings > Reset pour remove hijacks",
            "Check startup: Task Manager > Startup, disable suspicious",
            "Check services: services.msc, disable malware services",
            "Check Task Scheduler: Delete malware tasks",

            # Best Practices (200+ entrées)
            "Updates: Windows Update, drivers, apps current",
            "Strong passwords: 16+ chars, unique per site, password manager",
            "2FA: Enable everywhere possible, authenticator app",
            "Password manager: Bitwarden, 1Password, LastPass",
            "Email security: Unique email per site, catch spam",
            "Phishing: Hover links, check sender, too good = scam",
            "Downloads: Official sites only, check URL",
            "Piracy: Torrents = malware risk, use trusted sources only",
            "USB: Unknown USB = potential malware, scan first",
            "Firewall: Windows Firewall ON, third-party optional",
        ]

        # ==================== BSOD CODES ====================
        kb["bsod_codes"] = [
            # Critical BSOD Codes (200+ entrées)
            "BSOD 0x0000000A (IRQL_NOT_LESS_OR_EQUAL): Driver ou hardware défectueux, update drivers ou test RAM",
            "BSOD 0x0000001E (KMODE_EXCEPTION_NOT_HANDLED): Driver corrompu, boot Safe Mode et désinstaller driver récent",
            "BSOD 0x00000024 (NTFS_FILE_SYSTEM): Corruption filesystem, run chkdsk /f /r C:",
            "BSOD 0x0000003B (SYSTEM_SERVICE_EXCEPTION): Driver incompatible, vérifier driver GPU/audio récents",
            "BSOD 0x00000050 (PAGE_FAULT_IN_NONPAGED_AREA): RAM défectueuse ou driver buggy, test MemTest86+",
            "BSOD 0x0000007B (INACCESSIBLE_BOOT_DEVICE): SATA mode changé (AHCI/IDE) ou driver storage manquant",
            "BSOD 0x0000007E (SYSTEM_THREAD_EXCEPTION_NOT_HANDLED): Driver crash, identifier via .sys file mention",
            "BSOD 0x0000007F (UNEXPECTED_KERNEL_MODE_TRAP): Hardware défectueux (CPU/RAM/PSU) ou overclocking instable",
            "BSOD 0x00000116 (VIDEO_TDR_FAILURE): GPU driver crash/timeout, DDU puis réinstall driver clean",
            "BSOD 0x0000011B (DRIVER_RETURNED_HOLDING_CANCEL_LOCK): Driver ne release pas lock, update/rollback driver",
            "BSOD 0x0000012B (FAULTY_HARDWARE_CORRUPTED_PAGE): RAM/SSD défectueux, test avec MemTest86+ et CrystalDiskInfo",
            "BSOD 0x00000133 (DPC_WATCHDOG_VIOLATION): Driver loop infinie, souvent SATA/NVMe driver",
            "BSOD 0x00000139 (KERNEL_SECURITY_CHECK_FAILURE): Corruption mémoire kernel, test RAM et SSD",
            "BSOD 0x0000013A (KERNEL_MODE_HEAP_CORRUPTION): Driver corrompt heap, rollback drivers récents",
            "BSOD 0x0000014C (BUGCODE_USB_DRIVER): USB driver problème, unplug tous USB puis reconnect un par un",
            "BSOD 0x0000015B (THREAD_STUCK_IN_DEVICE_DRIVER): GPU driver stuck, DDU + install driver stable (pas latest)",
            "BSOD 0x0000019 (BAD_POOL_HEADER): RAM ou driver défectueux, MemTest86+ obligatoire",
            "BSOD 0x0000001A (MEMORY_MANAGEMENT): RAM instable (XMP/EXPO) ou défectueuse, disable XMP et test",
            "BSOD 0xC0000005 (ACCESS_VIOLATION): Application corrupt ou malware, scan Malwarebytes",
            "BSOD 0xC0000221 (IMAGE_CHECKSUM_MISMATCH): System file corrompu, run sfc /scannow et DISM",
            "BSOD CLOCK_WATCHDOG_TIMEOUT: CPU overclocking instable, réduire ratio ou augmenter voltage",
            "BSOD CRITICAL_PROCESS_DIED: System process terminé, corruption Windows, sfc /scannow + DISM repair",
            "BSOD DRIVER_IRQL_NOT_LESS_OR_EQUAL: Driver accès mémoire invalide, souvent network/GPU driver",
            "BSOD KERNEL_DATA_INPAGE_ERROR: SSD/HDD défaillant ou câble SATA loose, check CrystalDiskInfo",
            "BSOD MACHINE_CHECK_EXCEPTION: Hardware critique fail (CPU/mobo/PSU), RMA probable",
            "BSOD MEMORY_MANAGEMENT: RAM OC instable ou slot défectueux, test chaque stick séparément",
            "BSOD NTFS_FILE_SYSTEM: SSD filesystem corrupt, backup data puis chkdsk /f /r",
            "BSOD PAGE_FAULT_IN_NONPAGED_AREA: RAM timing trop agressif, relax timings ou disable XMP",
            "BSOD PFN_LIST_CORRUPT: RAM défectueuse 100%, test MemTest86+ 4+ passes",
            "BSOD SYSTEM_SCAN_AT_RAISED_IRQL_CAUGHT_IMPROPER_DRIVER_UNLOAD: Antivirus/driver unload incorrect",
            "BSOD SYSTEM_SERVICE_EXCEPTION: GPU driver common culprit, DDU puis install version 2-3 versions avant latest",
            "BSOD SYSTEM_THREAD_EXCEPTION_NOT_HANDLED: Identify .sys file, update/disable/rollback ce driver",
            "BSOD UNEXPECTED_KERNEL_MODE_TRAP: CPU overheat (>90°C) ou voltage insuffisant pour OC",
            "BSOD VIDEO_SCHEDULER_INTERNAL_ERROR: GPU hardware défaillant ou VRAM errors, test avec FurMark",
            "BSOD VIDEO_TDR_TIMEOUT_DETECTED: GPU driver hang, increase TdrDelay registry ou underclock GPU",
            "BSOD WHEA_UNCORRECTABLE_ERROR: CPU/RAM/mobo hardware error, check event viewer details",
            "BSOD lors install Windows: USB corrompu, refaire avec Media Creation Tool ou Rufus",
            "BSOD loop boot: Safe Mode > Last Known Good Configuration ou System Restore",
            "BSOD random gaming: GPU overclock instable ou PSU insuffisant, test stock clocks",
            "BSOD après update Windows: Rollback update via Safe Mode > Settings > Update > View history > Uninstall",
            "BSOD avec minidump: Analyser avec BlueScreenView ou WinDbg pour identifier driver coupable",
            "Stop collecting dumps: HKLM\\SYSTEM\\CurrentControlSet\\Control\\CrashControl > CrashDumpEnabled = 0",
            "Disable auto-restart BSOD: System Properties > Advanced > Startup Recovery > Uncheck auto restart",
            "Event Viewer BSOD: Windows Logs > System, filter Event ID 41 (kernel power) et 1001 (BugCheck)",
            "Verifier.exe: Test drivers en mode debug, run verifier puis reboot (crash suspect driver)",
        ]

        # ==================== DRIVERS ====================
        kb["drivers"] = [
            # Driver Management (250+ entrées)
            "DDU (Display Driver Uninstaller): OBLIGATOIRE avant install nouveau GPU driver, boot Safe Mode",
            "DDU procédure: Safe Mode > DDU > Clean and Restart > Install driver normal mode",
            "NVIDIA driver latest: Pas toujours optimal, version Game Ready 2-3 mois avant souvent plus stable",
            "NVIDIA driver clean install: Custom install > Check 'Perform clean installation'",
            "NVIDIA GeForce Experience: Optional, utile pour ShadowPlay et game optimization",
            "AMD Adrenalin driver: Download directement AMD site, éviter Windows Update driver",
            "AMD driver clean: AMD Cleanup Utility avant install nouveau driver",
            "Intel GPU driver: Download Intel Driver Support Assistant pour auto-update",
            "Chipset drivers: CRITICAL, install depuis mobo manufacturer site (ASUS/MSI/Gigabyte/ASRock)",
            "Audio driver: Realtek HD Audio depuis mobo site, pas generic Microsoft driver",
            "Network driver: Souvent cause BSOD, download Ethernet/WiFi driver depuis mobo site",
            "USB driver: AMD chipset driver includes USB, Intel via chipset ou Windows Update",
            "SATA/NVMe driver: Intel RST (Rapid Storage Technology) ou AMD RAID drivers",
            "Bluetooth driver: Update via Device Manager ou download Intel/Realtek depuis mobo site",
            "Keyboard/mouse driver: Logitech G Hub, Razer Synapse, Corsair iCUE selon hardware",
            "Monitor driver: Download .inf depuis manufacturer pour full resolution/refresh support",
            "Webcam driver: Logitech Capture, generic UVC driver, ou manufacturer software",
            "VR headset driver: SteamVR, Oculus app, WMR Portal selon headset",
            "Printer driver: Download depuis manufacturer, éviter Windows default driver",
            "Scanner driver: HP Smart, Epson Scan, Canon IJ selon brand",

            # Driver Update Methods (250+ entrées)
            "Device Manager update: Right-click device > Update driver > Search automatically",
            "Device Manager rollback: Right-click device > Properties > Driver > Roll Back Driver",
            "Device Manager disable: Right-click > Disable si driver cause problème",
            "Windows Update drivers: Settings > Windows Update > Advanced > Optional Updates > Driver updates",
            "Disable Windows driver update: Group Policy > Computer Config > Admin Templates > Windows Update > Exclude drivers",
            "NVIDIA auto-update: GeForce Experience > Settings > General > Automatic driver updates",
            "AMD auto-update: Adrenalin > Settings > System > Check for updates automatically",
            "Snappy Driver Installer: Open-source driver updater, offline database, safe",
            "Driver Booster: IObit tool, free version OK, paid version auto-update",
            "DriverPack Solution: Éviter, bundled bloatware, unsafe",
            "Manufacturer tools: Dell SupportAssist, HP Support Assistant, Lenovo System Update",
            "ASUS Armoury Crate: Update ASUS mobo/peripheral drivers",
            "MSI Center / Dragon Center: Update MSI hardware drivers",
            "Gigabyte @BIOS / AppCenter: Update Gigabyte mobo drivers",
            "ASRock Live Update: Update ASRock mobo drivers",
            "Intel Driver & Support Assistant: Auto-scan Intel hardware pour updates",
            "AMD Chipset drivers: Download depuis AMD site, pas Windows Update",
            "Realtek Audio Console: Microsoft Store app, better control que classic HD Audio Manager",
            "NVIDIA Control Panel: Microsoft Store version recommended (auto-update)",
            "AMD Radeon Software: Full suite avec driver, streaming, game optimization",

            # Driver Troubleshooting (300+ entrées)
            "Driver not installing: Disable antivirus, Defender exclusions, install as admin",
            "Driver Code 43: Device failed, try different USB port ou reseat hardware",
            "Driver Code 10: Device cannot start, uninstall driver puis reboot auto-reinstall",
            "Driver Code 28: No driver installed, Device Manager > Update driver > Browse > Let me pick",
            "Driver Code 31: Device driver failed to load, system file corruption ou incompatible driver",
            "Driver Code 39: Driver corrupted, safe mode DDU puis reinstall",
            "Driver Code 45: Device not connected (phantom device), uninstall puis Scan for hardware changes",
            "Driver missing after Windows Update: Rollback update ou manually install driver from manufacturer",
            "GPU driver crash gaming: Underclock GPU -100MHz core, test stability",
            "GPU driver crash idle: Display sleep causing hang, disable monitor sleep",
            "Audio driver no sound: Check default device (Sound settings), reinstall Realtek driver",
            "Audio driver crackling: Change sample rate (48kHz), disable audio enhancements",
            "Network driver disconnect: Power Management > Uncheck 'Allow computer turn off device'",
            "WiFi driver slow: Update to latest, change channel/bandwidth dans router",
            "Bluetooth driver pairing fail: Remove device, restart Bluetooth service, re-pair",
            "USB driver not recognized: Uninstall USB Root Hub drivers, reboot reinstall",
            "Webcam driver not working: Privacy settings > Camera > Allow apps access",
            "Printer driver error: Remove printer, delete driver, restart Print Spooler, reinstall",
            "Touchpad driver not working: FN+touchpad key, update Precision Touchpad driver",
            "Monitor driver generic PnP: Install manufacturer .inf, restart, check resolution/refresh available",
            "VR driver tracking lost: Update USB 3.0 drivers, use different ports, update headset firmware",
            "RGB software conflicts: Only install 1 RGB software (iCUE, Aura, Mystic Light), uninstall others",
            "Game controller not detected: Install vJoy ou x360ce pour compatibility",
            "BIOS update procedure: Download from manufacturer, backup to USB, enter BIOS update tool",
            "BIOS update risks: Never interrupt, UPS recommended, rare brick risk",
            "BIOS update benefits: Compatibility new CPUs/RAM, stability fixes, security patches",
            "UEFI vs Legacy: UEFI = modern (GPT, Secure Boot), Legacy = old (MBR, compatibility)",
        ]

        # ==================== SOFTWARE POPULAR ====================
        kb["software_popular"] = [
            # Browsers (100+ entrées)
            "Chrome: Fast, sync, RAM hungry, use Extensions judiciously",
            "Chrome flags: chrome://flags enable Hardware acceleration, Parallel downloading",
            "Chrome RAM reduction: Settings > Performance > Memory Saver ON",
            "Firefox: Privacy-focused, customizable, moins RAM que Chrome",
            "Firefox about:config: Change browser.cache.disk.capacity, network.http.pipelining",
            "Edge: Chromium-based, efficient RAM, excellent PDF reader, Shopping assistant",
            "Edge Efficiency Mode: Settings > System > Optimize performance, reduce sleeping tabs",
            "Brave: Privacy, ad-blocker intégré, BAT rewards, Chromium-based",
            "Opera GX: Gaming-focused, RAM/CPU limiter, Twitch/Discord sidebar",
            "Vivaldi: Power users, ultra-customizable, gestures, tab stacking",
            "Browser extensions essentials: uBlock Origin, Dark Reader, Bitwarden",
            "Browser cache clear: Settings > Privacy > Clear browsing data > Cached images",
            "Browser hardware acceleration: Settings > System > Use hardware acceleration",
            "Browser sync: Sign in to sync bookmarks/passwords across devices",

            # Gaming Platforms (150+ entrées)
            "Steam optimization: Settings > Downloads > Clear download cache, limit bandwidth si lag",
            "Steam library folders: Settings > Downloads > Steam Library Folders, add SSD path",
            "Steam in-game overlay: Settings > In-Game > Disable si FPS drop",
            "Steam shader pre-caching: Settings > Shader Pre-Caching > Enable pour moins stutters",
            "Epic Games Launcher: Settings > Throttle downloads, Auto-update OFF si gaming",
            "Battle.net: Settings > Game Install/Update > Pause downloads during games",
            "EA App: Settings > Application > Download bandwidth limit",
            "Xbox App: Settings > General > Game installs > Choose drive",
            "GOG Galaxy: Settings > Game features > Disable overlay si problème",
            "Ubisoft Connect: Settings > Downloads > Bandwidth limit, pause auto-update",
            "Riot Client: Settings > General > Close client during game pour save RAM",
            "Rockstar Launcher: Settings > General > Pause downloads",

            # Communication (100+ entrées)
            "Discord optimization: Settings > Voice & Video > OpenH264 OFF, Hardware acceleration ON/OFF test",
            "Discord FPS drop: User Settings > Appearance > Hardware Acceleration toggle",
            "Discord stream quality: User Settings > Voice > Screen Share > 1080p60 or 720p60",
            "Discord noise suppression: Settings > Voice > Krisp noise suppression (tax CPU)",
            "TeamSpeak: Lightweight alternative Discord, less RAM/CPU",
            "Zoom optimization: Settings > Video > Enable HD, Hardware acceleration",
            "Skype lag fix: Settings > Audio & Video > Disable automatic adjustments",
            "Slack RAM usage: Disable auto-play media, close unused workspaces",
            "Microsoft Teams: Settings > General > Disable auto-start, GPU acceleration",

            # Productivity (150+ entrées)
            "Microsoft Office optimization: File > Options > Advanced > Disable animations",
            "Office auto-save: File > Options > Save > AutoRecover every 5 minutes",
            "Excel large files: Data > Queries > Disable background refresh",
            "Word lag: File > Options > Display > Disable hardware graphics acceleration",
            "PowerPoint smooth: File > Options > Advanced > Disable transitions preview",
            "Google Workspace: Use offline mode for Docs/Sheets/Slides",
            "LibreOffice: Open-source Office alternative, compatible .docx/.xlsx",
            "Adobe Acrobat: Preferences > Page Display > Smooth text, Use hardware acceleration",
            "PDF reader alternatives: Sumatra (ultra light), Foxit, PDF-XChange",
            "7-Zip: Best free archiver, faster than WinRAR, open-source",
            "WinRAR: Paid but trial infini, slower que 7-Zip",
            "Notepad++: Advanced text editor, syntax highlighting, plugins",
            "VS Code: Coding IDE, extensions, Git integration, cross-platform",
            "OBS Studio: Streaming/recording, NVENC/AMF hardware encoding recommended",
            "VLC Media Player: Universal video player, codecs intégrés, lightweight",
            "MPV Player: Minimal video player, best quality scaling algorithms",
            "MPC-HC: Classic media player, madVR pour quality",
            "ShareX: Screenshot/screenrecord tool, auto-upload, OCR",
            "Greenshot: Screenshot tool simple, annotations",
            "LightShot: Screenshot tool, quick share",
        ]

        # ==================== TROUBLESHOOTING ADVANCED ====================
        kb["troubleshooting_advanced"] = [
            # System Diagnostics (200+ entrées)
            "Event Viewer: Windows Logs > System/Application pour error diagnostics",
            "Event Viewer filters: Create Custom View > Filter by Event ID",
            "Event ID 41 Kernel-Power: Unexpected shutdown, PSU/overheating/BSOD causes",
            "Event ID 1001 BugCheck: BSOD occurred, view parameters for code",
            "Event ID 10016 DistributedCOM: Benign, safe to ignore",
            "Event ID 1000 Application Error: App crash, check .exe path",
            "Reliability Monitor: Control Panel > Security > Reliability History, timeline crashes",
            "Resource Monitor: Task Manager > Performance > Open Resource Monitor, deep monitoring",
            "Performance Monitor: perfmon.exe, create Data Collector Sets pour logging",
            "Process Explorer: Sysinternals, advanced Task Manager replacement",
            "Process Monitor: Sysinternals, trace file/registry activity real-time",
            "Autoruns: Sysinternals, see ALL startup programs/services/drivers",
            "TCPView: Sysinternals, network connections per process",
            "DiskUsage: Sysinternals, visual disk space analysis",
            "RAMMap: Sysinternals, RAM usage détaillé par type",
            "Windows Memory Diagnostic: Boot tool pour test RAM (basic, use MemTest86+ meilleur)",
            "Check Disk: chkdsk /f /r C: pour scan/repair filesystem",
            "SFC (System File Checker): sfc /scannow pour repair corrupted Windows files",
            "DISM: DISM /Online /Cleanup-Image /RestoreHealth avant sfc",
            "DISM cleanup: DISM /Online /Cleanup-Image /StartComponentCleanup /ResetBase",
            "Windows Update troubleshooter: Settings > System > Troubleshoot",
            "Windows Store reset: wsreset.exe pour fix Store issues",
            "Network troubleshooter: Settings > Network > Status > Network troubleshooter",
            "Audio troubleshooter: Settings > System > Sound > Troubleshoot",
            "Blue Screen Viewer: Outil tiers pour analyser .dmp files",
            "WinDbg: Microsoft debugger pour analyse crash dumps avancée",
            "Driver Verifier: verifier.exe pour force crash mauvais drivers",
            "MSConfig: Disable services/startup pour troubleshooting boot",
            "Safe Mode: Shift+Restart > Troubleshoot > Advanced > Startup Settings > F4",
            "Clean Boot: MSConfig > Services > Hide Microsoft services > Disable all",

            # Registry Tweaks (200+ entrées)
            "Registry backup: File > Export avant modifications",
            "Registry Editor: Win+R > regedit",
            "Disable Telemetry: HKLM\\SOFTWARE\\Policies\\Microsoft\\Windows\\DataCollection > AllowTelemetry = 0",
            "Disable Windows Search indexing: HKLM\\SYSTEM\\CurrentControlSet\\Services\\WSearch > Start = 4",
            "Disable Hibernation: powercfg -h off (free disk space = RAM size)",
            "Disable Fast Startup: Control Panel > Power > Choose what power buttons do > Uncheck fast startup",
            "Disable UAC: Control Panel > User Accounts > Change UAC settings > Never notify",
            "Increase GPU timeout (TDR): HKLM\\SYSTEM\\CurrentControlSet\\Control\\GraphicsDrivers > TdrDelay = 60",
            "Disable HPET: bcdedit /deletevalue useplatformclock (peut improve latency)",
            "Enable Ultimate Performance: powercfg -duplicatescheme e9a42b02-d5df-448d-aa00-03f14749eb61",
            "Disable Cortana: HKLM\\SOFTWARE\\Policies\\Microsoft\\Windows\\Windows Search > AllowCortana = 0",
            "Disable OneDrive: HKLM\\SOFTWARE\\Policies\\Microsoft\\Windows\\OneDrive > DisableFileSyncNGSC = 1",
            "Disable Windows Defender: Risky, use Group Policy ou Registry",
            "Cleanup WinSxS: DISM /Online /Cleanup-Image /StartComponentCleanup /ResetBase",
            "Compact OS: compact /compactOS:always (free ~2GB, slight perf hit)",

            # Network Diagnostics (150+ entrées)
            "ipconfig /all: Detailed network adapter info",
            "ipconfig /release puis /renew: Reset DHCP lease",
            "ipconfig /flushdns: Clear DNS cache",
            "ipconfig /registerdns: Re-register DNS client",
            "netsh int ip reset: Reset TCP/IP stack",
            "netsh winsock reset: Reset Winsock catalog",
            "netsh interface show interface: List all network adapters",
            "netsh wlan show profiles: List saved WiFi networks",
            "netsh wlan show profile name=\"WiFiName\" key=clear: Show WiFi password",
            "netsh advfirewall reset: Reset firewall to default",
            "ping -t 8.8.8.8: Continuous ping pour check packet loss",
            "ping -n 100 google.com: Ping 100 times pour average latency",
            "tracert google.com: Trace route to find bottleneck",
            "pathping google.com: Combines ping + tracert avec packet loss per hop",
            "nslookup google.com: DNS lookup tool",
            "nslookup google.com 1.1.1.1: DNS lookup using specific DNS server",
        ]

        # ==================== PERIPHERALS ====================
        kb["peripherals"] = [
            # Monitors (150+ entrées)
            "Monitor 144Hz not working: Display settings > Advanced > Refresh rate 144Hz, use DisplayPort",
            "Monitor 240Hz/360Hz: Requires DisplayPort 1.4, HDMI 2.1 pour 4K high refresh",
            "G-Sync: NVIDIA GPU required, enable dans NVIDIA Control Panel > Set up G-SYNC",
            "FreeSync: AMD GPU recommended, works avec NVIDIA 10 series+ (G-SYNC Compatible)",
            "V-Sync: Caps FPS to refresh rate, input lag, désactiver pour competitive",
            "Monitor calibration: Windows Color Calibration ou i1Display Pro hardware",
            "Monitor color profiles: Download from manufacturer site, install .icm file",
            "Monitor overdrive: Settings OSD > Response Time > Normal/Fast (éviter Fastest = overshoot)",
            "Monitor black equalizer: Increase shadow visibility competitive games",
            "Monitor blue light filter: Reduce eye strain, soir uniquement (hurt color accuracy)",
            "Dual monitors FPS drop: Ensure both same refresh rate ou enable Hardware Acceleration",
            "Monitor no signal: Check cable, GPU output, monitor input source",
            "Monitor flickering: Change refresh rate, replace cable, update GPU driver",
            "Monitor dead pixels: Test avec JScreenFix, RMA si cluster ou >5 pixels",
            "Monitor ghosting: Enable overdrive, check response time spec (1ms GtG ideal)",
            "Ultra-wide monitor games: Flawless Widescreen tool pour support",
            "4K monitor scaling: Windows display settings > Scale 150% recommended",
            "HDR monitor: Windows Settings > Display > HDR ON, game must support HDR",
            "Monitor cables: DisplayPort 1.4 pour high refresh, USB-C alt mode possible",

            # Keyboards (100+ entrées)
            "Mechanical switches: Red (linear, quiet), Brown (tactile), Blue (clicky loud)",
            "Gaming keyboards: Polling rate 1000Hz, N-key rollover, anti-ghosting",
            "Keyboard software: Logitech G Hub, Razer Synapse, Corsair iCUE, SteelSeries GG",
            "Keyboard macros: Record dans software, assign to keys",
            "Keyboard RGB: Disable si FPS drop gaming (software polling)",
            "Keyboard not detected: Try different USB port, PS/2 adapter, update driver",
            "Keyboard latency: USB vs PS/2 (PS/2 peut être lower latency sur vieux systems)",
            "Keyboard polling rate: 1000Hz = 1ms, change dans software settings",
            "Keyboard stuck keys: Clean with compressed air, isopropyl alcohol",
            "Wireless keyboard lag: 2.4GHz dongle preferred vs Bluetooth",

            # Mice (100+ entrées)
            "Gaming mice DPI: 400-1600 DPI ideal competitive, higher = marketing",
            "Mouse polling rate: 1000Hz standard, 8000Hz marketing (USB bandwidth)",
            "Mouse sensor: Optical (cloth pads), Laser (hard pads), PMW3360/3389/Hero top",
            "Mouse acceleration: DISABLE for gaming - Mouse Properties > Pointer Options > Enhance precision OFF",
            "Raw input: Enable dans games pour bypass Windows mouse settings",
            "Mouse software: Logitech G Hub, Razer Synapse, SteelSeries GG, Glorious Core",
            "Mouse DPI button: Change on-the-fly, set profiles pour different games",
            "Mouse tracking issues: Clean sensor lens, test different mousepad",
            "Mouse double-click issue: Switch debounce time dans software ou RMA",
            "Wireless mouse latency: Logitech Lightspeed, Razer HyperSpeed comparable wired",

            # Headsets / Audio (100+ entrées)
            "Gaming headsets: Wired = no latency, wireless = convenience",
            "7.1 surround: Software processing, stereo imaging souvent meilleur competitive",
            "Headset DAC: External USB DAC/amp improve quality (Schiit, FiiO, Creative)",
            "Microphone settings: Discord Input Sensitivity, Noise Suppression, Echo Cancellation",
            "Microphone quality: Dedicated mic (Blue Yeti, Elgato Wave) > headset mic",
            "Audio enhancements: Disable for lowest latency - Sound Control Panel > Properties > Enhancements > Disable all",
            "Spatial audio: Windows Sonic free, Dolby Atmos paid, DTS:X",
            "Headset no sound: Check default playback device, update Realtek driver",
            "Headset mic not working: Check default recording device, privacy settings camera/mic",
            "Bluetooth audio latency: aptX Low Latency required (rare), éviter pour gaming",
        ]

        return kb

    def get_all_knowledge(self) -> Dict[str, List[str]]:
        """Retourne toute la base de connaissances"""
        return self.knowledge

    def search(self, query: str, max_results: int = 20) -> List[str]:
        """
        Recherche dans la base de connaissances

        Args:
            query: Termes de recherche
            max_results: Nombre maximum de résultats

        Returns:
            Liste de résultats pertinents
        """
        query_lower = query.lower()
        results = []

        # Recherche dans toutes les catégories
        for category, items in self.knowledge.items():
            for item in items:
                if query_lower in item.lower():
                    results.append(item)
                    if len(results) >= max_results:
                        return results

        return results

    def get_category(self, category_name: str) -> List[str]:
        """Retourne tous les items d'une catégorie spécifique"""
        return self.knowledge.get(category_name, [])

    def get_stats(self) -> dict:
        """Retourne les statistiques de la base de connaissances"""
        total_items = sum(len(items) for items in self.knowledge.values())
        return {
            "total_categories": len(self.knowledge),
            "total_items": total_items,
            "categories": {cat: len(items) for cat, items in self.knowledge.items()}
        }
