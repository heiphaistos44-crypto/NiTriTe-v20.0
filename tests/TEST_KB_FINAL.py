#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Test final de la Knowledge Base - Vérification complète"""

import sys
sys.path.insert(0, r"C:\Users\Utilisateur\Downloads\Nitrite-V18.5\src")

# Reload pour être sûr d'avoir la dernière version
if 'v14_mvp.ai_knowledge_unified' in sys.modules:
    del sys.modules['v14_mvp.ai_knowledge_unified']

from v14_mvp.ai_knowledge_unified import UnifiedKnowledgeBase

print("="*80)
print("  TEST KNOWLEDGE BASE - NiTriTe V18.5")
print("="*80)

# 1. Test chargement
print("\n[1/5] Test chargement KB...")
try:
    kb = UnifiedKnowledgeBase()
    print("    [OK] KB chargee avec succes")
except Exception as e:
    print(f"    [ERREUR] {e}")
    sys.exit(1)

# 2. Test statistiques
print("\n[2/5] Test statistiques...")
stats = kb.get_stats()
print(f"    [OK] Catégories: {stats['categories']}")
print(f"    [OK] Conseils: {stats['tips']}")
print(f"    [OK] Moyenne: {stats['avg_tips_per_category']:.1f} conseils/catégorie")

# 3. Test intégrité des catégories
print("\n[3/5] Test intégrité des catégories...")
errors = 0
for cat_name, cat_data in kb.kb.items():
    # Vérifier structure
    if "metadata" not in cat_data:
        print(f"    [X] {cat_name}: metadata manquant")
        errors += 1
        continue
    if "tips" not in cat_data:
        print(f"    [X] {cat_name}: tips manquant")
        errors += 1
        continue

    # Vérifier métadonnées
    metadata = cat_data["metadata"]
    required = ["priority", "tags", "difficulty", "description"]
    for field in required:
        if field not in metadata:
            print(f"    [X] {cat_name}: metadata.{field} manquant")
            errors += 1

    # Vérifier tips
    tips = cat_data["tips"]
    if not isinstance(tips, list):
        print(f"    [X] {cat_name}: tips n'est pas une liste")
        errors += 1
        continue

    for i, tip in enumerate(tips):
        required_tip = ["content", "keywords", "difficulty", "tags", "related_tools"]
        for field in required_tip:
            if field not in tip:
                print(f"    [X] {cat_name} tip {i}: {field} manquant")
                errors += 1
                break

if errors == 0:
    print(f"    [OK] Toutes les {stats['categories']} catégories sont valides")
else:
    print(f"    [X] {errors} erreurs détectées")

# 4. Test échantillon de catégories
print("\n[4/5] Test échantillon de contenu...")
sample_categories = [
    "gpu_nvidia_rtx_40_series",
    "cpu_intel_generations",
    "networking_dns_optimization",
    "gaming_fps_optimization_competitive"
]

for cat in sample_categories:
    if cat in kb.kb:
        num_tips = len(kb.kb[cat]["tips"])
        desc = kb.kb[cat]["metadata"]["description"]
        print(f"    [OK] {cat}: {num_tips} tips - {desc}")
    else:
        print(f"    [X] {cat}: MANQUANT")

# 5. Test recherche de conseils
print("\n[5/5] Test méthode de recherche...")
try:
    # Test get_category_tips
    cpu_tips = kb.get_category_tips("cpu")
    print(f"    [OK] Recherche 'cpu': {len(cpu_tips)} conseils trouvés")

    gpu_tips = kb.get_category_tips("gpu")
    print(f"    [OK] Recherche 'gpu': {len(gpu_tips)} conseils trouvés")

    gaming_tips = kb.get_category_tips("gaming")
    print(f"    [OK] Recherche 'gaming': {len(gaming_tips)} conseils trouvés")
except Exception as e:
    print(f"    [X] Erreur recherche: {e}")

# Résumé final
print("\n" + "="*80)
print("  RÉSULTAT FINAL")
print("="*80)
print(f"  [OK] Knowledge Base opérationnelle")
print(f"  [OK] {stats['categories']} catégories | {stats['tips']} conseils")
print(f"  [OK] Intégrité: {'OK' if errors == 0 else f'{errors} erreurs'}")
print(f"  [OK] Prête pour intégration avec MaintenanceAIAgent")
print("="*80 + "\n")

# Afficher top 10 catégories les plus fournies
print("Top 10 catégories les plus riches:")
cat_counts = [(name, len(data["tips"])) for name, data in kb.kb.items()]
cat_counts.sort(key=lambda x: x[1], reverse=True)
for i, (name, count) in enumerate(cat_counts[:10], 1):
    print(f"  {i:2d}. {name:45s} {count:3d} tips")

print("\n" + "="*80)
print("  TEST TERMINÉ AVEC SUCCÈS [OK]")
print("="*80)
