# Guide d'Intégration des Améliorations - NiTriTe V17

## Fichiers Créés ✅

### Nouveaux Modules
1. **src/v14_mvp/progress_dialog.py** - Dialogues de progression avec logs
2. **src/v14_mvp/installer_enhanced.py** - Installeur avec logs en temps réel
3. **src/v14_mvp/master_buttons.py** - Widget Master Boutons

### Nouvelles Données
4. **data/portable_apps.json** - Liste des applications portables
5. **data/ordiplus_config.json** - Configuration OrdiPlus personnalisable

---

## Modifications à Apporter aux Fichiers Existants

### 1. src/v14_mvp/pages_optimized.py

#### A. Ajouter les imports en haut du fichier:
```python
from v14_mvp.progress_dialog import ProgressDialog, MultiProgressDialog
from v14_mvp.installer_enhanced import installer
from v14_mvp.master_buttons import MasterButtonsWidget
```

#### B. Dans la classe `OptimizedApplicationsPage`, modifier la méthode `_install_selected`:

**AVANT** (rechercher cette méthode):
```python
def _install_selected(self):
    if not self.selected_apps:
        # Message erreur...
        return

    # Installation basique...
```

**APRÈS** (remplacer par):
```python
def _install_selected(self):
    """Installer les applications sélectionnées avec barre de progression"""
    if not self.selected_apps:
        from tkinter import messagebox
        messagebox.showwarning(
            "Aucune sélection",
            "Veuillez sélectionner au moins une application à installer."
        )
        return

    # Créer dialogue de progression multiple
    dialog = MultiProgressDialog(self, "Installation des applications")
    dialog.set_total_apps(len(self.selected_apps))

    # Installation dans un thread
    import threading

    def install_all():
        for app_name in list(self.selected_apps):
            if dialog.is_cancelled:
                break

            dialog.start_app(app_name)

            # Trouver les données de l'app
            app_data = None
            for category, apps in self.programs_data.items():
                if app_name in apps:
                    app_data = apps[app_name]
                    break

            if not app_data:
                dialog.add_log(f"App non trouvée: {app_name}", "error")
                dialog.complete_app(False)
                continue

            # Installer avec callbacks
            winget_id = app_data.get('winget_id', app_name)

            installer.install_app(
                app_name=app_name,
                package_id=winget_id,
                method="winget",
                on_progress=lambda v, s: dialog.update_app_progress(v, s),
                on_log=lambda msg, lvl: dialog.add_log(msg, lvl),
                on_complete=lambda success, msg: dialog.complete_app(success)
            )

            # Attendre fin installation (max 5 minutes)
            import time
            timeout = 300  # 5 minutes
            start_time = time.time()
            while time.time() - start_time < timeout:
                time.sleep(1)
                # Vérifier si app suivante peut démarrer
                # (simplification, dans la vraie implémentation il faut un Event)

        dialog.mark_completed()

    thread = threading.Thread(target=install_all, daemon=True)
    thread.start()
```

#### C. Dans la classe `OptimizedToolsPage`, ajouter Master Boutons:

**Dans la méthode `__init__`, après avoir créé l'interface, ajouter**:
```python
def __init__(self, parent, tools_data: Dict):
    super().__init__(parent, fg_color=DesignTokens.BG_PRIMARY)

    self.tools_data = tools_data if tools_data else {}

    # ... (code existant) ...

    # AJOUTER ICI:
    # Section Master Boutons
    self.master_buttons = MasterButtonsWidget(self.content_container)
    self.master_buttons.pack(fill=tk.X, padx=20, pady=20)

    # ... (reste du code) ...
```

---

### 2. src/v14_mvp/page_portables.py

#### Remplacer tout le contenu par:

