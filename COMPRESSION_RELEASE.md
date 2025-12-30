# Système de Compression pour la Release

## Problème

La release de NiTriTe V20 dépasse 2 Go à cause des dossiers volumineux :
- **Drivers**: 721 MB
- **Script Windows**: 260 MB
- **logiciel**: (si présent)

GitHub a une limite de 2 Go pour les releases, ce qui pose problème.

## Solution

Un système de compression/extraction automatique a été mis en place :

### 1. Compression pour la Release

Les dossiers volumineux sont compressés en archives ZIP avant la release.

**Commande :**
```bash
python compress_large_folders.py
```

**Résultat :**
- Crée le dossier `archives_compressed/` contenant :
  - `Drivers.zip`
  - `Script_Windows.zip`
  - `logiciel.zip` (si applicable)
- Affiche la taille économisée et le taux de compression

### 2. Extraction Automatique

Au **premier lancement** de l'application, le système :
1. Détecte la présence des archives dans `archives_compressed/`
2. Vérifie si les dossiers sont déjà extraits
3. Extrait automatiquement les archives si nécessaire
4. Affiche la progression dans la console

**Fichiers impliqués :**
- `src/v14_mvp/archive_manager.py` - Module de gestion des archives
- `src/v14_mvp/main_app.py` - Initialisation au démarrage (ligne ~541)

## Workflow de Release

### Étape 1 : Préparer la Release

```bash
# 1. Compresser les dossiers volumineux
python compress_large_folders.py

# 2. Vérifier que archives_compressed/ contient les ZIP
dir archives_compressed
```

### Étape 2 : Build de l'Exécutable

```bash
# Build avec PyInstaller (inclut archives_compressed/)
py -3.12 -m PyInstaller NiTriTe_V20_Portable.spec
```

**IMPORTANT:** Le fichier `.spec` a été configuré pour inclure `archives_compressed/` :

```python
datas=[
    ('data', 'data'),
    ('assets', 'assets'),
    ('src', 'src'),
    # Archives compressées pour release (extraction auto au lancement)
    ('archives_compressed', 'archives_compressed'),
],
```

**Note sur le fonctionnement avec PyInstaller:**
- Les archives sont incluses dans l'exécutable (dans `sys._MEIPASS`)
- Au premier lancement, elles sont extraites à côté de l'exe
- Les lancements suivants détectent les dossiers déjà extraits
- Pas de re-téléchargement ni re-extraction nécessaire

### Étape 3 : Créer la Release GitHub

1. **Supprimer** les dossiers non compressés de la release :
   - `Drivers/` (sauf fichiers < 100 MB comme install_all.bat)
   - `Script Windows/` (sauf scripts .cmd/.reg)
   - `logiciel/`

2. **Inclure** dans la release :
   - L'exécutable `dist/NiTriTe_V20_Portable.exe`
   - Le dossier `archives_compressed/` avec les ZIP
   - Les autres fichiers essentiels (data/, src/, etc.)

3. **Télécharger** la release sur GitHub

### Étape 4 : Expérience Utilisateur

Quand un utilisateur lance l'application pour la première fois :

```
[OK] Python 3.12.0
[>>] Lancement NiTriTe V18...
[..] Répertoire: C:\Users\...\NiTriTe
[..] Vérification des archives compressées...
⏳ Extraction de Drivers.zip...
✅ Drivers.zip extrait avec succès
⏳ Extraction de Script_Windows.zip...
✅ Script_Windows.zip extrait avec succès
[OK] Archives vérifiées
[..] Création de l'instance NiTriTeV18...
```

Les lancements suivants détectent que les dossiers sont déjà extraits et ne font rien.

## Avantages

✅ **Réduit la taille de la release** de ~1 Go (~50% de compression)
✅ **Transparent pour l'utilisateur** - extraction automatique
✅ **Pas de double stockage** - dossiers extraits une seule fois
✅ **Fonctionne hors ligne** - pas de téléchargement nécessaire
✅ **Compatible PyInstaller** - archives incluses dans l'exe

## Structure des Fichiers

```
NiTriTe-V20.0/
├── archives_compressed/          # Archives ZIP (inclus dans release)
│   ├── Drivers.zip               # ~300 MB compressé
│   ├── Script_Windows.zip        # ~100 MB compressé
│   └── logiciel.zip              # Si présent
│
├── Drivers/                      # Extrait au premier lancement
├── Script Windows/               # Extrait au premier lancement
├── logiciel/                     # Extrait au premier lancement
│
├── src/
│   └── v14_mvp/
│       ├── archive_manager.py    # Module de gestion
│       └── main_app.py           # Initialisation
│
└── compress_large_folders.py     # Script de compression
```

## Tests

### Tester la Compression

```bash
python compress_large_folders.py
```

Vérifier :
- Les archives sont créées dans `archives_compressed/`
- La taille est réduite significativement

### Tester l'Extraction

```bash
# 1. Renommer les dossiers existants
mv Drivers Drivers_backup
mv "Script Windows" "Script Windows_backup"

# 2. Lancer l'application
python -m src.v14_mvp.main_app

# 3. Vérifier que les dossiers sont extraits
dir Drivers
dir "Script Windows"
```

### Tester le Module Directement

```bash
python src/v14_mvp/archive_manager.py
```

## Dépannage

### Problème : Archives non trouvées

**Symptôme :** Message "Archive introuvable"

**Solution :**
1. Vérifier que `archives_compressed/` existe
2. Exécuter `python compress_large_folders.py`

### Problème : Extraction échoue

**Symptôme :** Message "Échec de l'extraction"

**Solution :**
1. Vérifier les permissions d'écriture
2. Vérifier l'espace disque disponible (~1 GB requis)
3. Vérifier l'intégrité des ZIP

### Problème : Double stockage

**Symptôme :** Dossiers ET archives présents

**Solution :**
- C'est normal pour la version développement
- Pour la release, inclure seulement `archives_compressed/`
- Les dossiers seront recréés automatiquement

## Maintenance

### Ajouter une Nouvelle Archive

1. Modifier `archive_manager.py` :
```python
self.managed_archives = {
    "Drivers.zip": "Drivers",
    "Script_Windows.zip": "Script Windows",
    "nouveau_dossier.zip": "nouveau_dossier"  # Ajouter ici
}
```

2. Modifier `compress_large_folders.py` :
```python
folders_to_compress = [
    ("Drivers", "Drivers.zip"),
    ("Script Windows", "Script_Windows.zip"),
    ("nouveau_dossier", "nouveau_dossier.zip"),  # Ajouter ici
]
```

3. Recompresser :
```bash
python compress_large_folders.py
```

## Notes Importantes

⚠️ **Ne PAS** commiter les archives ET les dossiers sur Git
⚠️ **Toujours** tester l'extraction avant une release
⚠️ **Inclure** `archives_compressed/` dans le `.spec` PyInstaller
⚠️ **Vérifier** la taille finale de la release (< 2 GB)

## Fichiers à Exclure de la Release

❌ **NE PAS inclure :**
- `Drivers/` (répertoire complet - sauf install_all.bat)
- `Script Windows/Tweaks Windows 11-10-8-7-Vista-XP/` (gros fichiers)
- `logiciel/` (si compressé)
- Fichiers `*_backup.py`
- Fichiers de test `test_*.py`

✅ **INCLURE :**
- `archives_compressed/` (avec tous les ZIP)
- Scripts `.cmd` et `.reg` de Script Windows
- `Drivers/Visual C Runtime/install_all.bat`
- Tous les autres fichiers essentiels

---

🤖 Généré avec [Claude Code](https://claude.com/claude-code)
