#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Script de correction ciblée des erreurs de syntaxe dans ai_knowledge_unified.py
Corrige UNIQUEMENT les guillemets de structure Python, pas le contenu
"""

import re

file_path = r"C:\Users\Utilisateur\Downloads\Nitrite-V18.5\src\v14_mvp\ai_knowledge_unified.py"

print("[*] Lecture fichier...")
with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

print(f"[OK] Fichier lu: {len(content)} caractères")

# Backup
backup_path = file_path + ".backup_targeted"
with open(backup_path, 'w', encoding='utf-8') as f:
    f.write(content)
print(f"[OK] Backup créé: {backup_path}")

print("[*] Application des corrections ciblées...")

# CORRECTION 1: Fins de "content" string tronquées avec " inch,
# Pattern: "content": "...texte... inch,
# Doit être: "content": "...texte...",
content = re.sub(
    r'(\s+"content":\s+"[^"]*) inch,\s*$',
    r'\1",',
    content,
    flags=re.MULTILINE
)
print("[OK] Correction 1: Fins de content strings")

# CORRECTION 2: "keywords": [...... inch -> "keywords": [......"]
# Pattern: "keywords": [....text inch,
# Doit être: "keywords": [...text"],
content = re.sub(
    r'(\s+"keywords":\s+\[[^\]]*) inch,',
    r'\1"],',
    content
)
print("[OK] Correction 2: Fins de keywords arrays")

# CORRECTION 3: Guillemets manquants dans keywords
# Pattern: ["keyword1 inch "keyword2"] -> ["keyword1", "keyword2"]
content = re.sub(
    r'(\[[^\]]*") inch (")',
    r'\1, \2',
    content
)
print("[OK] Correction 3: Guillemets séparateurs keywords")

# CORRECTION 4: "related_tools": [...... inch -> "related_tools": [......"]
content = re.sub(
    r'(\s+"related_tools":\s+\[[^\]]*) inch\]',
    r'\1"]',
    content
)
print("[OK] Correction 4: Related tools arrays")

# CORRECTION 5: Doubles espaces causés par suppressions
content = re.sub(r'  +', ' ', content)
print("[OK] Correction 5: Espaces multiples")

# CORRECTION 6: Cases spéciales - "windows 11 inches]" -> "windows 11"]
content = content.replace(' inches]', '"]')
content = content.replace(' inch]', '"]')
print("[OK] Correction 6: Cases spéciales")

# CORRECTION 7: "12 inchesVHPWR" -> "12vhpwr"
content = content.replace('inchesVHPWR', 'vhpwr')
content = content.replace('inches VHPWR', 'vhpwr')
print("[OK] Correction 7: inchesVHPWR")

# CORRECTION 8: Corriger les keywords arrays malformés
# Pattern: ["keyword inch, "other"] -> ["keyword", "other"]
content = re.sub(
    r'(\["[^"]*) inch,\s*(")',
    r'\1", \2',
    content
)
print("[OK] Correction 8: Keywords malformés")

# CORRECTION 9: Tags arrays similaires
content = re.sub(
    r'("tags":\s+\["[^"]*) inch,',
    r'\1",',
    content
)
print("[OK] Correction 9: Tags arrays")

# CORRECTION 10: Supprimer inch orphelins en fin de ligne
content = re.sub(r' inch\s*$', '"', content, flags=re.MULTILINE)
print("[OK] Correction 10: inch orphelins")

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

    # Force reload if already imported
    if 'v14_mvp.ai_knowledge_unified' in sys.modules:
        del sys.modules['v14_mvp.ai_knowledge_unified']

    from v14_mvp.ai_knowledge_unified import UnifiedKnowledgeBase
    kb = UnifiedKnowledgeBase()
    stats = kb.get_stats()
    print(f"[✓] SUCCES! KB chargée: {stats['total_categories']} catégories, {stats['total_tips']} conseils")
except SyntaxError as e:
    print(f"[X] ERREUR SYNTAXE: {e}")
    print(f"[!] Ligne problématique: {e.lineno}")
    print(f"[!] Fichier backup disponible: {backup_path}")
except Exception as e:
    print(f"[X] ERREUR: {e}")
    import traceback
    traceback.print_exc()
