# Guide des Scripts d'Ajout de Catégories

## Vue d'ensemble

Ce dossier contient plusieurs scripts pour enrichir massivement `ai_knowledge_unified.py` avec 28 nouvelles catégories techniques.

---

## Scripts Disponibles

### 1. `add_28_categories.py` (INITIAL - Problème d'encodage)
**Description**: Script initial complet avec toutes les catégories.
**Problème**: Erreur d'encodage Windows (CP1252 vs UTF-8) lors de l'affichage.
**Statut**: ❌ Ne pas utiliser directement

### 2. `batch_add_categories.py` ✅ **RECOMMANDÉ**
**Description**: Script batch fonctionnel qui a ajouté avec succès 4 catégories (Storage × 2, Motherboard/PSU × 2).
**Fonctionnalités**:
- Gestion UTF-8 correcte
- Format JSON compact pour les conseils
- Vérification automatique post-insertion
- Output console sans caractères spéciaux problématiques

**Usage**:
```bash
python batch_add_categories.py
```

**Résultat**:
```
SUCCESS!
  Categories: 10
  Total Tips: 288
  Avg Tips/Cat: 28.8
```

### 3. `add_remaining_categories.py`
**Description**: Script de référence pour les 22 catégories restantes.
**Statut**: 📝 Template/placeholder

---

## Comment Ajouter les 22 Catégories Restantes

### Méthode Recommandée: Lots de 4-5 Catégories

#### Lot 1: COOLING + MONITORS (4 catégories) - PROCHAINE ÉTAPE

Créer `batch_add_lot2_cooling_monitors.py`:

```python
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Batch Lot 2: Cooling (2) + Monitors (2)
"""

import sys

def add_cooling_and_monitors():
    file_path = r"C:\Users\Utilisateur\Downloads\Nitrite-V18.5\src\v14_mvp\ai_knowledge_unified.py"

    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    insertion_point = content.rfind("        return kb")

    new_code = '''
        # COOLING (2 categories)
        kb["cooling_air_vs_aio"] = {
            "metadata": {
                "priority": 4,
                "tags": ["cooling", "hardware", "temperature"],
                "difficulty": "intermediate",
                "description": "Air cooling vs AIO liquid cooling comparison"
            },
            "tips": [
                {"content": "Noctua NH-D15: Best air cooler 2024, 220W TDP cooling capacity, rivals 240mm AIOs, silent 1500 RPM, 100 euros", "keywords": ["nh-d15", "noctua", "air"], "difficulty": "intermediate", "tags": ["air-cooling"], "related_tools": []},
                # ... (20+ tips)
            ]
        }

        kb["thermal_solutions_laptops"] = {
            # ...
        }

        kb["monitor_gaming_specs"] = {
            # ...
        }

        kb["monitor_resolution_guide"] = {
            # ...
        }
'''

    new_content = content[:insertion_point] + new_code + "\n" + content[insertion_point:]

    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(new_content)

    return True

if __name__ == "__main__":
    print("Adding Lot 2: Cooling + Monitors...")
    add_cooling_and_monitors()
    print("Done!")
```

---

## Vérification Après Chaque Lot

```python
from ai_knowledge_unified import UnifiedKnowledgeBase

kb = UnifiedKnowledgeBase()
stats = kb.get_stats()

print(f"Categories: {stats['categories']}")
print(f"Total Tips: {stats['tips']}")
print(f"Avg: {stats['avg_tips_per_category']:.1f}")

# Lister toutes les catégories
for i, cat in enumerate(kb.get_all_categories(), 1):
    print(f"{i}. {cat}")
```

---

## Planning d'Ajout Recommandé

| Lot | Catégories | Conseils estimés | Script | Statut |
|-----|-----------|------------------|--------|--------|
| 0 | Initial (4) | 129 | - | ✅ Pré-existant |
| 1 | RAM + Storage + Mobo/PSU (6) | 160 | `batch_add_categories.py` | ✅ FAIT |
| 2 | Cooling + Monitors (4) | 100 | À créer | ⏳ Suivant |
| 3 | Monitors + Peripherals + Windows (5) | 125 | À créer | ⏳ |
| 4 | Windows + Drivers (5) | 125 | À créer | ⏳ |
| 5 | Gaming Performance (5) | 125 | À créer | ⏳ |
| 6 | Networking (3) | 75 | À créer | ⏳ |

**Total**: 32 catégories, ~839+ conseils

---

## Format Standard des Conseils

### Format Compact (recommandé pour batch)
```python
{"content": "Description technique", "keywords": ["kw1", "kw2"], "difficulty": "intermediate", "tags": ["tag1"], "related_tools": ["Tool1"]}
```

### Format Étendu (lisible)
```python
{
    "content": "Description technique complète avec chiffres et spécifications réelles",
    "keywords": ["keyword1", "keyword2", "keyword3"],
    "difficulty": "beginner|intermediate|advanced|expert",
    "tags": ["tag1", "tag2", "tag3"],
    "related_tools": ["Tool1", "Tool2"]
}
```

---

## Checklist Qualité par Conseil

- [ ] Contenu technique RÉEL (pas de placeholder)
- [ ] Chiffres précis (MHz, FPS, prix, etc.)
- [ ] Noms de produits/logiciels réels
- [ ] 3+ keywords pertinents
- [ ] Difficulté appropriée
- [ ] Tags descriptifs (2-3 minimum)
- [ ] Related tools si applicable

---

## Dépannage

### Erreur d'encodage console
**Problème**: `UnicodeEncodeError: 'charmap' codec can't encode character`
**Solution**: Utiliser le format batch sans output fancy (pas de ✓, ✗, etc.)

### Erreur de syntaxe Python
**Problème**: `SyntaxError: invalid syntax`
**Solution**: Vérifier les guillemets, virgules, accolades dans les conseils JSON

### Module non trouvé
**Problème**: `ModuleNotFoundError: No module named 'ai_knowledge_unified'`
**Solution**: Vérifier le PYTHONPATH ou `sys.path.insert(0, ...)`

---

## Contacts et Support

**Fichier cible**: `C:\Users\Utilisateur\Downloads\Nitrite-V18.5\src\v14_mvp\ai_knowledge_unified.py`
**Backup recommandé**: Faire une copie avant chaque batch
**Rapport détaillé**: Voir `RAPPORT_AJOUT_CATEGORIES.md`

---

## Progression Globale

```
[████████░░░░░░░░░░░░] 31.3% (10/32 catégories)
```

**Catégories ajoutées**: 10/32 (6 nouvelles)
**Conseils ajoutés**: 288 (~19-24% de l'objectif)
**Prochaine étape**: Lot 2 (Cooling + Monitors)
