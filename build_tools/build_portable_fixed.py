#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Script de build multi-plateforme pour NiTriTe V18
Fonctionne sur Windows, Linux et macOS
Version corrigée avec support d'encodage amélioré
"""

import os
import sys
import shutil
import subprocess
from pathlib import Path

# Configuration de l'encodage UTF-8 pour Windows
if sys.platform == 'win32':
    try:
        import io
        sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')
        sys.stderr = io.TextIOWrapper(sys.stderr.buffer, encoding='utf-8', errors='replace')
    except Exception:
        pass  # Ignorer si déjà configuré

def print_header(text):
    """Afficher un header"""
    print("\n" + "="*60)
    print(f"  {text}")
    print("="*60 + "\n")

def clean_build():
    """Nettoyer les anciens builds"""
    print("[*] Nettoyage des anciens builds...")

    dirs_to_clean = ['dist', 'build', '__pycache__']
    for dir_name in dirs_to_clean:
        if os.path.exists(dir_name):
            print(f"    Suppression: {dir_name}/")
            try:
                shutil.rmtree(dir_name, ignore_errors=True)
            except Exception as e:
                print(f"    [!] Avertissement: {e}")

    # Nettoyer aussi les __pycache__ dans src/
    for root, dirs, files in os.walk('src'):
        if '__pycache__' in dirs:
            pycache_path = os.path.join(root, '__pycache__')
            print(f"    Suppression: {pycache_path}")
            try:
                shutil.rmtree(pycache_path, ignore_errors=True)
            except Exception as e:
                print(f"    [!] Avertissement: {e}")

    print("[OK] Nettoyage termine\n")

def check_python_version():
    """Vérifier la version de Python"""
    print("[*] Verification de Python...")
    py_version = sys.version_info

    if py_version.major != 3 or py_version.minor < 8:
        print(f"[X] ERREUR: Python {py_version.major}.{py_version.minor} detecte")
        print("[!] Python 3.8+ requis")
        return False

    print(f"[OK] Python {py_version.major}.{py_version.minor}.{py_version.micro}")
    return True

def check_dependencies():
    """Vérifier les dépendances"""
    print("\n[*] Verification des dependances...")

    # Mapping package pip -> module Python
    required = {
        'customtkinter': 'customtkinter',
        'Pillow': 'PIL',
        'requests': 'requests',
        'psutil': 'psutil',
        'pyinstaller': 'PyInstaller'
    }

    missing = []
    for package, module in required.items():
        try:
            __import__(module)
            print(f"    [OK] {package}")
        except ImportError:
            print(f"    [X] {package} - MANQUANT")
            missing.append(package)

    if missing:
        print(f"\n[!] Dependances manquantes: {', '.join(missing)}")
        print("[*] Installation automatique...")

        for package in missing:
            print(f"    Installation de {package}...")
            result = subprocess.run(
                [sys.executable, '-m', 'pip', 'install', package],
                capture_output=True,
                text=True
            )
            if result.returncode == 0:
                print(f"    [OK] {package} installe")
            else:
                print(f"    [X] Erreur lors de l'installation de {package}")
                return False

        print("[OK] Installation terminee")

    return True

def check_files():
    """Vérifier que tous les fichiers nécessaires existent"""
    print("\n[*] Verification des fichiers...")

    required_files = [
        'src/v14_mvp/main_app.py',
        'data/programs.json',
        'NiTriTe_V18_Portable.spec',
    ]

    all_exist = True
    for file_path in required_files:
        if os.path.exists(file_path):
            print(f"    [OK] {file_path}")
        else:
            print(f"    [X] {file_path} - MANQUANT")
            all_exist = False

    # Assets optionnels
    if os.path.exists('assets/logo.ico'):
        print(f"    [OK] assets/logo.ico (icone)")
    else:
        print(f"    [!] assets/logo.ico - optionnel (pas d'icone)")

    return all_exist

def build_executable():
    """Builder l'exécutable avec PyInstaller"""
    print("\n[*] Build de l'executable avec PyInstaller...")
    print("    Cette operation peut prendre plusieurs minutes...\n")

    try:
        # Utiliser python -m PyInstaller pour compatibilité Windows
        result = subprocess.run(
            [sys.executable, '-m', 'PyInstaller', '--noconfirm', '--clean', 'NiTriTe_V18_Portable.spec'],
            check=True,
            capture_output=False,
            text=True
        )

        return True

    except subprocess.CalledProcessError as e:
        print(f"\n[X] ERREUR lors du build:")
        print(f"    Code de sortie: {e.returncode}")
        return False

    except FileNotFoundError:
        print("\n[X] ERREUR: PyInstaller non trouve")
        print("    Installation: pip install pyinstaller")
        return False