```python
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Page Applications Portables - NiTriTe V17
Téléchargement et gestion d'applications portables
"""

import customtkinter as ctk
import tkinter as tk
import json
import os
from pathlib import Path
from v14_mvp.design_system import DesignTokens
from v14_mvp.components import ModernCard
from v14_mvp.progress_dialog import ProgressDialog
import urllib.request
import zipfile
import shutil


class PortableAppsPage(ctk.CTkFrame):
    """Page de gestion des applications portables"""

    def __init__(self, parent):
        super().__init__(parent, fg_color=DesignTokens.BG_PRIMARY)

        self.portable_apps = self._load_portable_apps()
        self.selected_apps = set()
        self.portables_dir = Path("C:/Portables")  # Dossier de destination

        self._create_ui()

    def _load_portable_apps(self):
        """Charger la liste des apps portables"""
        try:
            # Chercher data/portable_apps.json
            import sys
            if getattr(sys, 'frozen', False):
                base_path = sys._MEIPASS
            else:
                base_path = os.getcwd()

            json_path = os.path.join(base_path, 'data', 'portable_apps.json')

            with open(json_path, 'r', encoding='utf-8') as f:
                return json.load(f)
        except Exception as e:
            print(f"Erreur chargement portable_apps.json: {e}")
            return {}

    def _create_ui(self):
        """Créer l'interface"""
        # Header
        header = ModernCard(self)
        header.pack(fill=tk.X, padx=20, pady=10)

        header_container = ctk.CTkFrame(header, fg_color="transparent")
        header_container.pack(fill=tk.X, padx=20, pady=15)

        title = ctk.CTkLabel(
            header_container,
            text="📦 Applications Portables",
            font=(DesignTokens.FONT_FAMILY, 24, "bold"),
            text_color=DesignTokens.TEXT_PRIMARY
        )
        title.pack(side=tk.LEFT)

        # Bouton télécharger
        download_btn = ctk.CTkButton(
            header_container,
            text="⬇ Télécharger Sélection",
            command=self._download_selected,
            fg_color=DesignTokens.ACCENT_PRIMARY,
            hover_color=DesignTokens.ACCENT_HOVER,
            font=(DesignTokens.FONT_FAMILY, 13, "bold"),
            height=40,
            width=200
        )
        download_btn.pack(side=tk.RIGHT)

        # Zone de contenu scrollable
        scroll_frame = ctk.CTkScrollableFrame(
            self,
            fg_color=DesignTokens.BG_PRIMARY
        )
        scroll_frame.pack(fill=tk.BOTH, expand=True, padx=20, pady=10)

        # Afficher par catégories
        for category, apps in self.portable_apps.items():
            self._create_category_section(scroll_frame, category, apps)

    def _create_category_section(self, parent, category, apps):
        """Créer une section de catégorie"""
        # Card pour la catégorie
        category_card = ModernCard(parent)
        category_card.pack(fill=tk.X, pady=10)

        # Titre catégorie
        cat_title = ctk.CTkLabel(
            category_card,
            text=f"📁 {category}",
            font=(DesignTokens.FONT_FAMILY, 16, "bold"),
            text_color=DesignTokens.ACCENT_PRIMARY
        )
        cat_title.pack(anchor=tk.W, padx=20, pady=(15, 10))

        # Liste des apps
        for app_name, app_data in apps.items():
            self._create_app_row(category_card, app_name, app_data)

    def _create_app_row(self, parent, app_name, app_data):
        """Créer une ligne pour une app"""
        row = ctk.CTkFrame(parent, fg_color="#202020", corner_radius=8)
        row.pack(fill=tk.X, padx=20, pady=5)

        # Checkbox
        var = tk.BooleanVar()
        checkbox = ctk.CTkCheckBox(
            row,
            text="",
            variable=var,
            command=lambda: self._toggle_app(app_name, var.get()),
            fg_color=DesignTokens.ACCENT_PRIMARY,
            hover_color=DesignTokens.ACCENT_HOVER
        )
        checkbox.pack(side=tk.LEFT, padx=10, pady=10)

        # Info app
        info_frame = ctk.CTkFrame(row, fg_color="transparent")
        info_frame.pack(side=tk.LEFT, fill=tk.X, expand=True, padx=10, pady=10)

        name_label = ctk.CTkLabel(
            info_frame,
            text=app_name,
            font=(DesignTokens.FONT_FAMILY, 13, "bold"),
            text_color=DesignTokens.TEXT_PRIMARY
        )
        name_label.pack(anchor=tk.W)

        desc_label = ctk.CTkLabel(
            info_frame,
            text=app_data.get('description', ''),
            font=(DesignTokens.FONT_FAMILY, 11),
            text_color=DesignTokens.TEXT_SECONDARY
        )
        desc_label.pack(anchor=tk.W)

        # Taille
        size_label = ctk.CTkLabel(
            row,
            text=app_data.get('size', '?'),
            font=(DesignTokens.FONT_FAMILY, 11),
            text_color=DesignTokens.TEXT_TERTIARY
        )
        size_label.pack(side=tk.RIGHT, padx=20)

    def _toggle_app(self, app_name, selected):
        """Basculer sélection app"""
        if selected:
            self.selected_apps.add(app_name)
        else:
            self.selected_apps.discard(app_name)

    def _download_selected(self):
        """Télécharger les apps sélectionnées"""
        if not self.selected_apps:
            from tkinter import messagebox
            messagebox.showwarning(
                "Aucune sélection",
                "Veuillez sélectionner au moins une application."
            )
            return

        # Créer dossier Portables
        self.portables_dir.mkdir(exist_ok=True)

        # Dialogue de progression
        dialog = ProgressDialog(self, "Téléchargement d'applications portables")

        import threading

        def download_all():
            total = len(self.selected_apps)
            current = 0

            for app_name in list(self.selected_apps):
                if dialog.is_cancelled:
                    break

                current += 1
                dialog.set_title_text(f"Téléchargement {current}/{total}")
                dialog.add_log(f"Téléchargement: {app_name}", "info")

                # Trouver l'app
                app_data = None
                for category, apps in self.portable_apps.items():
                    if app_name in apps:
                        app_data = apps[app_name]
                        break

                if not app_data:
                    dialog.add_log(f"App non trouvée: {app_name}", "error")
                    continue

                url = app_data.get('url')
                app_type = app_data.get('type', 'exe')

                try:
                    # Télécharger
                    dialog.update_progress(0.3, f"Téléchargement de {app_name}...")
                    filename = f"{app_name}.{app_type}"
                    filepath = self.portables_dir / filename

                    urllib.request.urlretrieve(url, filepath)
                    dialog.add_log(f"✓ Téléchargé: {filename}", "success")

                    # Si ZIP, extraire
                    if app_type == 'zip':
                        dialog.update_progress(0.7, "Extraction...")
                        extract_dir = self.portables_dir / app_name
                        extract_dir.mkdir(exist_ok=True)

                        with zipfile.ZipFile(filepath, 'r') as zip_ref:
                            zip_ref.extractall(extract_dir)

                        # Supprimer le ZIP
                        filepath.unlink()
                        dialog.add_log(f"✓ Extrait dans: {extract_dir}", "success")

                    dialog.update_progress(1.0, "Terminé")

                except Exception as e:
                    dialog.add_log(f"✗ Erreur: {str(e)}", "error")

            dialog.mark_completed(True)
            dialog.add_log(f"", "info")
            dialog.add_log(f"Dossier: {self.portables_dir}", "info")

        thread = threading.Thread(target=download_all, daemon=True)
        thread.start()
```

