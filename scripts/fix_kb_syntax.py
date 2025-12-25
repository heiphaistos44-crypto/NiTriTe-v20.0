#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Script de réparation des erreurs de syntaxe dans ai_knowledge_unified.py
Problème: guillemets doubles non échappés dans les strings
"""

import re

file_path = r"C:\Users\Utilisateur\Downloads\Nitrite-V18.5\src\v14_mvp\ai_knowledge_unified.py"

print("[*] Lecture fichier...")
with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

print(f"[OK] Fichier lu: {len(content)} caractères")

# Backup
backup_path = file_path + ".backup_syntax"
with open(backup_path, 'w', encoding='utf-8') as f:
    f.write(content)
print(f"[OK] Backup créé: {backup_path}")

# Corrections
print("[*] Application des corrections...")

# 1. Corriger "windows 11 inches" → "windows 11"
content = re.sub(r'windows 11 inch(?:es)?', 'windows 11', content, flags=re.IGNORECASE)

# 2. Corriger "12 inchesVHPWR" → "12VHPWR"
content = content.replace('12 inchesVHPWR', '12VHPWR')
content = content.replace('12inchesVHPWR', '12VHPWR')

# 3. Corriger les références de taille d'écran: remplacer par escaped quotes
# Mais d'abord, trouver tous les \" orphelins dans les content strings

# 4. Pour les mesures de moniteurs, utiliser une approche simple:
#    Remplacer X" par X-inch ou X inch selon contexte
patterns_to_fix = [
    (r'(\d+)"(\s+(?:1080p|1440p|4K|144Hz|240Hz|monitor|screen|display|ultrawide))', r'\1-inch\2'),
    (r'LG (\d+)GP', r'LG \1inch-GP'),  # LG 34"GP → LG 34inch-GP
    (r'Samsung (\d+)"', r'Samsung \1inch'),
]

for pattern, replacement in patterns_to_fix:
    content = re.sub(pattern, replacement, content)

# 5. Remplacer les " restants par inch dans le contexte de tailles
# Mais SEULEMENT dans les lignes "content"
lines = content.split('\n')
fixed_lines = []

for line in lines:
    if '"content"' in line and '{"content":' in line:
        # C'est une ligne de contenu, corriger les " dedans
        # Trouver le contenu entre les guillemets de "content": "..."
        match = re.search(r'"content":\s*"([^"]*(?:\\.[^"]*)*)"', line)
        if match:
            text_content = match.group(1)
            # Dans ce contenu, remplacer X" par X-inch
            fixed_content = re.sub(r'(\d+)"', r'\1-inch', text_content)
            # Reconstruire la ligne
            line = line.replace(text_content, fixed_content)

    fixed_lines.append(line)

content = '\n'.join(fixed_lines)

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
    from v14_mvp.ai_knowledge_unified import UnifiedKnowledgeBase
    kb = UnifiedKnowledgeBase()
    stats = kb.get_stats()
    print(f"[✓] SUCCES! KB chargée: {stats['categories']} catégories, {stats['tips']} conseils")
except SyntaxError as e:
    print(f"[X] ERREUR SYNTAXE: {e}")
    print(f"[!] Fichier backup disponible: {backup_path}")
except Exception as e:
    print(f"[X] ERREUR: {e}")