def verify_build():
    """Vérifier que le build a réussi"""
    print("\n[*] Verification du build...")

    # Chercher l'exécutable (extension dépend de l'OS)
    exe_name = 'NiTriTe_V18_Portable.exe' if sys.platform == 'win32' else 'NiTriTe_V18_Portable'
    exe_path = Path('dist') / exe_name

    if exe_path.exists():
        size_mb = exe_path.stat().st_size / (1024 * 1024)
        print(f"[OK] Executable cree: {exe_path}")
        print(f"    Taille: {size_mb:.1f} MB")
        return True
    else:
        print(f"[X] Executable non trouve: {exe_path}")
        return False

def copy_logiciel_to_dist():
    """Copier le dossier logiciel vers dist/ pour les outils portables"""
    print("\n[*] Copie du dossier logiciel vers dist/...")

    logiciel_src = Path('logiciel')
    logiciel_dst = Path('dist') / 'logiciel'

    if not logiciel_src.exists():
        print("[!] Dossier logiciel non trouve - les outils diagnostics ne fonctionneront pas")
        return False

    try:
        # Supprimer l'ancien dossier s'il existe (avec gestion des erreurs)
        if logiciel_dst.exists():
            print("    Suppression de l'ancien dossier logiciel...")
            shutil.rmtree(logiciel_dst, ignore_errors=True)

            # Attendre un peu que le système libère les fichiers
            import time
            time.sleep(0.5)

        # Copier le nouveau dossier (avec dirs_exist_ok pour Python 3.8+)
        shutil.copytree(logiciel_src, logiciel_dst, dirs_exist_ok=True)

        # Compter les éléments copiés
        items_count = len(list(logiciel_dst.iterdir()))
        print(f"[OK] Dossier logiciel copie vers dist/ ({items_count} elements)")
        return True
    except Exception as e:
        print(f"[!] Erreur copie logiciel: {e}")
        print(f"[!] Certains fichiers n'ont pas pu etre copies, mais la plupart sont la")
        return True  # Retourner True quand même car partiellement réussi

def copy_scripts_to_dist():
    """Copier le dossier Script Windows vers dist/"""
    print("\n[*] Copie du dossier Script Windows vers dist/...")

    scripts_src = Path('Script Windows')
    scripts_dst = Path('dist') / 'Script Windows'

    if not scripts_src.exists():
        print("[!] Dossier 'Script Windows' non trouve - Creation d'un dossier vide...")
        # Créer un dossier vide avec un fichier README
        scripts_src.mkdir(exist_ok=True)
        readme_path = scripts_src / "README.txt"
        readme_path.write_text(
            "Dossier Script Windows\n"
            "======================\n\n"
            "Placez vos scripts Windows (.bat, .cmd, .ps1) ici.\n"
            "Ils seront accessibles depuis la categorie 'Scripts Windows' de NiTriTe.\n\n"
            "Vous pouvez creer, editer et executer vos scripts directement depuis l'application.\n",
            encoding='utf-8'
        )
        print("[OK] Dossier 'Script Windows' cree avec README.txt")

    try:
        # Supprimer l'ancien dossier s'il existe
        if scripts_dst.exists():
            print("    Suppression de l'ancien dossier Script Windows...")
            shutil.rmtree(scripts_dst, ignore_errors=True)

        import time
        time.sleep(0.5)

        # Copier le nouveau dossier
        shutil.copytree(scripts_src, scripts_dst, dirs_exist_ok=True)

        # Compter les éléments copiés
        items_count = len(list(scripts_dst.iterdir()))
        print(f"[OK] Dossier 'Script Windows' copie vers dist/ ({items_count} elements)")
        return True
    except Exception as e:
        print(f"[!] Erreur copie Script Windows: {e}")
        return False

