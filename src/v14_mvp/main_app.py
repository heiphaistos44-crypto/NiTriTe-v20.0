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

# Import du système de chemins portables
try:
    from portable_paths import get_portable_config_dir, get_portable_temp_dir
except ImportError:
    # Fallback si portable_paths non disponible
    def get_portable_config_dir():
        return Path.home() / ".nitrite"
    def get_portable_temp_dir(subfolder=None):
        import tempfile
        if subfolder:
            return Path(tempfile.gettempdir()) / "nitrite_temp" / subfolder
        return Path(tempfile.gettempdir()) / "nitrite_temp"

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
from v14_mvp.navigation_colored import ModernNavigationColored
from v14_mvp.pages_simple import SimplePlaceholderPage
from v14_mvp.pages_optimized import OptimizedApplicationsPage, OptimizedToolsPage
from v14_mvp.pages_settings import SettingsPage
from v14_mvp.pages_full import UpdatesPage, BackupPage, DiagnosticPage, OptimizationsPage
from v14_mvp.page_drivers import DriversPage
from v14_mvp.page_scanvirus import ScanVirusPage
from v14_mvp.page_master_install import MasterInstallPage
from v14_mvp.page_portables import PortableAppsPage
from v14_mvp.page_os_downloads import OSDownloadsPage
from v14_mvp.page_system_utils import SystemUtilitiesPage
from v14_mvp.page_documentation import DocumentationPage
from v14_mvp.page_terminal import TerminalPage
from v14_mvp.page_theme_settings import ThemeSettingsPage
from v14_mvp.page_ai_agents import AIAgentsPage
from v14_mvp.page_activation import ActivationPage
from v14_mvp.page_logs import LogsPage
from v14_mvp.page_scripts_windows import WindowsScriptsPage
from v14_mvp.splash_loader import SplashScreen

# Charger le thème sauvegardé au démarrage
current_theme = ThemePalettes.get_current_theme()
ThemePalettes.apply_theme(current_theme)
print(f" Thème chargé: {current_theme}")


