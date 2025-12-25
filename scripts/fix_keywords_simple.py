#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Script simple pour corriger les keywords malformés
"""

import re

file_path = r"C:\Users\Utilisateur\Downloads\Nitrite-V18.5\src\v14_mvp\ai_knowledge_unified.py"

print("[*] Restauration backup...")
backup_path = file_path + ".backup_keywords"
with open(backup_path, 'r', encoding='utf-8') as f:
    content = f.read()
print(f"[OK] Backup restauré: {len(content)} caractères")

print("[*] Correction des keywords arrays...")

# Approche simple: ligne par ligne
lines = content.split('\n')
fixed_lines = []
corrections = 0

for line in lines:
    # Chercher pattern: "keywords": ["item1"], "item2", "item3"],
    match = re.search(r'^(\s*"keywords":\s+\[)"([^"]+)"\],\s*(".*"\]),', line)

    if match:
        indent = match.group(1)  # '    "keywords": ['
        first_item = match.group(2)  # 'item1'
        rest = match.group(3)  # '"item2", "item3"]'

        # Enlever le ] final et le reconstruire
        rest_clean = rest.rstrip('],')  # Enlever "],

        # Reconstituer
        fixed_line = f'{indent}"{first_item}", {rest_clean}],'
        fixed_lines.append(fixed_line)
        corrections += 1

        print(f"[FIX] Ligne {len(fixed_lines)}:")
        print(f"  AVANT: {line[:80]}...")
        print(f"  APRES: {fixed_line[:80]}...")
    else:
        fixed_lines.append(line)

content = '\n'.join(fixed_lines)

print(f"\n[OK] {corrections} corrections appliquées")

# Écrire
print("[*] Écriture fichier...")
with open(file_path, 'w', encoding='utf-8') as f:
    f.write(content)
print(f"[OK] Fichier écrit: {file_path}")

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
    print(f"[✓✓✓] SUCCES TOTAL!")
    print(f"    📚 Catégories: {stats['total_categories']}")
    print(f"    💡 Conseils: {stats['total_tips']}")
    print()
    print(f"[READY] Knowledge Base prête pour enrichissement!")
except SyntaxError as e:
    print(f"[X] Syntaxe Error: {e}")
    print(f"    Ligne {e.lineno}")
    # Afficher la ligne problématique
    lines = content.split('\n')
    if e.lineno and e.lineno <= len(lines):
        print(f"    Code: {lines[e.lineno-1]}")
except Exception as e:
    print(f"[X] Erreur: {e}")
    import traceback
    traceback.print_exc()
