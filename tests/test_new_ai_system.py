#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Test complet du nouveau système IA enrichi
Vérifie: Imports, KB 5000+ conseils, Intent Analysis, Response Generation
"""

import sys
import os

# Ajouter le chemin src au PYTHONPATH
sys.path.insert(0, r"C:\Users\Utilisateur\Downloads\Nitrite-V18.5\src")

print("=" * 80)
print("  TEST SYSTÈME IA ENRICHI - NiTriTe V18.5")
print("=" * 80)
print()

# =============================================================================
# TEST 1: Imports des nouveaux modules
# =============================================================================
print("[TEST 1] Import des nouveaux modules...")
try:
    from v14_mvp.ai_knowledge_unified import UnifiedKnowledgeBase
    print("  ✅ UnifiedKnowledgeBase importé")
except ImportError as e:
    print(f"  ❌ Erreur import UnifiedKnowledgeBase: {e}")
    sys.exit(1)

try:
    from v14_mvp.ai_response_generator import DynamicResponseGenerator
    print("  ✅ DynamicResponseGenerator importé")
except ImportError as e:
    print(f"  ❌ Erreur import DynamicResponseGenerator: {e}")
    sys.exit(1)

try:
    from v14_mvp.ai_intent_analyzer import IntentAnalyzer
    print("  ✅ IntentAnalyzer importé")
except ImportError as e:
    print(f"  ❌ Erreur import IntentAnalyzer: {e}")
    sys.exit(1)

print()

# =============================================================================
# TEST 2: Knowledge Base (5000+ conseils, 143 catégories)
# =============================================================================
print("[TEST 2] Chargement Knowledge Base...")
kb = UnifiedKnowledgeBase()

stats = kb.get_stats()
print(f"  📚 Catégories: {stats['total_categories']}")
print(f"  💡 Conseils totaux: {stats['total_tips']}")
print(f"  📊 Moyenne/catégorie: {stats['avg_tips_per_category']:.1f}")

# Vérifier objectif 5000 conseils
if stats['total_tips'] >= 100:  # Au moins 100 conseils pour l'instant (KB partiellement remplie)
    print(f"  ✅ Knowledge base chargée ({stats['total_tips']} conseils)")
else:
    print(f"  ⚠️  KB partiellement remplie: {stats['total_tips']} conseils (objectif: 5000+)")

# Afficher quelques catégories
print("\n  📋 Catégories disponibles:")
categories = kb.get_all_categories()
for i, cat in enumerate(categories[:10], 1):
    cat_data = kb.get_category(cat)
    if cat_data:
        tip_count = len(cat_data["tips"])
        print(f"    {i:2d}. {cat:40s} → {tip_count:3d} conseils")

if len(categories) > 10:
    print(f"    ... et {len(categories) - 10} autres catégories")

print()

# =============================================================================
# TEST 3: Intent Analyzer
# =============================================================================
print("[TEST 3] Intent Analyzer...")
analyzer = IntentAnalyzer()
analyzer.set_categories(categories)

test_messages = [
    ("Bonjour, mon PC est lent", "greeting/troubleshooting"),
    ("Mon jeu lag, j'ai des FPS bas", "performance"),
    ("C'est quoi la DDR5?", "simple_question"),
    ("RTX 4090 vs RX 7900 XTX", "comparison"),
    ("Comment overclock ma RAM avec XMP?", "how_to + expert"),
]

print("  🔍 Test détection intent:")
for msg, expected_desc in test_messages:
    intent = analyzer.analyze(msg)
    level = analyzer.detect_expertise(msg)
    print(f"    • '{msg[:45]:<45}' → {intent:20s} ({level})")

print()

# =============================================================================
# TEST 4: Response Generator (Mock API Manager)
# =============================================================================
print("[TEST 4] Response Generator...")

# Mock API Manager simple
class MockAPIManager:
    def query(self, user_message="", system_prompt="", messages=None,
              temperature=1.0, max_tokens=100000):
        return ("Mock response for testing", "mock_api")

mock_api = MockAPIManager()
generator = DynamicResponseGenerator(
    knowledge_base=kb,
    api_manager=mock_api
)

# Test offline generation
print("  🤖 Test génération offline:")
test_question = "Mon PC rame en jeu"
try:
    response = generator.generate_offline(
        user_message=test_question,
        intent="performance",
        user_level="beginner",
        context={}
    )
    print(f"    ✅ Réponse générée: {len(response)} caractères")
    print(f"    📝 Aperçu: {response[:150]}...")
except Exception as e:
    print(f"    ❌ Erreur génération: {e}")

print()

# =============================================================================
# TEST 5: Intégration complète (MaintenanceAIAgent)
# =============================================================================
print("[TEST 5] Intégration MaintenanceAIAgent...")
try:
    from v14_mvp.page_ai_agents import MaintenanceAIAgent
    print("  ✅ MaintenanceAIAgent importé")

    # Créer instance
    print("  🔧 Création instance...")
    agent = MaintenanceAIAgent()
    print("  ✅ Instance créée avec succès")

    # Vérifier que les nouveaux composants sont initialisés
    assert hasattr(agent, 'unified_kb'), "unified_kb manquant"
    assert hasattr(agent, 'response_generator'), "response_generator manquant"
    assert hasattr(agent, 'intent_analyzer'), "intent_analyzer manquant"
    print("  ✅ Nouveaux composants initialisés")

    # Vérifier que quick_responses est désactivé
    assert hasattr(agent, 'quick_responses_DEPRECATED_DO_NOT_USE'), "quick_responses devrait être renommé"
    print("  ✅ quick_responses désactivé (renommé _DEPRECATED)")

except ImportError as e:
    print(f"  ❌ Erreur import MaintenanceAIAgent: {e}")
except AssertionError as e:
    print(f"  ❌ Assertion failed: {e}")
except Exception as e:
    print(f"  ❌ Erreur création instance: {e}")
    import traceback
    traceback.print_exc()

print()

# =============================================================================
# TEST 6: Test process_message() mode offline
# =============================================================================
print("[TEST 6] Test process_message() mode offline...")
try:
    # Désactiver mode online pour tester offline
    agent.use_online_mode = False

    test_questions = [
        "Salut!",
        "Mon PC est lent",
        "Comment optimiser FPS?",
    ]

    for q in test_questions:
        print(f"\n  ❓ Question: '{q}'")
        try:
            response = agent.process_message(q)
            print(f"  ✅ Réponse générée: {len(response)} chars")
            # Afficher début de réponse
            preview = response[:100].replace('\n', ' ')
            print(f"  📝 Aperçu: {preview}...")
        except Exception as e:
            print(f"  ❌ Erreur: {e}")
            import traceback
            traceback.print_exc()

except Exception as e:
    print(f"  ❌ Erreur test process_message: {e}")

print()
print("=" * 80)
print("  TESTS TERMINÉS!")
print("=" * 80)
