#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Script FINAL de correction de TOUTES les erreurs " inch
"""

import re

file_path = r"C:\Users\Utilisateur\Downloads\Nitrite-V18.5\src\v14_mvp\ai_knowledge_unified.py"

print("[*] Lecture fichier...")
with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

print(f"[OK] Fichier lu: {len(content)} caractères")

# Backup
backup_path = file_path + ".backup_final"
with open(backup_path, 'w', encoding='utf-8') as f:
    f.write(content)
print(f"[OK] Backup créé: {backup_path}")

print("\n[*] Application corrections globales...")

# CORRECTION 1: " inch, → ", dans keywords/tags
before = content
content = content.replace(' inch,', '",')
count1 = before.count(' inch,') - content.count(' inch,')
print(f"[OK] Correction 1: {count1}x ' inch,' -> '\",''")

# CORRECTION 2: inches] -> "] dans keywords/tags
before = content
content = content.replace(' inches]', '"]')
count2 = before.count(' inches]') - content.count(' inches]')
print(f"[OK] Correction 2: {count2}x ' inches]' -> '\"The]'")

# CORRECTION 3: inch] -> "] dans keywords/tags
before = content
content = content.replace(' inch]', '"]')
count3 = before.count(' inch]') - content.count(' inch]')
print(f"[OK] Correction 3: {count3}x ' inch]' -> '\"The]'")

# CORRECTION 4: Lignes avec "keywords": [...], "other"],
# Deja corrige par le script precedent, on skip

# CORRECTION 5: Lignes avec pattern complexe {"content": "...inch,
# Pattern: texte se terminant par " inch, au lieu de ",
# On cherche: inch, "keywords"
# On remplace par: ", "keywords"
before = content
content = re.sub(r' inch,\s*("keywords")', r'",\n \1', content)
count5 = (before.count(' inch, "keywords') - content.count(' inch, "keywords'))
print(f"[OK] Correction 5: {count5}x ' inch,' avant keywords -> '\",''")

# CORRECTION 6: Lignes se terminant avec inch a la fin d'un content
# Pattern: ... GPSload time difference minimal Gen4 inch,
# Doit etre: ... GPS",
# Chercher lignes content qui se terminent par " inch,
lines = content.split('\n')
fixed_lines = []
count6 = 0

for line in lines:
    # Si la ligne contient "content": et se termine par inch, ou inch,
    if '"content":' in line and (' inch,' in line or ' inch"' in line):
        # Remplacer le dernier inch, ou inch" par ",
        if line.rstrip().endswith(' inch,'):
            line = line.rstrip()[:-6] + '",'  # Enlever " inch," et mettre ","
            count6 += 1
        elif ' inch, "keywords"' in line:
            # Deja corrige par correction 5
            pass

    fixed_lines.append(line)

content = '\n'.join(fixed_lines)
print(f"[OK] Correction 6: {count6}x fins de content strings corrigees")

# CORRECTION 7: Patterns residuels - guillemets manquants apres inch
# Pattern: "item1 inch "item2" -> "item1", "item2"
before = content
content = re.sub(r'(\w+) inch\s+(")', r'\1", \2', content)
count7 = len(re.findall(r'(\w+) inch\s+(")', before)) - len(re.findall(r'(\w+) inch\s+(")', content))
print(f"[OK] Correction 7: {count7}x inch + space + quote -> quote + comma")

total_corrections = count1 + count2 + count3 + count5 + count6 + count7
print(f"\n[TOTAL] {total_corrections} corrections appliquées\n")

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

    print("\n" + "="*70)
    print("  ✓✓✓ SUCCES TOTAL - KNOWLEDGE BASE CHARGÉE!")
    print("="*70)
    print(f"  📚 Catégories: {stats['total_categories']}")
    print(f"  💡 Conseils totaux: {stats['total_tips']}")
    print(f"  📊 Moyenne/catégorie: {stats['avg_tips_per_category']:.1f}")
    print("="*70)
    print("\n[READY] Knowledge Base prête pour enrichissement!")
    print(f"[TODO] Ajouter {143 - stats['total_categories']} catégories restantes")
    print(f"[TODO] Atteindre 5000+ conseils (actuellement: {stats['total_tips']})")
    print()

except SyntaxError as e:
    print(f"\n[X] ERREUR SYNTAXE: {e}")
    print(f"    Ligne: {e.lineno}")
    if hasattr(e, 'text') and e.text:
        print(f"    Code: {e.text}")
    print(f"\n[!] Backup disponible: {backup_path}")
except Exception as e:
    print(f"\n[X] ERREUR: {e}")
    import traceback
    traceback.print_exc()
