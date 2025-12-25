#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Test de l'agent IA ultra-enrichi
Vérifie: max_tokens 100K, 29 catégories, réponses détaillées
"""

import sys
import os
import io

# Force UTF-8 encoding for console output
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

# Ajouter le chemin du projet
sys.path.insert(0, r"C:\Users\Utilisateur\Downloads\Nitrite-V18.5\src")

print("=" * 80)
print("  TEST AGENT IA ULTRA-ENRICHI - NiTriTe V18.5")
print("=" * 80)
print()

# Import de l'agent
try:
    from v14_mvp.page_ai_agents import MaintenanceAIAgent
    print("✅ Import MaintenanceAIAgent réussi")
except Exception as e:
    print(f"❌ Erreur import: {e}")
    import traceback
    traceback.print_exc()
    sys.exit(1)

# Créer l'instance
try:
    print("\n[*] Création instance MaintenanceAIAgent...")
    agent = MaintenanceAIAgent()
    print("✅ Instance créée avec succès")
except Exception as e:
    print(f"❌ Erreur création instance: {e}")
    sys.exit(1)

# Vérifier les catégories de la knowledge base
print("\n" + "=" * 80)
print("  VÉRIFICATION KNOWLEDGE BASE")
print("=" * 80)
print(f"\n📚 Nombre total de catégories: {len(agent.knowledge_base)}")
print("\n📋 Liste des catégories:")
for i, category in enumerate(agent.knowledge_base.keys(), 1):
    tips_count = len(agent.knowledge_base[category])
    print(f"  {i:2d}. {category:40s} → {tips_count:3d} conseils")

total_tips = sum(len(tips) for tips in agent.knowledge_base.values())
print(f"\n🎯 TOTAL: {total_tips} conseils dans la knowledge base!")

# Vérifier les nouvelles catégories ajoutées
print("\n" + "=" * 80)
print("  NOUVELLES CATÉGORIES AJOUTÉES")
print("=" * 80)
new_categories = [
    "ram_expert_deepdive",
    "ssd_nvme_expert",
    "motherboard_chipset_expert",
    "monitor_display_expert",
    "keyboard_mouse_peripherals",
    "laptop_specific_optimization",
    "streaming_content_creation",
    "virtualization_containers",
    "linux_windows_dual_boot"
]

for cat in new_categories:
    if cat in agent.knowledge_base:
        count = len(agent.knowledge_base[cat])
        print(f"  ✅ {cat:40s} → {count} conseils")
    else:
        print(f"  ❌ {cat:40s} → MANQUANT!")

# Test question complexe
print("\n" + "=" * 80)
print("  TEST RÉPONSE AGENT IA")
print("=" * 80)

test_question = "Mon PC rame en jeu, j'ai des saccades et les FPS chutent"
print(f"\n❓ Question test: \"{test_question}\"\n")

try:
    response = agent.process_message(test_question)
    print("📝 RÉPONSE AGENT:")
    print("-" * 80)
    print(response)
    print("-" * 80)
    print(f"\n📊 Longueur réponse: {len(response)} caractères")
    print(f"📊 Nombre de lignes: {response.count(chr(10)) + 1}")
    print(f"📊 Estimation mots: ~{len(response.split())} mots")
except Exception as e:
    print(f"❌ Erreur génération réponse: {e}")
    import traceback
    traceback.print_exc()

# Test questions variées
print("\n" + "=" * 80)
print("  TEST QUESTIONS VARIÉES (DÉTECTION CONTEXTUELLE)")
print("=" * 80)

test_keywords = [
    ("Mon PC est lent au démarrage", "Ralentissement boot"),
    ("J'ai des FPS bas dans Cyberpunk", "Gaming/FPS"),
    ("Écran bleu au démarrage", "BSOD/Crash"),
    ("Ma RAM est-elle suffisante pour du gaming?", "Question mémoire"),
    ("Mon SSD NVMe est lent", "Problème stockage"),
    ("WiFi instable pendant les visioconférences", "Problème réseau")
]

print()
for test_msg, description in test_keywords:
    try:
        response = agent.process_message(test_msg)
        matched = "✅" if len(response) > 200 else "⚠️"
        words = len(response.split())
        print(f"{matched} {description:30s} → {len(response):5d} chars, ~{words:4d} mots")
    except:
        print(f"❌ {description:30s} → ERREUR")

print("\n" + "=" * 80)
print("  TEST TERMINÉ!")
print("=" * 80)
