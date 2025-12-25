#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Module d'Installation Amélioré - NiTriTe V17
Avec support des logs en temps réel
"""

import subprocess
import threading
from typing import Callable, Optional
import time
from v14_mvp.logger_system import logger


class EnhancedInstallationManager:
    """Gestionnaire d'installations avec logs en temps réel"""

    def __init__(self):
        self.winget_available = self._check_winget()
        self.chocolatey_available = self._check_chocolatey()

    def _check_winget(self) -> bool:
        """Vérifier si WinGet est disponible"""
        try:
            result = subprocess.run(
                ["winget", "--version"],
                capture_output=True,
                text=True,
                timeout=5
            )
            return result.returncode == 0
        except:
            return False

    def _check_chocolatey(self) -> bool:
        """Vérifier si Chocolatey est disponible"""
        try:
            result = subprocess.run(
                ["choco", "--version"],
                capture_output=True,
                text=True,
                timeout=5
            )
            return result.returncode == 0
        except:
            return False

    def install_app(
        self,
        app_name: str,
        package_id: Optional[str] = None,
        method: str = "winget",
        on_progress: Optional[Callable[[float, str], None]] = None,
        on_log: Optional[Callable[[str, str], None]] = None,
        on_complete: Optional[Callable[[bool, str], None]] = None
    ):
        """
        Installer une application avec logs en temps réel

        Args:
            app_name: Nom de l'application
            package_id: ID du package
            method: "winget", "chocolatey" ou "download"
            on_progress: Callback (value 0-1, status_text)
            on_log: Callback (message, level) - level: "info"|"success"|"error"|"warning"
            on_complete: Callback (success, message)
        """
        thread = threading.Thread(
            target=self._install_app_thread,
            args=(app_name, package_id, method, on_progress, on_log, on_complete),
            daemon=True
        )
        thread.start()

    def _install_app_thread(
        self,
        app_name: str,
        package_id: Optional[str],
        method: str,
        on_progress: Optional[Callable],
        on_log: Optional[Callable],
        on_complete: Optional[Callable]
    ):
        """Thread d'installation"""
        try:
            logger.info("Installation", f"Démarrage installation: {app_name}",
                       method=method, package_id=package_id or "N/A")

            if on_log:
                on_log(f"Démarrage installation de {app_name}", "info")

            if on_progress:
                on_progress(0.1, f"Recherche de {app_name}...")

            if method == "winget":
                success, message = self._install_with_winget(
                    app_name, package_id, on_progress, on_log
                )
            elif method == "chocolatey":
                success, message = self._install_with_chocolatey(
                    app_name, package_id, on_progress, on_log
                )
            else:
                success = False
                message = f"Méthode inconnue: {method}"
                logger.error("Installation", f"Méthode inconnue: {method}", app=app_name)

            if success:
                logger.success("Installation", f"{app_name} installé avec succès", method=method)
            else:
                logger.error("Installation", f"Échec installation {app_name}: {message}",
                           method=method, package_id=package_id or "N/A")

            if on_complete:
                on_complete(success, message)

        except Exception as e:
            logger.log_exception("Installation", e, f"Installation de {app_name}")
            if on_log:
                on_log(f"ERREUR FATALE: {str(e)}", "error")
            if on_complete:
                on_complete(False, f"Erreur: {str(e)}")

    def _install_with_winget(
        self,
        app_name: str,
        package_id: Optional[str],
        on_progress: Optional[Callable],
        on_log: Optional[Callable]
    ) -> tuple[bool, str]:
        """Installation via WinGet avec logs"""
        if not self.winget_available:
            if on_log:
                on_log("WinGet n'est pas disponible sur ce système", "error")
            return False, "WinGet non disponible"

        try:
            search_term = package_id or app_name

            if on_log:
                on_log(f"Recherche du package: {search_term}", "info")

            if on_progress:
                on_progress(0.2, "Préparation de l'installation...")

            # Commande WinGet - utiliser --id pour recherche précise par ID
            # IMPORTANT: On essaie d'abord SANS --scope pour laisser WinGet décider
            # Certains packages nécessitent machine scope, d'autres user scope
            cmd = [
                "winget", "install",
                "--id", search_term,
                "--exact",
                "--silent",
                "--accept-source-agreements",
                "--accept-package-agreements",
                "--disable-interactivity"
            ]

            cmd_str = " ".join(cmd)
            logger.info("WinGet", f"Commande: {cmd_str}", app=app_name, package_id=search_term)

            if on_log:
                on_log(f"Commande: winget install --id \"{search_term}\" --exact --silent", "info")

            if on_progress:
                on_progress(0.3, "Installation en cours...")

            # Exécuter avec capture en temps réel
            process = subprocess.Popen(
                cmd,
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                text=True,
                bufsize=1,
                universal_newlines=True
            )

            # Lire sortie en temps réel
            stdout_lines = []
            while True:
                output = process.stdout.readline()
                if output == '' and process.poll() is not None:
                    break
                if output:
                    line = output.strip()
                    stdout_lines.append(line)
                    if line and on_log:
                        # Détecter le niveau de log
                        if "error" in line.lower() or "failed" in line.lower() or "no package found" in line.lower():
                            on_log(line, "error")
                        elif "success" in line.lower() or "installed" in line.lower() or "successfully" in line.lower():
                            on_log(line, "success")
                        elif "warning" in line.lower():
                            on_log(line, "warning")
                        elif "downloading" in line.lower() or "installing" in line.lower():
                            on_log(line, "info")

                if on_progress:
                    on_progress(0.6, "Installation en cours...")

            # Lire stderr
            stderr = process.stderr.read()
            stderr_lines = []
            if stderr:
                for line in stderr.split('\n'):
                    if line.strip():
                        stderr_lines.append(line.strip())
                        if on_log:
                            on_log(line.strip(), "error")

            if on_progress:
                on_progress(0.9, "Finalisation...")

            returncode = process.poll()

            # Logger tous les détails
            logger.info("WinGet", f"Installation terminée: code retour = {returncode}",
                       app=app_name,
                       returncode=returncode,
                       returncode_hex=f"{returncode:#x}" if returncode else "0x0",
                       stdout_lines_count=len(stdout_lines),
                       stderr_lines_count=len(stderr_lines))

            # Logger stdout complet
            if stdout_lines:
                logger.debug("WinGet", f"Sortie stdout ({len(stdout_lines)} lignes)",
                            app=app_name,
                            stdout="\n".join(stdout_lines))

            # Logger stderr complet
            if stderr_lines:
                logger.warning("WinGet", f"Sortie stderr ({len(stderr_lines)} lignes)",
                              app=app_name,
                              stderr="\n".join(stderr_lines))

            # Vérifier le code de retour
            if returncode == 0:
                logger.success("WinGet", f"{app_name} installé avec succès")
                if on_log:
                    on_log(f"✓ {app_name} installé avec succès", "success")
                if on_progress:
                    on_progress(1.0, "Terminé")
                return True, f"✓ {app_name} installé"
            else:
                # Analyser les codes d'erreur WinGet
                error_msg = f"Échec installation (code: {returncode:#x})"

                # Codes d'erreur WinGet communs
                error_codes = {
                    -1978335212: "Package introuvable (0x8A150014)",
                    2316632084: "Package introuvable (0x8A150014)",
                    -1978335192: "Aucune version applicable (0x8A150028)",
                    -1978335191: "Installation nécessite admin (0x8A150029)",
                    -1978335189: "Installation annulée (0x8A15002B)",
                    -1978335148: "Échec du téléchargement (0x8A150054)",
                    -1978335189: "Accord de licence non accepté (0x8A15002B)",
                    -2147023673: "Accès refusé - Admin requis (0x80070005)",
                }

                error_code_hex = f"{returncode:#x}" if returncode else "0x0"

                # Vérifier les codes d'erreur connus
                if returncode in error_codes:
                    error_msg = f"✗ {error_codes[returncode]}"
                    logger.error("WinGet", f"Erreur connue: {error_msg}",
                                app=app_name,
                                package_id=search_term,
                                returncode=returncode,
                                error_code_hex=error_code_hex)

                    if on_log:
                        on_log(error_msg, "error")

                        # Suggestions selon l'erreur
                        if "introuvable" in error_msg.lower():
                            on_log("💡 Vérifiez l'ID du package avec: winget search \"" + app_name + "\"", "info")
                        elif "admin" in error_msg.lower() or "accès" in error_msg.lower():
                            on_log("💡 Cette application nécessite des privilèges administrateur", "warning")
                            on_log("💡 Relancez NiTriTe en tant qu'administrateur", "info")
                        elif "téléchargement" in error_msg.lower():
                            on_log("💡 Vérifiez votre connexion Internet", "info")
                elif stderr_lines:
                    # Utiliser le message d'erreur de stderr
                    error_msg = f"✗ {stderr_lines[-1]}"
                    logger.error("WinGet", f"Erreur installation: {error_msg}",
                                app=app_name,
                                package_id=search_term,
                                returncode=returncode,
                                error_code_hex=error_code_hex,
                                stderr="\n".join(stderr_lines[-5:]))
                else:
                    # Erreur générique
                    logger.error("WinGet", f"Erreur installation: code {error_code_hex}",
                                app=app_name,
                                package_id=search_term,
                                returncode=returncode,
                                error_code_hex=error_code_hex)

                if on_log:
                    on_log(error_msg, "error")
                    on_log(f"Code d'erreur: {error_code_hex}", "info")

                return False, error_msg

        except Exception as e:
            logger.log_exception("WinGet", e, f"Installation WinGet de {app_name} (package: {package_id})")
            if on_log:
                on_log(f"EXCEPTION: {str(e)}", "error")
            return False, f"Erreur: {str(e)}"

    def _install_with_chocolatey(
        self,
        app_name: str,
        package_id: Optional[str],
        on_progress: Optional[Callable],
        on_log: Optional[Callable]
    ) -> tuple[bool, str]:
        """Installation via Chocolatey avec logs"""
        if not self.chocolatey_available:
            if on_log:
                on_log("Chocolatey n'est pas disponible", "error")
            return False, "Chocolatey non disponible"

        try:
            search_term = package_id or app_name

            if on_log:
                on_log(f"Installation via Chocolatey: {search_term}", "info")

            if on_progress:
                on_progress(0.2, "Préparation...")

            cmd = [
                "choco", "install", search_term,
                "-y",
                "--no-progress"
            ]

            if on_log:
                on_log(f"Commande: {' '.join(cmd)}", "info")

            if on_progress:
                on_progress(0.3, "Installation en cours...")

            process = subprocess.Popen(
                cmd,
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                text=True,
                bufsize=1,
                universal_newlines=True
            )

            # Lire sortie en temps réel
            while True:
                output = process.stdout.readline()
                if output == '' and process.poll() is not None:
                    break
                if output and on_log:
                    line = output.strip()
                    if line:
                        if "error" in line.lower():
                            on_log(line, "error")
                        elif "success" in line.lower():
                            on_log(line, "success")
                        elif "warning" in line.lower():
                            on_log(line, "warning")
                        else:
                            on_log(line, "info")

                if on_progress:
                    on_progress(0.6, "Installation...")

            stderr = process.stderr.read()
            if stderr and on_log:
                for line in stderr.split('\n'):
                    if line.strip():
                        on_log(line.strip(), "error")

            if on_progress:
                on_progress(0.9, "Finalisation...")

            returncode = process.poll()

            if returncode == 0:
                if on_log:
                    on_log(f"✓ {app_name} installé avec succès", "success")
                if on_progress:
                    on_progress(1.0, "Terminé")
                return True, f"✓ {app_name} installé"
            else:
                if on_log:
                    on_log(f"✗ Échec (code {returncode})", "error")
                return False, f"Échec (code {returncode})"

        except Exception as e:
            if on_log:
                on_log(f"EXCEPTION: {str(e)}", "error")
            return False, f"Erreur: {str(e)}"


# Instance globale
installer = EnhancedInstallationManager()
