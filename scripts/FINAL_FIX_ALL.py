#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
SCRIPT FINAL - Corrige TOUTES les erreurs de syntaxe
Part du backup_syntax qui a la bonne indentation
Applique toutes les corrections necessaires
"""

import re

file_path = r"C:\Users\Utilisateur\Downloads\Nitrite-V18.5\src\v14_mvp\ai_knowledge_unified.py"
backup_source = file_path + ".backup_syntax"

print("="*80)
print("  SCRIPT FINAL DE CORRECTION - ai_knowledge_unified.py")
print("="*80)
print()

# ETAPE 1: Restaurer backup avec bonne indentation
print("[1] Restauration backup avec indentation correcte...")
with open(backup_source, 'r', encoding='utf-8') as f:
    content = f.read()
print(f"[OK] Backup charge: {len(content)} caracteres")

# Backup du backup au cas où
with open(file_path + ".backup_BEFORE_FINAL", 'w', encoding='utf-8') as f:
    f.write(content)
print("[OK] Securite backup cree")

# ETAPE 2: Corrections globales ( inch -> ")
print("\n[2] Correction ' inch,' -> '\",''...")
count1 = content.count(' inch,')
content = content.replace(' inch,', '",')
print(f"[OK] {count1} occurrences corrigees")

print("\n[3] Correction ' inches]' -> '\"]'...")
count2 = content.count(' inches]')
content = content.replace(' inches]', '"]')
print(f"[OK] {count2} occurrences corrigees")

print("\n[4] Correction ' inch]' -> '\"]'...")
count3 = content.count(' inch]')
content = content.replace(' inch]', '"]')
print(f"[OK] {count3} occurrences corrigees")

# ETAPE 3: Corriger keywords malformes SPECIFIQUES
print("\n[5] Correction keywords arrays malformes...")
count4 = 0

# Pattern: "keywords": ["item1"], "item2", "item3"],
# -> "keywords": ["item1", "item2", "item3"],
# Ligne par ligne pour preserver indentation

lines = content.split('\n')
fixed_lines = []

for line in lines:
    original = line

    # Si ligne "keywords" ou "tags" SANS "difficulty" (pas compacte)
    # ET contient ], "
    if ('"keywords":' in line or '"tags":' in line) and '"difficulty":' not in line and '], "' in line:
        # Pattern: ], "text"], -> , "text"],
        line = re.sub(r'\], "([^"]+)"\],', r', "\1"],', line)
        if line != original:
            count4 += 1

    fixed_lines.append(line)

content = '\n'.join(fixed_lines)
print(f"[OK] {count4} keywords arrays corriges")

# ETAPE 4: Corriger lignes compactes
print("\n[6] Correction lignes compactes...")
lines = content.split('\n')
fixed_lines = []
count5 = 0

for line in lines:
    if '{"content":' in line and '"keywords":' in line and '"difficulty":' in line:
        # Fermer keywords avant difficulty
        line = re.sub(r'",\s*"difficulty":', r'"], "difficulty":', line)
        # Fermer tags avant related_tools
        line = re.sub(r'",\s*"related_tools":', r'"], "related_tools":', line)
        count5 += 1

    fixed_lines.append(line)

content = '\n'.join(fixed_lines)
print(f"[OK] {count5} lignes compactes corrigees")

# ETAPE 5: Corrections specifiques
print("\n[7] Corrections specifiques...")
# Ligne 1929: 27", 150% -> 27 inch, 150%
if '27", 150%' in content:
    content = content.replace('27", 150%', '27 inch, 150%')
    print("[OK] Ligne 1929 corrigee (27 inch)")

# ETAPE 6: Ecrire fichier final
print("\n[8] Ecriture fichier final...")
with open(file_path, 'w', encoding='utf-8') as f:
    f.write(content)
print(f"[OK] Fichier ecrit: {file_path}")

# ETAPE 7: Test import
print("\n[9] Test import final...")
print("-"*80)

try:
    import sys
    sys.path.insert(0, r"C:\Users\Utilisateur\Downloads\Nitrite-V18.5\src")

    # Force reload
    if 'v14_mvp.ai_knowledge_unified' in sys.modules:
        del sys.modules['v14_mvp.ai_knowledge_unified']

    from v14_mvp.ai_knowledge_unified import UnifiedKnowledgeBase
    kb = UnifiedKnowledgeBase()
    stats = kb.get_stats()

    print()
    print("="*80)
    print("   ✓✓✓ SUCCES TOTAL - KNOWLEDGE BASE OPERATIONNELLE ✓✓✓")
    print("="*80)
    print()
    print(f"   Categories totales:  {stats['total_categories']}")
    print(f"   Conseils totaux:     {stats['total_tips']}")
    print(f"   Moyenne/categorie:   {stats['avg_tips_per_category']:.1f}")
    print()
    print("="*80)
    print()
    print(f"[OBJECTIF] 143 categories (+{143 - stats['total_categories']} restantes)")
    print(f"[OBJECTIF] 5000+ conseils (+{5000 - stats['total_tips']} restants)")
    print()
    print("[READY] Knowledge Base prete pour enrichissement!")
    print()

except SyntaxError as e:
    print()
    print("[X] ERREUR SYNTAXE:")
    print(f"    Ligne {e.lineno}: {e}")
    if hasattr(e, 'text') and e.text:
        print(f"    Code: {e.text.strip()}")
    print()
    print(f"[!] Backup securite: {file_path}.backup_BEFORE_FINAL")

except Exception as e:
    print()
    print(f"[X] ERREUR: {e}")
    import traceback
    traceback.print_exc()
