#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Application Principale - NiTriTe V18
Point d'entrée principal avec architecture moderne
"""


import sys
import os
# Ajoute le dossier src/ au sys.path si nécessaire (PyInstaller)
if getattr(sys, 'frozen', False):
    # Exécution dans l'exécutable PyInstaller
    base_path = sys._MEIPASS
    src_path = os.path.join(base_path, 'src')
    if src_path not in sys.path:
        sys.path.insert(0, src_path)
else:
    # Exécution normale (dev)
    src_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
    if src_path not in sys.path:
        sys.path.insert(0, src_path)


import customtkinter as ctk
import tkinter as tk
import json
import os
import sys
from pathlib import Path

# --- Correction import dynamique du package v14_mvp ---
try:
    from v14_mvp import design_system
except ModuleNotFoundError:
    # Ajoute src/ au sys.path si le package n'est pas trouvable
    current_dir = os.path.abspath(os.path.dirname(__file__))
    src_dir = os.path.abspath(os.path.join(current_dir, '..'))
    if src_dir not in sys.path:
        sys.path.insert(0, src_dir)

def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(os.path.dirname(__file__))
    return os.path.abspath(os.path.join(base_path, relative_path))

from v14_mvp.design_system import DesignTokens, ModernColors, ThemePalettes
from v14_mvp.navigation import ModernNavigation
from v14_mvp.pages_simple import SimplePlaceholderPage
from v14_mvp.pages_optimized import OptimizedApplicationsPage, OptimizedToolsPage
from v14_mvp.pages_settings import SettingsPage
from v14_mvp.pages_full import UpdatesPage, BackupPage, DiagnosticPage, OptimizationsPage
from v14_mvp.page_master_install import MasterInstallPage
from v14_mvp.page_portables import PortableAppsPage
from v14_mvp.page_os_downloads import OSDownloadsPage
from v14_mvp.page_terminal import TerminalPage
from v14_mvp.page_theme_settings import ThemeSettingsPage
from v14_mvp.page_ai_agents import AIAgentsPage
from v14_mvp.page_logs import LogsPage
from v14_mvp.page_scripts_windows import WindowsScriptsPage
from v14_mvp.splash_loader import SplashScreen

# Charger le thème sauvegardé au démarrage
current_theme = ThemePalettes.get_current_theme()
ThemePalettes.apply_theme(current_theme)
print(f"🎨 Thème chargé: {current_theme}")


class NiTriTeV18(ctk.CTk):
    """Application principale NiTriTe V18"""

    def __init__(self):
        super().__init__()

        # Configuration base
        self.title("NiTriTe V18.0 - Maintenance Informatique Professionnelle")
        self.geometry("1400x800")
        self.minsize(1200, 700)
        
        # Maximiser la fenêtre au démarrage
        try:
            self.state('zoomed')  # Windows
        except:
            pass  # Ignorer si erreur
        
        # Thème - Charger le mode d'apparence sauvegardé
        try:
            import os
            import json
            config_path = os.path.join(os.path.expanduser("~"), ".nitrite_config.json")
            if os.path.exists(config_path):
                with open(config_path, 'r', encoding='utf-8') as f:
                    config = json.load(f)
                    appearance_mode = config.get("appearance_mode", "dark")
                    ctk.set_appearance_mode(appearance_mode)
                    print(f"🎨 Mode d'apparence chargé: {appearance_mode}")
            else:
                ctk.set_appearance_mode("dark")
        except:
            ctk.set_appearance_mode("dark")

        ctk.set_default_color_theme("blue")
        
        # Charger données directement (sans splash temporairement)
        print("🔄 Chargement des données...")
        self.programs_data = self._load_programs()
        self.tools_data = self._load_tools()
        self.config_data = {}
        self.current_page_widget = None
        
        print(f"✅ {len(self.programs_data)} catégories chargées")
        print(f"✅ {sum(len(apps) for apps in self.programs_data.values())} applications")
        
        # Créer UI
        self._create_main_layout()

        # Charger page par défaut
        self._show_page("applications")

        # Intercepter la fermeture de l'application
        self.protocol("WM_DELETE_WINDOW", self._on_closing)
    
    def _load_programs(self):
        """Charger données programmes (compatible PyInstaller et bureau)"""
        try:
            # Cherche toujours à la racine du projet (data/programs.json)
            programs_path = resource_path(os.path.join('data', 'programs.json'))
            if not os.path.exists(programs_path):
                # Fallback chemin absolu depuis cwd
                programs_path = os.path.abspath(os.path.join(os.getcwd(), 'data', 'programs.json'))
            if os.path.exists(programs_path):
                with open(programs_path, 'r', encoding='utf-8') as f:
                    return json.load(f)
            else:
                print(f"⚠️ Fichier non trouvé: {programs_path}")
                return {}
        except Exception as e:
            print(f"❌ Erreur chargement programmes: {e}")
            import traceback
            traceback.print_exc()
            return {}
    
    def _load_tools(self):
        """Charger données outils (compatible PyInstaller et bureau)"""
        try:
            import importlib.util
            # Cherche toujours src/tools_data_complete.py à la racine du projet
            module_path = resource_path(os.path.join('src', 'tools_data_complete.py'))
            if not os.path.exists(module_path):
                # Fallback chemin absolu depuis cwd
                module_path = os.path.abspath(os.path.join(os.getcwd(), 'src', 'tools_data_complete.py'))
            if not os.path.exists(module_path):
                # Essai chemin alternatif (PyInstaller peut extraire à la racine)
                module_path = resource_path('tools_data_complete.py')
            spec = importlib.util.spec_from_file_location(
                "tools_data_complete",
                module_path
            )
            if spec and spec.loader:
                tools_module = importlib.util.module_from_spec(spec)
                spec.loader.exec_module(tools_module)
                return tools_module.get_all_tools()
            else:
                print("⚠️ Module tools_data_complete introuvable")
                return {}
        except Exception as e:
            print(f"⚠️ Erreur chargement tools: {e}")
            import traceback
            traceback.print_exc()
            return {}
    
    def _create_main_layout(self):
        """Créer layout principal"""
        # Container principal
        main_container = ctk.CTkFrame(self, fg_color=DesignTokens.BG_PRIMARY)
        main_container.pack(fill=tk.BOTH, expand=True)
        
        # Navigation
        self.navigation = ModernNavigation(
            main_container,
            on_page_change=self._show_page
        )
        self.navigation.pack(side=tk.LEFT, fill=tk.Y)
        
        # Container contenu
        self.content_container = ctk.CTkFrame(
            main_container,
            fg_color=DesignTokens.BG_PRIMARY
        )
        self.content_container.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
    
    def _show_page(self, page_id):
        """Afficher une page"""
        # Nettoyer page actuelle
        if self.current_page_widget:
            self.current_page_widget.pack_forget()
            self.current_page_widget.destroy()
        
        # Créer nouvelle page
        if page_id == "applications":
            self.current_page_widget = OptimizedApplicationsPage(
                self.content_container,
                self.programs_data
            )
        
        elif page_id == "tools":
            self.current_page_widget = OptimizedToolsPage(
                self.content_container,
                self.tools_data
            )
        
        elif page_id == "master_install":
            self.current_page_widget = MasterInstallPage(
                self.content_container,
                self.programs_data
            )
        
        elif page_id == "portables":
            self.current_page_widget = PortableAppsPage(
                self.content_container
            )

        elif page_id == "os_downloads":
            self.current_page_widget = OSDownloadsPage(
                self.content_container
            )

        elif page_id == "terminal":
            self.current_page_widget = TerminalPage(
                self.content_container
            )
        
        elif page_id == "updates":
            self.current_page_widget = UpdatesPage(
                self.content_container
            )
        
        elif page_id == "backup":
            self.current_page_widget = BackupPage(
                self.content_container
            )
        
        elif page_id == "optimizations":
            self.current_page_widget = OptimizationsPage(
                self.content_container
            )
        
        elif page_id == "diagnostic":
            self.current_page_widget = DiagnosticPage(
                self.content_container
            )

        elif page_id == "logs":
            self.current_page_widget = LogsPage(
                self.content_container
            )

        elif page_id == "ai_agents":
            self.current_page_widget = AIAgentsPage(
                self.content_container
            )

        elif page_id == "scripts":
            self.current_page_widget = WindowsScriptsPage(
                self.content_container
            )

        elif page_id == "settings":
            self.current_page_widget = SettingsPage(
                self.content_container
            )

        # Afficher nouvelle page
        if self.current_page_widget:
            self.current_page_widget.pack(fill=tk.BOTH, expand=True)

    def _on_closing(self):
        """Gérer la fermeture de l'application avec dialogue de nettoyage"""
        from tkinter import messagebox
        import shutil

        # Demander confirmation pour nettoyer les données
        response = messagebox.askyesnocancel(
            "Fermeture de NiTriTe",
            "Voulez-vous supprimer toutes les données et dépendances NiTriTe de cet ordinateur?\n\n"
            "✅ OUI: Supprimer tous les dossiers NiTriTe (Bureau, Documents, Config)\n"
            "❌ NON: Fermer sans supprimer\n"
            "⏹️ ANNULER: Ne pas fermer l'application",
            icon='question'
        )

        if response is None:  # Annuler
            return  # Ne rien faire, ne pas fermer

        elif response:  # OUI - Nettoyer
            try:
                from pathlib import Path
                folders_to_clean = []

                # Dossier Bureau
                desktop_nitrite = Path.home() / "Desktop" / "NiTriTe_Portables"
                if desktop_nitrite.exists():
                    folders_to_clean.append(str(desktop_nitrite))

                # Dossier Documents (ancien emplacement)
                docs_nitrite = Path.home() / "Documents" / "NiTriTe_Portables"
                if docs_nitrite.exists():
                    folders_to_clean.append(str(docs_nitrite))

                # Fichier de configuration
                config_file = Path.home() / ".nitrite_config.json"
                if config_file.exists():
                    folders_to_clean.append(str(config_file))

                # Dossier logiciel local (si existe)
                try:
                    from v14_mvp.pages_full import get_local_software_folder
                    software_dir = Path(get_local_software_folder())
                    if software_dir.exists():
                        folders_to_clean.append(str(software_dir))
                except:
                    pass

                if folders_to_clean:
                    messagebox.showinfo(
                        "Nettoyage en cours",
                        f"Suppression de {len(folders_to_clean)} élément(s):\n\n" +
                        "\n".join(f"• {f}" for f in folders_to_clean[:5]) +
                        (f"\n... et {len(folders_to_clean)-5} autre(s)" if len(folders_to_clean) > 5 else "")
                    )

                    # Supprimer les dossiers
                    deleted_count = 0
                    for folder_path in folders_to_clean:
                        try:
                            path = Path(folder_path)
                            if path.is_file():
                                path.unlink()
                                deleted_count += 1
                            elif path.is_dir():
                                shutil.rmtree(folder_path, ignore_errors=True)
                                deleted_count += 1
                        except Exception as e:
                            print(f"Erreur suppression {folder_path}: {e}")

                    messagebox.showinfo(
                        "Nettoyage terminé",
                        f"✅ {deleted_count} élément(s) supprimé(s)\n\n"
                        "NiTriTe va maintenant se fermer."
                    )
                else:
                    messagebox.showinfo(
                        "Aucune donnée",
                        "Aucune donnée NiTriTe trouvée à supprimer."
                    )

            except Exception as e:
                messagebox.showerror(
                    "Erreur de nettoyage",
                    f"Une erreur est survenue lors du nettoyage:\n\n{str(e)}"
                )

        # Fermer l'application (que l'utilisateur ait choisi OUI ou NON)
        self.destroy()


