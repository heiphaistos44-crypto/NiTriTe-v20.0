# Guide Complet de Build - NiTriTe V17 Beta

## Table des matières
1. [Prérequis](#prérequis)
2. [Installation](#installation)
3. [Build de la version portable](#build-de-la-version-portable)
4. [Tests](#tests)
5. [Dépannage](#dépannage)

---

## Prérequis

### Système d'exploitation
- **Windows 10/11** (64-bit recommandé)
- **Droits administrateur** (pour certaines installations)

### Python
- **Version requise**: Python 3.8 à 3.12
- **Téléchargement**: https://www.python.org/downloads/

**IMPORTANT lors de l'installation de Python:**
- ✅ Cochez "Add Python to PATH"
- ✅ Cochez "Install for all users" (optionnel mais recommandé)

### Vérifier votre installation Python
```batch
python --version
```
Doit afficher: `Python 3.x.x` (où x.x est entre 8.0 et 12.x)

---

## Installation

### Option 1: Installation Automatique (RECOMMANDÉ)

1. **Double-cliquez sur**: `INSTALL_DEPENDENCIES.bat`
2. Attendez que toutes les dépendances s'installent
3. Vérifiez qu'il n'y a pas d'erreurs

### Option 2: Installation Manuelle

```batch
# Mettre à jour pip
python -m pip install --upgrade pip

# Installer les dépendances
python -m pip install -r requirements.txt
```

### Vérifier les dépendances

**Double-cliquez sur**: `TEST_DEPENDENCIES.bat`

Ou en ligne de commande:
```batch
python -c "import customtkinter; import PIL; import requests; import psutil; import PyInstaller; print('Toutes les dependances OK')"
```

---

## Build de la version portable

### Méthode Simple (RECOMMANDÉ)

1. **Double-cliquez sur**: `BUILD_PORTABLE_V17_FIXED.bat`
2. Attendez la fin du build (5-10 minutes)
3. L'exécutable sera dans le dossier `dist/`

### Méthode Avancée (Ligne de commande)

```batch
# Nettoyer les anciens builds
python build_portable_fixed.py

# Ou utiliser l'ancien script (peut avoir des problèmes d'encodage)
python build_portable.py
```

### Résultats du Build

Après un build réussi:
- **Exécutable**: `dist/NiTriTe_V17_Portable.exe`
- **Package portable**: `release/` (contient tout le nécessaire)

---

## Tests

### Test en Mode Développement

Avant de compiler, testez l'application:

```batch
# Double-cliquez sur
LANCER_NITRITE_V17.bat

# Ou en ligne de commande
python src/v14_mvp/main_app.py
```

### Test de l'Exécutable

Après compilation:
1. Allez dans le dossier `dist/`
2. Double-cliquez sur `NiTriTe_V17_Portable.exe`
3. Vérifiez que toutes les fonctionnalités marchent:
   - ✅ Affichage de la liste des applications
   - ✅ Recherche fonctionnelle
   - ✅ Navigation entre les pages
   - ✅ Installation d'applications (en mode admin si nécessaire)

---

## Structure du Projet

```
Nitrite-V17-Beta-Portable/
│
├── src/                          # Code source
│   ├── v14_mvp/                  # Application principale V14
│   │   ├── main_app.py           # Point d'entrée
│   │   ├── design_system.py      # Système de design
│   │   ├── navigation.py         # Navigation
│   │   ├── pages_*.py            # Pages de l'application
│   │   ├── components.py         # Composants réutilisables
│   │   └── installer.py          # Gestionnaire d'installation
│   │
│   └── (autres modules legacy)
│
├── data/
│   └── programs.json             # Base de données des applications
│
├── assets/
│   └── logo.ico                  # Icône de l'application
│
├── config/                       # Fichiers de configuration
│
├── NiTriTe_V17_Portable.spec     # Configuration PyInstaller
├── requirements.txt              # Dépendances Python
│
├── build_portable_fixed.py       # Script de build (CORRIGÉ)
├── build_portable.py             # Script de build original
│
├── BUILD_PORTABLE_V17_FIXED.bat  # Lancer le build (RECOMMANDÉ)
├── INSTALL_DEPENDENCIES.bat      # Installer dépendances
├── TEST_DEPENDENCIES.bat         # Tester dépendances
└── LANCER_NITRITE_V17.bat        # Tester en mode dev
```

---

## Dépannage

### Problème: "Python n'est pas reconnu"

**Solution**:
1. Réinstallez Python
2. **COCHEZ** "Add Python to PATH"
3. Redémarrez votre ordinateur

### Problème: Erreurs d'encodage (UnicodeEncodeError)

**Solution**:
- ✅ Utilisez `BUILD_PORTABLE_V17_FIXED.bat` au lieu de l'ancien script
- ✅ Ou utilisez `python build_portable_fixed.py`

### Problème: Module 'customtkinter' non trouvé

**Solution**:
```batch
python -m pip install customtkinter
```

Ou réinstallez toutes les dépendances:
```batch
INSTALL_DEPENDENCIES.bat
```

### Problème: Build échoue avec "FileNotFoundError"

**Vérifications**:
1. Le fichier `data/programs.json` existe-t-il?
2. Le fichier `src/v14_mvp/main_app.py` existe-t-il?
3. Le fichier `NiTriTe_V17_Portable.spec` existe-t-il?

**Solution**:
```batch
# Vérifier les fichiers
dir data\programs.json
dir src\v14_mvp\main_app.py
dir NiTriTe_V17_Portable.spec
```

### Problème: L'exécutable ne se lance pas

**Solutions possibles**:
1. **Antivirus**: Ajoutez le dossier `dist/` aux exclusions
2. **Permissions**: Lancez en tant qu'administrateur
3. **Fichiers manquants**: Vérifiez que `data/` et `assets/` sont bien inclus

### Problème: L'application se lance mais les données sont vides

**Cause**: Le fichier `data/programs.json` n'est pas trouvé

**Solution**:
1. Vérifiez que le fichier existe
2. Vérifiez le contenu du fichier (doit être un JSON valide)
3. Testez en mode dev d'abord: `LANCER_NITRITE_V17.bat`

### Problème: Build très lent (>10 minutes)

**Causes possibles**:
- Antivirus qui scanne chaque fichier
- Disque dur lent (HDD vs SSD)

**Solutions**:
- Désactivez temporairement l'antivirus
- Ajoutez le dossier du projet aux exclusions
- Utilisez un SSD si possible

---

## Optimisations du Build

### Réduire la taille de l'exécutable

Dans `NiTriTe_V17_Portable.spec`, vous pouvez:

1. **Activer UPX** (déjà activé):
```python
upx=True
```

2. **Exclure des modules non utilisés**:
```python
excludes=['matplotlib', 'numpy', 'pandas']
```

3. **Optimiser le code Python**:
```python
optimize=2  # Au lieu de 0
```

### Accélérer le Build

1. **Désactiver le nettoyage automatique** (si vous rebuildez souvent):
```batch
python -m PyInstaller NiTriTe_V17_Portable.spec
# Sans --clean
```

2. **Utiliser le cache de PyInstaller**:
- Ne pas supprimer le dossier `build/` entre deux builds

---

## Distribution

### Créer un package pour distribution

Le script crée automatiquement un dossier `release/` avec:
- ✅ L'exécutable `NiTriTe_V17_Portable.exe`
- ✅ Le fichier de lancement `LANCER_V17_PORTABLE.bat`
- ✅ Un README pour les utilisateurs

### Compresser pour distribution

```batch
# Compresser le dossier release/
# Utilisez 7-Zip, WinRAR ou l'outil de compression Windows
```

**Nom suggéré**: `NiTriTe-V17-Beta-Portable-Windows.zip`

---

## Versions et Changelog

### Version actuelle: V17 Beta

**Améliorations**:
- ✅ Interface moderne avec CustomTkinter
- ✅ Support de PyInstaller pour version portable
- ✅ Correction des problèmes d'encodage UTF-8
- ✅ Amélioration du système de build
- ✅ Gestionnaire d'installation avec WinGet

**Corrections dans cette version**:
- 🔧 Problèmes d'encodage Windows (cp1252 → UTF-8)
- 🔧 Scripts de build améliorés
- 🔧 Meilleure gestion des erreurs
- 🔧 Documentation complète

---

## Support et Contribution

### Signaler un bug
1. Vérifiez que vous utilisez la dernière version
2. Testez en mode développement (`LANCER_NITRITE_V17.bat`)
3. Notez l'erreur complète (traceback)

### Logs et Debug

En cas de problème avec l'exécutable:
1. Lancez depuis l'invite de commande:
```batch
cd dist
NiTriTe_V17_Portable.exe
```
2. Les erreurs s'afficheront dans la console

---

## Licence et Crédits

**NiTriTe V17 Beta** - Maintenance Informatique Professionnelle

Pour plus d'informations, consultez `README.md` à la racine du projet.

---

## Checklist Avant Distribution

- [ ] Toutes les dépendances sont installées
- [ ] Tests en mode développement réussis
- [ ] Build sans erreurs
- [ ] Test de l'exécutable
- [ ] Vérification de toutes les fonctionnalités
- [ ] Création du package portable
- [ ] Compression du package
- [ ] Test sur une machine vierge (si possible)

---

**Dernière mise à jour**: Décembre 2025
**Version du guide**: 1.0
