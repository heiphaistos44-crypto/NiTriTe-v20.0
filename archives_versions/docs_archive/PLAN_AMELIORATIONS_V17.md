# Plan d'Améliorations - NiTriTe V17 Beta

## Vue d'Ensemble

Ce document détaille toutes les améliorations demandées pour NiTriTe V17.

---

## 📋 Liste des Améliorations

### 1. Page Applications ✅ (En cours)
**Objectif**: Ajouter barre de chargement avec logs CMD lors des installations

**Fichiers à modifier**:
- `src/v14_mvp/pages_optimized.py` (OptimizedApplicationsPage)
- `src/v14_mvp/installer.py` (InstallationManager)

**Nouveau fichier créé**:
- ✅ `src/v14_mvp/progress_dialog.py` (Composant de progression)

**Modifications nécessaires**:
- [x] Créer ProgressDialog et MultiProgressDialog
- [ ] Modifier InstallationManager pour envoyer des logs
- [ ] Modifier OptimizedApplicationsPage pour utiliser le dialogue
- [ ] Intégrer les callbacks de progression

---

### 2. Page Outils - Master Boutons ⏳ (À faire)
**Objectif**: Créer catégorie "Master Boutons" avec 6 boutons utilitaires

**Fichiers à modifier**:
- `src/v14_mvp/pages_optimized.py` (OptimizedToolsPage)

**Boutons à ajouter**:
1. **Activation Windows/Office**
   - Commande: `irm https://get.activated.win | iex`
   - Requiert: Admin
   - Exécution: PowerShell

2. **MSCONFIG**
   - Commande: `msconfig`
   - Requiert: Pas forcément admin
   - Exécution: CMD

3. **Gestionnaire des tâches**
   - Commande: `taskmgr`
   - Requiert: Non
   - Exécution: CMD

4. **MSINFO**
   - Commande: `msinfo32`
   - Requiert: Non
   - Exécution: CMD

5. **Ouvrir %Temp%**
   - Commande: Explorer vers `%Temp%`
   - Requiert: Non
   - Exécution: explorer.exe

6. **Ouvrir %LocalAppData%**
   - Commande: Explorer vers `%LocalAppData%`
   - Requiert: Non
   - Exécution: explorer.exe

**Implémentation**:
- Créer une nouvelle classe MasterButtonsSection
- Ajouter gestion des commandes admin (UAC)
- Créer des boutons avec icônes distinctifs

---

### 3. Page Mises à Jour ⏳ (À faire)
**Objectif**: Afficher les vraies mises à jour Windows Update

**Fichiers à modifier**:
- `src/v14_mvp/pages_full.py` (UpdatesPage)

**Problèmes actuels**:
- winget update ne trouve qu'une mise à jour
- Windows Update trouve plus de mises à jour

**Solutions**:
1. **Option A**: Utiliser l'API Windows Update (WMI)
   ```python
   import win32com.client
   update_session = win32com.client.Dispatch("Microsoft.Update.Session")
   update_searcher = update_session.CreateUpdateSearcher()
   ```

2. **Option B**: Parser la sortie de `Get-WindowsUpdate` (PowerShell)
   ```powershell
   Get-WindowsUpdate -MicrosoftUpdate
   ```

3. **Option C**: Utiliser PSWindowsUpdate module
   ```powershell
   Install-Module PSWindowsUpdate
   Get-WindowsUpdate
   ```

**Fonctionnalités à ajouter**:
- Liste des mises à jour Windows disponibles
- Statut de chaque mise à jour
- Bouton pour installer les mises à jour
- Progression de l'installation

---

### 4. Page Apps Portables ⏳ (À faire)
**Objectif**: Ajouter liste d'applications portables téléchargeables

**Fichiers à modifier**:
- `src/v14_mvp/page_portables.py` (PortableAppsPage)
- `data/portable_apps.json` (nouveau fichier de données)

**Applications portables suggérées**:
```json
{
  "Outils Système": {
    "7-Zip Portable": {
      "url": "https://www.7-zip.org/a/7z2301-x64.exe",
      "description": "Archiveur puissant",
      "size": "1.5 MB"
    },
    "Notepad++ Portable": {
      "url": "https://github.com/notepad-plus-plus/notepad-plus-plus/releases/download/v8.6/npp.8.6.portable.x64.zip",
      "description": "Éditeur de texte avancé",
      "size": "5 MB"
    },
    "VLC Portable": {
      "url": "https://get.videolan.org/vlc/last/win64/vlc-3.0.20-win64.zip",
      "description": "Lecteur multimédia",
      "size": "40 MB"
    }
  },
  "Réseau": {
    "PuTTY Portable": {
      "url": "https://the.earth.li/~sgtatham/putty/latest/w64/putty.exe",
      "description": "Client SSH/Telnet",
      "size": "3 MB"
    },
    "WinSCP Portable": {
      "url": "https://winscp.net/download/WinSCP-6.1.2-Portable.zip",
      "description": "Client SFTP/FTP",
      "size": "10 MB"
    }
  },
  "Utilitaires": {
    "Everything Portable": {
      "url": "https://www.voidtools.com/Everything-1.4.1.1024.x64.zip",
      "description": "Recherche de fichiers ultra-rapide",
      "size": "2 MB"
    },
    "TreeSize Free Portable": {
      "url": "https://downloads.jam-software.de/treesize_free/TreeSizeFree-Portable.zip",
      "description": "Analyse de l'espace disque",
      "size": "8 MB"
    }
  }
}
```