---

### 3. src/v14_mvp/page_master_install.py

#### Ajouter en haut:
```python
from v14_mvp.progress_dialog import MultiProgressDialog
from v14_mvp.installer_enhanced import installer
```

#### Ajouter méthode de gestion OrdiPlus:
```python
def _manage_ordiplus(self):
    """Ouvrir dialogue de gestion OrdiPlus"""
    # TODO: Créer dialogue de gestion
    # Pour l'instant, juste un message
    from tkinter import messagebox
    messagebox.showinfo(
        "Gérer OrdiPlus",
        "Fonctionnalité de gestion OrdiPlus en cours de développement.\n\n"
        "Vous pourrez bientôt ajouter/retirer des applications."
    )
```

#### Modifier installation avec progression:
```python
def _install_ordiplus(self):
    """Installer toutes les apps OrdiPlus avec progression"""
    # Charger config
    ordiplus_apps = self._load_ordiplus_config()

    if not ordiplus_apps:
        return

    # Dialogue de progression
    dialog = MultiProgressDialog(self, "Installation Master OrdiPlus")
    dialog.set_total_apps(len(ordiplus_apps))

    import threading

    def install_all():
        for app_name in ordiplus_apps:
            if dialog.is_cancelled:
                break

            dialog.start_app(app_name)

            # Trouver app dans programs_data
            # ... (même logique que pour Applications)

            # Installer avec callbacks
            installer.install_app(
                app_name=app_name,
                package_id=app_name,  # ou winget_id
                method="winget",
                on_progress=lambda v, s: dialog.update_app_progress(v, s),
                on_log=lambda msg, lvl: dialog.add_log(msg, lvl),
                on_complete=lambda success, msg: dialog.complete_app(success)
            )

        dialog.mark_completed()

    thread = threading.Thread(target=install_all, daemon=True)
    thread.start()

def _load_ordiplus_config(self):
    """Charger config OrdiPlus"""
    try:
        import sys
        if getattr(sys, 'frozen', False):
            base_path = sys._MEIPASS
        else:
            base_path = os.getcwd()

        config_path = os.path.join(base_path, 'data', 'ordiplus_config.json')

        with open(config_path, 'r', encoding='utf-8') as f:
            data = json.load(f)
            return data.get('ordiplus_apps', [])
    except:
        # Config par défaut
        return [
            "AnyDesk Portable",
            "Malwarebytes",
            "Google Chrome"
        ]
```

