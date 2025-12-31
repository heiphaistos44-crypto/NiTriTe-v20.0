#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Page Scripts Windows - NiTriTe V17
Exécution et gestion de scripts Windows (BAT, CMD, PS1)
"""

import customtkinter as ctk
import tkinter as tk
from tkinter import messagebox, scrolledtext
from pathlib import Path
import subprocess
import os
from v14_mvp.design_system import DesignTokens
from v14_mvp.components import ModernCard, ModernButton, ModernStatsCard
from v14_mvp.logger_system import logger


class WindowsScriptsPage(ctk.CTkFrame):
    """Page de gestion et exécution de scripts Windows"""

    def __init__(self, parent):
        super().__init__(parent, fg_color=DesignTokens.BG_PRIMARY)

        try:
            logger.info("PageScriptsWindows", "Initialisation de la page Scripts Windows")

            # Dossier des scripts (au niveau du projet ou portable)
            self.scripts_folder = self._get_scripts_folder()
            logger.info("PageScriptsWindows", f"Dossier scripts: {self.scripts_folder}")
            self.scripts_folder.mkdir(parents=True, exist_ok=True)

            self.scripts = []

            logger.debug("PageScriptsWindows", "Création du header")
            self._create_header()
            logger.debug("PageScriptsWindows", "Header créé")

            logger.debug("PageScriptsWindows", "Création des stats")
            self._create_stats()
            logger.debug("PageScriptsWindows", "Stats créées")

            logger.debug("PageScriptsWindows", "Création du contenu")
            self._create_content()
            logger.debug("PageScriptsWindows", "Contenu créé")

            logger.debug("PageScriptsWindows", "Rafraîchissement des scripts")
            self._refresh_scripts()
            logger.info("PageScriptsWindows", "Page Scripts Windows chargée avec succès")

        except Exception as e:
            logger.log_exception("PageScriptsWindows", e, "Erreur lors de l'initialisation de la page Scripts Windows")
            # Créer un message d'erreur visible
            error_label = ctk.CTkLabel(
                self,
                text=f" Erreur de chargement de la page Scripts Windows:\n\n{str(e)}",
                font=(DesignTokens.FONT_FAMILY, 14),
                text_color="#ff4444"
            )
            error_label.pack(expand=True)

    def _get_scripts_folder(self):
        """Obtenir le dossier des scripts"""
        # Essayer plusieurs emplacements
        possible_paths = [
            Path(__file__).parent.parent.parent / "Script Windows",
            Path.cwd() / "Script Windows",
            Path.home() / "Documents" / "NiTriTe_Scripts"
        ]

        for path in possible_paths:
            if path.exists():
                return path

        # Si aucun n'existe, utiliser le premier
        return possible_paths[0]

    def _create_header(self):
        """Header de la page"""
        header = ModernCard(self)
        header.pack(fill=tk.X, padx=20, pady=10)

        container = ctk.CTkFrame(header, fg_color="transparent")
        container.pack(fill=tk.X, padx=20, pady=15)

        left_side = ctk.CTkFrame(container, fg_color="transparent")
        left_side.pack(side=tk.LEFT, fill=tk.X, expand=True)

        title = ctk.CTkLabel(
            left_side,
            text="📜 Scripts Windows",
            font=(DesignTokens.FONT_FAMILY, 24, "bold"),
            text_color=DesignTokens.TEXT_PRIMARY
        )
        title.pack(side=tk.LEFT)

        subtitle = ctk.CTkLabel(
            left_side,
            text="Exécution en un clic • BAT, CMD, PS1",
            font=(DesignTokens.FONT_FAMILY, DesignTokens.FONT_SIZE_MD),
            text_color=DesignTokens.TEXT_SECONDARY
        )
        subtitle.pack(side=tk.LEFT, padx=20)

        # Boutons
        btn_frame = ctk.CTkFrame(container, fg_color="transparent")
        btn_frame.pack(side=tk.RIGHT)

        ModernButton(
            btn_frame,
            text=" Ouvrir Dossier",
            variant="outlined",
            command=self._open_folder
        ).pack(side=tk.LEFT, padx=5)

        ModernButton(
            btn_frame,
            text=" Nouveau Script",
            variant="filled",
            command=self._create_new_script
        ).pack(side=tk.LEFT, padx=5)

        ModernButton(
            btn_frame,
            text=" Rafraîchir",
            variant="outlined",
            command=self._refresh_scripts
        ).pack(side=tk.LEFT, padx=5)

    def _create_stats(self):
        """Stats"""
        stats_frame = ctk.CTkFrame(self, fg_color="transparent")
        stats_frame.pack(fill=tk.X, padx=20, pady=10)

        self.stats_total = ModernStatsCard(
            stats_frame,
            "Scripts BAT/CMD",
            0,
            "",
            DesignTokens.ACCENT_PRIMARY
        )
        self.stats_total.pack(side=tk.LEFT, fill=tk.X, expand=True, padx=5)

        self.stats_powershell = ModernStatsCard(
            stats_frame,
            "Scripts PowerShell",
            0,
            "",
            DesignTokens.INFO
        )
        self.stats_powershell.pack(side=tk.LEFT, fill=tk.X, expand=True, padx=5)

        self.stats_folder = ModernStatsCard(
            stats_frame,
            "Dossier",
            str(self.scripts_folder.name),
            "",
            DesignTokens.SUCCESS
        )
        self.stats_folder.pack(side=tk.LEFT, fill=tk.X, expand=True, padx=5)

    def _create_content(self):
        """Contenu avec liste des scripts"""
        scroll = ctk.CTkScrollableFrame(self, fg_color=DesignTokens.BG_PRIMARY)
        scroll.pack(fill=tk.BOTH, expand=True, padx=20, pady=10)

        self.scripts_container = scroll

    def _refresh_scripts(self):
        """Rafraîchir la liste des scripts"""
        # Vider le container
        for widget in self.scripts_container.winfo_children():
            widget.destroy()

        # Scanner le dossier récursivement
        self.scripts = []
        bat_count = 0
        ps_count = 0

        if self.scripts_folder.exists():
            # Utiliser rglob pour scanner récursivement les sous-dossiers
            for file in sorted(self.scripts_folder.rglob('*')):
                if file.is_file() and file.suffix.lower() in ['.bat', '.cmd', '.ps1']:
                    self.scripts.append(file)

                    if file.suffix.lower() in ['.bat', '.cmd']:
                        bat_count += 1
                    elif file.suffix.lower() == '.ps1':
                        ps_count += 1

        # Mettre à jour les stats
        self.stats_total.update_value(bat_count)
        self.stats_powershell.update_value(ps_count)

        # Afficher les scripts
        if self.scripts:
            for script in self.scripts:
                self._create_script_card(script)
        else:
            # Message si aucun script
            msg = ctk.CTkLabel(
                self.scripts_container,
                text=" Aucun script trouvé\n\nCliquez sur 'Nouveau Script' pour en créer un",
                font=(DesignTokens.FONT_FAMILY, DesignTokens.FONT_SIZE_MD),
                text_color=DesignTokens.TEXT_SECONDARY,
                justify=tk.CENTER
            )
            msg.pack(pady=50)

    def _create_script_card(self, script_path: Path):
        """Créer une carte pour un script"""
        card = ModernCard(self.scripts_container)
        card.pack(fill=tk.X, pady=5)

        container = ctk.CTkFrame(card, fg_color="transparent")
        container.pack(fill=tk.X, padx=15, pady=12)

        # Icône selon le type
        if script_path.suffix.lower() == '.ps1':
            icon = ""
            type_label = "PowerShell"
            color = DesignTokens.INFO
        else:
            icon = ""
            type_label = "Batch"
            color = DesignTokens.ACCENT_PRIMARY

        # Info gauche
        left = ctk.CTkFrame(container, fg_color="transparent")
        left.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        # Nom avec icône
        name_frame = ctk.CTkFrame(left, fg_color="transparent")
        name_frame.pack(anchor="w")

        ctk.CTkLabel(
            name_frame,
            text=icon,
            font=(DesignTokens.FONT_FAMILY, 20)
        ).pack(side=tk.LEFT, padx=(0, 10))

        ctk.CTkLabel(
            name_frame,
            text=script_path.name,
            font=(DesignTokens.FONT_FAMILY, DesignTokens.FONT_SIZE_MD, "bold"),
            text_color=DesignTokens.TEXT_PRIMARY
        ).pack(side=tk.LEFT)

        ctk.CTkLabel(
            name_frame,
            text=f"• {type_label}",
            font=(DesignTokens.FONT_FAMILY, DesignTokens.FONT_SIZE_SM),
            text_color=color
        ).pack(side=tk.LEFT, padx=10)

        # Chemin relatif (catégorie)
        try:
            relative_path = script_path.relative_to(self.scripts_folder).parent
            if str(relative_path) != ".":
                category_label = ctk.CTkLabel(
                    name_frame,
                    text=f" {relative_path}",
                    font=(DesignTokens.FONT_FAMILY, DesignTokens.FONT_SIZE_SM),
                    text_color=DesignTokens.TEXT_TERTIARY
                )
                category_label.pack(side=tk.LEFT, padx=5)
        except:
            pass

        # Taille du fichier
        size_kb = script_path.stat().st_size / 1024
        size_text = f"{size_kb:.1f} KB" if size_kb < 1024 else f"{size_kb/1024:.1f} MB"

        ctk.CTkLabel(
            left,
            text=f" Taille: {size_text}",
            font=(DesignTokens.FONT_FAMILY, DesignTokens.FONT_SIZE_SM),
            text_color=DesignTokens.TEXT_TERTIARY
        ).pack(anchor="w", pady=(5, 0))

        # Boutons à droite
        buttons = ctk.CTkFrame(container, fg_color="transparent")
        buttons.pack(side=tk.RIGHT)

        ModernButton(
            buttons,
            text=" Exécuter",
            variant="filled",
            size="sm",
            command=lambda: self._run_script(script_path)
        ).pack(side=tk.LEFT, padx=3)

        ModernButton(
            buttons,
            text=" Éditer",
            variant="outlined",
            size="sm",
            command=lambda: self._edit_script(script_path)
        ).pack(side=tk.LEFT, padx=3)

        ModernButton(
            buttons,
            text="",
            variant="text",
            size="sm",
            command=lambda: self._delete_script(script_path)
        ).pack(side=tk.LEFT, padx=3)

    def _run_script(self, script_path: Path):
        """Exécuter un script"""
        try:
            if script_path.suffix.lower() == '.ps1':
                # PowerShell
                subprocess.Popen(
                    ['powershell.exe', '-ExecutionPolicy', 'Bypass', '-File', str(script_path)],
                    cwd=str(script_path.parent),
                    creationflags=subprocess.CREATE_NEW_CONSOLE
                )
                messagebox.showinfo(
                    "Script lancé",
                    f"Le script PowerShell '{script_path.name}' a été lancé dans une nouvelle fenêtre."
                )
            else:
                # Batch/CMD
                subprocess.Popen(
                    ['cmd.exe', '/c', 'start', 'cmd.exe', '/k', str(script_path)],
                    cwd=str(script_path.parent),
                    shell=False
                )
                messagebox.showinfo(
                    "Script lancé",
                    f"Le script '{script_path.name}' a été lancé dans une nouvelle fenêtre de commande."
                )
        except Exception as e:
            messagebox.showerror(
                "Erreur d'exécution",
                f"Impossible d'exécuter le script:\n\n{str(e)}"
            )

    def _edit_script(self, script_path: Path):
        """Éditer un script"""
        # Créer fenêtre d'édition
        editor_window = ctk.CTkToplevel(self)
        editor_window.title(f"Éditer - {script_path.name}")
        editor_window.geometry("800x600")

        # Centrer
        editor_window.update_idletasks()
        x = (editor_window.winfo_screenwidth() // 2) - (800 // 2)
        y = (editor_window.winfo_screenheight() // 2) - (600 // 2)
        editor_window.geometry(f"800x600+{x}+{y}")

        # Container
        main = ctk.CTkFrame(editor_window, fg_color=DesignTokens.BG_PRIMARY)
        main.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

        # Titre
        title = ctk.CTkLabel(
            main,
            text=f" {script_path.name}",
            font=(DesignTokens.FONT_FAMILY, 18, "bold"),
            text_color=DesignTokens.TEXT_PRIMARY
        )
        title.pack(pady=10)

        # Zone de texte pour l'édition
        text_frame = ctk.CTkFrame(main, fg_color=DesignTokens.BG_ELEVATED)
        text_frame.pack(fill=tk.BOTH, expand=True, pady=10)

        logger.debug("PageScriptsWindows", f"Création Text widget pour édition de {script_path.name}",
                    bg="#1e1e1e", fg="#ffffff")

        text_editor = tk.Text(
            text_frame,
            wrap=tk.NONE,
            bg="#1e1e1e",
            fg="#ffffff",
            font=("Consolas", 11),
            insertbackground="#ffffff",
            relief=tk.FLAT,
            padx=10,
            pady=10
        )
        text_editor.pack(fill=tk.BOTH, expand=True, side=tk.LEFT)

        logger.debug("PageScriptsWindows", "Text widget créé et packed",
                    actual_bg=text_editor.cget("bg"),
                    actual_fg=text_editor.cget("fg"))

        # Scrollbars
        v_scroll = tk.Scrollbar(text_frame, command=text_editor.yview)
        v_scroll.pack(side=tk.RIGHT, fill=tk.Y)
        text_editor.config(yscrollcommand=v_scroll.set)

        h_scroll = tk.Scrollbar(text_frame, orient=tk.HORIZONTAL, command=text_editor.xview)
        h_scroll.pack(side=tk.BOTTOM, fill=tk.X)
        text_editor.config(xscrollcommand=h_scroll.set)

        # Charger le contenu
        try:
            content = script_path.read_text(encoding='utf-8')
        except:
            try:
                content = script_path.read_text(encoding='cp1252')
            except:
                content = script_path.read_text(encoding='latin-1')

        text_editor.insert("1.0", content)

        # Boutons
        btn_frame = ctk.CTkFrame(main, fg_color="transparent")
        btn_frame.pack(pady=10)

        def save_script():
            new_content = text_editor.get("1.0", tk.END).rstrip('\n')
            try:
                script_path.write_text(new_content, encoding='utf-8')
                messagebox.showinfo("Sauvegarde réussie", f"Le script '{script_path.name}' a été sauvegardé.")
                editor_window.destroy()
                self._refresh_scripts()
            except Exception as e:
                messagebox.showerror("Erreur", f"Impossible de sauvegarder:\n\n{str(e)}")

        ModernButton(
            btn_frame,
            text=" Sauvegarder",
            variant="filled",
            command=save_script
        ).pack(side=tk.LEFT, padx=5)

        ModernButton(
            btn_frame,
            text=" Annuler",
            variant="outlined",
            command=editor_window.destroy
        ).pack(side=tk.LEFT, padx=5)

    def _delete_script(self, script_path: Path):
        """Supprimer un script"""
        response = messagebox.askyesno(
            "Confirmer la suppression",
            f"Êtes-vous sûr de vouloir supprimer le script:\n\n{script_path.name}\n\nCette action est irréversible.",
            icon='warning'
        )

        if response:
            try:
                script_path.unlink()
                messagebox.showinfo("Suppression réussie", f"Le script '{script_path.name}' a été supprimé.")
                self._refresh_scripts()
            except Exception as e:
                messagebox.showerror("Erreur", f"Impossible de supprimer:\n\n{str(e)}")

    def _create_new_script(self):
        """Créer un nouveau script"""
        # Fenêtre de création
        create_window = ctk.CTkToplevel(self)
        create_window.title("Nouveau Script")
        create_window.geometry("600x550")
        create_window.transient(self)
        create_window.grab_set()

        # Centrer
        create_window.update_idletasks()
        x = (create_window.winfo_screenwidth() // 2) - (600 // 2)
        y = (create_window.winfo_screenheight() // 2) - (550 // 2)
        create_window.geometry(f"600x550+{x}+{y}")

        # Container
        main = ctk.CTkFrame(create_window, fg_color=DesignTokens.BG_PRIMARY)
        main.pack(fill=tk.BOTH, expand=True, padx=20, pady=20)

        # Titre
        title = ctk.CTkLabel(
            main,
            text=" Créer un nouveau script",
            font=(DesignTokens.FONT_FAMILY, 20, "bold"),
            text_color=DesignTokens.TEXT_PRIMARY
        )
        title.pack(pady=(0, 20))

        # Nom du script
        ctk.CTkLabel(
            main,
            text="Nom du script:",
            font=(DesignTokens.FONT_FAMILY, DesignTokens.FONT_SIZE_MD),
            text_color=DesignTokens.TEXT_PRIMARY
        ).pack(anchor="w", pady=(10, 5))

        name_entry = ctk.CTkEntry(
            main,
            placeholder_text="Mon_Script",
            font=(DesignTokens.FONT_FAMILY, DesignTokens.FONT_SIZE_MD),
            fg_color=DesignTokens.BG_ELEVATED,
            width=400
        )
        name_entry.pack(pady=(0, 10))

        # Type de script
        ctk.CTkLabel(
            main,
            text="Type de script:",
            font=(DesignTokens.FONT_FAMILY, DesignTokens.FONT_SIZE_MD),
            text_color=DesignTokens.TEXT_PRIMARY
        ).pack(anchor="w", pady=(10, 5))

        script_type = tk.StringVar(value=".bat")

        types_frame = ctk.CTkFrame(main, fg_color="transparent")
        types_frame.pack(anchor="w", pady=(0, 10))

        ctk.CTkRadioButton(
            types_frame,
            text=" Batch (.bat)",
            variable=script_type,
            value=".bat",
            font=(DesignTokens.FONT_FAMILY, DesignTokens.FONT_SIZE_SM)
        ).pack(side=tk.LEFT, padx=10)

        ctk.CTkRadioButton(
            types_frame,
            text=" PowerShell (.ps1)",
            variable=script_type,
            value=".ps1",
            font=(DesignTokens.FONT_FAMILY, DesignTokens.FONT_SIZE_SM)
        ).pack(side=tk.LEFT, padx=10)

        # Template initial
        ctk.CTkLabel(
            main,
            text="Contenu initial (optionnel):",
            font=(DesignTokens.FONT_FAMILY, DesignTokens.FONT_SIZE_MD),
            text_color=DesignTokens.TEXT_PRIMARY
        ).pack(anchor="w", pady=(10, 5))

        logger.debug("PageScriptsWindows", "Création Text widget pour nouveau script",
                    bg="#1e1e1e", fg="#ffffff")

        content_text = tk.Text(
            main,
            height=10,
            wrap=tk.WORD,
            bg="#1e1e1e",
            fg="#ffffff",
            font=("Consolas", 10),
            relief=tk.FLAT,
            padx=10,
            pady=10,
            insertbackground="#ffffff"
        )
        content_text.pack(fill=tk.X, pady=(0, 15))

        logger.debug("PageScriptsWindows", "Text widget nouveau script créé",
                    actual_bg=content_text.cget("bg"),
                    actual_fg=content_text.cget("fg"))

        # Template par défaut
        content_text.insert("1.0", "@echo off\necho Hello World!\npause")

        # Boutons
        btn_frame = ctk.CTkFrame(main, fg_color="transparent")
        btn_frame.pack()

        def create_script():
            name = name_entry.get().strip()
            if not name:
                messagebox.showerror("Erreur", "Veuillez entrer un nom pour le script.")
                return

            # Nettoyer le nom
            name = name.replace(" ", "_")
            if not name.endswith(script_type.get()):
                name += script_type.get()

            script_path = self.scripts_folder / name

            if script_path.exists():
                messagebox.showerror("Erreur", f"Un script nommé '{name}' existe déjà.")
                return

            content = content_text.get("1.0", tk.END).rstrip('\n')

            try:
                script_path.write_text(content, encoding='utf-8')
                messagebox.showinfo("Succès", f"Le script '{name}' a été créé avec succès.")
                create_window.destroy()
                self._refresh_scripts()
            except Exception as e:
                messagebox.showerror("Erreur", f"Impossible de créer le script:\n\n{str(e)}")

        ModernButton(
            btn_frame,
            text=" Créer",
            variant="filled",
            command=create_script
        ).pack(side=tk.LEFT, padx=5)

        ModernButton(
            btn_frame,
            text=" Annuler",
            variant="outlined",
            command=create_window.destroy
        ).pack(side=tk.LEFT, padx=5)

    def _open_folder(self):
        """Ouvrir le dossier des scripts"""
        try:
            os.startfile(str(self.scripts_folder))
        except Exception as e:
            messagebox.showerror("Erreur", f"Impossible d'ouvrir le dossier:\n\n{str(e)}")