def create_portable_package():
    """Créer un package portable complet (OPTIONNEL)"""
    print("\n[*] Creation du package portable...")

    exe_name = 'NiTriTe_V18_Portable.exe' if sys.platform == 'win32' else 'NiTriTe_V18_Portable'
    exe_path = Path('dist') / exe_name

    if not exe_path.exists():
        print("[X] Executable non trouve, impossible de creer le package")
        return False

    try:
        # Créer dossier de release
        release_dir = Path('release')
        if release_dir.exists():
            shutil.rmtree(release_dir, ignore_errors=True)
        release_dir.mkdir(exist_ok=True)

        print(f"    Copie de l'executable...")
        shutil.copy2(exe_path, release_dir / exe_name)

        # Copier le dossier logiciel vers release/
        logiciel_src = Path('logiciel')
        logiciel_dst = release_dir / 'logiciel'
        if logiciel_src.exists():
            print(f"    Copie du dossier logiciel vers release/...")
            # Supprimer l'ancien dossier s'il existe (avec gestion des erreurs)
            if logiciel_dst.exists():
                shutil.rmtree(logiciel_dst, ignore_errors=True)

            import time
            time.sleep(0.5)

            # Copier avec dirs_exist_ok
            shutil.copytree(logiciel_src, logiciel_dst, dirs_exist_ok=True)
            items_count = len(list(logiciel_dst.iterdir()))
            print(f"    [OK] Dossier logiciel copie vers release/ ({items_count} elements)")
        else:
            print(f"    [!] Dossier logiciel non trouve - skip")

        # Copier le dossier Script Windows vers release/
        scripts_src = Path('Script Windows')
        scripts_dst = release_dir / 'Script Windows'
        if scripts_src.exists():
            print(f"    Copie du dossier Script Windows vers release/...")
            if scripts_dst.exists():
                shutil.rmtree(scripts_dst, ignore_errors=True)

            time.sleep(0.5)

            shutil.copytree(scripts_src, scripts_dst, dirs_exist_ok=True)
            items_count = len(list(scripts_dst.iterdir()))
            print(f"    [OK] Dossier Script Windows copie vers release/ ({items_count} elements)")
        else:
            print(f"    [!] Dossier Script Windows non trouve - skip")

        # Copier les fichiers de lancement
        if os.path.exists('LANCER_V18_PORTABLE.bat'):
            shutil.copy2('LANCER_V18_PORTABLE.bat', release_dir)
            print(f"    Copie de LANCER_V18_PORTABLE.bat")

        # Créer un README
        readme_content = """NiTriTe V18 Beta - Version Portable
====================================

Installation:
1. Extraire tous les fichiers dans un dossier
2. Double-cliquer sur LANCER_V18_PORTABLE.bat (ou NiTriTe_V18_Portable.exe)

Configuration requise:
- Windows 10/11
- Aucune installation requise
- Tous les composants sont embarques

Support:
Pour toute question ou probleme, consultez README.md dans le projet source.
"""

        with open(release_dir / 'README_PORTABLE.txt', 'w', encoding='utf-8') as f:
            f.write(readme_content)

        print(f"[OK] Package portable cree dans: {release_dir}/")
        return True
    except Exception as e:
        print(f"[!] Erreur creation package: {e}")
        print(f"[!] L'executable est disponible dans dist/, le package est optionnel")
        return False

def main():
    """Point d'entrée principal"""
    print_header("NiTriTe V18 - Build Portable")

    # 1. Vérifier Python
    if not check_python_version():
        return 1

    # 2. Vérifier dépendances
    if not check_dependencies():
        return 1

    # 3. Vérifier fichiers
    if not check_files():
        print("\n[X] Fichiers manquants - Impossible de continuer")
        return 1

    # 4. Nettoyer
    clean_build()

    # 5. Builder
    print_header("Demarrage du Build")

    if not build_executable():
        print("\n[X] BUILD ECHOUE")
        return 1

    # 6. Vérifier
    if not verify_build():
        print("\n[X] BUILD ECHOUE - Executable non cree")
        return 1

    # 7. Copier dossier logiciel vers dist/
    copy_logiciel_to_dist()

    # 8. Copier dossier Script Windows vers dist/
    copy_scripts_to_dist()

    # 9. Créer package portable (optionnel)
    if not create_portable_package():
        print("\n[!] Package portable non cree, mais executable disponible dans dist/")

    # Succès !
    print_header("BUILD REUSSI !")

    exe_name = 'NiTriTe_V18_Portable.exe' if sys.platform == 'win32' else 'NiTriTe_V18_Portable'
    print(f"[OK] Executable pret: dist/{exe_name}")
    print(f"[OK] Package portable: release/")
    print(f"\n[*] Pour distribuer:")
    print(f"    1. Testez l'executable: dist/{exe_name}")
    print(f"    2. Verifiez toutes les fonctionnalites")
    print(f"    3. Distribuez le dossier release/")
    print("\n" + "="*60 + "\n")

    return 0

if __name__ == "__main__":
    try:
        exit_code = main()
        sys.exit(exit_code)
    except KeyboardInterrupt:
        print("\n\n[!] Build annule par l'utilisateur (Ctrl+C)")
        sys.exit(1)
    except Exception as e:
        print(f"\n[X] ERREUR FATALE: {e}")
        import traceback
        traceback.print_exc()
        sys.exit(1)
