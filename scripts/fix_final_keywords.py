#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Script final pour corriger le pattern: [...], "item"],
Doit devenir: [..., "item"],
"""

import re

file_path = r"C:\Users\Utilisateur\Downloads\Nitrite-V18.5\src\v14_mvp\ai_knowledge_unified.py"

print("[*] Lecture fichier...")
with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

print(f"[OK] Fichier lu: {len(content)} caracteres")

# Backup
backup_path = file_path + ".backup_final2"
with open(file_path, 'w', encoding='utf-8') as f:
    f.write(content)
print(f"[OK] Backup: {backup_path}")

print("\n[*] Correction pattern [...], \"item\"],...")

# Pattern: ], "text"],
# Remplacer par: , "text"],
# Mais SEULEMENT dans le contexte "keywords": ou "tags":

fixed = 0

# Ligne par ligne pour un contrôle précis
lines = content.split('\n')
fixed_lines = []

for line_num, line in enumerate(lines, 1):
    original_line = line

    # Si la ligne contient "keywords": ou "tags": ET le pattern ], "...",
    if ('"keywords":' in line or '"tags":' in line) and '], "' in line:
        # Pattern: ], "item"], ou ], "item1", "item2"],
        # Remplacer ALL occurrences de ], " par , " dans cette ligne
        new_line = line.replace('], "', ', "')
        if new_line != line:
            fixed += 1
            if fixed <= 5:  # Afficher les 5 premiers
                print(f"  [L{line_num}] {line[:60]}...")
                print(f"       -> {new_line[:60]}...")
            line = new_line

    fixed_lines.append(line)

content = '\n'.join(fixed_lines)

print(f"\n[OK] {fixed} lignes corrigees")

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

    print("\n" + "="*70)
    print("  SUCCESS! KNOWLEDGE BASE CHARGEE!")
    print("="*70)
    print(f"  Categories: {stats['total_categories']}")
    print(f"  Conseils: {stats['total_tips']}")
    print(f"  Moyenne: {stats['avg_tips_per_category']:.1f} conseils/categorie")
    print("="*70)
    print()
    print(f"[TODO] Enrichir KB: {143 - stats['total_categories']} categories restantes")
    print(f"[TODO] Atteindre 5000+ conseils (actuellement: {stats['total_tips']})")
    print()

except SyntaxError as e:
    print(f"\n[X] Syntax Error ligne {e.lineno}: {e}")
    if hasattr(e, 'text'):
        print(f"    {e.text}")
except Exception as e:
    print(f"\n[X] Erreur: {e}")
    import traceback
    traceback.print_exc()
