#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Script de fusion des 500 scénarios générés dans ai_response_generator.py
"""

import os
import re

def merge_all_scenarios():
    """
    Fusionne les 4 fichiers générés dans ai_response_generator.py
    """

    base_path = os.path.dirname(os.path.abspath(__file__))

    # Fichiers générés par les agents
    generated_files = [
        "generated_scenarios_11_155.py",
        "generated_scenarios_156_260.py",
        "generated_scenarios_261_390.py",
        "generated_scenarios_391_500.py"
    ]

    # Lire tout le contenu généré
    all_scenarios_code = []

    print("🔄 Fusion des scénarios générés...")
    for gen_file in generated_files:
        file_path = os.path.join(base_path, gen_file)
        if os.path.exists(file_path):
            print(f"   ✅ Lecture: {gen_file}")
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()
                all_scenarios_code.append(content)
        else:
            print(f"   ⚠️  Fichier manquant: {gen_file}")

    # Fusionner tout le code
    merged_code = "\n\n".join(all_scenarios_code)

    # Sauvegarder le code fusionné
    merged_file = os.path.join(base_path, "all_scenarios_merged.py")
    with open(merged_file, 'w', encoding='utf-8') as f:
        f.write(merged_code)

    print(f"\n✅ Code fusionné sauvegardé: {merged_file}")
    print(f"📊 Taille: {len(merged_code)} caractères")
    print(f"📝 Lignes: {merged_code.count(chr(10))} lignes")

    # Compter les scénarios (elif statements)
    scenario_count = merged_code.count("elif any(word in msg_lower")
    print(f"🎯 Scénarios détectés: {scenario_count}")

    return merged_code, merged_file

def integrate_into_ai_response_generator(merged_code):
    """
    Intègre les scénarios dans ai_response_generator.py
    """

    ai_response_file = os.path.join(
        os.path.dirname(os.path.abspath(__file__)),
        "src", "v14_mvp", "ai_response_generator.py"
    )

    if not os.path.exists(ai_response_file):
        print(f"❌ Fichier non trouvé: {ai_response_file}")
        return False

    print(f"\n🔧 Intégration dans: {ai_response_file}")

    with open(ai_response_file, 'r', encoding='utf-8') as f:
        original_content = f.read()

    # Trouver la fin des 100 premiers scénarios
    # On cherche le dernier elif avant la section "FALLBACK GÉNÉRAL"

    # Marker pour insertion
    insertion_marker = "# ═══════════════════════════════════════════════════════════════════\n        # 🔥 100 SCÉNARIOS ULTRA-DÉTAILLÉS - 500 ÉTAPES\n        # ═══════════════════════════════════════════════════════════════════"

    # Remplacer par 500 scénarios
    new_marker = "# ═══════════════════════════════════════════════════════════════════\n        # 🔥🔥🔥 500 SCÉNARIOS ULTRA-DÉTAILLÉS - 5000+ ÉTAPES 🔥🔥🔥\n        # ═══════════════════════════════════════════════════════════════════"

    modified_content = original_content.replace(insertion_marker, new_marker)

    # Trouver où insérer les nouveaux scénarios (après le scénario #100)
    # On cherche la section FALLBACK
    fallback_pattern = r"(\s+# ═+\s+# 🎯 FALLBACK GÉNÉRAL)"

    match = re.search(fallback_pattern, modified_content)

    if match:
        insert_pos = match.start()

        # Insérer les nouveaux scénarios avant le FALLBACK
        new_content = (
            modified_content[:insert_pos] +
            "\n\n" +
            merged_code +
            "\n\n" +
            modified_content[insert_pos:]
        )

        # Sauvegarder
        backup_file = ai_response_file + ".backup_100scenarios"
        with open(backup_file, 'w', encoding='utf-8') as f:
            f.write(original_content)
        print(f"💾 Backup créé: {backup_file}")

        with open(ai_response_file, 'w', encoding='utf-8') as f:
            f.write(new_content)

        print(f"✅ Intégration réussie!")
        print(f"📊 Taille originale: {len(original_content)} → Nouvelle: {len(new_content)}")
        print(f"📈 Augmentation: +{len(new_content) - len(original_content)} caractères")

        return True
    else:
        print("❌ Section FALLBACK non trouvée, impossible d'insérer")
        return False

if __name__ == "__main__":
    print("═══════════════════════════════════════════════════════════════════")
    print("  🚀 FUSION ET INTÉGRATION DES 500 SCÉNARIOS")
    print("═══════════════════════════════════════════════════════════════════\n")

    # Étape 1: Fusionner les fichiers générés
    merged_code, merged_file = merge_all_scenarios()

    # Étape 2: Intégrer dans ai_response_generator.py
    success = integrate_into_ai_response_generator(merged_code)

    if success:
        print("\n🎉 SUCCÈS TOTAL! Les 500 scénarios sont maintenant intégrés!")
    else:
        print("\n⚠️  Intégration partielle, vérifiez les logs ci-dessus")
