#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Génère le contenu massif pour ai_knowledge_unified.py
143 catégories, 5000+ conseils
"""

# Cette structure sera copiée dans ai_knowledge_unified.py
MASSIVE_KB_CONTENT = """
            # =====================================================================
            # HARDWARE DEEP DIVE (20 catégories, ~900 conseils)
            # =====================================================================

            "gpu_nvidia_rtx_40_series": {
                "metadata": {
                    "priority": 5,
                    "tags": ["gpu", "nvidia", "hardware", "gaming"],
                    "difficulty": "intermediate",
                    "description": "NVIDIA RTX 40 series Ada Lovelace architecture"
                },
                "tips": [
                    {
                        "content": "RTX 4090: 16384 CUDA cores, 24GB GDDR6X, 450W TGP, gaming king 4K 120+ FPS all games ultra",
                        "keywords": ["4090", "flagship", "24gb", "cuda"],
                        "difficulty": "intermediate",
                        "tags": ["high-end"],
                        "related_tools": ["GPU-Z", "MSI Afterburner"]
                    },
                    {
                        "content": "RTX 4080: 9728 CUDA cores, 16GB GDDR6X, 320W, excellent 4K gaming 100+ FPS, better value than 4090",
                        "keywords": ["4080", "16gb", "4k"],
                        "difficulty": "intermediate",
                        "tags": ["high-end"],
                        "related_tools": ["GPU-Z"]
                    },
                    {
                        "content": "RTX 4070 Ti: 7680 CUDA cores, 12GB GDDR6X, 285W, sweet spot 1440p 144Hz gaming, replaces 3080",
                        "keywords": ["4070 ti", "1440p", "12gb"],
                        "difficulty": "intermediate",
                        "tags": ["mid-high"],
                        "related_tools": []
                    },
                    {
                        "content": "RTX 4070: 5888 CUDA cores, 12GB GDDR6X, 200W, efficient 1440p gaming, best perf/watt",
                        "keywords": ["4070", "efficient", "200w"],
                        "difficulty": "beginner",
                        "tags": ["mid-range"],
                        "related_tools": []
                    },
                    {
                        "content": "RTX 4060 Ti: 4352 CUDA cores, 8GB/16GB variants, 160W, 1080p high refresh king, DLSS 3 frame gen",
                        "keywords": ["4060 ti", "1080p", "dlss 3"],
                        "difficulty": "beginner",
                        "tags": ["mid-range"],
                        "related_tools": []
                    },
                    {
                        "content": "Ada Lovelace architecture: TSMC 4N (5nm custom), 2.5x ray-tracing vs Ampere, 2x power efficiency",
                        "keywords": ["ada lovelace", "architecture", "5nm"],
                        "difficulty": "advanced",
                        "tags": ["technical"],
                        "related_tools": []
                    },
                    {
                        "content": "DLSS 3 Frame Generation: RTX 40 exclusive, generates intermediate frames, 2x FPS boost, slight input lag (+10ms)",
                        "keywords": ["dlss 3", "frame generation", "rtx 40"],
                        "difficulty": "intermediate",
                        "tags": ["feature"],
                        "related_tools": []
                    },
                    {
                        "content": "DLSS 3.5 Ray Reconstruction: AI denoising ray-tracing, better image quality, all RTX cards (20/30/40)",
                        "keywords": ["dlss 3.5", "ray reconstruction", "denoising"],
                        "difficulty": "advanced",
                        "tags": ["feature"],
                        "related_tools": []
                    },
                    {
                        "content": "AV1 encode: Dual encoders 8th gen NVENC, better quality than H.264 at same bitrate, OBS/streaming",
                        "keywords": ["av1", "nvenc", "encoding"],
                        "difficulty": "intermediate",
                        "tags": ["streaming"],
                        "related_tools": ["OBS"]
                    },
                    {
                        "content": "12VHPWR connector: 600W capable, RTX 4070 Ti+, bend minimum 35mm from connector to avoid melt",
                        "keywords": ["12vhpwr", "connector", "power"],
                        "difficulty": "intermediate",
                        "tags": ["safety"],
                        "related_tools": []
                    },
                ]
            },

            "gpu_amd_rdna3": {
                "metadata": {
                    "priority": 5,
                    "tags": ["gpu", "amd", "hardware", "gaming"],
                    "difficulty": "intermediate",
                    "description": "AMD RDNA 3 architecture RX 7000 series"
                },
                "tips": [
                    {
                        "content": "RX 7900 XTX: 6144 stream processors, 24GB GDDR6, 355W, competes RTX 4080, better raster worse RT",
                        "keywords": ["7900 xtx", "24gb", "flagship"],
                        "difficulty": "intermediate",
                        "tags": ["high-end"],
                        "related_tools": ["GPU-Z"]
                    },
                    {
                        "content": "RX 7900 XT: 5376 SP, 20GB GDDR6, 300W, slightly slower than XTX, better value for 4K gaming",
                        "keywords": ["7900 xt", "20gb"],
                        "difficulty": "intermediate",
                        "tags": ["high-end"],
                        "related_tools": []
                    },
                    {
                        "content": "RX 7800 XT: 3840 SP, 16GB GDDR6, 263W, 1440p champion, competes RTX 4070, excellent value",
                        "keywords": ["7800 xt", "1440p", "16gb"],
                        "difficulty": "beginner",
                        "tags": ["mid-range"],
                        "related_tools": []
                    },
                    {
                        "content": "RX 7700 XT: 3456 SP, 12GB GDDR6, 245W, 1440p high refresh, competes RTX 4060 Ti 16GB",
                        "keywords": ["7700 xt", "12gb"],
                        "difficulty": "beginner",
                        "tags": ["mid-range"],
                        "related_tools": []
                    },
                    {
                        "content": "RX 7600: 2048 SP, 8GB GDDR6, 165W, 1080p gaming, best budget option under 300€",
                        "keywords": ["7600", "budget", "1080p"],
                        "difficulty": "beginner",
                        "tags": ["budget"],
                        "related_tools": []
                    },
                    {
                        "content": "RDNA 3 chiplet design: GCD (graphics) 5nm + MCD (memory/cache) 6nm, first chiplet GPU",
                        "keywords": ["rdna 3", "chiplet", "5nm"],
                        "difficulty": "advanced",
                        "tags": ["architecture"],
                        "related_tools": []
                    },
                    {
                        "content": "FSR 3 Frame Generation: Open source, works all GPUs (NVIDIA/AMD/Intel), similar to DLSS 3 FG",
                        "keywords": ["fsr 3", "frame generation", "open source"],
                        "difficulty": "intermediate",
                        "tags": ["feature"],
                        "related_tools": []
                    },
                    {
                        "content": "FSR 2.2 upscaling: Quality mode 1080p→4K, minimal quality loss, 40-60% FPS boost",
                        "keywords": ["fsr 2", "upscaling", "quality"],
                        "difficulty": "beginner",
                        "tags": ["feature"],
                        "related_tools": []
                    },
                    {
                        "content": "Infinity Cache: 96MB L3 cache (7900 XTX), reduces VRAM bandwidth needs, power efficient",
                        "keywords": ["infinity cache", "l3", "cache"],
                        "difficulty": "advanced",
                        "tags": ["technical"],
                        "related_tools": []
                    },
                    {
                        "content": "Radeon Chill: Dynamic FPS limiter, saves power when no movement, 20-30% power reduction idle scenes",
                        "keywords": ["radeon chill", "power saving", "fps limit"],
                        "difficulty": "beginner",
                        "tags": ["feature"],
                        "related_tools": ["Adrenalin"]
                    },
                ]
            },
"""

# Sauvegarde dans fichier
output_file = "massive_kb_categories.txt"
with open(output_file, 'w', encoding='utf-8') as f:
    f.write(MASSIVE_KB_CONTENT)

print(f"[OK] Contenu KB généré dans: {output_file}")
print(f"[OK] Ce contenu doit être copié dans ai_knowledge_unified.py")
print()
print("Note: Ce n'est qu'un DÉBUT - seulement 2 catégories GPU avec ~20 conseils")
print("Pour atteindre 5000+ conseils, il faut continuer avec les 139 autres catégories!")