def main():
    """Point d'entrée"""
    try:
        # Configurer encodage UTF-8 pour Windows (seulement si console disponible)
        if sys.platform == 'win32':
            try:
                import io
                # Vérifier que stdout/stderr existent et ont un buffer (mode console)
                if sys.stdout is not None and hasattr(sys.stdout, 'buffer'):
                    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')
                if sys.stderr is not None and hasattr(sys.stderr, 'buffer'):
                    sys.stderr = io.TextIOWrapper(sys.stderr.buffer, encoding='utf-8', errors='replace')
            except Exception:
                # Ignorer les erreurs d'encodage (mode GUI sans console)
                pass

        # Vérifier Python 3.8-3.12
        py_version = sys.version_info
        if py_version.major != 3 or py_version.minor < 8 or py_version.minor > 12:
            # En mode GUI, afficher erreur dans une fenêtre tkinter
            try:
                import tkinter as tk
                from tkinter import messagebox
                root = tk.Tk()
                root.withdraw()
                messagebox.showerror(
                    "Erreur Python",
                    f"Python {py_version.major}.{py_version.minor} détecté\n\n"
                    f"CustomTkinter requiert Python 3.8-3.12\n\n"
                    f"Téléchargez Python 3.12:\n"
                    f"https://www.python.org/downloads/"
                )
                root.destroy()
            except:
                pass
            return

        # Messages de debug (seulement si console disponible)
        if sys.stdout is not None:
            print(f"[OK] Python {py_version.major}.{py_version.minor}.{py_version.micro}")
            print("[>>] Lancement NiTriTe V18...")
            print(f"[..] Répertoire: {os.getcwd()}")
            print()
            print("[..] Création de l'instance NiTriTeV18...")

        # Lancer app
        app = NiTriTeV18()

        if sys.stdout is not None:
            print("[OK] Instance créée")
            print("[>>] Démarrage mainloop...")

        app.mainloop()

        if sys.stdout is not None:
            print("[OK] Application fermée normalement")

    except KeyboardInterrupt:
        if sys.stdout is not None:
            print("\n[!] Interruption utilisateur (Ctrl+C)")

    except Exception as e:
        # Afficher erreur dans une boîte de dialogue si possible
        try:
            import tkinter as tk
            from tkinter import messagebox
            import traceback

            error_msg = f"Type: {type(e).__name__}\n"
            error_msg += f"Message: {e}\n\n"
            error_msg += "Traceback:\n"
            error_msg += traceback.format_exc()

            root = tk.Tk()
            root.withdraw()
            messagebox.showerror("Erreur Critique - NiTriTe V18", error_msg)
            root.destroy()
        except:
            # Si impossible d'afficher GUI, essayer console
            if sys.stdout is not None:
                print(f"\n{'='*60}")
                print(f"[X] ERREUR CRITIQUE")
                print(f"{'='*60}")
                print(f"Type: {type(e).__name__}")
                print(f"Message: {e}")
                print(f"\n[i] Traceback complet:")
                print(f"{'-'*60}")
                import traceback
                traceback.print_exc()
                print(f"{'-'*60}")


if __name__ == "__main__":
    main()