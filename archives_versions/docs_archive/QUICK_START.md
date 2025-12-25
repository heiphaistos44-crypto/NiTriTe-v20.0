# Quick Start - NiTriTe V17 Beta

## Pour builder rapidement

### 1. Installer les dépendances (une seule fois)
```
Double-cliquer sur: INSTALL_DEPENDENCIES.bat
```

### 2. Builder la version portable
```
Double-cliquer sur: BUILD_PORTABLE_V17_FIXED.bat
```

### 3. Tester l'exécutable
```
Aller dans: dist\
Double-cliquer sur: NiTriTe_V17_Portable.exe
```

---

## Résumé des fichiers créés/corrigés

### Scripts de Build (NOUVEAUX - CORRIGÉS)
- ✅ **build_portable_fixed.py** - Script Python corrigé avec encodage UTF-8
- ✅ **BUILD_PORTABLE_V17_FIXED.bat** - Batch pour lancer le build facilement
- ✅ **INSTALL_DEPENDENCIES.bat** - Installer toutes les dépendances
- ✅ **TEST_DEPENDENCIES.bat** - Vérifier que tout est installé

### Documentation (NOUVELLE)
- ✅ **GUIDE_BUILD_COMPLET.md** - Guide complet et détaillé
- ✅ **QUICK_START.md** - Ce fichier (démarrage rapide)

### Scripts Existants (Non modifiés)
- ⚠️ **build_portable.py** - Ancien script (problèmes d'encodage sur Windows)
- ⚠️ **build_portable_v17.bat** - Ancien batch
- ✅ **LANCER_NITRITE_V17.bat** - Lancer en mode développement

---

## Problèmes Corrigés

### 1. Encodage UTF-8 (UnicodeEncodeError)
- ❌ **Avant**: Erreurs avec les emojis sur console Windows (cp1252)
- ✅ **Après**: Encodage UTF-8 forcé dans build_portable_fixed.py

### 2. Nettoyage incomplet
- ❌ **Avant**: Les dossiers __pycache__ n'étaient pas nettoyés partout
- ✅ **Après**: Nettoyage récursif dans tous les sous-dossiers

### 3. Installation des dépendances manquantes
- ❌ **Avant**: Installation manuelle une par une
- ✅ **Après**: Installation automatique si manquante

### 4. Package portable
- ❌ **Avant**: Seulement l'exécutable dans dist/
- ✅ **Après**: Package complet dans release/ avec README

### 5. Validation des fichiers
- ❌ **Avant**: Build échoue sans message clair
- ✅ **Après**: Vérification des fichiers requis avant le build

---

## Commandes Rapides

### Tester en mode développement
```batch
python src\v14_mvp\main_app.py
```
ou
```batch
LANCER_NITRITE_V17.bat
```

### Nettoyer manuellement
```batch
rmdir /s /q build dist release
```

### Vérifier Python
```batch
python --version
```
Doit afficher: Python 3.8 à 3.12

### Installer une dépendance manquante
```batch
python -m pip install <package_name>
```

---

## Arborescence après Build

```
Nitrite-V.17-Beta-Portable/
├── dist/
│   └── NiTriTe_V17_Portable.exe    ← EXECUTABLE
│
├── release/                         ← PACKAGE PORTABLE
│   ├── NiTriTe_V17_Portable.exe
│   ├── LANCER_V17_PORTABLE.bat
│   └── README_PORTABLE.txt
│
├── build/                           (cache PyInstaller)
│
└── (fichiers source...)
```

---

## Temps de Build Estimé

- **Première fois**: 5-10 minutes
- **Builds suivants**: 2-5 minutes (avec cache)
- **Taille finale**: ~50-100 MB

---

## Si Ça Ne Marche Pas

### 1. Python non trouvé
```
Réinstaller Python avec "Add to PATH" coché
```

### 2. Module non trouvé
```batch
INSTALL_DEPENDENCIES.bat
```

### 3. Build échoue
```batch
# Nettoyer et réessayer
rmdir /s /q build dist
python build_portable_fixed.py
```

### 4. Antivirus bloque
```
Ajouter le dossier du projet aux exclusions
```

---

## Support

Voir **GUIDE_BUILD_COMPLET.md** pour le dépannage complet.

---

**Version**: 1.0
**Date**: Décembre 2025
