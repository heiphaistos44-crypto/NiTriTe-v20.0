# NiTriTe V18.5 - Changelog

## 🎉 Nouvelles Fonctionnalités

### ✅ Mode 100% Portable
**Aucune trace sur le PC client**
- Tous les fichiers de configuration stockés dans `config/`
- Tous les logs stockés dans `logs/`
- Tous les téléchargements temporaires dans `temp/downloads/`
- Tous les scripts temporaires (.bat, .ps1) dans `temp/scripts/`
- Migration automatique des anciens configs depuis le home directory

**Structure portable complète:**
```
NiTriTe_V18_Portable.exe
├── config/                     # Configs portables
│   ├── nitrite_config.json
│   └── nitrite_theme.json
├── logs/                       # Logs portables
│   ├── nitrite_v18_[timestamp].log
│   └── errors.log
├── temp/                       # Fichiers temporaires portables
│   ├── downloads/
│   ├── scripts/
│   └── benchmark/
├── logiciel/                   # Outils diagnostiques
│   └── Custom/                 # 🆕 Apps personnalisées auto-scannées
└── data/
    ├── programs.json
    └── custom_diagnostic_tools.json  # 🆕 Config apps personnalisées
```

### 🔧 Boutons Pilotes Individuels (Updates)
**Page Updates → Pilotes Génériques Windows**
- 🔌 **Installer Pilotes USB** - Détection et installation des drivers USB
- 💿 **Installer Pilotes Chipset** - Drivers carte mère et chipset
- 📡 **Installer Pilotes Bluetooth** - Adapters Bluetooth
- 🖨️ **Installer Pilotes Imprimantes** - Drivers imprimantes

**Fonctionnement:**
1. Chaque bouton lance un scan `pnputil /scan-devices` avec admin
2. Ouvre Windows Update pour installation automatique
3. Terminal affiche la progression en temps réel
4. Scripts stockés dans dossier portable `temp/scripts/`

### 📦 Gestionnaire d'Applications Portables Personnalisées (Diagnostic)
**Page Diagnostic → Outils de Diagnostic**

**Bouton "➕ Ajouter Application":**
- Dialog graphique pour ajouter des apps portables personnalisées
- Sélecteur de fichier .exe avec file picker
- Choix du nom personnalisé
- 14 emojis au choix pour l'icône (📊🔧🛠️⚙️🔍📦💻🖥️⚡🎮📈🔬🧰🎯)
- Sauvegarde dans `data/custom_diagnostic_tools.json`

**Auto-scan du dossier `logiciel/Custom/`:**
- Détection automatique de tous les .exe dans le dossier
- Création automatique de boutons avec icône 📦
- Rafraîchissement à chaque démarrage
- Pas besoin de configuration manuelle

**Suppression d'apps:**
- Bouton ❌ sur chaque app personnalisée
- Apps auto-scannées : info pour supprimer le .exe du dossier
- Apps manuelles : suppression du JSON

**Stockage:**
- Apps manuelles : `data/custom_diagnostic_tools.json`
- Apps auto-découvertes : scannées dynamiquement depuis `logiciel/Custom/`
- Fusion intelligente sans doublons

### 📋 Terminal Redimensionnable (Logs)
**Page Logs**
- Terminal avec boutons ▼ / ▲ pour agrandir/réduire
- Fix du scroll parent lors du défilement terminal
- Hauteur par défaut: 500px logs, 300px terminal
- Redimensionnement fluide

## 🛠️ Améliorations Techniques

### Portable Paths System
**Nouveau module étendu:**
- `get_portable_config_dir()` - Dossier config portable
- `get_portable_logs_dir()` - Dossier logs portable
- `get_portable_temp_dir(subfolder)` - Temp avec sous-dossiers
  - Supporte: 'downloads', 'scripts', 'benchmark'
- Fallback automatique vers temp système si erreur

### Helper Functions
**`create_portable_temp_file(suffix, content)`:**
- Création de fichiers temp portables
- Encodage automatique (cp1252 pour .bat, utf-8 pour autres)
- Gestion du PID et timestamp pour noms uniques
- Utilisé par tous les scripts d'installation

### Backward Compatibility
**Migration automatique:**
- Détection de `~/.nitrite_config.json`
- Copie automatique vers `config/nitrite_config.json`
- Message console de confirmation
- Pas de perte de paramètres utilisateur

## 📊 Statistiques du Build

- **Taille**: ~745-750 MB
- **Python**: 3.12.10
- **PyInstaller**: 6.17.0
- **Modules**: +500 modules Python inclus
- **Fichiers portables**: 30+ outils diagnostiques
- **Custom tools**: Illimité (limité par `logiciel/Custom/`)

## 🧪 Tests Recommandés

### Test Mode Portable
1. Lancer l'exe depuis une clé USB
2. Vérifier qu'aucun fichier n'est créé dans `C:\Users\[User]\`
3. Vérifier `config/`, `logs/`, `temp/` créés à côté de l'exe
4. Fermer et relancer → configs persistées

### Test Pilotes Individuels
1. Page Updates → Pilotes Génériques Windows
2. Cliquer sur chaque bouton (USB, Chipset, Bluetooth, Imprimantes)
3. Vérifier ouverture Windows Update
4. Vérifier terminal affiche progression

### Test Custom Apps
1. Page Diagnostic → "➕ Ajouter Application"
2. Ajouter un .exe manuellement
3. Placer un .exe dans `logiciel/Custom/`
4. Relancer l'app → vérifier les 2 apps apparaissent
5. Cliquer sur l'app → vérifier lancement
6. Cliquer ❌ → vérifier suppression

## 🐛 Corrections de Bugs

- **Logger**: Utilise maintenant chemin portable au lieu de `data/logs/`
- **Installer Manager**: Téléchargements dans `temp/downloads/` portable
- **Scripts .bat**: Tous créés dans `temp/scripts/` portable
- **Cleanup**: Ne touche plus Desktop/Documents, seulement `temp/` et `__pycache__`

## ⚠️ Notes Importantes

1. **Dossier logiciel**: Ne pas toucher (requis pour outils diagnostiques)
2. **Dossier Script Windows**: Ne pas toucher (scripts système)
3. **Permission toolsv6.ini**: Erreur bénigne lors du build, n'affecte pas l'exe
4. **Custom folder**: Créé automatiquement au premier lancement

## 📝 Structure JSON Custom Tools

```json
{
  "version": "1.0",
  "auto_scan_enabled": true,
  "custom_folder": "logiciel/Custom",
  "custom_tools": [
    {
      "id": "custom_20251224_143000",
      "name": "Mon Outil",
      "emoji": "📊",
      "exe_path": "C:/path/tool.exe",
      "auto_discovered": false,
      "enabled": true,
      "created_date": "2025-12-24"
    }
  ]
}
```

## 🎯 Prochaines Étapes

- [ ] Tester sur plusieurs configurations Windows
- [ ] Vérifier compatibilité Windows 10/11
- [ ] Tester avec antivirus (possible faux positif)
- [ ] Optimiser taille du build si nécessaire
- [ ] Créer package d'installation final

---

**Build par**: Claude Sonnet 4.5
**Date**: 2025-12-24
**Version**: V18.5 Portable