class NiTriTeV18(ctk.CTk):
    """Application principale NiTriTe V18"""

    def __init__(self):
        super().__init__()

        # Configuration base
        self.title("NiTriTe V20.0 - Maintenance Informatique Professionnelle")
        self.geometry("1400x800")
        self.minsize(1200, 700)

        # Icône de la fenêtre
        try:
            import sys
            if getattr(sys, 'frozen', False):
                # Mode PyInstaller
                icon_path = Path(sys.executable).parent / 'assets' / 'Nitrite_icon1.ico'
            else:
                # Mode développement
                icon_path = Path(__file__).parent.parent.parent / 'assets' / 'Nitrite_icon1.ico'

            if icon_path.exists():
                self.iconbitmap(str(icon_path))
        except Exception as e:
            print(f"Impossible de charger l'icône de fenêtre: {e}")

        # Maximiser la fenêtre au démarrage
        try:
            self.state('zoomed')  # Windows
        except:
            pass  # Ignorer si erreur
        
        # Thème - Charger le mode d'apparence sauvegardé (MODE PORTABLE)
        try:
            import os
            import json
            config_dir = get_portable_config_dir()
            config_path = config_dir / "nitrite_config.json"

            # Migration: chercher ancien config dans home et le copier
            old_config_path = Path.home() / ".nitrite_config.json"
            if old_config_path.exists() and not config_path.exists():
                import shutil
                shutil.copy2(old_config_path, config_path)
                print(f" Config migrée: {old_config_path} → {config_path}")

            if config_path.exists():
                with open(config_path, 'r', encoding='utf-8') as f:
                    config = json.load(f)
                    appearance_mode = config.get("appearance_mode", "dark")
                    ctk.set_appearance_mode(appearance_mode)
                    print(f" Mode d'apparence chargé (portable): {appearance_mode}")
            else:
                ctk.set_appearance_mode("dark")
        except Exception as e:
            print(f" Erreur chargement config: {e}")
            ctk.set_appearance_mode("dark")

        ctk.set_default_color_theme("blue")
        
        # Charger données directement (sans splash temporairement)
        print(" Chargement des données...")
        self.programs_data = self._load_programs()
        self.tools_data = self._load_tools()
        self.config_data = {}
        self.current_page_widget = None
        
        print(f" {len(self.programs_data)} catégories chargées")
        print(f" {sum(len(apps) for apps in self.programs_data.values())} applications")
        
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
                print(f" Fichier non trouvé: {programs_path}")
                return {}
        except Exception as e:
            print(f" Erreur chargement programmes: {e}")
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
                print(" Module tools_data_complete introuvable")
                return {}
        except Exception as e:
            print(f" Erreur chargement tools: {e}")
            import traceback
            traceback.print_exc()
            return {}
    
    def _create_main_layout(self):
        """Créer layout principal"""
        # Container principal
        main_container = ctk.CTkFrame(self, fg_color=DesignTokens.BG_PRIMARY)
        main_container.pack(fill=tk.BOTH, expand=True)
        
        # Navigation avec icônes colorées
        self.navigation = ModernNavigationColored(
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

        elif page_id == "drivers":
            self.current_page_widget = DriversPage(
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

        elif page_id == "scanvirus":
            self.current_page_widget = ScanVirusPage(
                self.content_container
            )

        elif page_id == "activation":
            self.current_page_widget = ActivationPage(
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

        elif page_id == "system_utils":
            self.current_page_widget = SystemUtilitiesPage(
                self.content_container
            )

        elif page_id == "documentation":
            self.current_page_widget = DocumentationPage(
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
        """Gérer la fermeture de l'application avec nettoyage complet"""
        from tkinter import messagebox
        import shutil
        import tempfile

        # Demander confirmation
        response = messagebox.askyesnocancel(
            "Fermeture de NiTriTe",
            "Voulez-vous supprimer toutes les données et fichiers temporaires NiTriTe de cet ordinateur?\n\n"
            "✓ OUI: Supprimer tous les dossiers et fichiers temporaires NiTriTe\n"
            "✗ NON: Fermer sans supprimer\n"
            "⏹ ANNULER: Ne pas fermer l'application",
            icon='question'
        )

        if response is None:  # Annuler
            return

        elif response:  # OUI - Nettoyer
            try:
                from pathlib import Path
                folders_to_clean = []

                # MODE PORTABLE: Tout est dans le dossier app, on nettoie juste temp/

                # 1. Dossier temp/ portable
                try:
                    temp_portable = get_portable_temp_dir()
                    if temp_portable and temp_portable.exists():
                        folders_to_clean.append(str(temp_portable))
                except:
                    pass

                # 2. Cache Python
                try:
                    project_root = Path(__file__).parent.parent.parent
                    pycache_dirs = [
                        project_root / "src" / "__pycache__",
                        project_root / "src" / "v14_mvp" / "__pycache__"
                    ]
                    for pycache in pycache_dirs:
                        if pycache.exists():
                            folders_to_clean.append(str(pycache))
                except:
                    pass

                # 3. Anciens fichiers dans home (migration cleanup)
                old_config_file = Path.home() / ".nitrite_config.json"
                if old_config_file.exists():
                    folders_to_clean.append(str(old_config_file))

                old_theme_file = Path.home() / ".nitrite_theme.json"
                if old_theme_file.exists():
                    folders_to_clean.append(str(old_theme_file))

                old_nitrite_folder = Path.home() / ".nitrite"
                if old_nitrite_folder.exists():
                    folders_to_clean.append(str(old_nitrite_folder))

                # 4. Anciens dossiers temp système (fallback ancien code)
                system_temp = Path(tempfile.gettempdir())
                old_temp_downloads = system_temp / "NiTriTe_Downloads"
                if old_temp_downloads.exists():
                    folders_to_clean.append(str(old_temp_downloads))

                # Fichiers PowerShell temporaires anciens
                ps1_files = list(system_temp.glob("tmp*.ps1"))
                for ps1_file in ps1_files[:10]:  # Limiter à 10 pour éviter suppression excessive
                    folders_to_clean.append(str(ps1_file))

                # Note: Les logs, configs sont DANS le dossier app maintenant (mode portable)
                # Note: logiciel/ est CONSERVÉ (nécessaire pour l'application)
                # Note: Script Windows/ est CONSERVÉ

                if folders_to_clean:
                    # Afficher ce qui sera supprimé
                    messagebox.showinfo(
                        "Nettoyage en cours",
                        f"Suppression de {len(folders_to_clean)} élément(s):\n\n" +
                        "\n".join(f"• {Path(f).name}" for f in folders_to_clean[:8]) +
                        (f"\n... et {len(folders_to_clean)-8} autre(s)" if len(folders_to_clean) > 8 else "")
                    )

                    # Supprimer
                    deleted_count = 0
                    errors = []

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
                            errors.append(f"{Path(folder_path).name}: {str(e)}")
                            print(f"Erreur suppression {folder_path}: {e}")

                    # Message final
                    if errors:
                        messagebox.showwarning(
                            "Nettoyage terminé avec erreurs",
                            f"✓ {deleted_count} élément(s) supprimé(s)\n"
                            f"⚠ {len(errors)} erreur(s)\n\n"
                            f"Erreurs:\n" + "\n".join(errors[:3])
                        )
                    else:
                        messagebox.showinfo(
                            "Nettoyage terminé",
                            f"✓ {deleted_count} élément(s) supprimé(s)\n\n"
                            "NiTriTe va maintenant se fermer.\n"
                            "Seuls .exe, logiciel/, data/ et Script Windows/ ont été conservés."
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

        # Tuer le processus NiTriTe de manière forcée (demande utilisateur)
        try:
            import os
            import sys
            import psutil

            # Méthode 1: Tuer le processus actuel
            current_pid = os.getpid()
            parent = psutil.Process(current_pid)

            # Tuer tous les processus enfants d'abord
            for child in parent.children(recursive=True):
                try:
                    child.kill()
                except:
                    pass

            # Puis tuer le processus principal
            parent.kill()

        except ImportError:
            # Fallback si psutil n'est pas installé
            try:
                import os
                import signal
                pid = os.getpid()
                os.kill(pid, signal.SIGTERM)
            except:
                # Dernier recours: fermeture normale
                self.destroy()
                sys.exit(0)


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

        # Initialiser les archives compressées (extraction automatique si nécessaire)
        try:
            from v14_mvp.archive_manager import initialize_archives
            if sys.stdout is not None:
                print("[..] Vérification des archives compressées...")
            initialize_archives(show_progress=(sys.stdout is not None))
            if sys.stdout is not None:
                print("[OK] Archives vérifiées")
        except Exception as e:
            if sys.stdout is not None:
                print(f"[!] Avertissement: Erreur lors de l'initialisation des archives: {e}")
            # Continuer même en cas d'erreur (les archives sont optionnelles)

        if sys.stdout is not None:
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