"""
Interface GUI pour automation de scripts - NiTriTe V13
Éditeur, templates, planificateur
"""

import tkinter as tk
from tkinter import ttk, messagebox, scrolledtext, simpledialog
import customtkinter as ctk
import logging
from datetime import datetime
from typing import Dict, Optional

try:
    from script_automation import ScriptManager, ScriptTemplate, TaskScheduler
except ImportError:
    import sys
    from pathlib import Path
    sys.path.append(str(Path(__file__).parent))
    from script_automation import ScriptManager, ScriptTemplate, TaskScheduler


class ScriptAutomationGUI(ctk.CTkFrame):
    """Interface graphique pour automation de scripts"""

    def __init__(self, parent_frame, colors=None):
        # Initialiser le Frame parent
        super().__init__(parent_frame, fg_color='#0a0a0a', corner_radius=0)

        self.logger = logging.getLogger(__name__)

        # Couleurs
        self.colors = colors or {
            'bg': '#0a0a0a',
            'fg': '#ffffff',
            'primary': '#ff6b00',
            'secondary': '#1e1e2e',
            'success': '#00e676',
            'warning': '#ffa000',
            'danger': '#ff3d00',
            'text_secondary': '#888888',
            'border': '#333333'
        }

        # Managers
        self.script_manager = ScriptManager()
        self.task_scheduler = TaskScheduler()

        # Script actuel
        self.current_script_id = None

        # Interface
        self.create_ui()

    def create_ui(self):
        """Crée l'interface utilisateur"""
        # Container principal (self est déjà le Frame principal)
        main_container = ctk.CTkFrame(self, fg_color=self.colors['bg'])
        main_container.pack(fill=tk.BOTH, expand=True)

        canvas = tk.Canvas(main_container, fg_color=self.colors['bg'], highlightthickness=0)
        scrollbar = ttk.Scrollbar(main_container, orient=tk.VERTICAL, command=canvas.yview)

        self.scrollable_frame = ctk.CTkFrame(canvas, fg_color=self.colors['bg'])
        self.scrollable_frame.bind(
            "<Configure>",
            lambda e: canvas.configure(scrollregion=canvas.bbox("all"))
        )

        canvas.create_window((0, 0), window=self.scrollable_frame, anchor="nw")
        canvas.configure(yscrollcommand=scrollbar.set)

        canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        # Header
        self._create_header()

        # Notebook
        self.notebook = ttk.Notebook(self.scrollable_frame)
        self.notebook.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

        # Onglet 1: Éditeur de scripts
        self.editor_tab = ctk.CTkFrame(self.notebook, fg_color=self.colors['bg'])
        self.notebook.add(self.editor_tab, text="   Éditeur  ")
        self._create_editor_tab()

        # Onglet 2: Templates
        self.templates_tab = ctk.CTkFrame(self.notebook, fg_color=self.colors['bg'])
        self.notebook.add(self.templates_tab, text="   Templates  ")
        self._create_templates_tab()

        # Onglet 3: Mes Scripts
        self.scripts_tab = ctk.CTkFrame(self.notebook, fg_color=self.colors['bg'])
        self.notebook.add(self.scripts_tab, text="   Mes Scripts  ")
        self._create_scripts_tab()

        # Onglet 4: Planificateur
        self.scheduler_tab = ctk.CTkFrame(self.notebook, fg_color=self.colors['bg'])
        self.notebook.add(self.scheduler_tab, text="  ⏰ Planificateur  ")
        self._create_scheduler_tab()

    def _create_header(self):
        """Crée le header"""
        header = ctk.CTkFrame(self.scrollable_frame, fg_color=self.colors['secondary'], height=60)
        header.pack(fill=tk.X, padx=10, pady=10)
        header.pack_propagate(False)

        title = ctk.CTkLabel(
            header,
            text=" Automation de Scripts",
            fg_color=self.colors['secondary'],
            text_color=self.colors['primary'],
            font=('Segoe UI', 16, 'bold')
        )
        title.pack(side=tk.LEFT, padx=20)

    def _create_editor_tab(self):
        """Onglet éditeur de scripts"""
        container = ctk.CTkFrame(self.editor_tab, fg_color=self.colors['bg'])
        container.pack(fill=tk.BOTH, expand=True, padx=20, pady=20)

        # Toolbar
        toolbar = ctk.CTkFrame(container, fg_color=self.colors['secondary'])
        toolbar.pack(fill=tk.X, pady=(0, 10))

        # Nom du script
        name_frame = ctk.CTkFrame(toolbar, fg_color=self.colors['secondary'])
        name_frame.pack(side=tk.LEFT, padx=10, pady=10)

        ctk.CTkLabel(
            name_frame,
            text="Nom:",
            fg_color=self.colors['secondary'],
            text_color=self.colors['text_secondary'],
            font=('Segoe UI', 9)
        ).pack(side=tk.LEFT, padx=5)

        self.script_name_entry = ctk.CTkEntry(
            name_frame,
            fg_color='#1a1a1a',
            text_color=self.colors['fg'],
            font=('Segoe UI', 10),
            width=30,
            insertbackground=self.colors['primary']
        )
        self.script_name_entry.pack(side=tk.LEFT, padx=5)
        self.script_name_entry.insert(0, "Nouveau Script")

        # Langage
        ctk.CTkLabel(
            name_frame,
            text="Langage:",
            fg_color=self.colors['secondary'],
            text_color=self.colors['text_secondary'],
            font=('Segoe UI', 9)
        ).pack(side=tk.LEFT, padx=(20, 5))

        self.language_var = tk.StringVar(value="powershell")
        language_combo = ttk.Combobox(
            name_frame,
            textvariable=self.language_var,
            values=["powershell", "batch", "python"],
            state='readonly',
            width=12
        )
        language_combo.pack(side=tk.LEFT, padx=5)

        # Boutons
        btn_frame = ctk.CTkFrame(toolbar, fg_color=self.colors['secondary'])
        btn_frame.pack(side=tk.RIGHT, padx=10)

        ctk.CTkButton(
            btn_frame,
            text=" Sauvegarder",
            command=self.save_script,
            fg_color=self.colors['success'],
            text_color='white',
            font=('Segoe UI', 9, 'bold'),
            bd=0,
            padx=15,
            pady=6,
            cursor='hand2'
        ).pack(side=tk.LEFT, padx=5)

        ctk.CTkButton(
            btn_frame,
            text=" Exécuter",
            command=self.execute_current_script,
            fg_color=self.colors['primary'],
            text_color='white',
            font=('Segoe UI', 9, 'bold'),
            bd=0,
            padx=15,
            pady=6,
            cursor='hand2'
        ).pack(side=tk.LEFT, padx=5)

        ctk.CTkButton(
            btn_frame,
            text=" Nouveau",
            command=self.new_script,
            fg_color=self.colors['secondary'],
            text_color=self.colors['fg'],
            font=('Segoe UI', 9),
            bd=1,
            relief=tk.SOLID,
            padx=15,
            pady=6,
            cursor='hand2'
        ).pack(side=tk.LEFT, padx=5)

        # Éditeur de code
        editor_frame = ctk.CTkFrame(container, fg_color=self.colors['bg'])
        editor_frame.pack(fill=tk.BOTH, expand=True)

        # Numéros de lignes
        self.line_numbers = tk.Text(
            editor_frame,
            fg_color='#1a1a1a',
            text_color=self.colors['text_secondary'],
            font=('Consolas', 10),
            width=4,
            state='disabled',
            padx=5
        )
        self.line_numbers.pack(side=tk.LEFT, fill=tk.Y)

        # Zone de code
        self.code_editor = scrolledtext.ScrolledText(
            editor_frame,
            fg_color='#1a1a1a',
            text_color=self.colors['fg'],
            font=('Consolas', 10),
            insertbackground=self.colors['primary'],
            wrap=tk.NONE,
            undo=True,
            maxundo=-1
        )
        self.code_editor.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        # Bind pour numéros de lignes
        self.code_editor.bind('<KeyRelease>', self._update_line_numbers)
        self.code_editor.bind('<MouseWheel>', self._update_line_numbers)

        # Console de sortie
        ctk.CTkLabel(
            container,
            text="Console de sortie:",
            fg_color=self.colors['bg'],
            text_color=self.colors['text_secondary'],
            font=('Segoe UI', 9)
        ).pack(anchor='w', pady=(10, 5))

        self.output_console = scrolledtext.ScrolledText(
            container,
            fg_color='#000000',
            text_color='#00ff00',
            font=('Consolas', 9),
            height=8,
            wrap=tk.WORD,
            state='disabled'
        )
        self.output_console.pack(fill=tk.X, pady=(0, 10))

    def _create_templates_tab(self):
        """Onglet templates"""
        container = ctk.CTkFrame(self.templates_tab, fg_color=self.colors['bg'])
        container.pack(fill=tk.BOTH, expand=True, padx=20, pady=20)

        ctk.CTkLabel(
            container,
            text="Sélectionnez un template pour démarrer rapidement",
            fg_color=self.colors['bg'],
            text_color=self.colors['text_secondary'],
            font=('Segoe UI', 10)
        ).pack(pady=10)

        # Liste des templates
        templates_frame = ctk.CTkFrame(container, fg_color=self.colors['bg'])
        templates_frame.pack(fill=tk.BOTH, expand=True)

        templates = ScriptTemplate.get_all_templates()

        row = 0
        col = 0
        for template_id, template in templates.items():
            template_card = self._create_template_card(
                templates_frame,
                template_id,
                template['name'],
                template['description'],
                template['language']
            )
            template_card.grid(row=row, column=col, padx=10, pady=10, sticky='nsew')

            col += 1
            if col > 1:  # 2 colonnes
                col = 0
                row += 1

        # Configurer grid
        templates_frame.grid_columnconfigure(0, weight=1)
        templates_frame.grid_columnconfigure(1, weight=1)

    def _create_template_card(self, parent, template_id, name, description, language):
        """Crée une carte de template"""
        card = ctk.CTkFrame(parent, fg_color=self.colors['secondary'], relief=tk.FLAT)
        card.configure(highlightbackground=self.colors['border'], highlightthickness=1)

        # Header
        ctk.CTkLabel(
            card,
            text=name,
            fg_color=self.colors['secondary'],
            text_color=self.colors['primary'],
            font=('Segoe UI', 11, 'bold')
        ).pack(pady=(15, 5), padx=15)

        # Description
        ctk.CTkLabel(
            card,
            text=description,
            fg_color=self.colors['secondary'],
            text_color=self.colors['text_secondary'],
            font=('Segoe UI', 9),
            wraplength=250
        ).pack(pady=5, padx=15)

        # Badge langage
        language_badge = ctk.CTkLabel(
            card,
            text=language.upper(),
            fg_color=self.colors['primary'],
            text_color='white',
            font=('Segoe UI', 8, 'bold'),
            padx=8,
            pady=2
        )
        language_badge.pack(pady=10)

        # Bouton charger
        ctk.CTkButton(
            card,
            text=" Charger ce template",
            command=lambda: self.load_template(template_id),
            fg_color=self.colors['success'],
            text_color='white',
            font=('Segoe UI', 9, 'bold'),
            bd=0,
            padx=20,
            pady=8,
            cursor='hand2'
        ).pack(pady=(5, 15))

        return card

    def _create_scripts_tab(self):
        """Onglet mes scripts"""
        container = ctk.CTkFrame(self.scripts_tab, fg_color=self.colors['bg'])
        container.pack(fill=tk.BOTH, expand=True, padx=20, pady=20)

        # Header
        header = ctk.CTkFrame(container, fg_color=self.colors['bg'])
        header.pack(fill=tk.X, pady=10)

        ctk.CTkLabel(
            header,
            text="Mes Scripts Sauvegardés",
            fg_color=self.colors['bg'],
            text_color=self.colors['fg'],
            font=('Segoe UI', 12, 'bold')
        ).pack(side=tk.LEFT)

        ctk.CTkButton(
            header,
            text=" Actualiser",
            command=self.refresh_scripts_list,
            fg_color=self.colors['primary'],
            text_color='white',
            font=('Segoe UI', 9),
            bd=0,
            padx=15,
            pady=6,
            cursor='hand2'
        ).pack(side=tk.RIGHT)

        # Liste des scripts
        list_frame = ctk.CTkFrame(container, fg_color=self.colors['bg'])
        list_frame.pack(fill=tk.BOTH, expand=True)

        columns = ('Nom', 'Langage', 'Créé', 'Exécutions')
        self.scripts_tree = ttk.Treeview(list_frame, columns=columns, show='headings', height=15)

        self.scripts_tree.heading('Nom', text='Nom du Script')
        self.scripts_tree.heading('Langage', text='Langage')
        self.scripts_tree.heading('Créé', text='Date de Création')
        self.scripts_tree.heading('Exécutions', text='Exécutions')

        self.scripts_tree.column('Nom', width=250)
        self.scripts_tree.column('Langage', width=100)
        self.scripts_tree.column('Créé', width=150)
        self.scripts_tree.column('Exécutions', width=100)

        scrollbar = ttk.Scrollbar(list_frame, orient=tk.VERTICAL, command=self.scripts_tree.yview)
        self.scripts_tree.configure(yscrollcommand=scrollbar.set)

        self.scripts_tree.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        # Boutons d'action
        actions_frame = ctk.CTkFrame(container, fg_color=self.colors['bg'])
        actions_frame.pack(fill=tk.X, pady=10)

        ctk.CTkButton(
            actions_frame,
            text=" Modifier",
            command=self.edit_selected_script,
            fg_color=self.colors['primary'],
            text_color='white',
            font=('Segoe UI', 9, 'bold'),
            bd=0,
            padx=20,
            pady=8,
            cursor='hand2'
        ).pack(side=tk.LEFT, padx=5)

        ctk.CTkButton(
            actions_frame,
            text=" Exécuter",
            command=self.run_selected_script,
            fg_color=self.colors['success'],
            text_color='white',
            font=('Segoe UI', 9, 'bold'),
            bd=0,
            padx=20,
            pady=8,
            cursor='hand2'
        ).pack(side=tk.LEFT, padx=5)

        ctk.CTkButton(
            actions_frame,
            text=" Supprimer",
            command=self.delete_selected_script,
            fg_color=self.colors['danger'],
            text_color='white',
            font=('Segoe UI', 9, 'bold'),
            bd=0,
            padx=20,
            pady=8,
            cursor='hand2'
        ).pack(side=tk.LEFT, padx=5)

        # Charger les scripts
        self.refresh_scripts_list()

    def _create_scheduler_tab(self):
        """Onglet planificateur"""
        container = ctk.CTkFrame(self.scheduler_tab, fg_color=self.colors['bg'])
        container.pack(fill=tk.BOTH, expand=True, padx=20, pady=20)

        # Header
        header = ctk.CTkFrame(container, fg_color=self.colors['bg'])
        header.pack(fill=tk.X, pady=10)

        ctk.CTkLabel(
            header,
            text="Tâches Planifiées",
            fg_color=self.colors['bg'],
            text_color=self.colors['fg'],
            font=('Segoe UI', 12, 'bold')
        ).pack(side=tk.LEFT)

        ctk.CTkButton(
            header,
            text=" Nouvelle Tâche",
            command=self.add_scheduled_task,
            fg_color=self.colors['success'],
            text_color='white',
            font=('Segoe UI', 9, 'bold'),
            bd=0,
            padx=15,
            pady=6,
            cursor='hand2'
        ).pack(side=tk.RIGHT, padx=5)

        ctk.CTkButton(
            header,
            text=" Actualiser",
            command=self.refresh_tasks_list,
            fg_color=self.colors['primary'],
            text_color='white',
            font=('Segoe UI', 9),
            bd=0,
            padx=15,
            pady=6,
            cursor='hand2'
        ).pack(side=tk.RIGHT)

        # Liste des tâches
        list_frame = ctk.CTkFrame(container, fg_color=self.colors['bg'])
        list_frame.pack(fill=tk.BOTH, expand=True)

        columns = ('Nom', 'Script', 'Planification', 'Prochaine', 'État')
        self.tasks_tree = ttk.Treeview(list_frame, columns=columns, show='headings', height=12)

        self.tasks_tree.heading('Nom', text='Nom de la Tâche')
        self.tasks_tree.heading('Script', text='Script')
        self.tasks_tree.heading('Planification', text='Type')
        self.tasks_tree.heading('Prochaine', text='Prochaine Exécution')
        self.tasks_tree.heading('État', text='État')

        self.tasks_tree.column('Nom', width=200)
        self.tasks_tree.column('Script', width=150)
        self.tasks_tree.column('Planification', width=100)
        self.tasks_tree.column('Prochaine', width=150)
        self.tasks_tree.column('État', width=100)

        scrollbar = ttk.Scrollbar(list_frame, orient=tk.VERTICAL, command=self.tasks_tree.yview)
        self.tasks_tree.configure(yscrollcommand=scrollbar.set)

        self.tasks_tree.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        # Actions
        actions_frame = ctk.CTkFrame(container, fg_color=self.colors['bg'])
        actions_frame.pack(fill=tk.X, pady=10)

        ctk.CTkButton(
            actions_frame,
            text="⏸ Activer/Désactiver",
            command=self.toggle_selected_task,
            fg_color=self.colors['warning'],
            text_color='white',
            font=('Segoe UI', 9, 'bold'),
            bd=0,
            padx=20,
            pady=8,
            cursor='hand2'
        ).pack(side=tk.LEFT, padx=5)

        ctk.CTkButton(
            actions_frame,
            text=" Supprimer",
            command=self.delete_selected_task,
            fg_color=self.colors['danger'],
            text_color='white',
            font=('Segoe UI', 9, 'bold'),
            bd=0,
            padx=20,
            pady=8,
            cursor='hand2'
        ).pack(side=tk.LEFT, padx=5)

        # Charger les tâches
        self.refresh_tasks_list()

    def _update_line_numbers(self, event=None):
        """Met à jour les numéros de lignes"""
        lines = self.code_editor.get('1.0', 'end-1c').count('\n')

        self.line_numbers.configure(state='normal')
        self.line_numbers.delete('1.0', 'end')

        for i in range(1, lines + 2):
            self.line_numbers.insert('end', f"{i}\n")

        self.line_numbers.configure(state='disabled')

    def new_script(self):
        """Crée un nouveau script"""
        self.current_script_id = None
        self.code_editor.delete('1.0', 'end')
        self.script_name_entry.delete(0, 'end')
        self.script_name_entry.insert(0, "Nouveau Script")
        self.language_var.set("powershell")
        self._append_output("Nouveau script créé.\n", 'info')

    def save_script(self):
        """Sauvegarde le script"""
        name = self.script_name_entry.get().strip()
        code = self.code_editor.get('1.0', 'end-1c')
        language = self.language_var.get()

        if not name:
            messagebox.showerror("Erreur", "Veuillez entrer un nom pour le script")
            return

        try:
            if self.current_script_id:
                # Mise à jour
                self.script_manager.update_script(self.current_script_id, code)
                self._append_output(f"Script '{name}' mis à jour.\n", 'success')
            else:
                # Nouveau script
                self.current_script_id = self.script_manager.create_script(name, code, language)
                self._append_output(f"Script '{name}' sauvegardé.\n", 'success')

            self.refresh_scripts_list()

        except Exception as e:
            messagebox.showerror("Erreur", f"Erreur lors de la sauvegarde:\n{e}")

    def execute_current_script(self):
        """Exécute le script en cours d'édition"""
        if not self.current_script_id:
            messagebox.showwarning("Attention", "Veuillez d'abord sauvegarder le script")
            return

        self._append_output("\n" + "="*50 + "\n", 'info')
        self._append_output("Exécution du script...\n", 'info')

        def output_callback(output):
            self._append_output(output, 'output')

        try:
            result = self.script_manager.execute_script(self.current_script_id, output_callback)

            if result['success']:
                self._append_output("\n Script terminé avec succès\n", 'success')
            else:
                self._append_output(f"\n Erreur d'exécution:\n{result.get('stderr', 'Erreur inconnue')}\n", 'error')

        except Exception as e:
            self._append_output(f"\n Erreur: {e}\n", 'error')

    def load_template(self, template_id):
        """Charge un template dans l'éditeur"""
        template = ScriptTemplate.get_template(template_id)

        if template:
            self.current_script_id = None
            self.script_name_entry.delete(0, 'end')
            self.script_name_entry.insert(0, template['name'])
            self.language_var.set(template['language'])
            self.code_editor.delete('1.0', 'end')
            self.code_editor.insert('1.0', template['code'])

            # Passer à l'onglet éditeur
            self.notebook.select(self.editor_tab)

            self._append_output(f"Template '{template['name']}' chargé.\n", 'success')

    def refresh_scripts_list(self):
        """Actualise la liste des scripts"""
        self.scripts_tree.delete(*self.scripts_tree.get_children())

        scripts = self.script_manager.get_all_scripts()

        for script in scripts:
            created = datetime.fromisoformat(script['created']).strftime('%Y-%m-%d %H:%M')

            self.scripts_tree.insert('', 'end', values=(
                script['name'],
                script['language'].upper(),
                created,
                script['runs']
            ), tags=(script['id'],))

    def edit_selected_script(self):
        """Modifie le script sélectionné"""
        selection = self.scripts_tree.selection()

        if not selection:
            messagebox.showwarning("Attention", "Veuillez sélectionner un script")
            return

        script_id = self.scripts_tree.item(selection[0])['tags'][0]
        script = self.script_manager.get_script(script_id)

        self.current_script_id = script_id
        self.script_name_entry.delete(0, 'end')
        self.script_name_entry.insert(0, script['name'])
        self.language_var.set(script['language'])
        self.code_editor.delete('1.0', 'end')
        self.code_editor.insert('1.0', script['code'])

        # Passer à l'onglet éditeur
        self.notebook.select(self.editor_tab)

    def run_selected_script(self):
        """Exécute le script sélectionné"""
        selection = self.scripts_tree.selection()

        if not selection:
            messagebox.showwarning("Attention", "Veuillez sélectionner un script")
            return

        script_id = self.scripts_tree.item(selection[0])['tags'][0]
        self.current_script_id = script_id

        # Passer à l'onglet éditeur et exécuter
        self.notebook.select(self.editor_tab)
        self.execute_current_script()

    def delete_selected_script(self):
        """Supprime le script sélectionné"""
        selection = self.scripts_tree.selection()

        if not selection:
            messagebox.showwarning("Attention", "Veuillez sélectionner un script")
            return

        script_id = self.scripts_tree.item(selection[0])['tags'][0]

        if messagebox.askyesno("Confirmation", "Voulez-vous vraiment supprimer ce script ?"):
            try:
                self.script_manager.delete_script(script_id)
                self.refresh_scripts_list()
                self._append_output("Script supprimé.\n", 'info')
            except Exception as e:
                messagebox.showerror("Erreur", f"Erreur lors de la suppression:\n{e}")

    def add_scheduled_task(self):
        """Ajoute une nouvelle tâche planifiée"""
        # Créer une fenêtre de dialogue
        dialog = tk.Toplevel(self.parent)
        dialog.title("Nouvelle Tâche Planifiée")
        dialog.geometry("400x300")
        dialog.configure(fg_color=self.colors['bg'])

        # TODO: Implémenter formulaire complet
        messagebox.showinfo("Info", "Fonctionnalité de planification en cours d'implémentation")
        dialog.destroy()

    def refresh_tasks_list(self):
        """Actualise la liste des tâches"""
        self.tasks_tree.delete(*self.tasks_tree.get_children())

        tasks = self.task_scheduler.get_all_tasks()

        for task in tasks:
            state = " Activée" if task['enabled'] else "⏸ Désactivée"

            self.tasks_tree.insert('', 'end', values=(
                task['name'],
                task.get('script_id', 'N/A'),
                task['schedule_type'],
                task.get('next_run', 'N/A'),
                state
            ), tags=(task['id'],))

    def toggle_selected_task(self):
        """Active/désactive la tâche sélectionnée"""
        selection = self.tasks_tree.selection()

        if not selection:
            messagebox.showwarning("Attention", "Veuillez sélectionner une tâche")
            return

        task_id = self.tasks_tree.item(selection[0])['tags'][0]
        self.task_scheduler.toggle_task(task_id)
        self.refresh_tasks_list()

    def delete_selected_task(self):
        """Supprime la tâche sélectionnée"""
        selection = self.tasks_tree.selection()

        if not selection:
            messagebox.showwarning("Attention", "Veuillez sélectionner une tâche")
            return

        task_id = self.tasks_tree.item(selection[0])['tags'][0]

        if messagebox.askyesno("Confirmation", "Voulez-vous vraiment supprimer cette tâche ?"):
            self.task_scheduler.delete_task(task_id)
            self.refresh_tasks_list()

    def _append_output(self, text, tag='normal'):
        """Ajoute du texte à la console de sortie"""
        self.output_console.configure(state='normal')
        self.output_console.insert('end', text)

        # Auto-scroll
        self.output_console.see('end')
        self.output_console.configure(state='disabled')


# Test autonome
if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)

    root = tk.Tk()
    root.title("Test Script Automation")
    root.geometry("1200x800")
    root.configure(fg_color='#0a0a0a')

    gui = ScriptAutomationGUI(root)

    root.mainloop()