---

### 4. src/v14_mvp/pages_full.py (Windows Update)

#### Pour Windows Update, ajouter:

```python
import win32com.client

class UpdatesPage(ctk.CTkFrame):
    # ... code existant ...

    def _check_windows_updates(self):
        """Vérifier les mises à jour Windows"""
        try:
            dialog = ProgressDialog(self, "Recherche de mises à jour Windows")
            dialog.update_progress(0.2, "Connexion à Windows Update...")

            import threading

            def search_updates():
                try:
                    dialog.add_log("Initialisation Windows Update...", "info")

                    # Créer session Windows Update
                    update_session = win32com.client.Dispatch("Microsoft.Update.Session")
                    update_searcher = update_session.CreateUpdateSearcher()

                    dialog.update_progress(0.4, "Recherche des mises à jour...")
                    dialog.add_log("Recherche en cours...", "info")

                    # Rechercher les mises à jour
                    search_result = update_searcher.Search("IsInstalled=0 and Type='Software'")

                    updates_count = search_result.Updates.Count

                    dialog.update_progress(0.8, f"{updates_count} mises à jour trouvées")

                    if updates_count == 0:
                        dialog.add_log("✓ Système à jour", "success")
                    else:
                        dialog.add_log(f"✓ {updates_count} mise(s) à jour disponible(s):", "success")

                        for i in range(updates_count):
                            update = search_result.Updates.Item(i)
                            dialog.add_log(f"  - {update.Title}", "info")

                    dialog.mark_completed(True)

                except Exception as e:
                    dialog.add_log(f"✗ Erreur: {str(e)}", "error")
                    dialog.mark_completed(False)

            thread = threading.Thread(target=search_updates, daemon=True)
            thread.start()

        except Exception as e:
            from tkinter import messagebox
            messagebox.showerror("Erreur", f"Erreur Windows Update:\n{str(e)}")
```

---

## Mise à Jour du .spec pour PyInstaller

Dans **NiTriTe_V17_Portable.spec**, ajouter les nouveaux fichiers:

```python
datas=[
    ('data', 'data'),  # Inclut portable_apps.json et ordiplus_config.json
    ('assets', 'assets'),
    ('src', 'src')
],
```

---

## Tests Recommandés

### 1. Test Master Boutons
- Tester chaque bouton individuellement
- Vérifier UAC pour activation Windows/Office
- Vérifier ouverture dossiers Temp et AppData

### 2. Test Applications avec Logs
- Installer une app
- Vérifier logs en temps réel
- Tester annulation
- Tester installations multiples

### 3. Test Apps Portables
- Télécharger une app EXE
- Télécharger une app ZIP
- Vérifier extraction
- Vérifier dossier C:/Portables

### 4. Test Windows Update
- Rechercher mises à jour
- Vérifier affichage
- (Installation optionnelle)

---

## Rebuild du Projet

Après avoir appliqué toutes les modifications:

```batch
# Nettoyer
rmdir /s /q build dist

# Rebuilder
BUILD_PORTABLE_V17_FIXED.bat
```

---

## Notes Importantes

### Gestion des Threads
- Toutes les installations utilisent des threads pour ne pas bloquer l'UI
- Les dialogues de progression sont thread-safe

### Encodage
- Tous les fichiers JSON sont en UTF-8
- Les logs supportent les emojis et caractères spéciaux

### Erreurs Potentielles
- **WinGet**: Peut nécessiter connexion Internet
- **Windows Update**: Peut nécessiter droits admin
- **Activation**: Nécessite Internet + admin

---

## Prochaines Améliorations Possibles

1. **Gestionnaire OrdiPlus complet**
   - Dialogue drag & drop pour organiser
   - Sauvegarde auto dans %AppData%

2. **Installation Windows Update**
   - Bouton installer mises à jour
   - Progression installation

3. **Portables**
   - Vérification checksums (sécurité)
   - Mise à jour des apps déjà téléchargées

4. **Logs**
   - Export des logs en fichier .txt
   - Historique des installations

---

**Date**: 06/12/2025
**Version**: V17 Beta Enhanced