**Fonctionnalités**:
- Interface similaire à la page Applications
- Téléchargement avec barre de progression
- Extraction automatique des ZIP
- Organisation dans un dossier "Portables"
- Logs de téléchargement/installation

---

### 5. Page Master Install - OrdiPlus Modifiable ⏳ (À faire)
**Objectif**: Rendre la catégorie OrdiPlus modifiable

**Fichiers à modifier**:
- `src/v14_mvp/page_master_install.py` (MasterInstallPage)
- `data/ordiplus_config.json` (nouveau fichier de config)

**Fonctionnalités à ajouter**:
1. **Bouton "Gérer OrdiPlus"**
   - Ouvre un dialogue de gestion
   - Affiche toutes les apps de la catégorie OrdiPlus

2. **Dialogue de gestion**:
   - Liste des apps actuelles
   - Bouton "Ajouter une app" (sélection depuis liste globale)
   - Bouton "Retirer" pour chaque app
   - Bouton "Sauvegarder"

3. **Sauvegarde de la configuration**:
   ```json
   {
     "ordiplus_apps": [
       "AnyDesk Portable",
       "RustDesk Portable",
       "Malwarebytes",
       "..."
     ]
   }
   ```

4. **Chargement de la configuration**:
   - Au démarrage, charger depuis ordiplus_config.json
   - Si n'existe pas, utiliser config par défaut

---

### 6. Master Install - Barre de Progression ⏳ (À faire)
**Objectif**: Ajouter barre de chargement avec logs CMD

**Fichiers à modifier**:
- `src/v14_mvp/page_master_install.py` (MasterInstallPage)

**Utilisation du composant**:
- Utiliser `MultiProgressDialog` créé précédemment
- Afficher progression pour chaque app
- Logs en temps réel
- Gestion des erreurs

**Intégration**:
```python
from v14_mvp.progress_dialog import MultiProgressDialog

# Lors du clic sur "Installer Tout"
dialog = MultiProgressDialog(self, "Installation Master OrdiPlus")
dialog.set_total_apps(len(selected_apps))

for app in selected_apps:
    if dialog.is_cancelled:
        break

    dialog.start_app(app_name)

    # Installation avec callbacks
    success = install_app(app,
        on_progress=lambda v, s: dialog.update_app_progress(v, s),
        on_log=lambda msg, lvl: dialog.add_log(msg, lvl)
    )

    dialog.complete_app(success)

dialog.mark_completed()
```

---

## 📁 Nouveaux Fichiers à Créer

### 1. Composants
- [x] `src/v14_mvp/progress_dialog.py` - Dialogues de progression

### 2. Données
- [ ] `data/portable_apps.json` - Liste des apps portables
- [ ] `data/ordiplus_config.json` - Configuration OrdiPlus personnalisée

### 3. Utilitaires
- [ ] `src/v14_mvp/windows_update.py` - Module pour Windows Update
- [ ] `src/v14_mvp/admin_runner.py` - Module pour exécution admin

---

## 🔧 Modifications des Fichiers Existants

### 1. src/v14_mvp/installer.py
**Modifications**:
- Ajouter callbacks pour progression et logs
- Méthode `install_app()` doit accepter:
  - `on_progress(value, status)` callback
  - `on_log(message, level)` callback
- Parser la sortie en temps réel
- Détecter erreurs et succès

### 2. src/v14_mvp/pages_optimized.py
**Modifications**:
- `OptimizedApplicationsPage`:
  - Méthode `_install_selected()` → utiliser ProgressDialog
  - Installer les apps une par une avec logs

- `OptimizedToolsPage`:
  - Ajouter section "Master Boutons"
  - Créer les 6 boutons
  - Gérer exécution admin pour activation

### 3. src/v14_mvp/pages_full.py
**Modifications**:
- `UpdatesPage`:
  - Ajouter onglet "Windows Update"
  - Afficher liste des mises à jour disponibles
  - Bouton installer avec progression

