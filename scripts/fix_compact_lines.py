#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Script pour corriger les lignes compactes malformees
Format actuel: {"content": "...", "keywords": ["x", "y", "z", "difficulty": ...}
Format cible: {"content": "...", "keywords": ["x", "y", "z"], "difficulty": ...}
"""

import re

file_path = r"C:\Users\Utilisateur\Downloads\Nitrite-V18.5\src\v14_mvp\ai_knowledge_unified.py"

print("[*] Lecture fichier...")
with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

print(f"[OK] Fichier lu: {len(content)} caracteres")

# Backup
backup_path = file_path + ".backup_compact"
with open(backup_path, 'w', encoding='utf-8') as f:
    f.write(content)
print(f"[OK] Backup: {backup_path}")

print("\n[*] Correction lignes compactes malformees...")

lines = content.split('\n')
fixed_lines = []
fixed_count = 0

for line_num, line in enumerate(lines, 1):
    # Detecter lignes compactes problematiques:
    # {"content": "...", "keywords": [..., "difficulty": ...}
    # Le ", "difficulty" devrait etre ], "difficulty"

    if '{"content":' in line and '"keywords":' in line and '"difficulty":' in line:
        # Cette ligne est compacte et potentiellement malformee

        # Pattern 1: Fermer keywords avant "difficulty"
        # ... "nvme", "difficulty" -> ... "nvme"], "difficulty"
        line = re.sub(r'",\s*"difficulty":', r'"], "difficulty":', line)

        # Pattern 2: Fermer tags avant "related_tools"
        # ... "performance", "related_tools" -> ... "performance"], "related_tools"
        line = re.sub(r'",\s*"related_tools":', r'"], "related_tools":', line)

        # Pattern 3: S'assurer que tags a sa valeur en array
        # "tags": ["performance", "related_tools" -> "tags": ["performance"], "related_tools"
        # Deja corrige par Pattern 2

        fixed_count += 1
        if fixed_count <= 5:
            print(f"  [L{line_num}] Corrigee")

    fixed_lines.append(line)

content = '\n'.join(fixed_lines)

print(f"\n[OK] {fixed_count} lignes compactes corrigees")

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
    print("   SUCCESS - KNOWLEDGE BASE CHARGEE!")
    print("="*80)
    print(f"   Categories:     {stats['total_categories']}")
    print(f"   Conseils:       {stats['total_tips']}")
    print(f"   Moyenne/cat:    {stats['avg_tips_per_category']:.1f}")
    print("="*80)
    print()
    print(f"[READY] KB operationnelle!")
    print(f"[TODO] Enrichir: +{143 - stats['total_categories']} categories")
    print(f"[TODO] Atteindre 5000+ conseils (+{5000 - stats['total_tips']})")
    print()

except SyntaxError as e:
    print(f"\n[X] Syntax Error ligne {e.lineno}: {e}")
except Exception as e:
    print(f"\n[X] Erreur: {e}")
    import traceback
    traceback.print_exc()
