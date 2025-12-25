#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Script de correction des arrays keywords malformés
Corrige: "keywords": ["word1"], "word2", "word3"],
En:      "keywords": ["word1", "word2", "word3"],
"""

import re

file_path = r"C:\Users\Utilisateur\Downloads\Nitrite-V18.5\src\v14_mvp\ai_knowledge_unified.py"

print("[*] Lecture fichier...")
with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

print(f"[OK] Fichier lu: {len(content)} caractères")

# Backup
backup_path = file_path + ".backup_keywords"
with open(backup_path, 'w', encoding='utf-8') as f:
    f.write(content)
print(f"[OK] Backup créé: {backup_path}")

print("[*] Correction des keywords arrays malformés...")

# Pattern: "keywords": ["item1"], "item2", "item3"],
# Remplacer par: "keywords": ["item1", "item2", "item3"],
#
# Stratégie: Trouver toutes les lignes avec ce pattern et reconstruire correctement

def fix_keywords_line(match):
    """
    Fonction de callback pour re.sub
    Prend une ligne malformée et la reconstruit correctement
    """
    # match.group(1) = indentation + "keywords": [
    # match.group(2) = premier item entre guillemets
    # match.group(3) = le reste avec ], "item2", "item3"],

    indent = match.group(1)
    first_item = match.group(2)
    rest = match.group(3)

    # Extraire tous les items du reste: "item2", "item3"
    # Pattern pour trouver tous les "text" strings
    extra_items = re.findall(r'"([^"]+)"', rest)

    # Reconstruire la liste complète
    all_items = [first_item] + extra_items
    items_str = ', '.join([f'"{item}"' for item in all_items])

    return f'{indent}[{items_str}],'

# Pattern regex pour capturer:
# Groupe 1: indentation + "keywords": [
# Groupe 2: premier keyword
# Groupe 3: le reste jusqu'à ],
pattern = r'(\s*"keywords":\s+\[)"([^"]+)"\](,\s*"[^"]+(?:"|"\s*,\s*"[^"]+)*"\],)'

# Test du pattern d'abord
test_line = '"keywords": ["uhd 770"], "igpu", "quicksync"],'
test_match = re.search(pattern, test_line)
if test_match:
    print(f"[TEST] Pattern fonctionne!")
    print(f"  Input:  {test_line}")
    result = fix_keywords_line(test_match)
    print(f"  Output: \"keywords\": {result}")
else:
    print(f"[WARN] Pattern ne matche pas la ligne test")

# Appliquer sur tout le fichier
original_content = content
content = re.sub(pattern, fix_keywords_line, content)

corrections_count = len(re.findall(pattern, original_content))
print(f"[OK] {corrections_count} lignes keywords corrigées")

# Écrire le fichier corrigé
print("[*] Écriture fichier corrigé...")
with open(file_path, 'w', encoding='utf-8') as f:
    f.write(content)

print(f"[OK] Fichier corrigé écrit: {file_path}")

# Tester l'import
print("[*] Test import...")
try:
    import sys
    sys.path.insert(0, r"C:\Users\Utilisateur\Downloads\Nitrite-V18.5\src")

    # Force reload
    if 'v14_mvp.ai_knowledge_unified' in sys.modules:
        del sys.modules['v14_mvp.ai_knowledge_unified']

    from v14_mvp.ai_knowledge_unified import UnifiedKnowledgeBase
    kb = UnifiedKnowledgeBase()
    stats = kb.get_stats()
    print(f"[✓] SUCCES! KB chargée:")
    print(f"    Catégories: {stats['total_categories']}")
    print(f"    Conseils: {stats['total_tips']}")
except SyntaxError as e:
    print(f"[X] ERREUR SYNTAXE: {e}")
    print(f"    Ligne: {e.lineno}")
    print(f"[!] Backup: {backup_path}")
except Exception as e:
    print(f"[X] ERREUR: {e}")
    import traceback
    traceback.print_exc()
