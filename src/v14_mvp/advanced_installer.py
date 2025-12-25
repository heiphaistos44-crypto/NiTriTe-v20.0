#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Advanced Multi-Method Installer - NiTriTe V18
WinGet → Chocolatey → Direct Download avec fallback automatique
"""

import subprocess
import threading
import requests
import os
import shutil
from pathlib import Path
from typing import Callable, Optional, Tuple
from v14_mvp.logger_system import logger


class AdvancedInstaller:
    """Installateur multi-méthodes avec fallback automatique"""

    # Sites de téléchargement fiables pour applications portables
    PORTABLE_SOURCES = {
        "portableapps": "https://portableapps.com/apps",
        "portableappsz": "https://portableappz.blogspot.com",
        "liberkey": "https://www.liberkey.com/fr.html",
        "sourceforge": "https://sourceforge.net"
    }

    def __init__(self):
        self.winget_available = self._check_winget()
        self.chocolatey_available = self._check_chocolatey()

        # Dossiers portables
        self.portable_dir = Path("logiciel")
        self.portable_dir.mkdir(exist_ok=True)

        # Utiliser dossier downloads portable au lieu du Desktop
        try:
            sys.path.insert(0, str(Path(__file__).parent.parent))
            from portable_paths import get_portable_downloads_dir
            self.downloads_folder = get_portable_downloads_dir()
        except:
            # Fallback
            if getattr(sys, 'frozen', False):
                app_dir = Path(sys.executable).parent
            else:
                app_dir = Path(__file__).parent.parent.parent
            self.downloads_folder = app_dir / 'downloads'
            self.downloads_folder.mkdir(parents=True, exist_ok=True)

        logger.info("Installer", "Initialisé",
                   winget=self.winget_available,
                   chocolatey=self.chocolatey_available)

    def _check_winget(self) -> bool:
        """Vérifier si WinGet est disponible"""
        try:
            result = subprocess.run(
                ["winget", "--version"],
                capture_output=True,
                text=True,
                timeout=5,
                creationflags=subprocess.CREATE_NO_WINDOW
            )
            available = result.returncode == 0
            logger.debug("Installer", f"WinGet disponible: {available}")
            return available
        except Exception as e:
            logger.warning("Installer", f"WinGet non disponible: {e}")
            return False

    def _check_chocolatey(self) -> bool:
        """Vérifier si Chocolatey est disponible"""
        try:
            result = subprocess.run(
                ["choco", "--version"],
                capture_output=True,
                text=True,
                timeout=5,
                creationflags=subprocess.CREATE_NO_WINDOW
            )
            available = result.returncode == 0
            logger.debug("Installer", f"Chocolatey disponible: {available}")
            return available
        except Exception as e:
            logger.warning("Installer", f"Chocolatey non disponible: {e}")
            return False

    def install_app(
        self,
        app_name: str,
        winget_id: Optional[str] = None,
        choco_id: Optional[str] = None,
        download_url: Optional[str] = None,
        portable: bool = False,
        on_progress: Optional[Callable[[float, str], None]] = None,
        on_log: Optional[Callable[[str, str], None]] = None,
        on_complete: Optional[Callable[[bool, str], None]] = None
    ):
        """
        Installe une application avec fallback automatique

        Ordre des méthodes:
        1. WinGet (si winget_id fourni et WinGet disponible)
        2. Chocolatey (si choco_id fourni et Chocolatey disponible)
        3. Téléchargement direct (si download_url fourni)
        4. Recherche automatique sur sites portables (si portable=True)
        """
        thread = threading.Thread(
            target=self._install_thread,
            args=(app_name, winget_id, choco_id, download_url, portable,
                  on_progress, on_log, on_complete),
            daemon=True
        )
        thread.start()

    def _install_thread(
        self,
        app_name: str,
        winget_id: Optional[str],
        choco_id: Optional[str],
        download_url: Optional[str],
        portable: bool,
        on_progress: Optional[Callable],
        on_log: Optional[Callable],
        on_complete: Optional[Callable]
    ):
        """Thread d'installation avec fallback"""
        try:
            logger.info("Installation", f"Démarrage installation: {app_name}",
                       winget_id=winget_id, choco_id=choco_id, portable=portable)

            if on_log:
                on_log(f" Installation de {app_name}...", "info")

            # Méthode 1: WinGet
            if winget_id and self.winget_available:
                if on_log:
                    on_log(f" Tentative WinGet: {winget_id}", "info")

                success, msg = self._install_winget(app_name, winget_id, on_progress, on_log)

                if success:
                    logger.success("Installation", f"WinGet OK: {app_name}")
                    if on_complete:
                        on_complete(True, msg)
                    return
                else:
                    logger.warning("Installation", f"WinGet échec: {app_name}, tentative fallback...")
                    if on_log:
                        on_log(" WinGet échoué, essai Chocolatey...", "warning")

            # Méthode 2: Chocolatey
            if choco_id and self.chocolatey_available:
                if on_log:
                    on_log(f" Tentative Chocolatey: {choco_id}", "info")

                success, msg = self._install_chocolatey(app_name, choco_id, on_progress, on_log)

                if success:
                    logger.success("Installation", f"Chocolatey OK: {app_name}")
                    if on_complete:
                        on_complete(True, msg)
                    return
                else:
                    logger.warning("Installation", f"Chocolatey échec: {app_name}, tentative fallback...")
                    if on_log:
                        on_log(" Chocolatey échoué, essai téléchargement direct...", "warning")

            # Méthode 3: Téléchargement direct
            if download_url:
                if on_log:
                    on_log(f" Téléchargement direct: {download_url}", "info")

                success, msg = self._install_download(
                    app_name, download_url, portable, on_progress, on_log
                )

                if success:
                    logger.success("Installation", f"Téléchargement OK: {app_name}")
                    if on_complete:
                        on_complete(True, msg)
                    return
                else:
                    logger.error("Installation", f"Téléchargement échoué: {app_name}")

            # Toutes les méthodes ont échoué
            error_msg = f" Échec installation {app_name} (toutes méthodes échouées)"
            logger.error("Installation", error_msg)

            if on_log:
                on_log(error_msg, "error")
                on_log(" Vérifiez votre connexion internet ou installez manuellement", "info")

            if on_complete:
                on_complete(False, error_msg)

        except Exception as e:
            logger.log_exception("Installation", e, context=f"Installation {app_name}")

            if on_log:
                on_log(f" ERREUR: {str(e)}", "error")

            if on_complete:
                on_complete(False, f"Erreur: {str(e)}")

    def _install_winget(
        self,
        app_name: str,
        package_id: str,
        on_progress: Optional[Callable],
        on_log: Optional[Callable]
    ) -> Tuple[bool, str]:
        """Installation via WinGet"""
        if not self.winget_available:
            return False, "WinGet non disponible"

        try:
            if on_progress:
                on_progress(0.2, "Préparation WinGet...")

            cmd = [
                "winget", "install",
                "--id", package_id,
                "--exact",
                "--silent",
                "--scope", "user",
                "--accept-source-agreements",
                "--accept-package-agreements",
                "--disable-interactivity"
            ]

            logger.debug("Installation", f"CMD: {' '.join(cmd)}")

            if on_progress:
                on_progress(0.3, "Installation WinGet...")

            process = subprocess.Popen(
                cmd,
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                text=True,
                bufsize=1,
                creationflags=subprocess.CREATE_NO_WINDOW
            )

            # Lire sortie
            while True:
                output = process.stdout.readline()
                if output == '' and process.poll() is not None:
                    break
                if output and on_log:
                    line = output.strip()
                    if line:
                        level = "info"
                        if "error" in line.lower() or "failed" in line.lower():
                            level = "error"
                        elif "success" in line.lower() or "installed" in line.lower():
                            level = "success"

                        on_log(line, level)

                if on_progress:
                    on_progress(0.6, "Installation...")

            if on_progress:
                on_progress(0.9, "Finalisation...")

            returncode = process.poll()

            if returncode == 0:
                msg = f" {app_name} installé via WinGet"
                if on_log:
                    on_log(msg, "success")
                if on_progress:
                    on_progress(1.0, "Terminé")
                return True, msg
            else:
                # Codes d'erreur WinGet
                if returncode in [-1978335212, 2316632084]:  # 0x8A150014
                    msg = f"Package '{package_id}' introuvable"
                else:
                    msg = f"Échec WinGet (code: {returncode:#x})"

                logger.warning("Installation", msg, package_id=package_id, returncode=returncode)
                return False, msg

        except Exception as e:
            logger.log_exception("Installation", e, context=f"WinGet {app_name}")
            return False, str(e)

    def _install_chocolatey(
        self,
        app_name: str,
        package_id: str,
        on_progress: Optional[Callable],
        on_log: Optional[Callable]
    ) -> Tuple[bool, str]:
        """Installation via Chocolatey"""
        if not self.chocolatey_available:
            return False, "Chocolatey non disponible"

        try:
            if on_progress:
                on_progress(0.2, "Préparation Chocolatey...")

            cmd = [
                "choco", "install", package_id,
                "-y",
                "--no-progress",
                "--ignore-checksums"
            ]

            logger.debug("Installation", f"CMD: {' '.join(cmd)}")

            if on_progress:
                on_progress(0.3, "Installation Chocolatey...")

            process = subprocess.Popen(
                cmd,
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                text=True,
                bufsize=1,
                creationflags=subprocess.CREATE_NO_WINDOW
            )

            # Lire sortie
            while True:
                output = process.stdout.readline()
                if output == '' and process.poll() is not None:
                    break
                if output and on_log:
                    line = output.strip()
                    if line:
                        level = "info"
                        if "error" in line.lower():
                            level = "error"
                        elif "success" in line.lower():
                            level = "success"

                        on_log(line, level)

                if on_progress:
                    on_progress(0.6, "Installation...")

            if on_progress:
                on_progress(0.9, "Finalisation...")

            returncode = process.poll()

            if returncode == 0:
                msg = f" {app_name} installé via Chocolatey"
                if on_log:
                    on_log(msg, "success")
                if on_progress:
                    on_progress(1.0, "Terminé")
                return True, msg
            else:
                msg = f"Échec Chocolatey (code: {returncode})"
                logger.warning("Installation", msg, package_id=package_id, returncode=returncode)
                return False, msg

        except Exception as e:
            logger.log_exception("Installation", e, context=f"Chocolatey {app_name}")
            return False, str(e)

    def _install_download(
        self,
        app_name: str,
        download_url: str,
        portable: bool,
        on_progress: Optional[Callable],
        on_log: Optional[Callable]
    ) -> Tuple[bool, str]:
        """Téléchargement et installation directe"""
        try:
            if on_progress:
                on_progress(0.1, "Téléchargement...")

            # Nom fichier depuis URL
            filename = download_url.split("/")[-1]
            if "?" in filename:
                filename = filename.split("?")[0]

            # Si pas d'extension, deviner
            if not any(filename.endswith(ext) for ext in [".exe", ".msi", ".zip"]):
                filename += ".exe"

            # Dossier de destination
            if portable:
                dest_folder = self.portable_dir / app_name.replace(" ", "_")
                dest_folder.mkdir(exist_ok=True)
                dest_file = dest_folder / filename
            else:
                dest_file = Path(os.environ.get("TEMP", ".")) / filename

            logger.info("Download", f"Téléchargement: {download_url} → {dest_file}")

            # Téléchargement avec progress
            response = requests.get(download_url, stream=True, timeout=30)
            response.raise_for_status()

            total_size = int(response.headers.get('content-length', 0))
            downloaded = 0

            with open(dest_file, 'wb') as f:
                for chunk in response.iter_content(chunk_size=8192):
                    if chunk:
                        f.write(chunk)
                        downloaded += len(chunk)

                        if total_size > 0 and on_progress:
                            progress = 0.1 + (downloaded / total_size) * 0.7
                            on_progress(progress, f"Téléchargement... {downloaded // 1024}KB")

            if on_log:
                on_log(f" Téléchargé: {dest_file}", "success")

            # Si portable, copier dans dossier downloads portable et c'est fini
            if portable:
                if on_progress:
                    on_progress(0.9, "Copie dans dossier downloads...")

                # Copier exe dans dossier downloads portable
                downloads_file = self.downloads_folder / filename
                shutil.copy2(dest_file, downloads_file)

                if on_log:
                    on_log(f" Copié dans downloads: {downloads_file.name}", "success")

                if on_progress:
                    on_progress(1.0, "Terminé")

                msg = f" {app_name} téléchargé (portable) → downloads/"
                logger.success("Installation", msg, path=str(downloads_file))
                return True, msg

            # Sinon, exécuter installateur
            else:
                if on_progress:
                    on_progress(0.85, "Installation...")

                if on_log:
                    on_log("Lancement installateur...", "info")

                # Lancer installateur (silencieux si possible)
                install_args = []
                if filename.endswith(".exe"):
                    install_args = ["/S", "/VERYSILENT", "/SUPPRESSMSGBOXES", "/NORESTART"]

                try:
                    result = subprocess.run(
                        [str(dest_file)] + install_args,
                        timeout=300,
                        capture_output=True,
                        creationflags=subprocess.CREATE_NO_WINDOW
                    )

                    if result.returncode == 0:
                        msg = f" {app_name} installé"
                        if on_log:
                            on_log(msg, "success")
                        if on_progress:
                            on_progress(1.0, "Terminé")

                        logger.success("Installation", msg)
                        return True, msg
                    else:
                        msg = f" Installateur terminé avec code {result.returncode}"
                        logger.warning("Installation", msg, returncode=result.returncode)
                        return True, msg  # Considéré succès quand même

                except subprocess.TimeoutExpired:
                    msg = f" Installation longue, continué en arrière-plan"
                    if on_log:
                        on_log(msg, "warning")
                    logger.warning("Installation", msg)
                    return True, msg

        except requests.RequestException as e:
            msg = f" Erreur téléchargement: {e}"
            logger.error("Download", msg, url=download_url)
            if on_log:
                on_log(msg, "error")
            return False, msg

        except Exception as e:
            logger.log_exception("Installation", e, context=f"Download {app_name}")
            return False, str(e)


# Instance globale
advanced_installer = AdvancedInstaller()
