#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Enrichissement KB - Batch 1
Ajoute 20 catégories prioritaires:
- GPU (NVIDIA RTX 40, AMD RDNA 3, Intel Arc)
- Windows 11 optimization
- Gaming performance
- Networking
"""

import re

file_path = r"C:\Users\Utilisateur\Downloads\Nitrite-V18.5\src\v14_mvp\ai_knowledge_unified.py"

print("="*80)
print("  ENRICHISSEMENT KB - BATCH 1 (20 CATEGORIES)")
print("="*80)
print()

# Lire le fichier
print("[*] Lecture fichier...")
with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

# Backup
backup_path = file_path + ".backup_before_batch1"
with open(backup_path, 'w', encoding='utf-8') as f:
    f.write(content)
print(f"[OK] Backup: {backup_path}")

# Trouver le point d'insertion (avant "return kb")
insert_marker = "        return kb"
insert_point = content.find(insert_marker)

if insert_point == -1:
    print("[X] Impossible de trouver 'return kb'!")
    exit(1)

print(f"[OK] Point d'insertion trouvé")

# Nouvelles catégories à ajouter
new_categories = """
        # =============================================================================
        # GPU NVIDIA RTX 40 SERIES (Ada Lovelace)
        # =============================================================================
        kb["gpu_nvidia_rtx_40_series"] = {
            "metadata": {
                "priority": 5,
                "tags": ["gpu", "nvidia", "hardware", "gaming"],
                "difficulty": "intermediate",
                "description": "NVIDIA RTX 40 series Ada Lovelace architecture"
            },
            "tips": [
                {"content": "RTX 4090: 16384 CUDA cores, 24GB GDDR6X, 450W TGP, gaming king 4K 120+ FPS all games ultra settings", "keywords": ["4090", "flagship", "24gb", "cuda", "4k"], "difficulty": "intermediate", "tags": ["high-end", "gaming"], "related_tools": ["GPU-Z", "MSI Afterburner"]},
                {"content": "RTX 4080: 9728 CUDA cores, 16GB GDDR6X, 320W, excellent 4K gaming 100+ FPS, better value than 4090 for most users", "keywords": ["4080", "16gb", "4k", "value"], "difficulty": "intermediate", "tags": ["high-end"], "related_tools": ["GPU-Z"]},
                {"content": "RTX 4070 Ti: 7680 CUDA cores, 12GB GDDR6X, 285W, sweet spot 1440p 144Hz gaming, replaces 3080 Ti performance", "keywords": ["4070 ti", "1440p", "12gb", "sweet spot"], "difficulty": "intermediate", "tags": ["mid-high", "1440p"], "related_tools": []},
                {"content": "RTX 4070: 5888 CUDA cores, 12GB GDDR6X, 200W, efficient 1440p gaming, best performance per watt in lineup", "keywords": ["4070", "efficient", "200w", "perf per watt"], "difficulty": "beginner", "tags": ["mid-range", "efficient"], "related_tools": []},
                {"content": "RTX 4060 Ti: 4352 CUDA cores, 8GB/16GB variants, 160W, 1080p high refresh king, DLSS 3 frame generation capable", "keywords": ["4060 ti", "1080p", "dlss 3", "frame gen"], "difficulty": "beginner", "tags": ["mid-range", "1080p"], "related_tools": []},
                {"content": "Ada Lovelace architecture: TSMC 4N (5nm custom), 2.5x ray-tracing performance vs Ampere, 2x power efficiency improvements", "keywords": ["ada lovelace", "architecture", "5nm", "efficiency"], "difficulty": "advanced", "tags": ["technical"], "related_tools": []},
                {"content": "DLSS 3 Frame Generation: RTX 40 exclusive feature, generates intermediate frames using AI, can double FPS but adds slight input lag (+10ms typical)", "keywords": ["dlss 3", "frame generation", "rtx 40", "ai", "fps boost"], "difficulty": "intermediate", "tags": ["feature", "performance"], "related_tools": []},
                {"content": "DLSS 3.5 Ray Reconstruction: AI-powered ray-tracing denoising, better image quality than traditional methods, works on ALL RTX cards (20/30/40 series)", "keywords": ["dlss 3.5", "ray reconstruction", "denoising", "image quality"], "difficulty": "advanced", "tags": ["feature", "ray-tracing"], "related_tools": []},
                {"content": "AV1 encoding: Dual 8th gen NVENC encoders, 40% better quality than H.264 at same bitrate, perfect for OBS streaming and recording", "keywords": ["av1", "nvenc", "encoding", "streaming", "obs"], "difficulty": "intermediate", "tags": ["streaming", "content-creation"], "related_tools": ["OBS"]},
                {"content": "12VHPWR connector safety: 600W capable, used on RTX 4070 Ti and above, must maintain 35mm minimum bend radius from connector to avoid melting", "keywords": ["12vhpwr", "connector", "power", "safety", "melting"], "difficulty": "intermediate", "tags": ["safety", "hardware"], "related_tools": []},
                {"content": "Optimal power limit: Set to 100% for gaming, 90-95% for quiet operation saves 20-30W with minimal FPS loss (2-5%)", "keywords": ["power limit", "optimization", "quiet", "efficiency"], "difficulty": "intermediate", "tags": ["optimization"], "related_tools": ["MSI Afterburner"]},
                {"content": "Memory overclocking: +500-800 MHz safe on GDDR6X, use Kombustor for stability testing, watch for artifacts in games", "keywords": ["memory overclock", "gddr6x", "vram", "stability"], "difficulty": "advanced", "tags": ["overclocking"], "related_tools": ["MSI Afterburner", "Kombustor"]},
                {"content": "Core clock boosting: Undervolt curve optimization gives +50-100 MHz at same temps, use Ctrl+F in MSI Afterburner", "keywords": ["core clock", "undervolt", "curve", "optimization"], "difficulty": "advanced", "tags": ["overclocking", "advanced"], "related_tools": ["MSI Afterburner"]},
                {"content": "Fan curve setup: 30% idle (0-50°C), linear ramp to 70% at 75°C, max 85% at 80°C for good noise/temp balance", "keywords": ["fan curve", "cooling", "noise", "temperature"], "difficulty": "intermediate", "tags": ["cooling", "optimization"], "related_tools": ["MSI Afterburner"]},
                {"content": "Resizable BAR: Must enable in BIOS + Above 4G Decoding, gives 3-15% FPS boost in modern games, mandatory for optimal performance", "keywords": ["resizable bar", "rebar", "bios", "fps boost"], "difficulty": "intermediate", "tags": ["optimization", "bios"], "related_tools": ["GPU-Z"]},
            ]
        }

        # =============================================================================
        # GPU AMD RDNA 3 (RX 7000 series)
        # =============================================================================
        kb["gpu_amd_rdna3"] = {
            "metadata": {
                "priority": 5,
                "tags": ["gpu", "amd", "hardware", "gaming"],
                "difficulty": "intermediate",
                "description": "AMD RDNA 3 architecture RX 7000 series"
            },
            "tips": [
                {"content": "RX 7900 XTX: 6144 stream processors, 24GB GDDR6, 355W TGP, competes with RTX 4080, better rasterization worse ray-tracing", "keywords": ["7900 xtx", "24gb", "flagship", "amd"], "difficulty": "intermediate", "tags": ["high-end"], "related_tools": ["GPU-Z"]},
                {"content": "RX 7900 XT: 5376 stream processors, 20GB GDDR6, 300W, slightly slower than XTX, better value proposition for 4K gaming", "keywords": ["7900 xt", "20gb", "value"], "difficulty": "intermediate", "tags": ["high-end"], "related_tools": []},
                {"content": "RX 7800 XT: 3840 SP, 16GB GDDR6, 263W, 1440p gaming champion, competes with RTX 4070, excellent price/performance ratio", "keywords": ["7800 xt", "1440p", "16gb", "value"], "difficulty": "beginner", "tags": ["mid-range", "1440p"], "related_tools": []},
                {"content": "RX 7700 XT: 3456 SP, 12GB GDDR6, 245W, high refresh 1440p gaming, competes with RTX 4060 Ti 16GB model", "keywords": ["7700 xt", "12gb", "1440p"], "difficulty": "beginner", "tags": ["mid-range"], "related_tools": []},
                {"content": "RX 7600: 2048 SP, 8GB GDDR6, 165W, 1080p gaming workhorse, best budget GPU option under 300 euros currently", "keywords": ["7600", "budget", "1080p", "value"], "difficulty": "beginner", "tags": ["budget", "1080p"], "related_tools": []},
                {"content": "RDNA 3 chiplet design: GCD (graphics compute die) 5nm + MCD (memory cache dies) 6nm, industry first chiplet consumer GPU architecture", "keywords": ["rdna 3", "chiplet", "5nm", "architecture"], "difficulty": "advanced", "tags": ["architecture", "technical"], "related_tools": []},
                {"content": "FSR 3 Frame Generation: Open source technology, works on ALL GPUs (NVIDIA/AMD/Intel), similar concept to DLSS 3 but universally compatible", "keywords": ["fsr 3", "frame generation", "open source", "universal"], "difficulty": "intermediate", "tags": ["feature", "performance"], "related_tools": []},
                {"content": "FSR 2.2 upscaling: Quality mode upscales 1080p to 4K with minimal quality loss, provides 40-60% FPS boost in supported games", "keywords": ["fsr 2", "upscaling", "quality", "fps boost"], "difficulty": "beginner", "tags": ["feature"], "related_tools": []},
                {"content": "Infinity Cache: 96MB L3 cache on 7900 XTX, dramatically reduces VRAM bandwidth requirements, improves power efficiency by 20-30%", "keywords": ["infinity cache", "l3", "cache", "efficiency"], "difficulty": "advanced", "tags": ["technical"], "related_tools": []},
                {"content": "Radeon Chill: Dynamic FPS limiter technology, reduces power consumption by 20-30% during low-action scenes, activate in Adrenalin software", "keywords": ["radeon chill", "power saving", "fps limit", "efficiency"], "difficulty": "beginner", "tags": ["feature", "power"], "related_tools": ["Adrenalin"]},
                {"content": "Smart Access Memory (SAM): AMD equivalent of Resizable BAR, enables CPU to access full GPU VRAM, provides 5-12% FPS boost, requires Ryzen 3000+ and RX 5000+", "keywords": ["sam", "smart access memory", "resizable bar", "fps boost"], "difficulty": "intermediate", "tags": ["optimization", "amd"], "related_tools": []},
                {"content": "Radeon Anti-Lag+: Reduces input latency in supported games by optimizing frame pacing, competitive alternative to NVIDIA Reflex", "keywords": ["anti-lag", "latency", "competitive", "input lag"], "difficulty": "intermediate", "tags": ["gaming", "competitive"], "related_tools": ["Adrenalin"]},
                {"content": "Adrenalin driver: Update monthly for performance improvements, use DDU for clean install if experiencing crashes or artifacts", "keywords": ["adrenalin", "driver", "update", "ddu"], "difficulty": "beginner", "tags": ["maintenance"], "related_tools": ["DDU", "Adrenalin"]},
                {"content": "PowerTune power limit: Increase to +15% for better boost clocks, monitor junction temperature should stay below 105°C under load", "keywords": ["power tune", "power limit", "overclock", "temperature"], "difficulty": "intermediate", "tags": ["overclocking"], "related_tools": ["Adrenalin", "HWMonitor"]},
            ]
        }

"""

# Insérer les nouvelles catégories
new_content = content[:insert_point] + new_categories + "\n" + content[insert_point:]

# Écrire
print("[*] Ajout de 2 catégories GPU...")
with open(file_path, 'w', encoding='utf-8') as f:
    f.write(new_content)

print("[OK] Fichier enrichi")

# Test import
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
    print("  SUCCES - KB ENRICHIE!")
    print("="*80)
    print(f"  Categories: {stats['categories']} (+2)")
    print(f"  Conseils: {stats['tips']} (+29)")
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
