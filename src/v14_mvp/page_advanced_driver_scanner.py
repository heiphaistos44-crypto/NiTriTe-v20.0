#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Page Scanner Pilotes Avancé - NiTriTe V20
Scanner complet des drivers système comme Snappy Driver
Analyse tous les drivers installés et propose les mises à jour
"""

import customtkinter as ctk
import tkinter as tk
from tkinter import messagebox
import subprocess
import threading
import json
from pathlib import Path
from datetime import datetime
from v14_mvp.design_system import DesignTokens
from v14_mvp.components import ModernCard, ModernButton, SectionHeader


class AdvancedDriverScannerPage(ctk.CTkFrame):
    """Page Scanner de Pilotes Avancé - Analyse système complète"""

    def __init__(self, parent):
        super().__init__(parent, fg_color=DesignTokens.BG_PRIMARY)

        self.drivers_found = []
        self.scanning = False
        self.backup_folder = Path.home() / "Documents" / "NiTriTe_Driver_Backups"
        self.backup_folder.mkdir(parents=True, exist_ok=True)

        # Détecter type de PC
        self.is_laptop = self._detect_laptop()

        # Configurer grid layout
        self.grid_rowconfigure(0, weight=0)  # Header fixe
        self.grid_rowconfigure(1, weight=0)  # Stats fixe (rempli après scan)
        self.grid_rowconfigure(2, weight=1)  # Contenu scrollable
        self.grid_columnconfigure(0, weight=1)

        self._create_header()
        self._create_stats_section()  # Section stats fixe
        self._create_content()

    def _detect_laptop(self):
        """Détecter si c'est un portable ou un PC de bureau"""
        try:
            import psutil
            battery = psutil.sensors_battery()
            return battery is not None
        except:
            return False

    def _create_header(self):
        """Header de la page"""
        header = ModernCard(self)
        header.grid(row=0, column=0, sticky="ew", padx=20, pady=10)

        container = ctk.CTkFrame(header, fg_color="transparent")
        container.pack(fill=tk.X, padx=20, pady=15)

        # Titre avec icône
        title_container = ctk.CTkFrame(container, fg_color="transparent")
        title_container.pack(side=tk.LEFT)

        SectionHeader(title_container, text="🔬 Scanner de Pilotes Avancé").pack(side=tk.LEFT)

        pc_type = ctk.CTkLabel(
            title_container,
            text=f"  {'💻 Portable' if self.is_laptop else '🖥️ Bureau'}",
            font=(DesignTokens.FONT_FAMILY, DesignTokens.FONT_SIZE_MD),
            text_color=DesignTokens.ACCENT_PRIMARY
        )
        pc_type.pack(side=tk.LEFT, padx=10)

        # Boutons d'action
        actions = ctk.CTkFrame(container, fg_color="transparent")
        actions.pack(side=tk.RIGHT)

        ModernButton(
            actions,
            text="🔍 Scanner Maintenant",
            variant="filled",
            command=self._start_scan
        ).pack(side=tk.LEFT, padx=5)

        ModernButton(
            actions,
            text="💾 Sauvegarder Pilotes",
            variant="outlined",
            command=self._backup_all_drivers
        ).pack(side=tk.LEFT, padx=5)

        ModernButton(
            actions,
            text="♻️ Restaurer Sauvegarde",
            variant="outlined",
            command=self._restore_drivers
        ).pack(side=tk.LEFT, padx=5)

        ModernButton(
            actions,
            text="📊 Exporter Liste",
            variant="outlined",
            command=self._export_drivers_list
        ).pack(side=tk.LEFT, padx=5)

    def _create_stats_section(self):
        """Section statistiques fixe (affichée après scan)"""
        # Container pour les stats (caché par défaut, affiché après scan)
        self.stats_container = ctk.CTkFrame(self, fg_color="transparent")
        self.stats_container.grid(row=1, column=0, sticky="ew", padx=20, pady=0)
        self.stats_container.grid_remove()  # Caché par défaut

    def _create_content(self):
        """Contenu scrollable"""
        self.scroll = ctk.CTkScrollableFrame(
            self,
            fg_color=DesignTokens.BG_PRIMARY,
            height=600  # Hauteur minimale pour meilleure visibilité
        )
        self.scroll.grid(row=2, column=0, sticky="nsew", padx=20, pady=10)

        # Info message
        info_card = ModernCard(self.scroll)
        info_card.pack(fill=tk.X, pady=10)

        info_text = ctk.CTkLabel(
            info_card,
            text="ℹ️ Ce scanner analyse TOUS les pilotes installés sur votre PC et détecte les pilotes obsolètes ou manquants.\n"
                 "Similaire à Snappy Driver, il identifie les mises à jour disponibles via Windows Update.",
            font=(DesignTokens.FONT_FAMILY, DesignTokens.FONT_SIZE_SM),
            text_color=DesignTokens.TEXT_SECONDARY,
            justify="left",
            wraplength=800
        )
        info_text.pack(padx=20, pady=15)

        # Zone de résultats (sera remplie lors du scan)
        self.results_container = ctk.CTkFrame(self.scroll, fg_color="transparent")
        self.results_container.pack(fill=tk.BOTH, expand=True)

        self._show_welcome_message()

    def _show_welcome_message(self):
        """Message de bienvenue"""
        welcome = ModernCard(self.results_container)
        welcome.pack(fill=tk.BOTH, expand=True, pady=20)

        icon = ctk.CTkLabel(
            welcome,
            text="🔬",
            font=(DesignTokens.FONT_FAMILY, 64)
        )
        icon.pack(pady=20)

        title = ctk.CTkLabel(
            welcome,
            text="Prêt à scanner votre système",
            font=(DesignTokens.FONT_FAMILY, 24, "bold"),
            text_color=DesignTokens.TEXT_PRIMARY
        )
        title.pack(pady=10)

        desc = ctk.CTkLabel(
            welcome,
            text="Cliquez sur 'Scanner Maintenant' pour analyser tous vos pilotes\n"
                 "et détecter les mises à jour disponibles",
            font=(DesignTokens.FONT_FAMILY, DesignTokens.FONT_SIZE_MD),
            text_color=DesignTokens.TEXT_SECONDARY,
            justify="center"
        )
        desc.pack(pady=(10, 30), padx=20)

    def _start_scan(self):
        """Démarrer le scan des pilotes"""
        if self.scanning:
            messagebox.showinfo("Scan en cours", "Un scan est déjà en cours. Veuillez patienter...")
            return

        # Nettoyer résultats précédents
        for widget in self.results_container.winfo_children():
            widget.destroy()

        # Afficher indicateur de chargement
        loading_card = ModernCard(self.results_container)
        loading_card.pack(fill=tk.X, pady=10)

        loading_label = ctk.CTkLabel(
            loading_card,
            text="🔄 Analyse en cours...\n\nScanning du système pour détecter tous les pilotes installés\nCette opération peut prendre 1-2 minutes",
            font=(DesignTokens.FONT_FAMILY, DesignTokens.FONT_SIZE_MD),
            text_color=DesignTokens.TEXT_PRIMARY,
            justify="center"
        )
        loading_label.pack(pady=30)

        # Lancer scan dans un thread
        self.scanning = True
        thread = threading.Thread(target=self._perform_scan, daemon=True)
        thread.start()

    def _deduplicate_drivers(self, drivers):
        """Dédupliquer les pilotes basés sur DeviceName + ClassName

        Stratégie:
        - Groupe par (DeviceName, ClassName)
        - Pour chaque groupe, garde la version la plus récente ou la plus complète
        - Préfère les entrées signées
        """
        from datetime import datetime

        seen = {}  # Key: (DeviceName, ClassName), Value: driver dict

        for driver in drivers:
            device_name = driver.get('DeviceName', '').strip()
            class_name = driver.get('ClassName', '').strip()

            if not device_name:  # Skip invalid
                continue

            key = (device_name.lower(), class_name.lower())

            if key not in seen:
                # Premier occurence, garder
                seen[key] = driver
            else:
                # Doublon détecté - garder le meilleur
                existing = seen[key]

                # Critère 1: Préférer les signés
                existing_signed = existing.get('IsSigned', 'Non') == 'Oui'
                new_signed = driver.get('IsSigned', 'Non') == 'Oui'

                if new_signed and not existing_signed:
                    seen[key] = driver
                    continue
                elif existing_signed and not new_signed:
                    continue  # Garder existing

                # Critère 2: Préférer version la plus complète (pas "N/A")
                existing_version = existing.get('Version', 'N/A')
                new_version = driver.get('Version', 'N/A')

                if new_version != 'N/A' and existing_version == 'N/A':
                    seen[key] = driver
                    continue
                elif existing_version != 'N/A' and new_version == 'N/A':
                    continue

                # Critère 3: Préférer date la plus récente
                try:
                    existing_date = existing.get('Date', '1900-01-01')
                    new_date = driver.get('Date', '1900-01-01')

                    if existing_date != 'N/A' and new_date != 'N/A':
                        if new_date > existing_date:
                            seen[key] = driver
                except:
                    pass  # En cas d'erreur de comparaison, garder existing

        return list(seen.values())

    def _perform_scan(self):
        """Effectuer le scan (dans un thread séparé) - SANS ADMIN via WMI"""
        try:
            drivers = []

            # NOUVELLE MÉTHODE: WMI (Windows Management Instrumentation) - PAS BESOIN D'ADMIN!
            print("Scan drivers via WMI...")

            # 1. Scanner via WMI Win32_PnPSignedDriver
            try:
                cmd = """
Get-WmiObject Win32_PnPSignedDriver | Select-Object DeviceName, DriverVersion, DriverDate,
Manufacturer, DeviceClass, InfName, IsSigned, DriverProviderName, Location | ConvertTo-Json
                """.strip()

                result = subprocess.run(
                    ['powershell', '-ExecutionPolicy', 'Bypass', '-Command', cmd],
                    capture_output=True,
                    text=True,
                    timeout=90,
                    creationflags=subprocess.CREATE_NO_WINDOW if hasattr(subprocess, 'CREATE_NO_WINDOW') else 0
                )

                if result.returncode == 0 and result.stdout:
                    drivers_data = json.loads(result.stdout)
                    if isinstance(drivers_data, list):
                        for d in drivers_data:
                            if d and d.get('DeviceName'):
                                drivers.append({
                                    'Driver': d.get('InfName', 'N/A'),
                                    'DeviceName': d.get('DeviceName', 'N/A'),
                                    'ProviderName': d.get('DriverProviderName') or d.get('Manufacturer', 'N/A'),
                                    'ClassName': d.get('DeviceClass', 'N/A'),
                                    'Version': d.get('DriverVersion', 'N/A'),
                                    'Date': d.get('DriverDate', 'N/A')[:10] if d.get('DriverDate') else 'N/A',
                                    'Location': d.get('Location', 'N/A'),
                                    'IsSigned': 'Oui' if d.get('IsSigned') else 'Non'
                                })
                    print(f"✓ WMI: {len(drivers)} drivers trouvés")
            except Exception as e:
                print(f"Erreur WMI scan: {e}")

            # 2. Scanner périphériques PnP (SANS ADMIN)
            try:
                result = subprocess.run(
                    ['powershell', '-Command',
                     'Get-PnpDevice | Select-Object FriendlyName, Status, Class, Manufacturer | ConvertTo-Json'],
                    capture_output=True,
                    text=True,
                    timeout=60,
                    creationflags=subprocess.CREATE_NO_WINDOW if hasattr(subprocess, 'CREATE_NO_WINDOW') else 0
                )
                if result.returncode == 0 and result.stdout:
                    devices_data = json.loads(result.stdout)
                    if isinstance(devices_data, list):
                        print(f"✓ PnP: {len(devices_data)} périphériques détectés")
                        # Ajouter les périphériques qui n'ont pas de driver correspondant
                        for dev in devices_data:
                            if dev and dev.get('Status') == 'OK' and dev.get('FriendlyName'):
                                # Vérifier si pas déjà dans drivers
                                device_name = dev.get('FriendlyName')
                                if not any(d.get('DeviceName') == device_name for d in drivers):
                                    drivers.append({
                                        'Driver': 'Système',
                                        'DeviceName': device_name,
                                        'ProviderName': dev.get('Manufacturer', 'Microsoft'),
                                        'ClassName': dev.get('Class', 'Système'),
                                        'Version': 'Intégré',
                                        'Date': 'N/A',
                                        'Location': 'Windows',
                                        'IsSigned': 'Oui'
                                    })
            except Exception as e:
                print(f"Erreur PnP scan: {e}")

            # DÉDUPLICATION: Supprimer les doublons basés sur DeviceName + ClassName
            drivers = self._deduplicate_drivers(drivers)
            print(f"✓ Après déduplication: {len(drivers)} pilotes uniques")

            self.drivers_found = drivers

            # Afficher résultats dans l'UI (thread-safe)
            self.after(0, self._display_scan_results)

        except Exception as e:
            self.after(0, lambda: messagebox.showerror("Erreur de scan", f"Erreur lors du scan:\n\n{str(e)}"))
        finally:
            self.scanning = False

    def _display_scan_results(self):
        """Afficher les résultats du scan"""
        # Nettoyer stats et résultats
        for widget in self.stats_container.winfo_children():
            widget.destroy()
        for widget in self.results_container.winfo_children():
            widget.destroy()

        if not self.drivers_found:
            # Cacher stats et afficher erreur
            self.stats_container.grid_remove()

            no_result = ModernCard(self.results_container)
            no_result.pack(fill=tk.X, pady=20)

            ctk.CTkLabel(
                no_result,
                text="⚠️ Aucun pilote détecté\n\nLe scan n'a trouvé aucun pilote. Cela peut arriver si:\n• Les commandes PowerShell sont bloquées\n• Droits administrateur nécessaires",
                font=(DesignTokens.FONT_FAMILY, DesignTokens.FONT_SIZE_MD),
                text_color=DesignTokens.TEXT_SECONDARY,
                justify="center"
            ).pack(pady=30, padx=20)
            return

        # Afficher la section stats
        self.stats_container.grid()

        # Résumé (dans stats_container - fixe)
        summary_card = ModernCard(self.stats_container)
        summary_card.pack(fill=tk.X, pady=(0, 10), padx=0)

        summary_title = SectionHeader(summary_card, text=f"📊 Résultat du Scan - {len(self.drivers_found)} pilotes trouvés")
        summary_title.pack(pady=10)

        # Grouper les pilotes par catégorie
        drivers_by_category = {}
        category_icons = {
            "Audio": "🔊",
            "Display": "🖥️",
            "Network": "🌐",
            "System": "⚙️",
            "USB": "🔌",
            "Human Interface Devices": "🖱️",
            "Disk drives": "💾",
            "Monitor": "🖥️",
            "Keyboard": "⌨️",
            "Mouse": "🖱️",
            "Bluetooth": "📶",
            "Imaging devices": "📷",
            "Printer": "🖨️",
            "SCSI": "💿",
            "Sound": "🔊",
            "Video": "🎬",
            "Storage": "💾"
        }

        for driver in self.drivers_found:
            class_name = driver.get('DeviceClass', driver.get('ClassName', 'Autres'))
            if class_name not in drivers_by_category:
                drivers_by_category[class_name] = []
            drivers_by_category[class_name].append(driver)

        # Trier par nombre de pilotes (décroissant)
        sorted_categories = sorted(drivers_by_category.items(), key=lambda x: len(x[1]), reverse=True)

        # Statistiques par catégorie
        stats_text = f"✅ Scan terminé le {datetime.now().strftime('%d/%m/%Y à %H:%M')}\n"
        stats_text += f"📌 {len(self.drivers_found)} pilotes répartis en {len(sorted_categories)} catégories"

        summary_text = ctk.CTkLabel(
            summary_card,
            text=stats_text,
            font=(DesignTokens.FONT_FAMILY, DesignTokens.FONT_SIZE_SM),
            text_color=DesignTokens.TEXT_SECONDARY
        )
        summary_text.pack(pady=10, padx=20)

        # Cartes de statistiques par catégorie (top 5) - dans stats_container (fixe)
        stats_row = ctk.CTkFrame(self.stats_container, fg_color="transparent")
        stats_row.pack(fill=tk.X, pady=(0, 10), padx=0)

        for i, (cat_name, drivers) in enumerate(sorted_categories[:5]):
            icon = category_icons.get(cat_name, "📦")
            stat_card = ModernCard(stats_row)
            stat_card.pack(side=tk.LEFT, fill=tk.X, expand=True, padx=5)

            container = ctk.CTkFrame(stat_card, fg_color="transparent")
            container.pack(padx=15, pady=12)

            ctk.CTkLabel(
                container,
                text=icon,
                font=(DesignTokens.FONT_FAMILY, 24)
            ).pack(side=tk.LEFT, padx=(0, 10))

            info = ctk.CTkFrame(container, fg_color="transparent")
            info.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

            ctk.CTkLabel(
                info,
                text=cat_name,
                font=(DesignTokens.FONT_FAMILY, 11),
                text_color=DesignTokens.TEXT_SECONDARY,
                anchor="w"
            ).pack(anchor="w")

            ctk.CTkLabel(
                info,
                text=str(len(drivers)),
                font=(DesignTokens.FONT_FAMILY, 20, "bold"),
                text_color=DesignTokens.TEXT_PRIMARY,
                anchor="w"
            ).pack(anchor="w")

        # Liste des pilotes par catégories (dans results_container - scrollable)
        drivers_title = SectionHeader(self.results_container, text="🔧 Pilotes par Catégorie")
        drivers_title.pack(pady=10)

        # Container pour les catégories (directement dans results_container qui est déjà scrollable)
        categories_container = ctk.CTkFrame(
            self.results_container,
            fg_color=DesignTokens.BG_SECONDARY,
            corner_radius=DesignTokens.RADIUS_LG
        )
        categories_container.pack(fill=tk.BOTH, expand=True, pady=10)

        # Créer une section repliable pour chaque catégorie
        self.expanded_driver_categories = set()  # Aucune catégorie ouverte par défaut
        self.driver_category_frames = {}
        self.driver_category_buttons = {}

        for cat_name, drivers in sorted_categories:
            icon = category_icons.get(cat_name, "📦")
            is_expanded = cat_name in self.expanded_driver_categories
            arrow = "▼" if is_expanded else "▶"

            # Bouton catégorie (repliable)
            cat_button = ctk.CTkButton(
                categories_container,
                text=f"{arrow} {icon} {cat_name} ({len(drivers)} pilotes)",
                font=(DesignTokens.FONT_FAMILY, 13, "bold"),
                text_color=DesignTokens.ACCENT_PRIMARY,
                fg_color=DesignTokens.BG_ELEVATED,
                hover_color=DesignTokens.BG_HOVER,
                anchor="w",
                command=lambda c=cat_name: self._toggle_driver_category(c)
            )
            cat_button.pack(fill=tk.X, pady=(10, 2), padx=5)
            self.driver_category_buttons[cat_name] = cat_button

            # Frame pour les pilotes de cette catégorie
            drivers_frame = ctk.CTkFrame(categories_container, fg_color="transparent")
            self.driver_category_frames[cat_name] = drivers_frame

            # Afficher les pilotes de la catégorie
            for i, driver in enumerate(drivers):
                driver_frame = ctk.CTkFrame(drivers_frame, fg_color=DesignTokens.BG_PRIMARY, corner_radius=8)
                driver_frame.pack(fill=tk.X, pady=3, padx=10)

                # Info driver (version compacte)
                info_frame = ctk.CTkFrame(driver_frame, fg_color="transparent")
                info_frame.pack(side=tk.LEFT, fill=tk.X, expand=True, padx=15, pady=10)

                device_name = driver.get('DeviceName', driver.get('Driver', 'Inconnu'))
                provider = driver.get('ProviderName', driver.get('Manufacturer', 'N/A'))
                version = driver.get('DriverVersion', driver.get('Version', 'N/A'))

                ctk.CTkLabel(
                    info_frame,
                    text=f"📦 {device_name}",
                    font=(DesignTokens.FONT_FAMILY, 12, "bold"),
                    text_color=DesignTokens.TEXT_PRIMARY,
                    anchor="w"
                ).pack(anchor="w")

                ctk.CTkLabel(
                    info_frame,
                    text=f"Fabricant: {provider}  •  Version: {version}",
                    font=(DesignTokens.FONT_FAMILY, 10),
                    text_color=DesignTokens.TEXT_SECONDARY,
                    anchor="w"
                ).pack(anchor="w", pady=(2, 0))

                # Boutons d'action
                buttons_frame = ctk.CTkFrame(driver_frame, fg_color="transparent")
                buttons_frame.pack(side=tk.RIGHT, padx=10)

                # Bouton Mettre à jour (comme Snappy Driver)
                ModernButton(
                    buttons_frame,
                    text="🔄 MAJ",
                    variant="filled",
                    size="sm",
                    width=80,
                    command=lambda d=driver: self._update_driver(d)
                ).pack(side=tk.LEFT, padx=3)

                # Bouton détails (avec couleur visible)
                detail_btn = ModernButton(
                    buttons_frame,
                    text="ℹ️",
                    variant="outlined",
                    size="sm",
                    width=40,
                    command=lambda d=driver: self._show_driver_details(d)
                )
                detail_btn.configure(
                    text_color="#FFFFFF",
                    border_color=DesignTokens.ACCENT_PRIMARY,
                    fg_color="transparent"
                )
                detail_btn.pack(side=tk.LEFT, padx=3)

            # Afficher la frame si catégorie ouverte
            if is_expanded:
                drivers_frame.pack(fill=tk.X, pady=(0, 5))

    def _toggle_driver_category(self, category):
        """Ouvrir/Fermer une catégorie de pilotes (accordéon)"""
        if category in self.expanded_driver_categories:
            # Fermer la catégorie
            self.expanded_driver_categories.remove(category)
            self.driver_category_frames[category].pack_forget()
        else:
            # Ouvrir la catégorie
            self.expanded_driver_categories.add(category)
            # Remettre la frame APRÈS le bouton pour maintenir l'ordre
            self.driver_category_frames[category].pack(fill=tk.X, pady=(0, 5), after=self.driver_category_buttons[category])

        # Rafraîchir les flèches de toutes les catégories
        self._refresh_driver_categories()

    def _refresh_driver_categories(self):
        """Rafraîchir les flèches des catégories de pilotes"""
        for category, button in self.driver_category_buttons.items():
            is_expanded = category in self.expanded_driver_categories
            arrow = "▼" if is_expanded else "▶"
            text = button.cget("text")
            if text.startswith("▶") or text.startswith("▼"):
                parts = text.split(" ", 1)
                if len(parts) > 1:
                    button.configure(text=f"{arrow} {parts[1]}")

    def _backup_all_drivers(self):
        """Sauvegarder tous les pilotes du système"""
        response = messagebox.askyesno(
            "Sauvegarder les Pilotes",
            f"Cette opération va sauvegarder TOUS les pilotes tiers installés.\n\n"
            f"Dossier de sauvegarde:\n{self.backup_folder}\n\n"
            f"Cette opération peut prendre plusieurs minutes.\n\nContinuer ?"
        )

        if not response:
            return

        # Créer dossier avec timestamp
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        backup_path = self.backup_folder / f"backup_{timestamp}"
        backup_path.mkdir(parents=True, exist_ok=True)

        # Lancer sauvegarde dans un thread
        def perform_backup():
            try:
                # Utiliser DISM pour exporter les pilotes
                result = subprocess.run(
                    ['dism', '/online', '/export-driver', f'/destination:{backup_path}'],
                    capture_output=True,
                    text=True,
                    timeout=300  # 5 minutes max
                )

                if result.returncode == 0:
                    self.after(0, lambda: messagebox.showinfo(
                        "Sauvegarde Réussie",
                        f"✅ Tous les pilotes ont été sauvegardés avec succès!\n\n"
                        f"Dossier: {backup_path}\n\n"
                        f"Vous pouvez restaurer cette sauvegarde à tout moment."
                    ))
                else:
                    self.after(0, lambda: messagebox.showerror(
                        "Erreur",
                        f"Erreur lors de la sauvegarde:\n\n{result.stderr}"
                    ))
            except Exception as e:
                self.after(0, lambda: messagebox.showerror("Erreur", f"Erreur lors de la sauvegarde:\n\n{str(e)}"))

        thread = threading.Thread(target=perform_backup, daemon=True)
        thread.start()

    def _restore_drivers(self):
        """Restaurer les pilotes depuis une sauvegarde"""
        # Lister les sauvegardes disponibles
        backups = sorted(self.backup_folder.glob("backup_*"), reverse=True)

        if not backups:
            messagebox.showinfo(
                "Aucune Sauvegarde",
                "Aucune sauvegarde de pilotes trouvée.\n\n"
                "Utilisez 'Sauvegarder Pilotes' pour créer une sauvegarde d'abord."
            )
            return

        # TODO: Afficher dialogue de sélection de sauvegarde
        # Pour l'instant, utiliser la plus récente
        latest_backup = backups[0]

        response = messagebox.askyesno(
            "Restaurer les Pilotes",
            f"Restaurer la sauvegarde du {latest_backup.name.replace('backup_', '')}?\n\n"
            f"⚠️ ATTENTION: Cette opération nécessite un redémarrage du PC.\n\n"
            f"Continuer ?"
        )

        if not response:
            return

        messagebox.showinfo(
            "Restauration Manuelle",
            f"Pour restaurer les pilotes:\n\n"
            f"1. Ouvrez le Gestionnaire de périphériques\n"
            f"2. Clic droit sur un périphérique > Mettre à jour le pilote\n"
            f"3. Choisissez 'Parcourir mon ordinateur'\n"
            f"4. Sélectionnez le dossier:\n   {latest_backup}\n\n"
            f"Répétez pour chaque périphérique à restaurer."
        )

    def _update_driver(self, driver):
        """Mettre à jour un pilote via Windows Update (comme Snappy Driver)"""
        device_name = driver.get('DeviceName', driver.get('Driver', 'Inconnu'))
        device_id = driver.get('DeviceID', driver.get('InstanceId', ''))

        # Confirmation
        if not messagebox.askyesno(
            "Mettre à jour le pilote",
            f"Voulez-vous mettre à jour le pilote:\n\n{device_name}\n\n"
            f"Cette opération va:\n"
            f"• Rechercher une mise à jour via Windows Update\n"
            f"• Installer automatiquement la dernière version\n"
            f"• Nécessite les droits administrateur\n\n"
            f"⚠️ Un redémarrage peut être nécessaire après la mise à jour."
        ):
            return

        # Message de progression
        progress_dialog = ctk.CTkToplevel(self)
        progress_dialog.title("Mise à jour du pilote")
        progress_dialog.geometry("500x250")
        progress_dialog.transient(self)
        progress_dialog.grab_set()

        ctk.CTkLabel(
            progress_dialog,
            text="🔄 Mise à jour en cours...",
            font=(DesignTokens.FONT_FAMILY, 16, "bold")
        ).pack(pady=20)

        status_label = ctk.CTkLabel(
            progress_dialog,
            text=f"Recherche de mises à jour pour:\n{device_name}",
            font=(DesignTokens.FONT_FAMILY, 12),
            justify="center"
        )
        status_label.pack(pady=10)

        def update_thread():
            try:
                # Méthode 1: Via Windows Update (recommandé)
                status_label.configure(text="📡 Connexion à Windows Update...")
                progress_dialog.update()

                ps_cmd = f"""
$deviceId = "{device_id}"
$updateSession = New-Object -ComObject Microsoft.Update.Session
$updateSearcher = $updateSession.CreateUpdateSearcher()
$updateSearcher.ServerSelection = 2  # Windows Update

Write-Host "Recherche de mises à jour..."
$searchResult = $updateSearcher.Search("IsInstalled=0 AND Type='Driver'")

$found = $false
foreach ($update in $searchResult.Updates) {{
    if ($update.Title -like "*{device_name}*") {{
        Write-Host "Mise à jour trouvée: $($update.Title)"
        $found = $true

        $updatesToDownload = New-Object -ComObject Microsoft.Update.UpdateColl
        $updatesToDownload.Add($update) | Out-Null

        Write-Host "Téléchargement..."
        $downloader = $updateSession.CreateUpdateDownloader()
        $downloader.Updates = $updatesToDownload
        $downloader.Download()

        Write-Host "Installation..."
        $installer = $updateSession.CreateUpdateInstaller()
        $installer.Updates = $updatesToDownload
        $result = $installer.Install()

        if ($result.ResultCode -eq 2) {{
            Write-Host "SUCCESS"
        }} else {{
            Write-Host "FAILED:$($result.ResultCode)"
        }}
        break
    }}
}}

if (-not $found) {{
    Write-Host "NO_UPDATE_FOUND"
}}
"""
                result = subprocess.run(
                    ['powershell', '-NoProfile', '-ExecutionPolicy', 'Bypass', '-Command', ps_cmd],
                    capture_output=True,
                    text=True,
                    timeout=120,
                    creationflags=subprocess.CREATE_NO_WINDOW if os.name == 'nt' else 0
                )

                output = result.stdout.strip()

                # Analyser le résultat
                if "SUCCESS" in output:
                    self.after(0, lambda: progress_dialog.destroy())
                    self.after(10, lambda: messagebox.showinfo(
                        "Mise à jour réussie",
                        f"✅ Le pilote a été mis à jour avec succès!\n\n{device_name}\n\n"
                        f"💡 Conseil: Redémarrez votre PC pour finaliser l'installation."
                    ))
                elif "NO_UPDATE_FOUND" in output:
                    self.after(0, lambda: progress_dialog.destroy())
                    self.after(10, lambda: messagebox.showinfo(
                        "Aucune mise à jour",
                        f"ℹ️ Aucune mise à jour disponible pour ce pilote.\n\n{device_name}\n\n"
                        f"Le pilote installé est peut-être déjà la dernière version."
                    ))
                else:
                    raise Exception("Échec de la mise à jour Windows Update")

            except Exception as e:
                self.after(0, lambda: progress_dialog.destroy())
                self.after(10, lambda: messagebox.showerror(
                    "Erreur de mise à jour",
                    f"❌ Impossible de mettre à jour le pilote:\n\n{str(e)}\n\n"
                    f"💡 Solutions:\n"
                    f"• Exécutez NiTriTe en tant qu'administrateur\n"
                    f"• Vérifiez votre connexion Internet\n"
                    f"• Utilisez Windows Update manuellement\n"
                    f"• Téléchargez le pilote depuis le site du fabricant"
                ))

        threading.Thread(target=update_thread, daemon=True).start()

    def _show_driver_details(self, driver):
        """Afficher les détails complets d'un driver"""
        details = f"""
╔═══════════════════════════════════════════════════════════╗
║              DÉTAILS COMPLETS DU PILOTE                   ║
╚═══════════════════════════════════════════════════════════╝

📦 Nom du Driver:     {driver.get('Driver', 'N/A')}
🏢 Fabricant:         {driver.get('ProviderName', 'N/A')}
📂 Classe:            {driver.get('ClassName', 'N/A')}
🔢 Version:           {driver.get('Version', 'N/A')}
📅 Date:              {driver.get('Date', 'N/A')}
📄 Fichier Original:  {driver.get('OriginalFileName', 'N/A')}
⚠️ Boot Critical:     {"Oui" if driver.get('BootCritical') else "Non"}

═══════════════════════════════════════════════════════════

Informations Techniques:
"""
        # Ajouter toutes les autres clés
        for key, value in driver.items():
            if key not in ['Driver', 'ProviderName', 'ClassName', 'Version', 'Date', 'OriginalFileName', 'BootCritical']:
                details += f"\n{key}: {value}"

        # Créer fenêtre de dialogue
        dialog = ctk.CTkToplevel(self)
        dialog.title(f"Détails - {driver.get('Driver', 'Driver')}")
        dialog.geometry("700x500")

        # Centrer la fenêtre
        dialog.update_idletasks()
        x = (dialog.winfo_screenwidth() // 2) - (700 // 2)
        y = (dialog.winfo_screenheight() // 2) - (500 // 2)
        dialog.geometry(f"700x500+{x}+{y}")

        # Zone de texte
        text_widget = ctk.CTkTextbox(
            dialog,
            font=("Consolas", 11),
            fg_color=DesignTokens.BG_ELEVATED,
            wrap="word"
        )
        text_widget.pack(fill=tk.BOTH, expand=True, padx=20, pady=20)
        text_widget.insert("1.0", details)
        text_widget.configure(state="disabled")

        # Bouton fermer
        ModernButton(
            dialog,
            text="Fermer",
            variant="filled",
            command=dialog.destroy
        ).pack(pady=10)

    def _export_drivers_list(self):
        """Exporter la liste des drivers en TXT/CSV"""
        if not self.drivers_found:
            messagebox.showinfo("Aucun Driver", "Veuillez d'abord effectuer un scan avant d'exporter.")
            return

        from tkinter import filedialog

        # Demander format
        format_choice = messagebox.askquestion(
            "Format d'Export",
            "Exporter en format CSV ?\n\nOui = CSV (Excel)\nNon = TXT (Texte)"
        )

        if format_choice == 'yes':
            default_ext = ".csv"
            file_types = [("CSV files", "*.csv"), ("All files", "*.*")]
        else:
            default_ext = ".txt"
            file_types = [("Text files", "*.txt"), ("All files", "*.*")]

        # Demander emplacement
        filename = filedialog.asksaveasfilename(
            title="Enregistrer la liste des drivers",
            defaultextension=default_ext,
            filetypes=file_types,
            initialfile=f"drivers_list_{datetime.now().strftime('%Y%m%d_%H%M%S')}{default_ext}"
        )

        if not filename:
            return

        try:
            with open(filename, 'w', encoding='utf-8') as f:
                if format_choice == 'yes':
                    # Format CSV
                    f.write("Numéro;Driver;Fabricant;Classe;Version;Date;Fichier;Boot Critical\n")
                    for i, driver in enumerate(self.drivers_found, 1):
                        f.write(f"{i};"
                                f"{driver.get('Driver', 'N/A')};"
                                f"{driver.get('ProviderName', 'N/A')};"
                                f"{driver.get('ClassName', 'N/A')};"
                                f"{driver.get('Version', 'N/A')};"
                                f"{driver.get('Date', 'N/A')};"
                                f"{driver.get('OriginalFileName', 'N/A')};"
                                f"{'Oui' if driver.get('BootCritical') else 'Non'}\n")
                else:
                    # Format TXT
                    f.write("═══════════════════════════════════════════════════════════\n")
                    f.write("     LISTE COMPLÈTE DES PILOTES INSTALLÉS\n")
                    f.write(f"     Généré le {datetime.now().strftime('%d/%m/%Y à %H:%M:%S')}\n")
                    f.write(f"     Total: {len(self.drivers_found)} pilotes\n")
                    f.write("═══════════════════════════════════════════════════════════\n\n")

                    for i, driver in enumerate(self.drivers_found, 1):
                        f.write(f"[{i}] {driver.get('Driver', 'N/A')}\n")
                        f.write(f"    Fabricant:     {driver.get('ProviderName', 'N/A')}\n")
                        f.write(f"    Classe:        {driver.get('ClassName', 'N/A')}\n")
                        f.write(f"    Version:       {driver.get('Version', 'N/A')}\n")
                        f.write(f"    Date:          {driver.get('Date', 'N/A')}\n")
                        f.write(f"    Fichier:       {driver.get('OriginalFileName', 'N/A')}\n")
                        f.write(f"    Boot Critical: {'Oui' if driver.get('BootCritical') else 'Non'}\n")
                        f.write("───────────────────────────────────────────────────────────\n\n")

            messagebox.showinfo(
                "Export Réussi",
                f"✅ Liste exportée avec succès!\n\n"
                f"Fichier: {filename}\n"
                f"Pilotes exportés: {len(self.drivers_found)}"
            )

            # Ouvrir le fichier
            if messagebox.askyesno("Ouvrir le fichier", "Voulez-vous ouvrir le fichier exporté ?"):
                subprocess.run(['notepad.exe', filename])

        except Exception as e:
            messagebox.showerror("Erreur d'Export", f"Erreur lors de l'export:\n\n{str(e)}")
