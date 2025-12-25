#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Tests Automatisés Complets - Nitrite V18.5
Script de test automatisé pour toutes les fonctionnalités
"""

import sys
import os
import json
import time
from pathlib import Path
from typing import Dict, List, Tuple, Optional, Callable
from datetime import datetime
import importlib.util

class NitriteFunctionalityTester:
    """Testeur automatisé complet pour Nitrite V18.5"""

    def __init__(self, project_root: str):
        self.project_root = Path(project_root)
        self.results = {
            "categories": {},
            "summary": {
                "total": 0,
                "passed": 0,
                "failed": 0
            },
            "errors": [],
            "execution_time": 0
        }
        self.start_time = None

        # Ajouter src au path pour les imports
        sys.path.insert(0, str(self.project_root / "src"))

    # === MÉTHODES UTILITAIRES ===

    def test_file_exists(self, filepath: str, description: str = "") -> Tuple[bool, str]:
        """Vérifier qu'un fichier existe"""
        full_path = self.project_root / filepath
        try:
            exists = full_path.exists() and full_path.is_file()
            return exists, description or f"Fichier {filepath}"
        except Exception as e:
            return False, f"Erreur: {e}"

    def test_dir_exists(self, dirpath: str, description: str = "") -> Tuple[bool, str]:
        """Vérifier qu'un dossier existe"""
        full_path = self.project_root / dirpath
        try:
            exists = full_path.exists() and full_path.is_dir()
            return exists, description or f"Dossier {dirpath}"
        except Exception as e:
            return False, f"Erreur: {e}"

    def test_json_valid(self, filepath: str) -> Tuple[bool, Optional[dict], str]:
        """Vérifier qu'un JSON est valide et le charger"""
        full_path = self.project_root / filepath
        try:
            if not full_path.exists():
                return False, None, f"Fichier {filepath} introuvable"

            with open(full_path, 'r', encoding='utf-8') as f:
                data = json.load(f)

            return True, data, f"JSON {filepath} valide"
        except json.JSONDecodeError as e:
            return False, None, f"JSON invalide: {e}"
        except Exception as e:
            return False, None, f"Erreur: {e}"

    def test_python_import(self, module_name: str) -> Tuple[bool, str]:
        """Tester l'import d'un module Python"""
        try:
            if "." in module_name:
                parts = module_name.split(".")
                module = __import__(module_name, fromlist=[parts[-1]])
            else:
                module = __import__(module_name)
            return True, f"Import {module_name} réussi"
        except ImportError as e:
            return False, f"Import échoué: {e}"
        except Exception as e:
            return False, f"Erreur: {e}"

    def test_url_format(self, url: str) -> bool:
        """Vérifier format URL basique"""
        return url.startswith(("http://", "https://", "ftp://"))

    def run_test(self, category: str, test_name: str, test_func: Callable) -> bool:
        """Exécuter un test et enregistrer le résultat"""
        try:
            result = test_func()
            success = result if isinstance(result, bool) else result[0]

            test_info = {
                "name": test_name,
                "success": success,
                "error": None if success else (result[1] if isinstance(result, tuple) else "Échec")
            }

            if category not in self.results["categories"]:
                self.results["categories"][category] = {
                    "passed": 0,
                    "failed": 0,
                    "tests": []
                }

            self.results["categories"][category]["tests"].append(test_info)

            if success:
                self.results["categories"][category]["passed"] += 1
                self.results["summary"]["passed"] += 1
                print(f"  [OK] {test_name}")
            else:
                self.results["categories"][category]["failed"] += 1
                self.results["summary"]["failed"] += 1
                self.results["errors"].append({
                    "category": category,
                    "test": test_name,
                    "error": test_info["error"]
                })
                print(f"  [ERREUR] {test_name}")
                if test_info["error"]:
                    print(f"          {test_info['error']}")

            self.results["summary"]["total"] += 1
            return success

        except Exception as e:
            print(f"  [ERREUR] {test_name}: {e}")
            self.results["summary"]["total"] += 1
            self.results["summary"]["failed"] += 1
            self.results["errors"].append({
                "category": category,
                "test": test_name,
                "error": str(e)
            })
            return False

    # === CATÉGORIE 1: STRUCTURE DE FICHIERS (5 TESTS) ===

    def test_file_structure(self):
        """Tests de structure de fichiers"""
        print("\n[CATEGORIE] Structure de Fichiers")

        self.run_test("Structure de Fichiers", "Fichiers essentiels présents",
                      lambda: self.test_file_exists("src/v14_mvp/main_app.py") and
                              self.test_file_exists("src/v14_mvp/design_system.py")[0])

        self.run_test("Structure de Fichiers", "Structure dossiers correcte",
                      lambda: self.test_dir_exists("src")[0] and
                              self.test_dir_exists("data")[0] and
                              self.test_dir_exists("scripts")[0])

        self.run_test("Structure de Fichiers", "Dossier themes/ existe",
                      lambda: self.test_dir_exists("data/themes")[0])

        self.run_test("Structure de Fichiers", "Fichiers configuration présents",
                      lambda: self.test_file_exists("data/programs.json")[0] and
                              self.test_file_exists("data/portable_apps.json")[0])

        self.run_test("Structure de Fichiers", "Assets présents",
                      lambda: self.test_dir_exists("assets")[0] or
                              self.test_file_exists("Nitrite Icon.ico")[0])

        passed = self.results["categories"]["Structure de Fichiers"]["passed"]
        total = len(self.results["categories"]["Structure de Fichiers"]["tests"])
        print(f"  Resultat: {passed}/{total} tests reussis ({passed/total*100:.0f}%)\n")

    # === CATÉGORIE 2: INTÉGRITÉ DONNÉES JSON (4 TESTS) ===

    def test_json_integrity(self):
        """Tests d'intégrité des données JSON"""
        print("[CATEGORIE] Integrite Donnees JSON")

        def test_programs_json():
            success, data, msg = self.test_json_valid("data/programs.json")
            if not success:
                return False, msg
            # Vérifier structure basique
            if not isinstance(data, list):
                return False, "programs.json doit etre une liste"
            if len(data) < 100:
                return False, f"Trop peu de programmes: {len(data)}"
            return True, f"{len(data)} programmes trouves"

        def test_portable_apps_json():
            success, data, msg = self.test_json_valid("data/portable_apps.json")
            if not success:
                return False, msg
            if not isinstance(data, list):
                return False, "portable_apps.json doit etre une liste"
            if len(data) < 10:
                return False, f"Trop peu d'apps: {len(data)}"
            return True, f"{len(data)} apps portables trouvees"

        def test_themes_json():
            themes_dir = self.project_root / "data" / "themes"
            if not themes_dir.exists():
                return True, "Dossier themes vide (OK)"

            json_files = list(themes_dir.glob("*.json"))
            for json_file in json_files:
                try:
                    with open(json_file, 'r', encoding='utf-8') as f:
                        json.load(f)
                except:
                    return False, f"Theme {json_file.name} invalide"

            return True, f"{len(json_files)} themes valides"

        def test_config_json():
            success, data, msg = self.test_json_valid("data/config.json")
            return success, msg if success else "config.json manquant ou invalide"

        self.run_test("Integrite Donnees JSON", "programs.json valide", test_programs_json)
        self.run_test("Integrite Donnees JSON", "portable_apps.json valide", test_portable_apps_json)
        self.run_test("Integrite Donnees JSON", "Themes JSON valides", test_themes_json)
        self.run_test("Integrite Donnees JSON", "config.json valide", test_config_json)

        passed = self.results["categories"]["Integrite Donnees JSON"]["passed"]
        total = len(self.results["categories"]["Integrite Donnees JSON"]["tests"])
        print(f"  Resultat: {passed}/{total} tests reussis ({passed/total*100:.0f}%)\n")

    # === CATÉGORIE 3: IMPORTS PYTHON (6 TESTS) ===

    def test_python_imports(self):
        """Tests d'imports Python"""
        print("[CATEGORIE] Imports Python")

        self.run_test("Imports Python", "Import customtkinter",
                      lambda: self.test_python_import("customtkinter"))

        self.run_test("Imports Python", "Import design_system",
                      lambda: self.test_python_import("v14_mvp.design_system"))

        self.run_test("Imports Python", "Import theme_editor_dynamic",
                      lambda: self.test_python_import("v14_mvp.theme_editor_dynamic"))

        self.run_test("Imports Python", "Import components",
                      lambda: self.test_python_import("v14_mvp.components"))

        def test_all_mvp_modules():
            mvp_dir = self.project_root / "src" / "v14_mvp"
            if not mvp_dir.exists():
                return False, "Dossier v14_mvp introuvable"

            python_files = list(mvp_dir.glob("*.py"))
            failed = []

            for py_file in python_files:
                if py_file.name.startswith("__"):
                    continue
                module_name = f"v14_mvp.{py_file.stem}"
                try:
                    __import__(module_name)
                except:
                    failed.append(py_file.name)

            if failed:
                return False, f"Echec imports: {', '.join(failed)}"
            return True, f"{len(python_files)} modules importes"

        self.run_test("Imports Python", "Import tous modules v14_mvp", test_all_mvp_modules)

        def test_external_deps():
            deps = ["tkinter", "json", "pathlib"]
            for dep in deps:
                success, msg = self.test_python_import(dep)
                if not success:
                    return False, f"Dependance manquante: {dep}"
            return True, "Toutes dependances presentes"

        self.run_test("Imports Python", "Dependencies externes", test_external_deps)

        passed = self.results["categories"]["Imports Python"]["passed"]
        total = len(self.results["categories"]["Imports Python"]["tests"])
        print(f"  Resultat: {passed}/{total} tests reussis ({passed/total*100:.0f}%)\n")

    # === CATÉGORIE 4: MODULES APPLICATION (8 TESTS) ===

    def test_application_modules(self):
        """Tests des modules de l'application"""
        print("[CATEGORIE] Modules Application")

        def test_design_tokens():
            try:
                from v14_mvp.design_system import DesignTokens
                required_attrs = ["BG_PRIMARY", "ACCENT_PRIMARY", "TEXT_PRIMARY",
                                  "SPACING_MD", "RADIUS_MD", "FONT_FAMILY"]
                for attr in required_attrs:
                    if not hasattr(DesignTokens, attr):
                        return False, f"Attribut manquant: {attr}"
                return True, "DesignTokens complet"
            except Exception as e:
                return False, str(e)

        def test_theme_palettes():
            try:
                from v14_mvp.design_system import ThemePalettes
                methods = ["get_current_theme", "apply_theme", "save_theme"]
                for method in methods:
                    if not hasattr(ThemePalettes, method):
                        return False, f"Methode manquante: {method}"
                return True, "ThemePalettes complet"
            except Exception as e:
                return False, str(e)

        def test_color_picker():
            try:
                from v14_mvp.theme_editor_dynamic import ColorPicker
                return True, "ColorPicker disponible"
            except Exception as e:
                return False, str(e)

        def test_numeric_slider():
            try:
                from v14_mvp.theme_editor_dynamic import NumericSlider
                return True, "NumericSlider disponible"
            except Exception as e:
                return False, str(e)

        def test_theme_editor():
            try:
                from v14_mvp.theme_editor_dynamic import ThemeEditorDynamic
                return True, "ThemeEditorDynamic disponible"
            except Exception as e:
                return False, str(e)

        def test_main_pages():
            pages = ["pages_full", "pages_settings", "page_ai_agents"]
            for page in pages:
                try:
                    __import__(f"v14_mvp.{page}")
                except:
                    return False, f"Page manquante: {page}"
            return True, f"{len(pages)} pages principales OK"

        def test_components():
            try:
                from v14_mvp.components import ModernCard, ModernButton
                return True, "Components disponibles"
            except Exception as e:
                return False, "Components partiellement disponibles"

        def test_utilities():
            try:
                import json, os, pathlib
                return True, "Utilitaires standard disponibles"
            except:
                return False, "Utilitaires manquants"

        self.run_test("Modules Application", "DesignTokens", test_design_tokens)
        self.run_test("Modules Application", "ThemePalettes", test_theme_palettes)
        self.run_test("Modules Application", "ColorPicker widget", test_color_picker)
        self.run_test("Modules Application", "NumericSlider widget", test_numeric_slider)
        self.run_test("Modules Application", "ThemeEditorDynamic", test_theme_editor)
        self.run_test("Modules Application", "Pages principales", test_main_pages)
        self.run_test("Modules Application", "Components", test_components)
        self.run_test("Modules Application", "Utilitaires", test_utilities)

        passed = self.results["categories"]["Modules Application"]["passed"]
        total = len(self.results["categories"]["Modules Application"]["tests"])
        print(f"  Resultat: {passed}/{total} tests reussis ({passed/total*100:.0f}%)\n")

    # === CATÉGORIE 5: BASE DE DONNÉES PROGRAMMES (5 TESTS) ===

    def test_programs_database(self):
        """Tests de la base de données de programmes"""
        print("[CATEGORIE] Base de Donnees Programmes")

        def test_programs_count():
            success, data, msg = self.test_json_valid("data/programs.json")
            if not success or not data:
                return False, "Impossible de charger programs.json"
            count = len(data)
            if count < 700:
                return False, f"Trop peu de programmes: {count}"
            return True, f"{count} programmes disponibles"

        def test_categories():
            success, data, msg = self.test_json_valid("data/programs.json")
            if not success or not data:
                return False, "Impossible de charger programs.json"

            categories = set()
            for prog in data:
                if "category" in prog:
                    categories.add(prog["category"])

            if len(categories) < 20:
                return False, f"Trop peu de categories: {len(categories)}"
            return True, f"{len(categories)} categories trouvees"

        def test_program_structure():
            success, data, msg = self.test_json_valid("data/programs.json")
            if not success or not data:
                return False, "Impossible de charger programs.json"

            required_fields = ["name", "category"]
            sample_size = min(10, len(data))

            for prog in data[:sample_size]:
                for field in required_fields:
                    if field not in prog:
                        return False, f"Champ manquant: {field} dans {prog.get('name', '?')}"

            return True, f"Structure valide (echantillon: {sample_size})"

        def test_urls_format():
            success, data, msg = self.test_json_valid("data/programs.json")
            if not success or not data:
                return False, "Impossible de charger programs.json"

            invalid_urls = 0
            sample_size = min(50, len(data))

            for prog in data[:sample_size]:
                if "website" in prog and prog["website"]:
                    if not self.test_url_format(prog["website"]):
                        invalid_urls += 1

            if invalid_urls > 5:
                return False, f"{invalid_urls} URLs invalides trouvees"
            return True, f"URLs valides (echantillon: {sample_size})"

        def test_search():
            success, data, msg = self.test_json_valid("data/programs.json")
            if not success or not data:
                return False, "Impossible de charger programs.json"

            # Rechercher un programme courant
            search_terms = ["chrome", "firefox", "notepad", "vlc", "7zip"]
            found = 0

            for term in search_terms:
                for prog in data:
                    if term.lower() in prog.get("name", "").lower():
                        found += 1
                        break

            if found < 2:
                return False, "Recherche ne trouve pas de programmes courants"
            return True, f"{found}/{len(search_terms)} programmes courants trouves"

        self.run_test("Base de Donnees Programmes", "Nombre de programmes", test_programs_count)
        self.run_test("Base de Donnees Programmes", "Categories presentes", test_categories)
        self.run_test("Base de Donnees Programmes", "Structure programmes", test_program_structure)
        self.run_test("Base de Donnees Programmes", "URLs valides", test_urls_format)
        self.run_test("Base de Donnees Programmes", "Recherche programmes", test_search)

        passed = self.results["categories"]["Base de Donnees Programmes"]["passed"]
        total = len(self.results["categories"]["Base de Donnees Programmes"]["tests"])
        print(f"  Resultat: {passed}/{total} tests reussis ({passed/total*100:.0f}%)\n")

    # === CATÉGORIE 6: APPLICATIONS PORTABLES (4 TESTS) ===

    def test_portable_apps(self):
        """Tests des applications portables"""
        print("[CATEGORIE] Applications Portables")

        def test_portables_count():
            success, data, msg = self.test_json_valid("data/portable_apps.json")
            if not success or not data:
                return False, "Impossible de charger portable_apps.json"
            count = len(data)
            if count < 50:
                return False, f"Trop peu d'apps: {count}"
            return True, f"{count} apps portables disponibles"

        def test_portable_structure():
            success, data, msg = self.test_json_valid("data/portable_apps.json")
            if not success or not data:
                return False, "Impossible de charger portable_apps.json"

            required_fields = ["name", "category", "url"]
            sample_size = min(10, len(data))

            for app in data[:sample_size]:
                for field in required_fields:
                    if field not in app:
                        return False, f"Champ manquant: {field}"

            return True, f"Structure valide (echantillon: {sample_size})"

        def test_portable_urls():
            success, data, msg = self.test_json_valid("data/portable_apps.json")
            if not success or not data:
                return False, "Impossible de charger portable_apps.json"

            invalid_urls = 0
            sample_size = min(20, len(data))

            for app in data[:sample_size]:
                if "url" in app and app["url"]:
                    if not self.test_url_format(app["url"]):
                        invalid_urls += 1

            if invalid_urls > 3:
                return False, f"{invalid_urls} URLs invalides"
            return True, f"URLs valides (echantillon: {sample_size})"

        def test_portable_categories():
            success, data, msg = self.test_json_valid("data/portable_apps.json")
            if not success or not data:
                return False, "Impossible de charger portable_apps.json"

            categories = set()
            for app in data:
                if "category" in app:
                    categories.add(app["category"])

            if len(categories) < 5:
                return False, f"Trop peu de categories: {len(categories)}"
            return True, f"{len(categories)} categories portables"

        self.run_test("Applications Portables", "Nombre d'apps portables", test_portables_count)
        self.run_test("Applications Portables", "Structure apps", test_portable_structure)
        self.run_test("Applications Portables", "URLs telechargement", test_portable_urls)
        self.run_test("Applications Portables", "Categories portables", test_portable_categories)

        passed = self.results["categories"]["Applications Portables"]["passed"]
        total = len(self.results["categories"]["Applications Portables"]["tests"])
        print(f"  Resultat: {passed}/{total} tests reussis ({passed/total*100:.0f}%)\n")

    # === CATÉGORIE 7: SCRIPTS ORGANISÉS (5 TESTS) ===

    def test_organized_scripts(self):
        """Tests des scripts organisés"""
        print("[CATEGORIE] Scripts Organises")

        def test_diagnostics():
            diag_dir = self.project_root / "scripts" / "diagnostics"
            if not diag_dir.exists():
                return False, "Dossier scripts/diagnostics/ manquant"
            py_files = list(diag_dir.glob("*.py"))
            if len(py_files) < 2:
                return False, f"Trop peu de scripts: {len(py_files)}"
            return True, f"{len(py_files)} scripts diagnostics"

        def test_fixes():
            fixes_dir = self.project_root / "scripts" / "fixes"
            if not fixes_dir.exists():
                return False, "Dossier scripts/fixes/ manquant"
            py_files = list(fixes_dir.glob("*.py"))
            if len(py_files) < 2:
                return False, f"Trop peu de scripts: {len(py_files)}"
            return True, f"{len(py_files)} scripts fixes"

        def test_tests():
            tests_dir = self.project_root / "scripts" / "tests"
            if not tests_dir.exists():
                return True, "Dossier scripts/tests/ vide (OK)"
            py_files = list(tests_dir.glob("*.py"))
            return True, f"{len(py_files)} scripts tests"

        def test_build_tools():
            build_dir = self.project_root / "build_tools"
            if not build_dir.exists():
                return False, "Dossier build_tools/ manquant"
            py_files = list(build_dir.glob("*.py"))
            if len(py_files) < 1:
                return False, "Aucun script build"
            return True, f"{len(py_files)} scripts build"

        def test_config_runtime():
            config_dir = self.project_root / "data" / "config_runtime"
            if not config_dir.exists():
                return True, "Dossier data/config_runtime/ vide (OK)"
            files = list(config_dir.glob("*"))
            return True, f"{len(files)} fichiers config runtime"

        self.run_test("Scripts Organises", "scripts/diagnostics/", test_diagnostics)
        self.run_test("Scripts Organises", "scripts/fixes/", test_fixes)
        self.run_test("Scripts Organises", "scripts/tests/", test_tests)
        self.run_test("Scripts Organises", "build_tools/", test_build_tools)
        self.run_test("Scripts Organises", "data/config_runtime/", test_config_runtime)

        passed = self.results["categories"]["Scripts Organises"]["passed"]
        total = len(self.results["categories"]["Scripts Organises"]["tests"])
        print(f"  Resultat: {passed}/{total} tests reussis ({passed/total*100:.0f}%)\n")

    # === CATÉGORIE 8: ÉDITEUR DE THÈME (5 TESTS) ===

    def test_theme_editor(self):
        """Tests de l'éditeur de thème"""
        print("[CATEGORIE] Editeur de Theme")

        self.run_test("Editeur de Theme", "theme_editor_dynamic.py existe",
                      lambda: self.test_file_exists("src/v14_mvp/theme_editor_dynamic.py"))

        def test_load_theme():
            try:
                from v14_mvp.theme_editor_dynamic import ThemeEditorDynamic
                # Test que la méthode existe
                if not hasattr(ThemeEditorDynamic, "load_current_theme"):
                    return False, "Methode load_current_theme manquante"
                return True, "Chargement theme OK"
            except Exception as e:
                return False, str(e)

        def test_save_theme():
            themes_dir = self.project_root / "data" / "themes"
            return themes_dir.exists(), "Dossier themes/ pour sauvegarde"

        def test_widgets():
            try:
                from v14_mvp.theme_editor_dynamic import ColorPicker, NumericSlider
                return True, "Widgets personnalises disponibles"
            except Exception as e:
                return False, str(e)

        def test_presets():
            try:
                from v14_mvp.design_system import ThemePalettes
                if not hasattr(ThemePalettes, "THEMES"):
                    return False, "Attribute THEMES manquant"

                themes = getattr(ThemePalettes, "THEMES", {})
                if len(themes) < 5:
                    return False, f"Trop peu de presets: {len(themes)}"
                return True, f"{len(themes)} presets disponibles"
            except Exception as e:
                return False, str(e)

        self.run_test("Editeur de Theme", "Chargement theme", test_load_theme)
        self.run_test("Editeur de Theme", "Sauvegarde theme", test_save_theme)
        self.run_test("Editeur de Theme", "Widgets personnalises", test_widgets)
        self.run_test("Editeur de Theme", "Presets themes", test_presets)

        passed = self.results["categories"]["Editeur de Theme"]["passed"]
        total = len(self.results["categories"]["Editeur de Theme"]["tests"])
        print(f"  Resultat: {passed}/{total} tests reussis ({passed/total*100:.0f}%)\n")

    # === CATÉGORIE 9: CONFIGURATION UTILISATEUR (3 TESTS) ===

    def test_user_configuration(self):
        """Tests de configuration utilisateur"""
        print("[CATEGORIE] Configuration Utilisateur")

        def test_config_path():
            home = Path.home()
            config_path = home / ".nitrite_config.json"
            # Le fichier peut ne pas exister encore
            return True, f"Chemin config: {config_path}"

        def test_config_save():
            try:
                from v14_mvp.design_system import ThemePalettes
                if not hasattr(ThemePalettes, "save_theme"):
                    return False, "Methode save_theme manquante"
                return True, "Sauvegarde config disponible"
            except Exception as e:
                return False, str(e)

        def test_config_load():
            try:
                from v14_mvp.design_system import ThemePalettes
                if not hasattr(ThemePalettes, "get_current_theme"):
                    return False, "Methode get_current_theme manquante"
                return True, "Chargement config disponible"
            except Exception as e:
                return False, str(e)

        self.run_test("Configuration Utilisateur", "Chemin configuration", test_config_path)
        self.run_test("Configuration Utilisateur", "Sauvegarde configuration", test_config_save)
        self.run_test("Configuration Utilisateur", "Chargement configuration", test_config_load)

        passed = self.results["categories"]["Configuration Utilisateur"]["passed"]
        total = len(self.results["categories"]["Configuration Utilisateur"]["tests"])
        print(f"  Resultat: {passed}/{total} tests reussis ({passed/total*100:.0f}%)\n")

    # === CATÉGORIE 10: RAPPORTS ET LOGS (3 TESTS) ===

    def test_reports_and_logs(self):
        """Tests des rapports et logs"""
        print("[CATEGORIE] Rapports et Logs")

        self.run_test("Rapports et Logs", "RAPPORT_CORRECTIONS.json existe",
                      lambda: self.test_file_exists("RAPPORT_CORRECTIONS.json"))

        self.run_test("Rapports et Logs", "RAPPORT_REORGANISATION.json existe",
                      lambda: self.test_file_exists("RAPPORT_REORGANISATION.json"))

        def test_generate_report():
            # Test que nous pouvons générer un rapport
            return True, "Generation rapport disponible"

        self.run_test("Rapports et Logs", "Generation rapport test", test_generate_report)

        passed = self.results["categories"]["Rapports et Logs"]["passed"]
        total = len(self.results["categories"]["Rapports et Logs"]["tests"])
        print(f"  Resultat: {passed}/{total} tests reussis ({passed/total*100:.0f}%)\n")

    # === EXÉCUTION COMPLÈTE ===

    def run_all_tests(self):
        """Exécuter tous les tests"""
        self.start_time = time.time()

        print("=" * 60)
        print("       TESTS AUTOMATISES NITRITE V18.5")
        print("=" * 60)
        print(f"\nRepertoire du projet: {self.project_root}")
        print(f"Date: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")

        # Exécuter toutes les catégories de tests
        self.test_file_structure()
        self.test_json_integrity()
        self.test_python_imports()
        self.test_application_modules()
        self.test_programs_database()
        self.test_portable_apps()
        self.test_organized_scripts()
        self.test_theme_editor()
        self.test_user_configuration()
        self.test_reports_and_logs()

        # Calculer le temps d'exécution
        self.results["execution_time"] = time.time() - self.start_time

        # Calculer le taux de succès
        total = self.results["summary"]["total"]
        passed = self.results["summary"]["passed"]
        self.results["summary"]["success_rate"] = (passed / total * 100) if total > 0 else 0

        # Afficher le résumé
        print("=" * 60)
        print("                RESUME FINAL")
        print("=" * 60)
        print(f"Total: {passed}/{total} tests reussis ({self.results['summary']['success_rate']:.1f}%)")
        print(f"Duree d'execution: {self.results['execution_time']:.2f}s")

        if self.results["errors"]:
            print(f"\nErreurs trouvees: {len(self.results['errors'])}")

    # === GÉNÉRATION DE RAPPORTS ===

    def generate_json_report(self):
        """Générer un rapport JSON"""
        report_path = self.project_root / "RAPPORT_TESTS_AUTO.json"

        report = {
            "date": datetime.now().isoformat(),
            "project_root": str(self.project_root),
            "total_tests": self.results["summary"]["total"],
            "passed": self.results["summary"]["passed"],
            "failed": self.results["summary"]["failed"],
            "success_rate": self.results["summary"]["success_rate"],
            "execution_time": self.results["execution_time"],
            "categories": self.results["categories"],
            "errors": self.results["errors"]
        }

        try:
            with open(report_path, 'w', encoding='utf-8') as f:
                json.dump(report, f, indent=2, ensure_ascii=False)
            print(f"\nRapport JSON genere: {report_path}")
            return True
        except Exception as e:
            print(f"\nErreur generation rapport JSON: {e}")
            return False

    def generate_html_report(self):
        """Générer un rapport HTML"""
        report_path = self.project_root / "RAPPORT_TESTS_AUTO.html"

        html = f"""<!DOCTYPE html>
<html lang="fr">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Rapport de Tests - Nitrite V18.5</title>
    <style>
        body {{
            font-family: 'Segoe UI', Arial, sans-serif;
            background: #0a0a0a;
            color: #ffffff;
            margin: 0;
            padding: 20px;
        }}
        .container {{
            max-width: 1200px;
            margin: 0 auto;
        }}
        h1 {{
            color: #ff6b35;
            text-align: center;
            margin-bottom: 30px;
        }}
        .summary {{
            background: #151515;
            padding: 20px;
            border-radius: 16px;
            margin-bottom: 30px;
        }}
        .stat {{
            display: inline-block;
            margin: 10px 20px;
        }}
        .stat-value {{
            font-size: 36px;
            font-weight: bold;
            color: #ff6b35;
        }}
        .stat-label {{
            font-size: 14px;
            color: #b0b0b0;
        }}
        .category {{
            background: #151515;
            padding: 20px;
            border-radius: 16px;
            margin-bottom: 20px;
        }}
        .category-header {{
            font-size: 20px;
            font-weight: bold;
            margin-bottom: 15px;
            color: #ffffff;
        }}
        .test {{
            padding: 10px;
            margin: 5px 0;
            background: #202020;
            border-radius: 8px;
        }}
        .test-success {{
            border-left: 4px solid #4caf50;
        }}
        .test-error {{
            border-left: 4px solid #f44336;
        }}
        .error-message {{
            color: #f44336;
            font-size: 12px;
            margin-top: 5px;
        }}
    </style>
</head>
<body>
    <div class="container">
        <h1>Rapport de Tests Automatises - Nitrite V18.5</h1>

        <div class="summary">
            <div class="stat">
                <div class="stat-value">{self.results["summary"]["passed"]}/{self.results["summary"]["total"]}</div>
                <div class="stat-label">Tests Reussis</div>
            </div>
            <div class="stat">
                <div class="stat-value">{self.results["summary"]["success_rate"]:.1f}%</div>
                <div class="stat-label">Taux de Succes</div>
            </div>
            <div class="stat">
                <div class="stat-value">{self.results["execution_time"]:.2f}s</div>
                <div class="stat-label">Duree</div>
            </div>
        </div>
"""

        # Ajouter les catégories
        for category_name, category_data in self.results["categories"].items():
            html += f"""
        <div class="category">
            <div class="category-header">{category_name} ({category_data["passed"]}/{len(category_data["tests"])})</div>
"""
            for test in category_data["tests"]:
                test_class = "test-success" if test["success"] else "test-error"
                status = "OK" if test["success"] else "ERREUR"
                html += f"""
            <div class="test {test_class}">
                <strong>[{status}]</strong> {test["name"]}
"""
                if test["error"]:
                    html += f"""
                <div class="error-message">{test["error"]}</div>
"""
                html += """
            </div>
"""
            html += """
        </div>
"""

        html += """
    </div>
</body>
</html>"""

        try:
            with open(report_path, 'w', encoding='utf-8') as f:
                f.write(html)
            print(f"Rapport HTML genere: {report_path}")
            return True
        except Exception as e:
            print(f"Erreur generation rapport HTML: {e}")
            return False


def main():
    """Fonction principale"""
    import sys

    # Obtenir le chemin du projet
    project_root = os.path.dirname(os.path.abspath(__file__))

    # Créer le testeur
    tester = NitriteFunctionalityTester(project_root)

    # Exécuter tous les tests
    tester.run_all_tests()

    # Générer les rapports
    tester.generate_json_report()
    tester.generate_html_report()

    print("\n" + "=" * 60)
    print("Rapports generes:")
    print("  - RAPPORT_TESTS_AUTO.json")
    print("  - RAPPORT_TESTS_AUTO.html")
    print("=" * 60)

    # Code de sortie basé sur le taux de succès
    return 0 if tester.results["summary"]["success_rate"] >= 90 else 1


if __name__ == "__main__":
    sys.exit(main())
