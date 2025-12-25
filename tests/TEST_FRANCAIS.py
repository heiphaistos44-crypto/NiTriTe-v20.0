#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Test génération réponses françaises AVANT rebuild"""

import sys
import os

# Forcer UTF-8 pour Windows
if sys.platform == "win32":
    os.environ['PYTHONIOENCODING'] = 'utf-8'
    sys.stdout.reconfigure(encoding='utf-8')

sys.path.insert(0, r"C:\Users\Utilisateur\Downloads\Nitrite-V18.5\src")

# Forcer reload des modules
for module in list(sys.modules.keys()):
    if module.startswith('v14_mvp'):
        del sys.modules[module]

from v14_mvp.ai_response_generator import DynamicResponseGenerator
from v14_mvp.ai_knowledge_unified import UnifiedKnowledgeBase
from v14_mvp.ai_intent_analyzer import IntentAnalyzer

print("="*80)
print("  TEST GÉNÉRATION FRANÇAISE - MODE OFFLINE")
print("="*80)

# 1. Charger KB
print("\n[1/4] Chargement Knowledge Base...")
try:
    kb = UnifiedKnowledgeBase()
    stats = kb.get_stats()
    print(f"    ✓ KB chargée: {stats['categories']} catégories, {stats['tips']} conseils")
except Exception as e:
    print(f"    ✗ ERREUR: {e}")
    sys.exit(1)

# 2. Initialiser générateur
print("\n[2/4] Initialisation générateur...")
try:
    gen = DynamicResponseGenerator(kb, None)
    print(f"    ✓ Générateur créé")
except Exception as e:
    print(f"    ✗ ERREUR: {e}")
    sys.exit(1)

# 3. Initialiser intent analyzer
print("\n[3/4] Initialisation intent analyzer...")
try:
    analyzer = IntentAnalyzer()
    print(f"    ✓ Analyzer créé")
except Exception as e:
    print(f"    ✗ ERREUR: {e}")
    sys.exit(1)

# 4. Tests questions françaises
print("\n[4/4] Test questions françaises...")
test_questions = [
    ("mon pc surchauffe", "troubleshooting"),
    ("mon pc est lent", "performance"),
    ("comment améliorer les fps", "performance"),
]

for question, expected_intent in test_questions:
    print(f"\n" + "="*80)
    print(f"QUESTION: '{question}'")
    print("-"*80)

    # Analyser intent
    intent = analyzer.analyze(question)
    user_level = analyzer.detect_expertise(question, {"user_expertise_level": "beginner"})

    print(f"Intent détecté: {intent} (attendu: {expected_intent})")
    print(f"Niveau: {user_level}")

    # Générer réponse
    try:
        response = gen.generate_offline(
            user_message=question,
            intent=intent,
            user_level=user_level,
            context={}
        )

        print(f"\nRÉPONSE:\n{response}\n")

        # Vérifier que c'est en français
        french_indicators = ["pour", "avec", "dans", "étape", "tu", "ton", "voilà"]
        has_french = any(word in response.lower() for word in french_indicators)

        # Vérifier qu'il n'y a pas trop d'anglais
        english_words = ["switch", "KVM", "RPCS3", "emulator", "crackling"]
        has_english = any(word in response for word in english_words)

        if has_french and not has_english:
            print("✓ RÉPONSE EN FRANÇAIS CORRECTE")
        elif has_english:
            print("✗ CONTIENT DES MOTS ANGLAIS SUSPECTS!")
        else:
            print("⚠ Difficile à déterminer")

    except Exception as e:
        print(f"✗ ERREUR GÉNÉRATION: {e}")
        import traceback
        traceback.print_exc()

print("\n" + "="*80)
print("  TEST TERMINÉ")
print("="*80)
print("\nSi tu vois des réponses 100% en français avec étapes numérotées:")
print("  → Le code fonctionne! Lance REBUILD_CLEAN.bat")
print("\nSi tu vois encore de l'anglais (KVM, RPCS3, audio crackling):")
print("  → Problème dans le code, dis-le moi!")
print("="*80)