### 4. src/v14_mvp/page_portables.py
**Modifications**:
- Charger `data/portable_apps.json`
- Interface de sélection (comme Applications)
- Téléchargement avec `ProgressDialog`
- Extraction automatique
- Organisation des fichiers

### 5. src/v14_mvp/page_master_install.py
**Modifications**:
- Bouton "Gérer OrdiPlus" → ouvre dialogue
- Charger/sauvegarder configuration
- Installation avec `MultiProgressDialog`

---

## 🎨 Design des Nouveaux Composants

### Dialogue de Gestion OrdiPlus
```
┌─────────────────────────────────────────────┐
│  Gérer la catégorie OrdiPlus           [X]  │
├─────────────────────────────────────────────┤
│                                             │
│  Applications actuelles dans OrdiPlus:      │
│  ┌───────────────────────────────────────┐ │
│  │ ☑ AnyDesk Portable          [Retirer]│ │
│  │ ☑ RustDesk Portable         [Retirer]│ │
│  │ ☑ Malwarebytes              [Retirer]│ │
│  │ ...                                   │ │
│  └───────────────────────────────────────┘ │
│                                             │
│  [+ Ajouter une application]                │
│                                             │
│  ┌───────────────────┐  ┌────────────────┐ │
│  │    Annuler       │  │   Sauvegarder  │ │
│  └───────────────────┘  └────────────────┘ │
└─────────────────────────────────────────────┘
```

### Boutons Master (dans Outils)
```
┌─────────────────────────────────────────────┐
│  Master Boutons                             │
├─────────────────────────────────────────────┤
│  ┌──────────────┐  ┌──────────────┐        │
│  │ 🔑 Activation│  │ ⚙ MSCONFIG   │        │
│  │ Windows/     │  │              │        │
│  │ Office       │  │              │        │
│  └──────────────┘  └──────────────┘        │
│                                             │
│  ┌──────────────┐  ┌──────────────┐        │
│  │ 📊 Gest.     │  │ ℹ MSINFO     │        │
│  │ Tâches       │  │              │        │
│  └──────────────┘  └──────────────┘        │
│                                             │
│  ┌──────────────┐  ┌──────────────┐        │
│  │ 🗂 Temp      │  │ 📁 AppData   │        │
│  │ Folder       │  │ Local        │        │
│  └──────────────┘  └──────────────┘        │
└─────────────────────────────────────────────┘
```

---

## ⚠️ Points d'Attention

### 1. Activation Windows/Office
- **IMPORTANT**: Exécution de script PowerShell depuis Internet
- Nécessite:
  - Droits administrateur (UAC)
  - Confirmation utilisateur
  - Avertissement de sécurité

### 2. Windows Update via API
- Nécessite `pywin32` (déjà installé)
- Peut nécessiter droits admin
- Temps de recherche potentiellement long

### 3. Téléchargement Apps Portables
- Vérifier espace disque disponible
- Gérer interruptions réseau
- Vérifier intégrité des fichiers (checksums si possible)

### 4. Configuration Modifiable
- Sauvegarder dans `data/` (embarqué dans exe)
- Alternative: `%AppData%/NiTriTe/config.json` (persistant)

---

## 📊 Estimation de Travail

### Priorités

**P0 - Critique**:
1. Barre de progression Applications (déjà commencé)
2. Master Boutons dans Outils

**P1 - Important**:
3. Apps Portables téléchargeables
4. OrdiPlus modifiable

**P2 - Nice to have**:
5. Windows Update amélioré
6. Barre de progression Master Install

### Temps Estimé
- P0: ~2-3 heures de développement
- P1: ~3-4 heures de développement
- P2: ~2-3 heures de développement

**Total**: ~8-10 heures de développement + tests

---

## 🚀 Prochaines Étapes

### Immédiat
1. ✅ Créer progress_dialog.py
2. ⏳ Modifier installer.py pour ajouter callbacks
3. ⏳ Intégrer ProgressDialog dans pages_optimized.py

### Court terme
4. Créer section Master Boutons
5. Ajouter portable_apps.json
6. Implémenter téléchargement portables

### Moyen terme
7. Windows Update via API
8. OrdiPlus modifiable
9. Tests complets
10. Rebuild exe final

---

## 📝 Notes de Développement

### Architecture
- Tous les dialogues de progression sont dans `progress_dialog.py`
- Séparation claire entre UI et logique métier
- Callbacks pour communication async

### Tests
- Tester chaque fonctionnalité individuellement
- Tester en mode dev avant de builder
- Tester sur machine vierge si possible

### Documentation
- Mettre à jour README avec nouvelles fonctionnalités
- Documenter configuration OrdiPlus
- Guide d'utilisation des Master Boutons

---

**Date de création**: 06/12/2025
**Version cible**: V17 Beta Enhanced
**Statut**: 🟡 En cours
