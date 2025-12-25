#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Script INTELLIGENT pour corriger keywords malformés
Ne touche PAS aux lignes compactes avec "difficulty" sur la même ligne
"""

import re

file_path = r"C:\Users\Utilisateur\Downloads\Nitrite-V18.5\src\v14_mvp\ai_knowledge_unified.py"

print("[*] Lecture fichier...")
with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

print(f"[OK] Fichier lu: {len(content)} caracteres")

# Backup
backup_path = file_path + ".backup_smart"
with open(backup_path, 'w', encoding='utf-8') as f:
    f.write(content)
print(f"[OK] Backup: {backup_path}")

print("\n[*] Correction intelligente keywords/tags...")

lines = content.split('\n')
fixed_lines = []
fixed_count = 0

for line_num, line in enumerate(lines, 1):
    original_line = line

    # Condition 1: La ligne contient "keywords": ou "tags":
    # Condition 2: La ligne NE contient PAS "difficulty": (eviter lignes compactes)
    # Condition 3: La ligne contient le pattern ], "
    if ('"keywords":' in line or '"tags":' in line) and '"difficulty":' not in line and '], "' in line:

        # Pattern specifique: ], "text"],
        # On veut remplacer par: , "text"],
        # MAIS seulement si c'est suivi de ], (fermeture finale)

        # Regex: ], "([^"]+)"\],
        # Remplacer par: , "\1"],
        new_line = re.sub(r'\], "([^"]+)"\],', r', "\1"],', line)

        if new_line != line:
            fixed_count += 1
            if fixed_count <= 10:
                print(f"  [L{line_num}] AVANT: {line[:70]}...")
                print(f"          APRES: {new_line[:70]}...")
            line = new_line

    fixed_lines.append(line)

content = '\n'.join(fixed_lines)

print(f"\n[OK] {fixed_count} lignes corrigees")

# Ecrire
print("\n[*] Ecriture fichier...")
with open(file_path, 'w', encoding='utf-8') as f:
    f.write(content)
print(f"[OK] Fichier ecrit")

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

    print("\n" + "="*80)
    print("   ✓✓✓ SUCCESS - KNOWLEDGE BASE CHARGEE ✓✓✓")
    print("="*80)
    print(f"   Categories:     {stats['total_categories']}")
    print(f"   Conseils:       {stats['total_tips']}")
    print(f"   Moyenne/cat:    {stats['avg_tips_per_category']:.1f}")
    print("="*80)
    print()
    print(f"[NEXT] Enrichir KB: +{143 - stats['total_categories']} categories")
    print(f"[NEXT] Atteindre 5000+ conseils (+{5000 - stats['total_tips']} restants)")
    print()

except SyntaxError as e:
    print(f"\n[X] Syntax Error ligne {e.lineno}: {e}")
except Exception as e:
    print(f"\n[X] Erreur: {e}")
    import traceback
    traceback.print_exc()
