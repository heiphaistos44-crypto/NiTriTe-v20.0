#!/usr/bin/env python3
"""
NiTriTe V18.5 Knowledge Base Enrichment - Phase 2: Hardware Categories
Target: Add detailed technical tips to hardware-related categories
Goal: Reach 3000+ total tips with highly specific, technical content
"""

import sys
sys.path.insert(0, r"C:\Users\Utilisateur\Downloads\Nitrite-V18.5\src")

# Force reload to get fresh instance
if 'v14_mvp.ai_knowledge_unified' in sys.modules:
    del sys.modules['v14_mvp.ai_knowledge_unified']

from v14_mvp.ai_knowledge_unified import UnifiedKnowledgeBase

def count_tips(kb_dict):
    """Count total tips across all categories"""
    total = 0
    for category, data in kb_dict.items():
        if isinstance(data, dict) and "tips" in data:
            total += len(data["tips"])
    return total

def enrich_hardware_categories():
    """Add detailed technical tips to hardware categories"""

    # Initialize knowledge base
    kb_instance = UnifiedKnowledgeBase()
    kb = kb_instance.kb

    print("=" * 80)
    print("NITRITE V18.5 - PHASE 2 HARDWARE ENRICHMENT")
    print("=" * 80)

    before_count = count_tips(kb)
    print(f"\nBEFORE: {before_count} total tips")
    print("\nAdding tips to hardware categories...\n")

    # ========================================================================
    # GPU INTEL ARC (Priority 1 - only 8 tips)
    # ========================================================================

    if "gpu_intel_arc" in kb:
        before = len(kb["gpu_intel_arc"]["tips"])
        kb["gpu_intel_arc"]["tips"].extend([
            {
                "content": "Intel Arc A770 ReBAR (Resizable BAR) is mandatory for optimal performance. Enable in BIOS under PCI Subsystem Settings > Above 4G Decoding (Enabled) + Re-Size BAR Support (Enabled). Without ReBAR, expect 20-40% performance loss in gaming workloads. Verify activation: GPU-Z shows 'Resizable BAR: Enabled'. Requires UEFI mode, CSM disabled, Windows 10 20H1+ or Windows 11.",
                "keywords": ["ReBAR", "Resizable BAR", "Intel Arc", "performance"],
                "difficulty": "intermediate",
                "tags": ["gpu", "bios", "optimization"],
                "related_tools": ["GPU-Z", "BIOS"]
            },
            {
                "content": "Arc GPU driver updates are critical - monthly releases fix major performance issues. Use Intel Driver & Support Assistant for auto-updates or manual DDU (Display Driver Uninstaller) clean install quarterly. Example: Driver 31.0.101.4502 (Q4 2023) improved A750 performance 15-30% in DX11 titles vs launch drivers. Always benchmark before/after with 3DMark Time Spy to validate improvements.",
                "keywords": ["Intel Arc drivers", "DDU", "driver updates"],
                "difficulty": "beginner",
                "tags": ["drivers", "maintenance"],
                "related_tools": ["DDU", "Intel DSA", "3DMark"]
            },
            {
                "content": "Arc A750/A770 XeSS (Xe Super Sampling) delivers better quality than DLSS at 'Quality' mode in many titles. Enable in-game: Graphics > Upscaling > XeSS Quality. Typical gains: 1440p native 65fps → XeSS Quality 95fps (+46%), visual parity 95%+. Works on competitor GPUs via DP4a but Arc gets XMX acceleration. Test in Hitman 3, Shadow of the Tomb Raider, F1 22 for best results.",
                "keywords": ["XeSS", "upscaling", "performance boost"],
                "difficulty": "beginner",
                "tags": ["gaming", "optimization"],
                "related_tools": ["Game settings"]
            },
            {
                "content": "Arc A380 6GB is optimal for AV1 encoding - hardware encoder beats software x265 by 30x speed while maintaining quality. OBS Studio 29+: Settings > Output > Encoder > 'AV1 (Intel Arc)'. Streaming: 1080p60 @ 8Mbps AV1 = 1080p60 @ 12Mbps H.264 quality. Recording: Use CQP 20-25 for archival. AV1 decode also accelerates YouTube/Twitch playback, reducing CPU usage 60%+.",
                "keywords": ["AV1", "encoding", "streaming", "Arc A380"],
                "difficulty": "intermediate",
                "tags": ["content creation", "streaming"],
                "related_tools": ["OBS Studio", "Handbrake"]
            },
            {
                "content": "Arc GPU undervolting via Intel Arc Control: Right-click desktop > Intel Graphics > Performance > Voltage/Frequency Curve. A770 example: -150mV offset reduces power 25W (225W→200W), temps 8°C (74°C→66°C), maintains 99% performance. Start -50mV, stress test Port Royal 30min, increase -25mV increments until instability. Silicon lottery varies -100mV to -200mV safe range.",
                "keywords": ["undervolting", "Arc Control", "power efficiency"],
                "difficulty": "advanced",
                "tags": ["overclocking", "optimization"],
                "related_tools": ["Intel Arc Control", "3DMark"]
            },
            {
                "content": "Intel Arc Deep Link requires Intel 12th/13th/14th gen CPU + Arc GPU for cross-device acceleration. Hyper Encode: CPU Quick Sync + GPU Arc combine for 2x AV1 encoding speed. Hyper Compute: Auto-distributes AI workloads (Stable Diffusion, Topaz AI) between iGPU + dGPU for 40% faster inference. Enable in Intel Arc Control > Preferences > Deep Link Technologies. Verify: Task Manager shows multi-GPU usage.",
                "keywords": ["Deep Link", "Hyper Encode", "multi-GPU"],
                "difficulty": "expert",
                "tags": ["productivity", "AI"],
                "related_tools": ["Intel Arc Control", "Task Manager"]
            },
            {
                "content": "Arc ray tracing performance optimization: DX12 Ultimate titles perform better than DXR 1.0/1.1. Arc A770 handles RT Medium settings 1440p60fps in Control, Metro Exodus Enhanced. Avoid RT Ultra - 50% fps loss vs Nvidia 4070. Combine RT Medium + XeSS Performance for 1440p balanced experience. Enable in-game shader caching and run built-in benchmarks twice (first run compiles shaders).",
                "keywords": ["ray tracing", "DXR", "optimization"],
                "difficulty": "intermediate",
                "tags": ["gaming", "graphics"],
                "related_tools": ["Game settings"]
            },
            {
                "content": "Arc GPU VRAM allocation tuning for 16GB A770: Intel Arc Control > Gaming > Per-Game Settings. For VRAM-hungry titles (Hogwarts Legacy, Last of Us), set Max VRAM = 15GB (leave 1GB headroom). Monitor with GPU-Z: Memory Controller Load. If >95% sustained, reduce texture quality one notch. Arc's GDDR6 bandwidth (512-560 GB/s) can bottleneck before VRAM fills, watch for 'GPU Memory' spike.",
                "keywords": ["VRAM management", "Arc A770", "texture settings"],
                "difficulty": "advanced",
                "tags": ["optimization", "troubleshooting"],
                "related_tools": ["Intel Arc Control", "GPU-Z"]
            },
            {
                "content": "Arc A-series power connector stability: A770 LE uses 2x 8-pin, A750 uses 1x 8+6pin. Avoid daisy-chained cables - use separate PCIe cables from PSU for each connector. Unstable power causes driver timeouts, black screens. Quality PSU required: 650W+ (80+ Gold) for A750, 750W+ for A770. Test stability: FurMark 15min, HWiNFO64 monitoring 12V rail (should stay 11.8V-12.2V under load).",
                "keywords": ["power delivery", "PSU", "stability"],
                "difficulty": "intermediate",
                "tags": ["hardware", "troubleshooting"],
                "related_tools": ["HWiNFO64", "FurMark"]
            },
            {
                "content": "Intel Arc Control per-game profiles: Create game-specific settings instead of global. Example: Competitive FPS > Max Performance mode + VSync off + Low latency on. Productivity apps > Balanced mode + Panel Self Refresh on. Change per-game: Arc Control > Gaming > Add Game > Performance Settings. Saves power when multitasking, prevents background GPU boost waste. Profiles auto-switch on app focus.",
                "keywords": ["game profiles", "power management", "optimization"],
                "difficulty": "beginner",
                "tags": ["gaming", "productivity"],
                "related_tools": ["Intel Arc Control"]
            },
            {
                "content": "Arc GPU DirectX 9 performance fix: Legacy DX9 games run through Microsoft D3D9On12 translation layer with 15-30% overhead. Workaround: Use DXVK wrapper (translates DX9→Vulkan) for 2x+ improvement. Download dxvk-2.3, copy d3d9.dll to game folder. Example: CS:GO 180fps native DX9 → 320fps DXVK. Verify: Check game uses Vulkan renderer in logs. Works: Skyrim, Fallout 3, older Source games.",
                "keywords": ["DirectX 9", "DXVK", "compatibility"],
                "difficulty": "advanced",
                "tags": ["gaming", "compatibility"],
                "related_tools": ["DXVK"]
            },
            {
                "content": "Arc A770 thermal pad mod for GDDR6 cooling: Factory pads sometimes insufficient, causing VRAM thermal throttling at 95°C+. Replace with Thermalright Odyssey 1.5mm pads (12.8 W/mK) on memory chips, 3mm on VRM. Reduces VRAM temps 15-20°C (95°C→78°C). Check before: HWiNFO64 'GPU Memory Junction Temperature'. After: sustained high-memory workloads (Furmark, mining) stay <85°C. Voids warranty - assess risk.",
                "keywords": ["thermal pads", "VRAM cooling", "hardware mod"],
                "difficulty": "expert",
                "tags": ["hardware", "cooling"],
                "related_tools": ["HWiNFO64", "Thermal pads"]
            },
            {
                "content": "Intel Arc command center vs legacy control panel: Arc Control (modern UWP app) offers per-game profiles, XeSS settings, performance monitoring. Graphics Command Center (legacy) has advanced color controls, multi-display Mosaic, custom resolutions. Install both: Arc Control for gaming, GCC for professional displays. Access custom resolutions: GCC > Display > Custom Resolutions > Add (useful for 1440p 165Hz monitors with DP 1.4 compression).",
                "keywords": ["Arc Control", "Graphics Command Center", "display settings"],
                "difficulty": "intermediate",
                "tags": ["configuration", "display"],
                "related_tools": ["Intel Arc Control", "Intel GCC"]
            },
            {
                "content": "Arc GPU PCIe 4.0 bandwidth requirements: A770 needs x16 PCIe 4.0 or minimum x8 for full performance. Running x8 3.0 loses 5-10% in 4K/high-texture scenarios. Check: GPU-Z > Bus Interface shows 'PCIe 4.0 x16 @ x16'. If @x8, verify: BIOS slot config, no M.2 drives stealing lanes (some boards share PCIe lanes). Render test: 3DMark Port Royal x16 vs x8 should be <3% variance.",
                "keywords": ["PCIe bandwidth", "bottleneck", "lanes"],
                "difficulty": "advanced",
                "tags": ["hardware", "performance"],
                "related_tools": ["GPU-Z", "3DMark"]
            },
            {
                "content": "Arc A-series multi-monitor optimization: Intel Xe Display Engine supports 4x 8K60Hz or 8x 4K60Hz simultaneous. For productivity: Enable Panel Self Refresh (PSR) in Arc Control to save 5-10W idle power per display. Mixed refresh setups (144Hz gaming + 60Hz secondary): Set 'Use advanced GPU scheduling' in Windows Graphics Settings to prevent stuttering. DP 2.0 on A770 enables 4K 240Hz with DSC compression.",
                "keywords": ["multi-monitor", "Display Engine", "Panel Self Refresh"],
                "difficulty": "intermediate",
                "tags": ["display", "productivity"],
                "related_tools": ["Intel Arc Control", "Windows Settings"]
            },
            {
                "content": "Arc GPU compatibility with older systems: Requires UEFI/UEFI-CSM (not Legacy BIOS), PCIe 3.0+ slot, Windows 10 64-bit 20H1 (build 19041)+. No Windows 7 support. For older Intel platforms (Z170, Z270), update BIOS for ReBAR support - check manufacturer website. AMD Ryzen 3000+ platforms work well. Avoid pre-2015 motherboards - often lack UEFI GOP drivers. Test boot: If POST fails, disable CSM in BIOS, enable UEFI-only mode.",
                "keywords": ["compatibility", "UEFI", "legacy systems"],
                "difficulty": "intermediate",
                "tags": ["hardware", "troubleshooting"],
                "related_tools": ["BIOS"]
            },
            {
                "content": "Arc GPU AI acceleration for local models: Intel XMX cores (Xe Matrix Extensions) accelerate INT8/FP16 inference. Stable Diffusion Web UI: Use --use-ipex flag for Intel optimization, 40% faster vs base PyTorch. LLama.cpp: Build with SYCL backend for Arc acceleration. A770 16GB handles 13B parameter models at 15-20 tokens/sec (vs CPU 3-5 t/s). Install Intel Extension for PyTorch (IPEX) 2.1+ for framework support.",
                "keywords": ["AI acceleration", "XMX", "Stable Diffusion"],
                "difficulty": "expert",
                "tags": ["AI", "machine learning"],
                "related_tools": ["PyTorch", "IPEX", "Stable Diffusion"]
            },
            {
                "content": "Arc GPU fan curve optimization: Intel Arc Control > Performance > Fan > Custom Curve. Default: 0% until 60°C (silent), ramps to 100% at 85°C (loud). Optimized curve: 30% base, 50% @ 65°C, 75% @ 75°C, 100% @ 80°C. Prevents thermal cycling, maintains quieter operation, keeps temps 70-75°C gaming. A770 LE Limited Edition has better cooler (stays <70°C), custom models vary widely (ASRock has weaker cooling +8°C vs reference).",
                "keywords": ["fan curve", "cooling", "acoustics"],
                "difficulty": "beginner",
                "tags": ["cooling", "optimization"],
                "related_tools": ["Intel Arc Control"]
            },
            {
                "content": "Arc GPU video memory error correction: Arc A750/A770 use non-ECC GDDR6, but driver includes software error detection. Monitor stability: HWiNFO64 > GPU Memory Errors counter. Non-zero values after gaming/rendering indicate: overclocked VRAM instability, failing memory chips, or thermal issues. If errors appear: reduce VRAM overclock, improve case airflow, check thermal pad contact. Consistent errors = RMA candidate (likely hardware defect).",
                "keywords": ["memory errors", "stability", "diagnostics"],
                "difficulty": "advanced",
                "tags": ["troubleshooting", "hardware"],
                "related_tools": ["HWiNFO64"]
            },
            {
                "content": "Intel Arc Alchemist mesh shader support: Full DX12 Ultimate mesh shaders via hardware acceleration in Xe-HPG architecture. Games supporting mesh shaders (Resident Evil Village, Alan Wake 2) get 10-15% better geometry performance on Arc vs older GPUs. Enable: Automatic in DX12 mode. Developer note: oneAPI rendering toolkit supports mesh shader development with Arc-optimized samples. Future-proof feature as more UE5 games adopt Nanite-like systems.",
                "keywords": ["mesh shaders", "DX12 Ultimate", "Xe-HPG"],
                "difficulty": "expert",
                "tags": ["graphics", "API"],
                "related_tools": ["DX12"]
            }
        ])
        print(f"[OK] gpu_intel_arc: {before} -> {len(kb['gpu_intel_arc']['tips'])} tips (+{len(kb['gpu_intel_arc']['tips']) - before})")

    # ========================================================================
    # CPU OVERCLOCKING ADVANCED
    # ========================================================================

    if "cpu_overclocking_advanced" in kb:
        before = len(kb["cpu_overclocking_advanced"]["tips"])
        kb["cpu_overclocking_advanced"]["tips"].extend([
            {
                "content": "Intel 13900K/14900K SP (Silicon Prediction) rating determines OC potential. Check via HWiNFO64 or BIOS 'CPU Bin' value: SP 70-79 = average, 80-89 = good, 90-100 = golden. Golden chips hit 5.8GHz all-core @ 1.35V, average needs 1.42V for same. SP rating calculated from VF (Voltage-Frequency) curves at factory test. Use this to set realistic voltage targets - low SP chips can't safely match high-end guides without degradation.",
                "keywords": ["silicon prediction", "SP rating", "binning"],
                "difficulty": "expert",
                "tags": ["overclocking", "intel"],
                "related_tools": ["HWiNFO64", "BIOS"]
            },
            {
                "content": "AMD Ryzen 7000X3D undervolting via Curve Optimizer: BIOS > PBO > Curve Optimizer > All Cores -30. 7800X3D example: stock 1.35V → CO -30 = 1.25V effective, same performance, temps drop 8-12°C (89°C→78°C). X3D CPUs can't overclock but CO improves V-Cache thermals. Test stability: CoreCycler 12hr, OCCT AVX2 1hr. Unstable = reduce to -25 or -20. Best cooling gains without losing AMD's boost algorithms.",
                "keywords": ["Curve Optimizer", "X3D", "undervolting"],
                "difficulty": "advanced",
                "tags": ["AMD", "optimization"],
                "related_tools": ["BIOS", "CoreCycler", "OCCT"]
            },
            {
                "content": "LLC (Load Line Calibration) levels prevent Vdroop: Under load, CPU voltage drops from BIOS-set value. Example: Set 1.35V → reads 1.28V under load (Vdroop). LLC compensates: Level 1 (low) = max droop, Level 7 (high) = overshoot. Optimal: Mid-LLC (4-5 on Asus) provides 0.02-0.04V droop - prevents voltage spikes damaging VRM, maintains stability. Monitor: HWiNFO64 'CPU Core Voltage (SVI2 TFN)' idle vs load delta <0.06V ideal.",
                "keywords": ["LLC", "Vdroop", "load line calibration"],
                "difficulty": "expert",
                "tags": ["overclocking", "voltage"],
                "related_tools": ["HWiNFO64", "BIOS"]
            },
            {
                "content": "Per-core overclocking for hybrid architectures: Intel 12th/13th/14th gen has P-cores + E-cores needing different voltages. BIOS: Set P-cores 5.6GHz @ 1.38V, E-cores 4.3GHz @ 1.25V independently. Use Asus 'AI OC' or MSI 'OC Explorer' for per-core tuning. Gaming workloads: Disable E-cores in Windows > System > System Information > Advanced > Processor Scheduling (improves 1% lows, reduces latency). Productivity: Keep E-cores for multithreading efficiency.",
                "keywords": ["per-core OC", "P-cores", "E-cores", "hybrid"],
                "difficulty": "expert",
                "tags": ["intel", "overclocking"],
                "related_tools": ["BIOS", "Windows Settings"]
            },
            {
                "content": "AVX offset protects CPU from AVX workload voltage spikes: Prime95 AVX2 draws 30-40% more current than non-AVX loads. Set AVX offset -2 to -4 (reduces multiplier during AVX): 5.5GHz normal becomes 5.3GHz AVX (-2 offset). Prevents thermal throttling, allows higher base OC. BIOS > CPU Config > AVX Offset. Monitor: HWiNFO64 shows multiplier drop during Blender renders, Handbrake encodes. Non-AVX gaming stays at max OC.",
                "keywords": ["AVX offset", "AVX2", "voltage protection"],
                "difficulty": "advanced",
                "tags": ["overclocking", "stability"],
                "related_tools": ["BIOS", "HWiNFO64"]
            },
            {
                "content": "CPU ring/cache overclocking scales performance: Ring ratio (Uncore) handles L3 cache, memory controller. Intel: Sync ring to core ratio (5.5GHz core = 5.5GHz ring) for best latency, or -300MHz offset for stability (5.5GHz core + 5.2GHz ring). AMD: Infinity Fabric = half RAM speed (DDR5-6000 = 3000MHz FCLK). Test: AIDA64 Cache benchmark - higher ring improves L3 bandwidth 10-20%. Unstable ring causes WHEA errors in Event Viewer.",
                "keywords": ["ring ratio", "cache OC", "uncore", "FCLK"],
                "difficulty": "expert",
                "tags": ["overclocking", "latency"],
                "related_tools": ["BIOS", "AIDA64"]
            },
            {
                "content": "VRM thermal management for sustained overclocking: High-end OC (5.7GHz+ Intel, 5.5GHz+ AMD) generates 250-350W CPU power, VRM handles 400W+ input. Monitor VRM temps: HWiNFO64 'VR MOS' sensors (should stay <100°C). If >110°C, add 40mm fan aimed at VRM heatsinks. Motherboard tier list: Tier S (18-stage 90A MOSFETs) handles 350W sustained, Tier B (12-stage 60A) only 200W before throttling. Use Buildzoid's VRM tier lists.",
                "keywords": ["VRM", "power delivery", "thermal throttling"],
                "difficulty": "advanced",
                "tags": ["cooling", "hardware"],
                "related_tools": ["HWiNFO64", "VRM tier lists"]
            },
            {
                "content": "BIOS microcode updates fix CPU vulnerabilities but reduce OC: Spectre/Meltdown/Downfall patches impose performance penalties 2-8%. Check current microcode: CPU-Z > Instructions. Update via BIOS flash or Windows Update. Post-update: Re-test stability (previous OC may become unstable), re-benchmark (performance may drop 3-5%). Trade-off decision: keep old BIOS for maximum OC (security risk) vs update for patches (lose 100-200MHz potential).",
                "keywords": ["microcode", "security patches", "BIOS updates"],
                "difficulty": "intermediate",
                "tags": ["bios", "security"],
                "related_tools": ["CPU-Z", "BIOS"]
            },
            {
                "content": "Adaptive vs Override voltage modes: Override (fixed 1.35V) maintains constant voltage - simpler, higher idle power. Adaptive (1.35V under load, drops idle) saves power, prevents degradation, but complex setup. BIOS: Adaptive Mode + Offset 0.001V + Turbo voltage 1.350V. Test: HWiNFO64 shows voltage scales 0.8V idle → 1.35V load. Adaptive can cause instability if motherboard voltage regulation poorly implemented (Gigabyte better than ASRock here).",
                "keywords": ["adaptive voltage", "override mode", "voltage modes"],
                "difficulty": "expert",
                "tags": ["overclocking", "power management"],
                "related_tools": ["BIOS", "HWiNFO64"]
            },
            {
                "content": "CPU degradation monitoring: Long-term high voltage (>1.45V Intel, >1.40V AMD) causes electron migration degradation. Symptoms: previously stable OC becomes unstable after 6-12 months, requires +0.02-0.05V for same frequency. Track: Excel log of voltage/frequency pairs monthly. Test with same workload: y-cruncher 2.5B digits. If voltage needs creep >0.05V in year, degradation occurring. Safe limits: Intel ≤1.40V 24/7, AMD ≤1.35V to minimize degradation over 3-5yr lifespan.",
                "keywords": ["degradation", "electron migration", "safe voltages"],
                "difficulty": "expert",
                "tags": ["overclocking", "longevity"],
                "related_tools": ["y-cruncher", "Excel"]
            },
            {
                "content": "BIOS training procedures for stable OC: After changing CPU/RAM settings, full training required. Process: Clear CMOS, set XMP/EXPO, set CPU OC, save, shutdown 30sec, cold boot. First boot takes 2-5min (memory training). If training fails (loops 3+ times), settings too aggressive. Advanced: ASUS 'Memory Try It!' pre-tested profiles skip manual training. Save stable profile to BIOS slot, backup with USB 'Save to File' for disaster recovery.",
                "keywords": ["BIOS training", "memory training", "cold boot"],
                "difficulty": "intermediate",
                "tags": ["bios", "stability"],
                "related_tools": ["BIOS"]
            },
            {
                "content": "Intel Thermal Velocity Boost (TVB) vs manual OC: TVB adds +100-200MHz when temps <70°C. Manual all-core OC disables TVB, losing single-thread boost. Hybrid approach: Enable TVB + negative AVX offset + undervolt for best of both worlds. Example: 13900K stock TVB hits 5.8GHz single-thread, 5.5GHz all-core manual OC provides better multi-threaded but loses 5.8GHz peaks. For gaming: TVB preferred. For rendering: manual all-core wins. Check HWiNFO64 'Effective Clock' to see actual frequencies.",
                "keywords": ["TVB", "Thermal Velocity Boost", "boost algorithms"],
                "difficulty": "advanced",
                "tags": ["intel", "overclocking"],
                "related_tools": ["HWiNFO64", "BIOS"]
            },
            {
                "content": "AMD PBO2 (Precision Boost Overdrive 2) advanced tuning: BIOS > AMD Overclocking > PBO Limits = Motherboard, Scalar = 10X, Curve Optimizer = Per-Core (test each core). Ryzen 9 7950X example: CCD0 cores -30, CCD1 cores -20 (different silicon quality per chiplet). Max boost improves 100-200MHz (5.7GHz → 5.85GHz single-core). Test per-core: CoreCycler isolates failing cores. Power limits: PPT 230W, TDC 160A, EDC 180A for max performance on good cooling.",
                "keywords": ["PBO2", "Precision Boost", "per-core tuning"],
                "difficulty": "expert",
                "tags": ["AMD", "overclocking"],
                "related_tools": ["BIOS", "CoreCycler"]
            },
            {
                "content": "Delid and liquid metal application for extreme cooling: Intel CPUs use cheap TIM (thermal paste) between die and IHS (integrated heat spreader). Delid with Rockit Cool kit, replace with Thermal Grizzly Conductonaut (liquid metal). Temp reduction: 15-25°C at same frequency (9900K: 85°C → 62°C @ 5.0GHz). Enables extra 200-300MHz OC headroom. CRITICAL: Liquid metal eats aluminum (use nickel-plated coolers only), practice delid on dead CPU first. Voids warranty immediately.",
                "keywords": ["delid", "liquid metal", "IHS"],
                "difficulty": "expert",
                "tags": ["cooling", "hardware mod"],
                "related_tools": ["Rockit Cool", "Thermal Grizzly"]
            },
            {
                "content": "CPU cooler mounting pressure affects temps: Too tight warps IHS, too loose loses contact. Optimal: Tighten screws diagonal pattern, 50-75% finger strength, stop when slight resistance. Test: Run OCCT 10min, check HWiNFO64 'Core Temp' delta between cores. >8°C variance = uneven pressure, remount. Thermal paste application: Pea-sized dot center of IHS, cooler pressure spreads evenly. Avoid X-pattern or full-spread (traps air bubbles). Re-paste yearly for best performance.",
                "keywords": ["cooler mounting", "thermal paste", "contact pressure"],
                "difficulty": "intermediate",
                "tags": ["cooling", "installation"],
                "related_tools": ["HWiNFO64", "Thermal paste"]
            },
            {
                "content": "Windows power plan impacts overclocking stability: 'High Performance' keeps cores at max frequency (good for benchmarking, wastes power). 'Balanced' allows C-states (CPU idle states) which can conflict with OC. Best: 'Ryzen Balanced' (AMD) or 'Ultimate Performance' (Intel - hidden, enable via powercfg -duplicatescheme e9a42b02-d5df-448d-aa00-03f14749eb61). Disable C-states in BIOS for absolute stability but +20-40W idle power draw. Enable C-states for efficiency but test stability thoroughly.",
                "keywords": ["power plan", "C-states", "CPU states"],
                "difficulty": "intermediate",
                "tags": ["windows", "power management"],
                "related_tools": ["Windows Settings", "BIOS"]
            },
            {
                "content": "Extreme overclocking with chilled water or LN2: Sub-ambient cooling enables 6.0GHz+ frequencies. Chilled water (10°C): Custom loop with TEC (thermoelectric cooler) or phase-change chiller. LN2 (liquid nitrogen -196°C): Requires insulated pot, petroleum jelly barriers against condensation. 14900K world records: 9.1GHz single-core LN2, 6.2GHz 8-core chilled water. CRITICAL: Condensation shorts motherboard, insulate socket/VRM/RAM with clear nail polish or dielectric grease. Extreme voltages (1.7V+) degrade CPU in hours - for benchmarking only.",
                "keywords": ["LN2", "extreme OC", "sub-ambient"],
                "difficulty": "expert",
                "tags": ["extreme overclocking", "cooling"],
                "related_tools": ["LN2 pot", "Phase-change"]
            },
            {
                "content": "Memory controller stability affects CPU overclocking: RAM OC stresses IMC (integrated memory controller) inside CPU. Running DDR5-7200+ on Intel 13th/14th gen requires SA (System Agent) voltage +0.05V (1.25V → 1.30V), VDDQ +0.05V. Symptoms of IMC instability: random reboots, WHEA errors, memory training failures. Test IMC: TM5 with Anta777 Extreme config 3 cycles. If fails: increase SA voltage +0.02V steps to max 1.40V. Poor IMC silicon can't handle DDR5-7000+ regardless of RAM quality.",
                "keywords": ["IMC", "System Agent", "memory controller"],
                "difficulty": "expert",
                "tags": ["overclocking", "memory"],
                "related_tools": ["TM5", "BIOS"]
            },
            {
                "content": "Stability testing hierarchy for OC validation: Level 1 (5min): Cinebench R23 - catches gross instability. Level 2 (1hr): OCCT AVX2 Medium - stresses voltage regulation. Level 3 (12hr): Prime95 Small FFT - maximum heat/power. Level 4 (24hr): y-cruncher Component Stress Tester - catches rare edge cases. Daily OC: Pass Level 2. 24/7 OC: Pass Level 3. Mission-critical: Pass Level 4. Gaming-only: Can skip Prime95 (unrealistic AVX stress), use Realbench 4hr instead.",
                "keywords": ["stability testing", "stress testing", "validation"],
                "difficulty": "intermediate",
                "tags": ["testing", "stability"],
                "related_tools": ["Cinebench", "OCCT", "Prime95", "y-cruncher"]
            },
            {
                "content": "BIOS failsafe features prevent brick: Modern boards have dual BIOS (backup chip), Safe Boot (auto-resets OC after 3 failed boots), BIOS flashback (recover from USB without CPU). Learn your board's recovery: Asus = Hold MemOK! 3sec, MSI = Flash BIOS button + USB, Gigabyte = Dual BIOS auto-switches. Test recovery procedure before extreme OC attempts. Keep stable BIOS profile saved to USB. Remove AC power 30sec before CMOS reset to fully discharge capacitors.",
                "keywords": ["BIOS recovery", "dual BIOS", "failsafe"],
                "difficulty": "beginner",
                "tags": ["bios", "safety"],
                "related_tools": ["BIOS", "USB drive"]
            }
        ])
        print(f"[OK] cpu_overclocking_advanced: {before} -> {len(kb['cpu_overclocking_advanced']['tips'])} tips (+{len(kb['cpu_overclocking_advanced']['tips']) - before})")

    # ========================================================================
    # RAM OVERCLOCKING TIGHTENING
    # ========================================================================

    if "ram_overclocking_tightening" in kb:
        before = len(kb["ram_overclocking_tightening"]["tips"])
        kb["ram_overclocking_tightening"]["tips"].extend([
            {
                "content": "DDR5 primary timings impact performance non-linearly: tCL (CAS Latency), tRCD (RAS to CAS Delay), tRP (RAS Precharge). Stock DDR5-6000 CL36-36-36 @ 1.35V. Samsung B-die equivalent (Hynix A-die DDR5): 6400 CL32-38-38 @ 1.40V (+15% bandwidth, -8% latency vs stock). Tighten tCL first (biggest impact), then tRP, then tRCD. Test each: TM5 Anta777 config 1 cycle. Gains: AIDA64 latency 70ns → 63ns, gaming 1% lows +8-12fps.",
                "keywords": ["primary timings", "CAS latency", "DDR5"],
                "difficulty": "advanced",
                "tags": ["memory", "overclocking"],
                "related_tools": ["TM5", "AIDA64", "BIOS"]
            },
            {
                "content": "Secondary timings for advanced tuning: tRFC (Refresh Cycle Time) most impactful - lower = better performance. DDR5-6000 default tRFC 560ns, optimal 420-460ns depending on chip density. tRRD_S/L (Row to Row Delay Short/Long): reduce to 4/6 from 8/12. tFAW (Four Activate Window): lower to 16 from 32. Test each timing individually, combine stable values. Monitor: HWiNFO64 'Memory Errors'. Single error = instability, increase failed timing +1. Profile: save stable config to BIOS slot before continuing.",
                "keywords": ["secondary timings", "tRFC", "tRRD"],
                "difficulty": "expert",
                "tags": ["memory", "overclocking"],
                "related_tools": ["BIOS", "HWiNFO64", "TM5"]
            },
            {
                "content": "DDR4 Samsung B-die identification and tuning: B-die = best DDR4 overclocking IC. Identify: Thaiphoon Burner reads SPD chip data. Indicators: 3200MHz CL14, 3600MHz CL16, or 4000MHz CL19 XMP profiles often B-die. Optimal tune: 3800MHz CL14-15-15-28 @ 1.50V (Intel), 3800MHz CL16-16-16-32 @ 1.45V (AMD safe FCLK 1900MHz). Requires good IMC, 1.45-1.50V VDIMM safe for B-die long-term. Reference: GitHub DDR4 OC Guide has complete B-die tuning profiles.",
                "keywords": ["B-die", "Samsung", "DDR4 OC"],
                "difficulty": "expert",
                "tags": ["memory", "DDR4"],
                "related_tools": ["Thaiphoon Burner", "BIOS"]
            },
            {
                "content": "VDDQ and VDD2 voltage tuning for DDR5: VDDQ powers I/O, VDD2 powers die core. Stock: 1.10V VDDQ, 1.10V VDD2. Overclocking DDR5-7000+: increase VDDQ 1.35-1.40V, VDD2 1.25-1.30V. Some kits need split voltages (VDDQ 1.40V + VDD2 1.25V). Monitor temps: DIMMs with temp sensor should stay <55°C. Active cooling (40mm fan) required above 1.40V. ASUS: BIOS > DRAM Voltage Control. Test: Karhu RAM Test 6000%+ coverage. Wrong voltage ratio causes errors despite 'enough' voltage.",
                "keywords": ["VDDQ", "VDD2", "DDR5 voltage"],
                "difficulty": "expert",
                "tags": ["voltage", "DDR5"],
                "related_tools": ["BIOS", "Karhu RAM Test"]
            },
            {
                "content": "Gear modes and memory dividers: Intel DDR5 Gear 2 = memory frequency ÷ 2 for memory controller (DDR5-6400 = 3200MHz controller). Gear 1 = 1:1 ratio (lower latency, harder to stabilize). Optimal: DDR5-6000 Gear 2 for stability, or DDR5-5600 Gear 1 for lower latency (depends on use case). AMD: UCLK = MCLK = FCLK 1:1:1 ratio ideal (DDR5-6000 = 3000MHz FCLK). Test: AIDA64 memory latency - Gear 1 can be 3-5ns lower despite slower frequency. Balance: Gear 2 6400MHz vs Gear 1 5600MHz depends on IMC quality.",
                "keywords": ["gear mode", "memory divider", "FCLK"],
                "difficulty": "advanced",
                "tags": ["memory", "latency"],
                "related_tools": ["BIOS", "AIDA64"]
            },
            {
                "content": "Tertiary timings granular tuning: tREFI (Refresh Interval) default 65535, safe range 32768-65535 (lower = more stable in heat, higher = better performance). tRDRD_sg/dg/dr/dd (Read to Read delays): minimize to 4-6 depending on board topology. tWRWR variants: similar tuning. tRDWR (Read to Write): tight as possible, typically 8-12. Manual entry in BIOS tertiary timings section. Use DRAM Calculator for Ryzen as reference baseline, adjust per-stick. Test: TM5 Absolut config overnight.",
                "keywords": ["tertiary timings", "tREFI", "granular tuning"],
                "difficulty": "expert",
                "tags": ["memory", "advanced"],
                "related_tools": ["DRAM Calculator", "TM5", "BIOS"]
            },
            {
                "content": "Single-rank vs dual-rank performance impact: Dual-rank (2Rx8) provides 5-10% better performance via rank interleaving but harder to overclock high frequencies. 2x 16GB dual-rank = hardest on IMC. 4x 8GB single-rank = easier to hit DDR5-7000+. Check: CPU-Z SPD tab shows rank config. Optimal: 2x 16GB dual-rank DDR5-6000 CL30 (best price/performance), or 2x 24GB (newer, sometimes single-rank despite capacity). 4-DIMM configs limit max frequency -400 to -800MHz vs 2-DIMM.",
                "keywords": ["rank", "dual-rank", "single-rank", "interleaving"],
                "difficulty": "intermediate",
                "tags": ["memory", "configuration"],
                "related_tools": ["CPU-Z", "BIOS"]
            },
            {
                "content": "Memory training customization in BIOS: RTL/IOL (Round Trip Latency / IO Latency) values auto-trained but can manually optimize. ASUS: Mem Tweak Mode = 1, manually set RTL = tCL + 8-12 (varies by board). MSI: Advanced DRAM Config > Fast Boot = Disabled for retraining each boot (slower POST, better stability testing). Gigabyte: Profile Mismatching = Enabled allows mixing XMP kits (not recommended but works). Save stable auto-trained values before manual tuning.",
                "keywords": ["memory training", "RTL", "IOL"],
                "difficulty": "expert",
                "tags": ["memory", "BIOS"],
                "related_tools": ["BIOS"]
            },
            {
                "content": "RAM overclocking with integrated graphics: iGPU shares system RAM, sensitive to instability. Intel HD/UHD or AMD Radeon Graphics: memory errors cause artifacts, driver crashes. Test: Unigine Heaven with iGPU while running TM5 simultaneously (dual stress). If crashes only during iGPU load, increase VDDQ +0.02V or loosen tRCD. Dedicated GPU users can ignore iGPU stability, but professional workstation users transcoding via Quick Sync need perfect stability.",
                "keywords": ["iGPU", "shared memory", "stability"],
                "difficulty": "advanced",
                "tags": ["memory", "graphics"],
                "related_tools": ["TM5", "Unigine"]
            },
            {
                "content": "Command rate (CR) impact on performance: CR 1T = one command per clock (fast), CR 2T = one command per two clocks (easier stability). DDR4: 1T possible with 2-DIMM, 2T required for 4-DIMM usually. DDR5: Gear 2 default 2T, Gear 1 requires 2T most configurations. Performance: 1T gives 2-4% latency improvement. If unstable at 1T: increase tRCD +2, or accept 2T. BIOS: Command Rate setting under DRAM Timing Control. Test: Check Event Viewer for WHEA errors after switching to 1T.",
                "keywords": ["command rate", "1T", "2T"],
                "difficulty": "intermediate",
                "tags": ["memory", "latency"],
                "related_tools": ["BIOS", "Event Viewer"]
            },
            {
                "content": "Temperature impact on RAM stability: DDR5 rated 0-85°C but performance degrades >60°C (timings auto-loosen, errors increase). Active cooling: 40mm fan blowing on DIMMs keeps <45°C under load. Passive heatspreaders help 5-10°C. Monitor: HWiNFO64 'DIMM Temperature' sensor (if equipped). High ambient (summer 30°C+ room): may need loosen timings or reduce voltage vs winter stable config. Critical for 1.45V+ setups which generate significant heat. RGB RAM runs 5°C hotter due to RGB controller power draw.",
                "keywords": ["RAM temperature", "cooling", "thermal stability"],
                "difficulty": "intermediate",
                "tags": ["cooling", "memory"],
                "related_tools": ["HWiNFO64", "Case fans"]
            },
            {
                "content": "XMP/EXPO profiles as overclocking baseline: XMP (Intel) and EXPO (AMD) are manufacturer-tested profiles, not guaranteed stable on all systems. Process: Enable XMP, boot, test stability. If unstable: increase VDIMM +0.05V, loosen tCL +2, or lower frequency -200MHz. Some boards 'ASUS OC Profile' or 'MSI Memory Try It!' offer alternative timings for same frequency. Never mix XMP kits (different ICs, subtimings conflict). For manual OC: use XMP as starting point, adjust from there.",
                "keywords": ["XMP", "EXPO", "profiles"],
                "difficulty": "beginner",
                "tags": ["memory", "overclocking"],
                "related_tools": ["BIOS"]
            },
            {
                "content": "tRFC optimization calculator method: tRFC (nanoseconds) = (tRFC_value / Memory_Frequency_MHz) × 2000. Example: tRFC 560 @ DDR5-6000 = (560/6000)×2000 = 187ns. Optimal range: 180-220ns depending on IC type. Hynix M-die: 200-220ns safe. Samsung B-die (DDR5): 180-200ns possible. Test: reduce tRFC -20 steps until TM5 errors, add +40 for safety margin. Performance gain: 560→420 tRFC improves AIDA64 read speed 10-15%, latency -2ns. Biggest single timing for performance gains.",
                "keywords": ["tRFC optimization", "nanoseconds", "calculation"],
                "difficulty": "advanced",
                "tags": ["memory", "optimization"],
                "related_tools": ["Calculator", "TM5", "AIDA64"]
            },
            {
                "content": "RAM disk topology and signal integrity: T-Topology (older boards): 4-DIMM configuration optimal, 2-DIMM may limit frequency. Daisy-Chain (modern): 2-DIMM optimal, 4-DIMM adds signal reflections limiting frequency. Check motherboard QVL (Qualified Vendor List) for tested RAM kits. Trace length impacts max frequency: Short traces (ITX boards) can hit DDR5-8000+, Long traces (EATX) limit DDR5-7200. Populated slots matter: A2/B2 (2nd/4th slots) preferred on daisy-chain boards for best signal integrity.",
                "keywords": ["topology", "daisy-chain", "T-topology", "signal integrity"],
                "difficulty": "expert",
                "tags": ["hardware", "memory"],
                "related_tools": ["Motherboard manual"]
            },
            {
                "content": "Per-stick tuning for mixed quality RAM: Even matched kits have variance. Test each stick individually: 1 DIMM A2 slot, TM5 6 cycles, note max stable frequency. Example: Stick 1 = DDR5-6600 stable, Stick 2 = DDR5-6400 stable. System limited by weakest stick, run 6400 both. Advanced: some BIOS allow per-DIMM voltage (rare), add +0.02V to weaker stick. Most cost-effective: sell weak stick, buy matched pair. Production binning variance causes 200-400MHz difference even in 'matched' kits from same box.",
                "keywords": ["per-stick testing", "binning variance"],
                "difficulty": "advanced",
                "tags": ["memory", "troubleshooting"],
                "related_tools": ["TM5", "BIOS"]
            },
            {
                "content": "Memory error types and diagnostics: WHEA errors (Windows Hardware Error Architecture) in Event Viewer indicate CPU-RAM instability. 'Bus/Interconnect Error' = IMC voltage too low. 'Cache Hierarchy Error' = CPU cache/ring unstable (increase ring voltage or reduce CPU OC). 'Memory Errors' = DRAM timing/voltage issue. Karhu RAM Test: Fast errors (<100%) = primary timings wrong, Late errors (>5000%) = secondary/tertiary timings marginal. TM5: Errors in test 0-4 = voltage, test 5-12 = timings. Use error patterns to guide adjustments.",
                "keywords": ["WHEA errors", "diagnostics", "error types"],
                "difficulty": "expert",
                "tags": ["troubleshooting", "memory"],
                "related_tools": ["Event Viewer", "Karhu", "TM5"]
            },
            {
                "content": "BIOS version impacts RAM compatibility: Newer BIOS updates improve memory training algorithms, add higher frequency support. Example: ASUS Z790 BIOS 0702 added DDR5-7600 support vs 0504 max DDR5-7200. Check manufacturer website for 'Improved memory compatibility' in changelog. Downside: newer BIOS may have bugs, conservative approach = use BIOS from 6-12 months ago (community-tested). Always backup current BIOS before updating. Flash via BIOS Flashback (safest) not Windows utilities.",
                "keywords": ["BIOS version", "memory compatibility", "training"],
                "difficulty": "intermediate",
                "tags": ["BIOS", "compatibility"],
                "related_tools": ["BIOS Flashback"]
            },
            {
                "content": "Subtimings impact on real-world performance: tWR (Write Recovery Time), tRTP (Read to Precharge), tWTR (Write to Read). Gaming: tWR and tWTR most impactful (affect read-after-write latency in game streaming scenarios). Productivity: tRTP improves database query speeds. Defaults: tWR 48, tRTP 12, tWTR_S/L 4/12. Optimized: tWR 24, tRTP 8, tWTR_S/L 2/6. Test specific: Civilization VI turn times improve 15-20% with tight tWR. Compile times improve 8-12% with tight tRTP. Application-specific tuning yields targeted gains.",
                "keywords": ["subtimings", "tWR", "tRTP", "tWTR"],
                "difficulty": "expert",
                "tags": ["memory", "optimization"],
                "related_tools": ["BIOS", "Benchmarks"]
            },
            {
                "content": "AMD EXPO vs manual tuning for Ryzen 7000: EXPO profiles optimize for AMD platform (includes VDDQ/VDD2 splits, optimized tRFC for Infinity Fabric). Manual tuning: Start EXPO, note voltages, adjust. Ryzen sweet spot: DDR5-6000 CL30 with FCLK 2000MHz 1:1 ratio (UCLK=MCLK=FCLK). Higher than DDR5-6400 often requires FCLK 2:1 mode (loses latency). Tune for latency not bandwidth: AIDA64 latency target <65ns. Use DRAM Calculator for Ryzen 'Safe' profile as reference, adjust per system. AMD systems more sensitive to memory tuning than Intel (direct IF connection).",
                "keywords": ["EXPO", "AMD", "Infinity Fabric", "Ryzen"],
                "difficulty": "advanced",
                "tags": ["AMD", "memory"],
                "related_tools": ["BIOS", "DRAM Calculator", "AIDA64"]
            },
            {
                "content": "Pro-level memory overclocking workflow: 1) Baseline: Boot stock, run AIDA64 + latency test for reference. 2) Enable XMP/EXPO, test TM5 3 cycles. 3) Increase frequency +200MHz, auto timings, test. 4) When frequency unstable, step back -200MHz. 5) Tighten primary timings -2 CL, test. 6) Optimize tRFC -40 steps until unstable, +40 back. 7) Tighten secondaries per guide. 8) Tertiary fine-tuning. 9) Voltage optimization (reduce while stable). 10) Final validation: TM5 Absolut 6 cycles + Karhu 10000%. Document: Excel sheet with voltage/timing combos. Time investment: 20-40 hours for fully optimized kit.",
                "keywords": ["workflow", "methodology", "optimization process"],
                "difficulty": "expert",
                "tags": ["memory", "overclocking"],
                "related_tools": ["TM5", "Karhu", "AIDA64", "BIOS", "Excel"]
            }
        ])
        print(f"[OK] ram_overclocking_tightening: {before} -> {len(kb['ram_overclocking_tightening']['tips'])} tips (+{len(kb['ram_overclocking_tightening']['tips']) - before})")

    # ========================================================================
    # GPU OVERCLOCKING CURVES
    # ========================================================================

    if "gpu_overclocking_curves" in kb:
        before = len(kb["gpu_overclocking_curves"]["tips"])
        kb["gpu_overclocking_curves"]["tips"].extend([
            {
                "content": "Nvidia voltage-frequency curve editor in MSI Afterburner: Press Ctrl+F to open curve, each point = voltage step (0.700V-1.100V in 0.012V increments). Stock RTX 4080: peaks 2820 MHz @ 1.050V. Optimal undervolt: find highest frequency at 0.925V (typically 2700 MHz), drag all points above 0.925V down to same level, apply. Stress test Port Royal 20min. Result: 2700 MHz locked, 50W less power (320W→270W), 8°C cooler, 96% performance of stock. Improves efficiency dramatically.",
                "keywords": ["voltage curve", "MSI Afterburner", "undervolt", "efficiency"],
                "difficulty": "advanced",
                "tags": ["gpu", "overclocking"],
                "related_tools": ["MSI Afterburner", "3DMark"]
            },
            {
                "content": "AMD Radeon voltage curve tuning via Radeon Software: Open Adrenalin > Performance > Tuning > Custom > Enable Undervolt GPU. RX 7900 XTX: Stock max 1.200V @ 2500 MHz. Reduce max frequency voltage: 1.100V limit, tune max frequency 2650 MHz. Test stability: Unigine Superposition 4K Optimized loop 1 hour. Modern RDNA3 benefits less from undervolting than Nvidia (5-8% power savings vs 15-20% Nvidia) but still worthwhile. Alternative: MorePowerTool for advanced voltage control, requires signed driver disable.",
                "keywords": ["AMD undervolt", "Radeon Software", "RDNA3"],
                "difficulty": "advanced",
                "tags": ["gpu", "AMD"],
                "related_tools": ["Radeon Software", "Unigine", "MorePowerTool"]
            },
            {
                "content": "Finding silicon quality via curve exploration: Methodology: Start at 0.850V point in curve, increase frequency +30MHz, test Heaven benchmark 5min loop. Continue until artifacts/crashes. Example results: RTX 3080 FE: 1815 MHz @ 0.850V (good), RTX 3080 TUF: 1890 MHz @ 0.850V (excellent). Document each voltage point's max frequency in Excel. High-quality silicon sustains 100+ MHz advantage across entire curve. Use data to determine if further pushing worthwhile or if chip is average/below.",
                "keywords": ["silicon lottery", "binning", "testing methodology"],
                "difficulty": "expert",
                "tags": ["overclocking", "testing"],
                "related_tools": ["MSI Afterburner", "Heaven", "Excel"]
            },
            {
                "content": "Multi-point curve optimization for variable workloads: Instead of flat curve, create stepped profile: Gaming (high FPS, medium loads) = 1950 MHz @ 0.900V. Productivity (sustained loads) = 1875 MHz @ 0.875V. Save as separate Afterburner profiles (Profile 1, Profile 2). Hotkey switching: Settings > General > Profile hotkeys (Ctrl+1, Ctrl+2). Auto-switch possible via third-party tools (Profile Scheduler). Allows max performance when needed, efficiency for background rendering/encoding. Manages thermals in small cases.",
                "keywords": ["multi-profile", "profile switching", "workload optimization"],
                "difficulty": "intermediate",
                "tags": ["optimization", "profiles"],
                "related_tools": ["MSI Afterburner"]
            },
            {
                "content": "Curve stability testing hierarchy: Quick test (5min): Heaven Benchmark 1080p Ultra loop - catches gross instability. Medium test (30min): 3DMark Port Royal / Time Spy Stress Test 20 loops - 97%+ pass required. Long test (2hr): Specific game with known stability issues (Red Dead Redemption 2, Cyberpunk 2077 RT Ultra) - catches real-world edge cases. Extended test (8hr): Overnight mining or Folding@Home - ultimate stability verification. Daily OC: pass medium test. 24/7: pass long test. Mission-critical rendering: pass extended.",
                "keywords": ["stability testing", "validation", "stress testing"],
                "difficulty": "intermediate",
                "tags": ["testing", "stability"],
                "related_tools": ["Heaven", "3DMark", "Games"]
            },
            {
                "content": "Power limit interaction with voltage curves: Nvidia Power Limit slider (50-106% typically) acts as power ceiling even with curve applied. Example: RTX 4090 @ 0.925V curve uses 380W, but 100% PL = 450W limit. Reduce PL to 85% (383W limit) for slight safety margin, or increase PL 106% for extra headroom during transient spikes. AMD: Power limit affects minimum voltage floor. Optimal: Set curve first, then adjust PL to match actual power draw +5% headroom. Monitor: HWiNFO64 'GPU Power' while gaming should be 5-10% below PL limit to prevent throttling.",
                "keywords": ["power limit", "PL", "throttling"],
                "difficulty": "advanced",
                "tags": ["power management", "overclocking"],
                "related_tools": ["MSI Afterburner", "HWiNFO64"]
            },
            {
                "content": "Memory clock optimization separate from core curve: GPU memory (GDDR6/GDDR6X) overclocks independently. Start: +0 MHz memory, optimize core curve first. Then: increase memory +100 MHz, test for artifacts (run VRAM-heavy game like Resident Evil Village 4K max textures). Continue +100 MHz until artifacts appear, reduce -200 MHz for safety. Typical gains: GDDR6X (RTX 4080) +1000-1400 MHz stable, GDDR6 (RX 7800 XT) +600-1000 MHz. Performance: +3-7% in 4K scenarios, minimal improvement 1080p (core-limited).",
                "keywords": ["memory overclock", "GDDR6X", "VRAM"],
                "difficulty": "intermediate",
                "tags": ["memory", "overclocking"],
                "related_tools": ["MSI Afterburner", "Games"]
            },
            {
                "content": "Temperature-dependent curve behavior: GPU Boost 3.0 (Nvidia) and Precision Boost (AMD) dynamically adjust frequency based on temperature. Every 10°C above 60°C = -15 to -30 MHz. Example: RTX 4070 Ti @ 65°C hits 2850 MHz, @ 75°C drops to 2790 MHz. Improve cooling (better fans, repaste, case airflow): target <70°C to maintain max boost. Aggressive fan curve: 60% @ 65°C, 80% @ 75°C, 100% @ 80°C. Acoustics trade-off: Custom deshroud + 120mm fans quieter than stock at same temps. Monitor: HWiNFO64 'GPU Temperature' + 'GPU Boost Clock' correlation.",
                "keywords": ["thermal throttling", "GPU Boost", "cooling"],
                "difficulty": "intermediate",
                "tags": ["cooling", "performance"],
                "related_tools": ["HWiNFO64", "MSI Afterburner"]
            },
            {
                "content": "BIOS modding for voltage unlock: Factory VBIOS limits maximum voltage (typically 1.070-1.100V Nvidia, 1.200V AMD). Advanced: Flash modified BIOS with higher limits (1.200V+ Nvidia) using NVFlash or ATIFlash. CRITICAL RISKS: Permanent damage if done wrong, voids warranty, potential brick. Research: TechPowerUp VBIOS database, overclock.net guides. Safer alternative: Soft Power Play Table mod (AMD) via MorePowerTool - no flash required. Only pursue for extreme overclocking (LN2, competitive benchmarking). Daily users: stick to software voltage limits (safer).",
                "keywords": ["BIOS mod", "VBIOS", "voltage unlock"],
                "difficulty": "expert",
                "tags": ["extreme overclocking", "hardware mod"],
                "related_tools": ["NVFlash", "MorePowerTool", "TechPowerUp"]
            },
            {
                "content": "Per-game curve profiles for optimal experience: Competitive FPS (Valorant, CS2): Max frequency curve, higher power draw acceptable for minimum latency. AAA single-player (Cyberpunk, Starfield): Balanced curve (0.925V sweet spot), save power/heat for sustained sessions. Ray tracing titles: Aggressive undervolt to manage RT core heat spike. Indie/older games: Heavy undervolt (saves power, GPU overkill anyway). Setup: Create named profiles in Afterburner, document which games use which profile. Switch manually or use automation (RivaTuner can detect .exe and auto-switch profiles).",
                "keywords": ["per-game profiles", "gaming optimization", "profile management"],
                "difficulty": "intermediate",
                "tags": ["gaming", "profiles"],
                "related_tools": ["MSI Afterburner", "RivaTuner"]
            },
            {
                "content": "Voltage curve artifacts diagnosis: Visual artifacts indicate type of instability. Black screen/driver crash = voltage too low for frequency, increase +0.012V or reduce frequency -30 MHz. Texture corruption/flickering = memory overclock too high, reduce mem -200 MHz. Screen tearing (Vsync off) = normal, not instability. Colored dots/sparkling = power delivery issue, check PCIe cables, reduce power limit. Systematic approach: Isolate core vs memory by testing separately (core curve + 0 mem OC, then stock core + mem OC). Document which artifact = which fix.",
                "keywords": ["artifacts", "troubleshooting", "instability"],
                "difficulty": "advanced",
                "tags": ["troubleshooting", "diagnostics"],
                "related_tools": ["MSI Afterburner"]
            },
            {
                "content": "OC Scanner automated curve optimization: Nvidia RTX 20/30/40 series: MSI Afterburner > OC Scanner button runs 20min automated voltage curve test. Algorithm tests each voltage point, finds max stable frequency, applies curve. Results: typically conservative (safety margin built in). Post-scan: manually adjust curve +15-30 MHz per point, re-test. Pros: good starting point for beginners. Cons: slower than manual tuning, may miss optimal configurations. Use case: Quick baseline before manual refinement. AMD equivalent: Auto-Undervolt in Radeon Software (less sophisticated).",
                "keywords": ["OC Scanner", "automated tuning", "Nvidia"],
                "difficulty": "beginner",
                "tags": ["automation", "overclocking"],
                "related_tools": ["MSI Afterburner"]
            },
            {
                "content": "Clock stretching detection and mitigation: Modern GPUs 'clock stretch' when unstable - report high frequency but reduce effective clocks to prevent crash. Symptom: frequency shows 2800 MHz in monitoring but performance drops 10-15%. Detection: 3DMark scores below expected, or frame pacing inconsistent (monitor frame times in RTSS). Fix: increase voltage +0.012V or reduce frequency -30 MHz. Validation: Compare 3DMark scores at different points - real 2700 MHz scores higher than stretched 2800 MHz. AMD RDNA2/3 especially prone, monitor GFX clock vs reported boost.",
                "keywords": ["clock stretching", "effective clocks", "instability"],
                "difficulty": "expert",
                "tags": ["troubleshooting", "performance"],
                "related_tools": ["3DMark", "RTSS", "HWiNFO64"]
            },
            {
                "content": "Custom fan curves for noise-optimized overclocking: GPU fans stock curves prioritize thermals over acoustics. Custom: 30% @ <60°C (silent idle), 50% @ 70°C, 70% @ 75°C, 90% @ 80°C, 100% @ 85°C (emergency). MSI Afterburner: Settings > Fan > Enable user defined software automatic fan control. Quality fans (high static pressure): Noctua NF-A12x25 deshroud mod provides better cooling at lower RPM vs stock. Target: <75°C gaming with <50% fan speed for silent experience. Balance: Undervolt curve + moderate fan curve = best noise/performance ratio.",
                "keywords": ["fan curve", "acoustics", "cooling optimization"],
                "difficulty": "beginner",
                "tags": ["cooling", "noise"],
                "related_tools": ["MSI Afterburner"]
            },
            {
                "content": "Precision X1 vs Afterburner for curve editing: MSI Afterburner: More popular, better RivaTuner integration, cross-vendor (works AMD). EVGA Precision X1: Nvidia-only, cleaner interface, per-voltage point frequency adjustment easier. Feature comparison: Both have curve editor, profiles, fan control. Afterburner advantage: RTSS on-screen display, wider compatibility. Precision advantage: Voltage-frequency locking more intuitive. Recommendation: Try both, use whichever UI feels better. Can't run simultaneously (conflict), choose one. Power users: Afterburner for RivaTuner OSD capabilities.",
                "keywords": ["Precision X1", "Afterburner comparison", "software tools"],
                "difficulty": "beginner",
                "tags": ["software", "tools"],
                "related_tools": ["MSI Afterburner", "EVGA Precision X1"]
            },
            {
                "content": "Advanced curve techniques: Voltage floor lifting for mid-range GPUs. Budget cards (RTX 4060, RX 7600) sometimes drop to very low voltages (0.700V) during light gaming, causing stutters when boost spikes. Fix: Set minimum voltage floor 0.850V by dragging all points below 0.850V up to 0.850V @ their current frequency. Increases idle power +5-10W but eliminates microstutter in esports titles. Monitor: HWiNFO64 'GPU Core Voltage' shouldn't drop below set floor during gaming. Validates smoothness: RTSS frame time graph should show consistent 16.6ms (60fps) without spikes.",
                "keywords": ["voltage floor", "stuttering", "mid-range GPUs"],
                "difficulty": "advanced",
                "tags": ["optimization", "troubleshooting"],
                "related_tools": ["MSI Afterburner", "HWiNFO64", "RTSS"]
            },
            {
                "content": "Curve optimization for multi-GPU setups: SLI/CrossFire deprecated, but productivity multi-GPU (CUDA/OpenCL rendering) benefits from curve tuning. Apply same curve to both GPUs, but test individually first (may have different silicon quality). GPU 1: 2800 MHz @ 0.925V stable. GPU 2: 2700 MHz @ 0.925V stable. System limited by weaker GPU in many workloads - use conservative curve matching GPU 2's capability. Advanced: Per-GPU profiles if apps can utilize GPUs independently (Blender can assign tasks per GPU). Monitor per-GPU temps: HWiNFO64 shows GPU 0/GPU 1 separately, adjust fan curves per card.",
                "keywords": ["multi-GPU", "SLI", "rendering"],
                "difficulty": "expert",
                "tags": ["multi-GPU", "productivity"],
                "related_tools": ["MSI Afterburner", "HWiNFO64"]
            },
            {
                "content": "VRAM thermal throttling and curve interaction: GDDR6X (RTX 3080/3090/4080/4090) runs hot, thermal pads critical. VRAM throttles at 100-110°C, reduces memory clock automatically. Symptoms: 3DMark scores drop after 10min into test (VRAM heatsoak). Check: HWiNFO64 'GPU Memory Junction Temperature'. If >95°C sustained: Improve case airflow, repad with quality pads (Thermalright Odyssey), or reduce memory overclock. Curve impact: Undervolting core reduces overall GPU heat, helps VRAM thermals indirectly. Combined approach: Core undervolt + moderate memory OC + good pads = optimal.",
                "keywords": ["VRAM throttling", "thermal pads", "GDDR6X"],
                "difficulty": "advanced",
                "tags": ["cooling", "memory"],
                "related_tools": ["HWiNFO64", "Thermal pads"]
            },
            {
                "content": "Safe voltage limits for long-term 24/7 overclocking: Nvidia: ≤1.000V completely safe long-term, 1.000-1.050V safe for 3-5 years, >1.050V degrades chip faster (electromigration). AMD: ≤1.150V safe RDNA2/3, higher voltages acceptable for short bursts. Conservative recommendation: Find optimal frequency @ 0.950V for Nvidia, @ 1.100V for AMD. Degradation signs: OC becomes unstable after 12-24 months, requires higher voltage for same frequency. Mining/24-7 rendering: Use conservative curves. Gaming-only (4-8hr/day): More aggressive safe. Balance longevity vs performance based on usage pattern and upgrade cycle.",
                "keywords": ["safe voltages", "longevity", "degradation"],
                "difficulty": "intermediate",
                "tags": ["overclocking", "safety"],
                "related_tools": ["MSI Afterburner"]
            },
            {
                "content": "Voltage curve persistence across driver updates: Afterburner profiles save locally (C:\\Users\\[User]\\AppData\\Roaming\\MSI Afterburner), survive driver updates. Radeon Software profiles reset on major driver updates - backup tuning screenshots or export profiles. Best practice: After stable curve achieved, document all settings (screenshot curve, write down voltages/frequencies, save MSI profile to USB backup). Post-driver update: reimport Afterburner profile, re-test stability (driver changes can affect behavior). Critical: DDU clean install erases Radeon tuning - AMD users export/import profiles via Radeon Software before DDU.",
                "keywords": ["driver updates", "profile backup", "persistence"],
                "difficulty": "beginner",
                "tags": ["maintenance", "drivers"],
                "related_tools": ["MSI Afterburner", "Radeon Software", "DDU"]
            }
        ])
        print(f"[OK] gpu_overclocking_curves: {before} -> {len(kb['gpu_overclocking_curves']['tips'])} tips (+{len(kb['gpu_overclocking_curves']['tips']) - before})")

    # ========================================================================
    # RAM STRESS TESTING
    # ========================================================================

    if "ram_stress_testing" in kb:
        before = len(kb["ram_stress_testing"]["tips"])
        kb["ram_stress_testing"]["tips"].extend([
            {
                "content": "TestMem5 (TM5) with Anta777 Extreme config: Download TM5 v0.12 + Anta777 Extreme .cfg. Place config in TM5 folder, run as admin, select Extreme profile. 3 cycles = basic stability (30-45min), 6 cycles = good for daily OC (1-1.5hr), 25 cycles = ultimate validation (6-8hr). Each test targets different RAM failure modes: Test 0-4 = voltage stress, Test 5-8 = timing stress, Test 9-12 = thermal stress. Single error = unstable, increase VDIMM +0.02V or loosen timings. Faster than MemTest86, better than Windows Memory Diagnostic.",
                "keywords": ["TM5", "Anta777", "stress testing", "RAM validation"],
                "difficulty": "intermediate",
                "tags": ["testing", "memory"],
                "related_tools": ["TestMem5", "Anta777 config"]
            },
            {
                "content": "Karhu RAM Test comprehensive methodology: Purchase license ($10), run as admin. Start with 6000% coverage for initial validation (8-16 hours depending on RAM size). 10000%+ coverage for mission-critical systems. Statistics: 6000% catches 99%+ errors, diminishing returns above 10000%. Monitor: Karhu shows errors per GB tested. 0 errors = stable. 1 error in first 100% = serious instability, 1 error at 8000%+ = marginal (may accept for daily use). Advantages over TM5: better long-term stability detection, catches thermal-related errors after hours of runtime.",
                "keywords": ["Karhu", "coverage percentage", "long-term testing"],
                "difficulty": "advanced",
                "tags": ["testing", "stability"],
                "related_tools": ["Karhu RAM Test"]
            },
            {
                "content": "MemTest86 UEFI bootable testing: Download from PassMark, create bootable USB via ImageUSB. Boot from USB, run full 4-pass test (6-12 hours for 32GB RAM). Tests actual hardware without OS interference - catches errors Windows-based tests miss. Critical for diagnosing hardware failures vs OC instability. Pass criteria: 0 errors across all tests. Even 1 error = bad RAM stick or failed overclock. Use Test 7 (Block Move) and Test 13 (Hammer Test) for specific failure modes. Professional validation: Run MemTest86 overnight after completing TM5/Karhu in Windows.",
                "keywords": ["MemTest86", "UEFI", "hardware testing", "bootable"],
                "difficulty": "intermediate",
                "tags": ["testing", "diagnostics"],
                "related_tools": ["MemTest86", "ImageUSB"]
            },
            {
                "content": "y-cruncher Component Stress Tester for RAM+CPU combo: Download y-cruncher, run Component Stress Tester (CST). Tests FFT computations stressing RAM, CPU cache, CPU cores simultaneously. Configuration: Select 'All Tests' + 'Pause on Error'. Duration: 2 hours minimum, 8 hours for validation. Fails indicate: CPU instability, RAM instability, or IMC (memory controller) instability. Differentiate: If only y-cruncher fails but TM5 passes = CPU/IMC issue, increase System Agent voltage. If both fail = RAM timings/voltage. More comprehensive than Prime95 alone for overclocked systems.",
                "keywords": ["y-cruncher", "CST", "CPU+RAM testing", "IMC"],
                "difficulty": "advanced",
                "tags": ["testing", "CPU", "memory"],
                "related_tools": ["y-cruncher"]
            },
            {
                "content": "Prime95 Large FFT RAM stress mode: Download Prime95, run torture test > Custom > 4096-8192K FFT (targets RAM), 90% available RAM, run 1-4 hours. Tests RAM bandwidth and CPU simultaneously. Worker threads = CPU cores for maximum stress. Monitoring: HWiNFO64 watch 'Memory Errors' counter, CPU temps (should stay <90°C). Failure modes: 'FATAL ERROR: Rounding was 0.5' = RAM unstable, 'Hardware failure detected' = CPU or RAM. Stop test: no errors for 1hr = likely stable. Less sensitive than TM5/Karhu for pure RAM testing but validates system-wide stability under heavy compute.",
                "keywords": ["Prime95", "Large FFT", "bandwidth testing"],
                "difficulty": "intermediate",
                "tags": ["testing", "CPU", "memory"],
                "related_tools": ["Prime95", "HWiNFO64"]
            },
            {
                "content": "GSAT (Google Stressful Application Test) for Linux users: Open-source RAM tester, compile from source. Run: 'stressapptest -M 28000 -s 7200' (28GB test for 2 hours). Parameters: -M = megabytes to test (leave 4GB for OS), -s = seconds. Advantages: Lightweight, runs on Linux servers, no GUI overhead. Pair with memtester for comprehensive Linux validation. Results: 'PASS' = stable, any 'FAIL' or hung process = unstable. Use case: Server overclocking, headless systems, Linux workstations. Alternative to Windows-focused tools, validates ECC RAM configurations properly.",
                "keywords": ["GSAT", "Linux", "stressapptest", "server"],
                "difficulty": "expert",
                "tags": ["Linux", "testing", "server"],
                "related_tools": ["GSAT", "memtester"]
            },
            {
                "content": "Real-world application stress testing: After synthetic tests pass, validate with actual workloads. Video encoding: Handbrake 4K HEVC encode 2hr movie (RAM bandwidth stress). Compilation: Compile large project (Chromium, Linux kernel) - errors during compile = instability. 3D rendering: Blender CPU render complex scene overnight. Gaming: Extended session in RAM-intensive title (Cities Skylines, Factorio, Minecraft modded). Each workflow stresses RAM differently - synthetic passes but real-world fails indicates edge case timing issue. Run relevant workloads for your use case.",
                "keywords": ["real-world testing", "application stress", "workflow validation"],
                "difficulty": "intermediate",
                "tags": ["testing", "productivity"],
                "related_tools": ["Handbrake", "Blender", "Games"]
            },
            {
                "content": "HCI MemTest multi-instance methodology: Download HCI MemTest (free version), run multiple instances. Calculation: (Total RAM - 8GB for OS) ÷ threads = MB per instance. Example: 32GB RAM, 16 threads = 1500 MB per instance. Launch 16 instances, set each to 1500 MB, start all. Run to 200%+ coverage (2-4 hours). Any instance showing errors = instable. Advantages: Free, good coverage, multi-threaded. Disadvantages: Manual setup tedious vs TM5 automation. Historical use: Before TM5 popularity, was gold standard for RAM overclocking validation.",
                "keywords": ["HCI MemTest", "multi-instance", "coverage"],
                "difficulty": "intermediate",
                "tags": ["testing", "free tools"],
                "related_tools": ["HCI MemTest"]
            },
            {
                "content": "Memory error monitoring via HWiNFO64 sensors: HWiNFO64 > Sensors > scroll to 'Memory Errors Corrected'. Counter increments when ECC corrects errors or when non-ECC has correctable events. For overclockers: This counter should ALWAYS be 0. Non-zero during gaming/testing = unstable RAM overclock, even if no crash occurred. Reset counter between tests: Right-click > Reset > Min/Max/Avg. Run workload, check after. Single increment = marginal stability (tighten less or add voltage). Regular increments = seriously unstable. Windows Event Viewer: Check for WHEA errors (Windows Hardware Error Architecture) correlated with memory.",
                "keywords": ["HWiNFO64", "memory errors", "monitoring", "WHEA"],
                "difficulty": "intermediate",
                "tags": ["monitoring", "diagnostics"],
                "related_tools": ["HWiNFO64", "Event Viewer"]
            },
            {
                "content": "Temperature-dependent stability testing: RAM overclocks stable cold boot may fail after thermal soak. Test procedure: 1) Cold boot, run TM5 3 cycles (30-45min). 2) Monitor DIMM temps in HWiNFO64 (start ~35°C, reach 50-55°C after 30min). 3) Continue testing 3 more cycles at heat-soaked temperature. Failures in second half = thermal instability, solutions: improve case airflow, add 40mm fan on DIMMs, reduce VDIMM -0.02V, or loosen timings. DDR5 especially sensitive >60°C. Summer ambient temps 30°C+ can destabilize winter-validated overclocks - seasonal re-testing recommended.",
                "keywords": ["thermal stability", "temperature testing", "heat soak"],
                "difficulty": "advanced",
                "tags": ["testing", "cooling"],
                "related_tools": ["TM5", "HWiNFO64"]
            },
            {
                "content": "Per-test failure analysis in TM5: Each TM5 test targets specific failure modes. Test 0 (Small FFT): CPU cache/ring instability - increase CPU ring voltage or reduce ring frequency. Test 1-3: VDIMM insufficient - increase +0.02V. Test 4 (Extreme): Timing stress - loosen tRCD/tRP +1. Test 6 (Sequential Read/Write): tRFC too tight - increase +20. Test 8 (Random Read): tWR/tWTR too tight. Test 10-12: Thermal issues or VDDQ/VDD2 (DDR5) voltage insufficient. Record which test fails, adjust corresponding parameter. Multiple test failures = broad instability, increase voltage first.",
                "keywords": ["TM5 analysis", "failure diagnosis", "test modes"],
                "difficulty": "expert",
                "tags": ["troubleshooting", "testing"],
                "related_tools": ["TestMem5"]
            },
            {
                "content": "Overnight soak testing for production systems: For mission-critical systems (workstations, servers), run extended tests overnight/weekend. Protocol: TM5 Anta777 Extreme 25 cycles (~8hr) + Karhu 10000% (12-24hr) + y-cruncher CST 8hr = 24-48hr total. Pass all three = extremely high confidence. Schedule: Friday night start, check Monday morning. Document: Screenshot final results, save logs. Any error in 48hr = not production-ready, troubleshoot and re-test. Cost of instability (data corruption, crashes) exceeds time investment in thorough testing. Home users: 6hr TM5 sufficient.",
                "keywords": ["soak testing", "production validation", "mission-critical"],
                "difficulty": "advanced",
                "tags": ["testing", "professional"],
                "related_tools": ["TM5", "Karhu", "y-cruncher"]
            },
            {
                "content": "Testing after BIOS updates or driver changes: RAM stability not guaranteed persistent across firmware/software changes. After motherboard BIOS update: Re-run TM5 6 cycles minimum (memory training algorithms may have changed). After Windows major updates: Quick TM5 3 cycle validation. After RAM driver updates (Intel/AMD chipset drivers): TM5 3 cycles. After GPU driver update: Generally unaffected unless using iGPU (which shares system RAM). Create testing schedule: Post-update checklist includes quick RAM validation. Catches regressions early before data corruption manifests.",
                "keywords": ["BIOS updates", "validation schedule", "regression testing"],
                "difficulty": "intermediate",
                "tags": ["maintenance", "testing"],
                "related_tools": ["TM5", "BIOS"]
            },
            {
                "content": "Multi-boot scenario RAM testing: If dual-booting Windows + Linux, test RAM stability in both OS. Windows: TM5 6 cycles. Linux: GSAT 2 hours or memtester. OS-level differences (memory management, kernel drivers) can expose different instabilities. Example: Windows stable but Linux crashes under heavy swap usage indicates marginal tRFC. Virtualization users (VMware, Hyper-V): Test with VMs running - hypervisor memory management adds stress. Passthrough configurations especially need validation. Professional setup: Test in all operating modes before declaring stable.",
                "keywords": ["multi-boot", "dual-boot", "cross-OS testing"],
                "difficulty": "advanced",
                "tags": ["testing", "multi-OS"],
                "related_tools": ["TM5", "GSAT", "memtester"]
            },
            {
                "content": "RAM stress testing with integrated graphics: iGPU (Intel UHD, AMD Radeon Graphics) shares system RAM as VRAM. Dual stress test: Run TM5 + Unigine Heaven simultaneously. iGPU memory access patterns differ from CPU, can expose instability CPU-only testing misses. Increase test intensity: Allocate 4-8GB to iGPU in BIOS, run demanding iGPU workload (video transcoding via Quick Sync/VCE while stress testing). Failure during iGPU load = increase VDDQ (DDR5) or VDIMM (DDR4), or reduce memory frequency. Dedicated GPU users can skip, but professionals using Quick Sync encoding must validate.",
                "keywords": ["iGPU testing", "integrated graphics", "shared memory"],
                "difficulty": "advanced",
                "tags": ["testing", "graphics"],
                "related_tools": ["TM5", "Unigine", "Video transcoding"]
            },
            {
                "content": "Stress testing workflow optimization: Efficient validation saves time. Tiered approach: 1) Quick test: TM5 1 cycle (10min) - catches obviously bad settings immediately. 2) Short validation: TM5 3 cycles (45min) - adequate for testing incremental changes during tuning. 3) Medium validation: TM5 6 cycles (90min) - confirms daily OC stability. 4) Long validation: Karhu 6000% (8-12hr) - final check before calling overclock 'done'. Iterate efficiently: Quick test after each timing change, short validation when you think settings good, long validation only on final profile. Don't waste time - fast failures during quick tests save hours.",
                "keywords": ["workflow", "testing strategy", "time management"],
                "difficulty": "intermediate",
                "tags": ["methodology", "testing"],
                "related_tools": ["TM5", "Karhu"]
            },
            {
                "content": "False positive handling and retesting: Rare: single error at 90% through long test may be cosmic ray or random OS background process interference. Protocol: If error occurs after 4+ hours of clean testing, note error type/timing, reboot, re-run full test. If second run passes completely = likely false positive (accept as stable). If error repeats (same test, similar timing) = real instability. Conservative approach: Any error = instability, adjust settings. Aggressive approach: Isolated errors after 4hr+ can be dismissed if non-repeatable. Production: Zero-tolerance. Gaming: One-error tolerance acceptable to some users.",
                "keywords": ["false positives", "cosmic rays", "error handling"],
                "difficulty": "advanced",
                "tags": ["troubleshooting", "methodology"],
                "related_tools": ["TM5", "Karhu"]
            },
            {
                "content": "RAM kit asymmetry testing: Even matched kits have variance. Test each stick individually: Install one DIMM in A2 slot, run TM5 6 cycles, note max stable frequency/timings. Repeat for second stick. Example results: Stick 1 = DDR5-6800 CL32 stable, Stick 2 = DDR5-6400 CL32 stable. System limited by weaker stick. Options: 1) Run conservative settings (6400 CL32 both), 2) Increase voltage on weak stick if BIOS allows per-DIMM voltage (rare), 3) Sell weak stick, buy matched pair. Silicon lottery applies to RAM - production binning variance causes 200-400MHz spread even in 'matched' kits.",
                "keywords": ["per-stick testing", "kit asymmetry", "silicon variance"],
                "difficulty": "advanced",
                "tags": ["testing", "diagnostics"],
                "related_tools": ["TM5"]
            },
            {
                "content": "Professional data integrity testing with ECC RAM: ECC (Error-Correcting Code) RAM detects and corrects single-bit errors, detects multi-bit. Enable ECC in BIOS (requires ECC RAM + compatible motherboard/CPU). Monitor: HWiNFO64 'Corrected Memory Errors' and 'Uncorrected Memory Errors'. Corrected errors = single-bit flips (ECC fixed automatically), still indicates marginal stability. Uncorrected errors = multi-bit corruption, critical failure. Workstation overclock validation: ECC must show 0 corrected errors during 24hr stress test. Any corrected errors = reduce overclock. Non-ECC can't detect these errors - silent corruption risk without ECC.",
                "keywords": ["ECC RAM", "error correction", "data integrity"],
                "difficulty": "expert",
                "tags": ["professional", "server", "ECC"],
                "related_tools": ["HWiNFO64", "BIOS"]
            },
            {
                "content": "Stress testing across CPU load scenarios: RAM behavior changes under different CPU loads. Test matrix: 1) Idle CPU + TM5 (memory-focused). 2) Heavy CPU load (Prime95 Small FFT) + TM5 simultaneously (tests IMC under thermal stress). 3) Mixed load (gaming simulation - run game benchmark loop + background tasks). Scenario 2 may fail when 1 passes = IMC thermal throttling or insufficient System Agent voltage. Increase SA voltage +0.02V or improve CPU cooling. Professional setups: Test in your specific workflow environment (heavy multitasking, VMs running, etc) before declaring stable.",
                "keywords": ["load scenarios", "IMC stress", "combined testing"],
                "difficulty": "expert",
                "tags": ["testing", "advanced"],
                "related_tools": ["TM5", "Prime95"]
            }
        ])
        print(f"[OK] ram_stress_testing: {before} -> {len(kb['ram_stress_testing']['tips'])} tips (+{len(kb['ram_stress_testing']['tips']) - before})")

    # ========================================================================
    # CPU STRESS TESTING (continued in next section due to length...)
    # Let me continue with CPU, GPU, and remaining categories
    # ========================================================================

    if "cpu_stress_testing" in kb:
        before = len(kb["cpu_stress_testing"]["tips"])
        kb["cpu_stress_testing"]["tips"].extend([
            {
                "content": "Prime95 Small FFT maximum heat test: Download Prime95, Torture Test > Smallest FFT size (4K-8K). Tests CPU cores with AVX2 instructions, generates maximum power draw (30-40% higher than gaming). Run 30min for heat test (verify cooling adequacy), 6-12hr for stability validation. Monitoring: HWiNFO64 CPU Package Power (should be <240W sustained most CPUs, <350W extreme CPUs like 13900K/7950X), temps <90°C safe, <95°C max. Failures: 'Rounding error' or 'Hardware failure' = CPU unstable, increase voltage +0.01V or reduce frequency -100MHz.",
                "keywords": ["Prime95", "Small FFT", "AVX2", "maximum heat"],
                "difficulty": "intermediate",
                "tags": ["CPU", "stress testing"],
                "related_tools": ["Prime95", "HWiNFO64"]
            },
            {
                "content": "OCCT CPU stress test with AVX2/AVX512 modes: OCCT offers targeted instruction set testing. OCCT > CPU > SSE (baseline), AVX2 (heavy), AVX-512 (extreme for supported CPUs). Intel 10th-14th gen: AVX2 mode recommended. AMD Ryzen: AVX2 sufficient (no AVX-512 consumer chips). Run 1 hour minimum. Monitoring: Built-in graph shows voltage, temps, clocks. Error detection: Any detected error halts test immediately. Advantages over Prime95: Better error detection, graphical interface, auto-stops on instability. Use AVX2 mode for daily overclock validation, AVX-512 for extreme validation on Intel HEDT.",
                "keywords": ["OCCT", "AVX2", "AVX-512", "instruction sets"],
                "difficulty": "advanced",
                "tags": ["stress testing", "CPU"],
                "related_tools": ["OCCT", "HWiNFO64"]
            },
            {
                "content": "Cinebench R23 looping for quick stability check: Cinebench R23 > Advanced Benchmark > Enable loop mode, set 10 runs minimum (30-45 minutes). Monitors: Scores should be within 1-2% variance between runs. Score degradation (run 1: 32000 points, run 10: 30500 points) indicates thermal throttling - improve cooling. Any crash or score drop >3% = instability. Advantages: Quick, realistic workload (3D rendering), built-in looping, scores for comparison. Limitations: Less stressful than Prime95, won't catch all instability. Use case: Initial validation after overclock changes, then deeper test with Prime95/OCCT.",
                "keywords": ["Cinebench R23", "loop testing", "quick validation"],
                "difficulty": "beginner",
                "tags": ["testing", "benchmarking"],
                "related_tools": ["Cinebench R23"]
            },
            {
                "content": "y-cruncher stress testing for FP precision: y-cruncher Component Stress Tester (CST) tests CPU floating-point units, cache, memory subsystem simultaneously. More comprehensive than Prime95 alone. Configuration: CST > All Tests, run 2-8 hours. Monitors: Built-in validation checks results for accuracy. Any validation failure = system instability (CPU, RAM, or cache). Specific failures: 'FFT verification error' = CPU FPU issue, 'Memory allocation failed' = RAM issue. Pair with Prime95: If Prime95 passes but y-cruncher fails = cache/IMC voltage insufficient (increase ring/cache voltage). Professional rendering workstations: Must pass y-cruncher for data integrity.",
                "keywords": ["y-cruncher", "floating-point", "cache testing"],
                "difficulty": "advanced",
                "tags": ["CPU", "testing"],
                "related_tools": ["y-cruncher"]
            },
            {
                "content": "CoreCycler per-core stability testing: Download CoreCycler, configure with Prime95 or y-cruncher. Tests each CPU core individually in sequence to isolate weak cores. AMD Ryzen per-core boost relies on all cores stable - single weak core limits entire CPU. Run overnight (8-12hr), log shows which core failed. Core 0 failed = reduce Curve Optimizer on Core 0 by -5 (make less aggressive). Intel hybrid: Test P-cores and E-cores separately with different settings. Critical for Curve Optimizer tuning (AMD) and per-core overclocking (Intel). Saves time vs guessing which core unstable.",
                "keywords": ["CoreCycler", "per-core testing", "Curve Optimizer"],
                "difficulty": "expert",
                "tags": ["AMD", "Intel", "testing"],
                "related_tools": ["CoreCycler", "Prime95", "y-cruncher"]
            },
            {
                "content": "Handbrake video encoding stress test for real-world validation: Encode 4K video with Handbrake using CPU preset (x265 or AV1). 2-hour movie takes 4-8 hours to encode (sustained realistic load). Monitoring: CPU utilization 100%, temps sustained 70-85°C, clocks maintained (no throttling). Validation: Compare encode against known-good baseline - corruption in output video = CPU instability during encode. Practical stress: If your workflow includes video encoding, 3D rendering, compilation - test with actual workloads after synthetic tests pass. Failure in real-world but synthetic passes = marginal stability, reduce overclock slightly.",
                "keywords": ["Handbrake", "video encoding", "real-world stress"],
                "difficulty": "intermediate",
                "tags": ["productivity", "testing"],
                "related_tools": ["Handbrake", "HWiNFO64"]
            },
            {
                "content": "Blender Benchmark CPU stress: Download Blender Benchmark, run all scenes (monster, junkshop, classroom). CPU rendering test with production-realistic workload. Run each scene 3x, compare times - variance <2% indicates thermal stability. Longer than Cinebench, more realistic than Prime95 for 3D artists. Log scores: Compare against online database to validate performance matches overclock expectations. If scores lower than expected despite successful overclock = thermal throttling (cooling inadequate) or power limit throttling (increase motherboard power limits). Use case: Professional validation for rendering workstations.",
                "keywords": ["Blender", "3D rendering", "production testing"],
                "difficulty": "intermediate",
                "tags": ["3D rendering", "testing"],
                "related_tools": ["Blender Benchmark"]
            },
            {
                "content": "IntelBurnTest and LinX AVX torture: IntelBurnTest (IBT) or LinX runs Intel Linpack libraries with AVX instructions. Extremely stressful - generates even more heat than Prime95 Small FFT. Use case: Quick validation (10 runs = 15-30min) or absolute stress test. Very High setting: 10-20 runs sufficient. Monitoring: Temps will spike highest possible (100°C+ without good cooling). GFlops result: Should be consistent across runs (±1%). Warnings: Can damage CPUs if cooling inadequate - start with Standard setting first. Modern alternative: OCCT AVX2 mode safer with similar stress levels. Historical tool, still used by extreme overclockers.",
                "keywords": ["IntelBurnTest", "LinX", "Linpack", "AVX torture"],
                "difficulty": "expert",
                "tags": ["extreme testing", "CPU"],
                "related_tools": ["IntelBurnTest", "LinX"]
            },
            {
                "content": "Realbench stress test for realistic gaming/productivity mix: ASUS Realbench combines image editing, encoding, OpenCL, multitasking. More realistic than synthetic Prime95 for typical user workloads. Run Stress Test 8 hours for full validation. Benchmark mode: Scores for comparison, run 3x for consistency check (<2% variance). Failures: 'OpenCL test failed' may indicate GPU or RAM instability in hybrid CPU+GPU tests. Advantage: Tests system holistically (CPU+RAM+GPU), catches issues multi-component stress reveals. Good supplement to CPU-only tests, especially for gaming PCs where GPU also loaded.",
                "keywords": ["Realbench", "mixed workload", "realistic testing"],
                "difficulty": "intermediate",
                "tags": ["testing", "gaming"],
                "related_tools": ["ASUS Realbench"]
            },
            {
                "content": "Thermal throttling identification during stress tests: HWiNFO64 sensors: 'Thermal Throttling' flag shows Yes/No, 'CPU Clock' should maintain target frequency. Throttling symptoms: Clock speed drops from 5.5GHz to 5.2GHz after 10min of Prime95. Temperature correlation: Throttling usually begins 95-100°C (Intel TjMax varies by model, AMD ~95°C). Solutions: Improve cooling (better cooler, repaste, case airflow), reduce voltage (less heat generation), reduce frequency (lower heat output). Testing protocol: If throttling occurs during stress test, overclock NOT stable for intended workload - either improve cooling or reduce OC.",
                "keywords": ["thermal throttling", "temperature monitoring", "TjMax"],
                "difficulty": "intermediate",
                "tags": ["cooling", "troubleshooting"],
                "related_tools": ["HWiNFO64"]
            },
            {
                "content": "Power limit throttling vs thermal throttling: Modern CPUs have power limits (PL1 long duration, PL2 short duration). Intel: PL1 default 125W-253W depending on SKU, PL2 up to 350W. Monitoring: HWiNFO64 'CPU Package Power' vs 'CPU Power Limit'. If power hits limit, clock reduces even if temps OK. Symptoms: Sustained workloads drop from 5.4GHz to 5.0GHz despite temps only 75°C. Solution: BIOS > Advanced CPU > Increase PL1/PL2 limits (or set unlimited on Z-series motherboards). Validation: Post-adjustment, clocks sustained at target, power consumption rises to match workload without artificial limit.",
                "keywords": ["power limits", "PL1", "PL2", "throttling"],
                "difficulty": "advanced",
                "tags": ["power management", "overclocking"],
                "related_tools": ["HWiNFO64", "BIOS"]
            },
            {
                "content": "VRM stress testing for motherboard validation: CPU stress tests also stress motherboard VRM (voltage regulator modules). Monitor: HWiNFO64 'VR MOS' temperature sensors (VRM MOSFETs). Safe: <90°C, Warm: 90-100°C, Hot: 100-110°C (throttling may occur), Dangerous: >110°C (shutdown risk). Budget motherboards with weak VRM (10-phase design, low-amperage MOSFETs) can't sustain high-end CPU overclocks. Solutions: Add 40mm fan directed at VRM heatsinks, improve case airflow, reduce CPU power draw (lower voltage/frequency), or upgrade motherboard. Buildzoid VRM tier list: Check your board's tier before pushing extreme overclocks.",
                "keywords": ["VRM testing", "MOSFET temps", "power delivery"],
                "difficulty": "advanced",
                "tags": ["motherboard", "cooling"],
                "related_tools": ["HWiNFO64", "Fans"]
            },
            {
                "content": "Multi-program stress testing combo: Simultaneous stress for ultimate validation. Run Prime95 Small FFT (CPU) + TM5 (RAM) + FurMark (GPU) simultaneously for 1-2 hours. Tests: CPU stability, RAM stability, GPU stability, power supply adequacy, case cooling under full system load. PSU validation: HWiNFO64 monitor '12V rail' should stay 11.8-12.2V under load (if motherboard has voltage sensors). Any component failure during combined test = that component unstable or insufficient PSU. Extreme validation: Use for 24/7 workstations, render farms, or confirming new PSU adequacy.",
                "keywords": ["combined stress", "multi-component", "full system"],
                "difficulty": "expert",
                "tags": ["testing", "system validation"],
                "related_tools": ["Prime95", "TM5", "FurMark", "HWiNFO64"]
            },
            {
                "content": "Stress testing across different workload types: Different apps stress CPU differently. AVX-heavy (Prime95, encoding): Tests worst-case power/thermal. Gaming simulation (Realbench, actual games): Tests boost behavior, power transitions. Idle-to-load transitions: Tests voltage regulation response. Compile workload (compile Chromium): Tests sustained multi-core with cache pressure. Create test matrix covering your use case: Gamer = game benchmarks + Realbench. Content creator = Handbrake + Blender. Professional = specific app validation. Passing synthetic tests but failing real apps = tune for real apps (synthetics don't matter if workflow unstable).",
                "keywords": ["workload diversity", "application testing", "use case validation"],
                "difficulty": "advanced",
                "tags": ["methodology", "testing"],
                "related_tools": ["Various"]
            },
            {
                "content": "WHEA error monitoring in Windows Event Viewer: Windows Hardware Error Architecture logs errors invisible to stress test apps. Event Viewer > Windows Logs > System, filter Current Log > Event ID 18 or 19. WHEA error types: 'Bus/Interconnect Error' = memory controller, 'Cache Hierarchy Error' = CPU cache/ring, 'Processor Core Error' = CPU core instability. Post-stress test: Check Event Viewer for WHEA errors even if test didn't crash. Any logged WHEA = instability detected, increase relevant voltage. Clean run: 0 WHEA errors after 8hr stress test. Critical: WHEA errors can cause silent data corruption without crashing - check logs regularly.",
                "keywords": ["WHEA errors", "Event Viewer", "silent errors"],
                "difficulty": "intermediate",
                "tags": ["diagnostics", "monitoring"],
                "related_tools": ["Event Viewer"]
            },
            {
                "content": "Seasonal stress testing for ambient temperature variance: CPU overclock stable in winter (20°C room) may fail in summer (30°C room). Higher ambient = higher CPU temps at same load. Example: Winter stable 5.5GHz @ 1.35V reaches 82°C, Summer same settings reach 92°C (thermal throttles). Solutions: Seasonal profiles (winter aggressive, summer conservative), improve cooling before summer, or accept seasonal performance variance. Best practice: Validate overclock at warmest expected ambient temperature. Air conditioning impact: Consistent 22°C room enables year-round stable OC. Enthusiasts: Re-test stability when seasons change significantly.",
                "keywords": ["ambient temperature", "seasonal testing", "environmental factors"],
                "difficulty": "intermediate",
                "tags": ["testing", "cooling"],
                "related_tools": ["HWiNFO64", "Stress tests"]
            },
            {
                "content": "AVX offset validation: Intel CPUs with AVX offset (reduces multiplier during AVX loads) need separate testing. Test non-AVX: Cinebench R23 (maintains base OC, e.g., 5.5GHz). Test AVX: Prime95 Small FFT (drops to 5.3GHz with -2 offset). Both should be stable independently. Monitor: HWiNFO64 'Effective Clock' shows actual frequency. Offset too large: Loses performance in AVX workloads unnecessarily. No offset with high OC: May crash or overheat during AVX. Optimal: Minimum offset that prevents AVX thermal/stability issues. Test both workload types to ensure balanced configuration.",
                "keywords": ["AVX offset", "frequency validation", "workload types"],
                "difficulty": "advanced",
                "tags": ["Intel", "overclocking"],
                "related_tools": ["Cinebench", "Prime95", "HWiNFO64"]
            },
            {
                "content": "Cache/Ring overclock stress testing: CPU ring/uncore/cache frequency (different names, same thing) requires separate validation. After CPU core stable, test ring OC: Increase ring ratio to match core ratio (5.5GHz core = 5.5GHz ring attempt). Stress test: Prime95 Blend (stresses cache) or AIDA64 Cache benchmark loop. Instability symptoms: WHEA Cache Hierarchy errors in Event Viewer, system crashes during tests. Solution: Reduce ring -100MHz increments, or increase ring/cache voltage +0.02V. Sweet spot: -200 to -300MHz below core frequency (5.5GHz core + 5.2-5.3GHz ring) balances performance and stability.",
                "keywords": ["cache OC", "ring ratio", "uncore"],
                "difficulty": "expert",
                "tags": ["overclocking", "cache"],
                "related_tools": ["Prime95", "AIDA64", "Event Viewer"]
            },
            {
                "content": "Degradation tracking over time: Long-term high voltage causes CPU degradation (electron migration). Track stability monthly: Same test (Prime95 1hr), same monitoring, log date + voltage required for stable OC. Example log: Month 1: 5.5GHz @ 1.35V stable. Month 12: 5.5GHz requires 1.37V for stability (+0.02V). Degradation rate: >0.02V per year = fast degradation (voltage too high), <0.01V per year = acceptable. Early signs: Occasional WHEA errors where none before, need extra voltage for same frequency. Mitigation: Reduce voltage proactively to extend lifespan. Track in Excel spreadsheet with test dates and results.",
                "keywords": ["degradation tracking", "long-term stability", "electron migration"],
                "difficulty": "expert",
                "tags": ["monitoring", "longevity"],
                "related_tools": ["Prime95", "Excel", "Event Viewer"]
            },
            {
                "content": "Bootloop troubleshooting after failed stress test: System crashes during stress test, won't POST after restart. Solutions: 1) Clear CMOS (motherboard button or jumper), resets BIOS to defaults. 2) Try safe boot (some boards auto-reduce OC after 3 failed boots). 3) Remove AC power 30sec to discharge capacitors fully. 4) Single-RAM stick in A2 slot for basic POST. 5) Reset BIOS battery if CMOS clear doesn't work. Prevention: Save known-good BIOS profile to USB before aggressive OC attempts. Learn your motherboard's recovery features (BIOS Flashback, dual BIOS) before problems occur. Keep stable backup profile saved.",
                "keywords": ["bootloop", "recovery", "CMOS clear"],
                "difficulty": "intermediate",
                "tags": ["troubleshooting", "BIOS"],
                "related_tools": ["BIOS", "Motherboard"]
            }
        ])
        print(f"[OK] cpu_stress_testing: {before} -> {len(kb['cpu_stress_testing']['tips'])} tips (+{len(kb['cpu_stress_testing']['tips']) - before})")

    # Final stats
    after_count = count_tips(kb)
    added = after_count - before_count

    print("\n" + "=" * 80)
    print("ENRICHMENT COMPLETE!")
    print("=" * 80)
    print(f"\nBEFORE: {before_count} tips")
    print(f"AFTER:  {after_count} tips")
    print(f"ADDED:  {added} tips")
    print(f"\nProgress: {after_count}/5000 ({after_count/5000*100:.1f}%)")
    print("\nPhase 2 Hardware Categories enrichment successful!")
    print("=" * 80)

if __name__ == "__main__":
    enrich_hardware_categories()
