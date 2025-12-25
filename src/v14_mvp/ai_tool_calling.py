#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Tool Calling System pour AI Agent
Permet à l'agent IA de proposer et exécuter des commandes système
AVEC CONFIRMATION OBLIGATOIRE de l'utilisateur pour sécurité
"""

import subprocess
import platform
import re
from typing import Dict, List, Tuple, Optional
from tkinter import messagebox

class ToolCallSystem:
    """
    Système de tool calling pour exécuter des commandes système proposées par l'IA
    Sécurité: Confirmation utilisateur OBLIGATOIRE avant exécution
    """

    def __init__(self):
        self.is_windows = platform.system() == "Windows"

        # Commandes sûres (whitelist)
        self.safe_commands = {
            # Diagnostic
            "systeminfo": {"safe": True, "description": "Afficher informations système"},
            "tasklist": {"safe": True, "description": "Liste processus actifs"},
            "ipconfig": {"safe": True, "description": "Configuration réseau"},
            "netstat": {"safe": True, "description": "Connexions réseau actives"},
            "ping": {"safe": True, "description": "Test connectivité réseau"},
            "tracert": {"safe": True, "description": "Tracer route réseau"},
            "nslookup": {"safe": True, "description": "Requête DNS"},
            "wmic": {"safe": True, "description": "WMI info (CPU, RAM, GPU, etc.)"},
            "powercfg": {"safe": True, "description": "Configuration alimentation"},
            "sfc": {"safe": False, "description": "Scan fichiers système (admin required)", "requires_admin": True},
            "DISM": {"safe": False, "description": "Réparation image Windows (admin required)", "requires_admin": True},
            "chkdsk": {"safe": False, "description": "Vérification disque (admin required)", "requires_admin": True},

            # Gestion
            "dir": {"safe": True, "description": "Lister fichiers/dossiers"},
            "ls": {"safe": True, "description": "Lister fichiers (PowerShell)"},
            "Get-Process": {"safe": True, "description": "Liste processus (PowerShell)"},
            "Get-Service": {"safe": True, "description": "Liste services (PowerShell)"},
            "Get-NetAdapter": {"safe": True, "description": "Adapters réseau (PowerShell)"},

            # Nettoyage
            "cleanmgr": {"safe": True, "description": "Nettoyage disque"},
            "defrag": {"safe": False, "description": "Défragmentation (admin required)", "requires_admin": True},
        }

        # Commandes DANGEREUSES (blacklist absolue)
        self.dangerous_commands = [
            "del", "rm", "rmdir", "format", "fdisk", "diskpart",
            "shutdown", "restart", "reboot", "taskkill",
            "reg delete", "Remove-Item", "Remove-ItemProperty",
            "net user", "net localgroup", "takeown", "icacls",
        ]

        # Historique des commandes exécutées
        self.execution_history = []

    def parse_ai_response_for_commands(self, ai_response: str) -> List[Dict[str, str]]:
        """
        Parser la réponse de l'IA pour extraire les commandes proposées

        Recherche des patterns:
        - Commandes en code blocks ```cmd ou ```powershell
        - Lignes commençant par $ ou >
        - Format explicite "Exécuter: commande"

        Returns:
            Liste de dicts {command, type, description}
        """
        commands = []

        # Pattern 1: Code blocks
        code_block_pattern = r'```(?:cmd|powershell|bash)?\s*\n(.*?)\n```'
        code_blocks = re.findall(code_block_pattern, ai_response, re.DOTALL | re.IGNORECASE)

        for block in code_blocks:
            lines = block.strip().split('\n')
            for line in lines:
                line = line.strip()
                if line and not line.startswith('#'):  # Ignorer commentaires
                    commands.append({
                        "command": line,
                        "type": "code_block",
                        "description": "Commande suggérée par l'IA"
                    })

        # Pattern 2: Lignes avec > ou $
        prompt_pattern = r'^[\$>]\s*(.+)$'
        lines = ai_response.split('\n')
        for line in lines:
            match = re.match(prompt_pattern, line.strip())
            if match:
                command = match.group(1).strip()
                if command:
                    commands.append({
                        "command": command,
                        "type": "inline",
                        "description": "Commande inline"
                    })

        # Pattern 3: "Exécuter: ..."
        execute_pattern = r'(?:Exécuter|Execute|Run):\s*`?([^`\n]+)`?'
        matches = re.findall(execute_pattern, ai_response, re.IGNORECASE)
        for match in matches:
            commands.append({
                "command": match.strip(),
                "type": "explicit",
                "description": "Commande explicite"
            })

        return commands

    def is_command_safe(self, command: str) -> Tuple[bool, str]:
        """
        Vérifier si une commande est sûre à exécuter

        Returns:
            (is_safe, reason)
        """
        command_lower = command.lower().strip()

        # Check blacklist
        for dangerous in self.dangerous_commands:
            if dangerous.lower() in command_lower:
                return (False, f"❌ Commande dangereuse détectée: '{dangerous}' - REFUSÉE pour sécurité")

        # Vérifier caractères suspects
        suspicious_chars = [';', '&&', '||', '|', '>', '>>', '<']
        for char in suspicious_chars:
            if char in command and char not in command_lower.replace('ipconfig', ''):  # Exception ipconfig /all
                return (False, f"⚠️ Caractère suspect '{char}' détecté - Chaînage de commandes non autorisé")

        # Extraire commande de base
        base_command = command.split()[0] if command.split() else ""

        # Check whitelist
        for safe_cmd, info in self.safe_commands.items():
            if base_command.lower().startswith(safe_cmd.lower()):
                if info.get("requires_admin") and not self._is_admin():
                    return (False, f"⚠️ Cette commande nécessite les droits administrateur")
                return (True, f"✅ Commande vérifiée: {info['description']}")

        # Commande inconnue = prudence
        return (False, f"⚠️ Commande non reconnue - Par sécurité, demander confirmation manuelle")

    def _is_admin(self) -> bool:
        """Vérifier si le processus a les droits admin"""
        try:
            import ctypes
            return ctypes.windll.shell32.IsUserAnAdmin() != 0
        except:
            return False

    def execute_command(self, command: str, shell_type: str = "cmd") -> Dict[str, any]:
        """
        Exécuter une commande système

        Args:
            command: Commande à exécuter
            shell_type: "cmd" ou "powershell"

        Returns:
            Dict avec stdout, stderr, returncode, success
        """
        try:
            if shell_type == "powershell":
                full_command = ["powershell", "-Command", command]
            else:
                full_command = command

            result = subprocess.run(
                full_command,
                capture_output=True,
                text=True,
                timeout=30,  # Timeout 30s pour sécurité
                shell=(shell_type == "cmd")
            )

            # Log dans historique
            self.execution_history.append({
                "command": command,
                "shell": shell_type,
                "success": result.returncode == 0,
                "output_length": len(result.stdout)
            })

            return {
                "stdout": result.stdout,
                "stderr": result.stderr,
                "returncode": result.returncode,
                "success": result.returncode == 0
            }

        except subprocess.TimeoutExpired:
            return {
                "stdout": "",
                "stderr": "❌ Commande timeout après 30 secondes",
                "returncode": -1,
                "success": False
            }
        except Exception as e:
            return {
                "stdout": "",
                "stderr": f"❌ Erreur exécution: {str(e)}",
                "returncode": -1,
                "success": False
            }

    def propose_and_execute_with_confirmation(
        self,
        commands: List[Dict[str, str]],
        callback_ui=None
    ) -> List[Dict]:
        """
        Proposer les commandes à l'utilisateur et exécuter après confirmation

        Args:
            commands: Liste des commandes à proposer
            callback_ui: Fonction callback pour UI (tkinter messagebox par défaut)

        Returns:
            Liste des résultats d'exécution
        """
        results = []

        for cmd_info in commands:
            command = cmd_info["command"]

            # Vérifier sécurité
            is_safe, safety_msg = self.is_command_safe(command)

            # Préparer message de confirmation
            confirmation_msg = f"""
🤖 L'agent IA suggère d'exécuter cette commande:

📝 Commande: {command}

{safety_msg}

Voulez-vous exécuter cette commande?
(Les résultats seront affichés après exécution)
"""

            # Demander confirmation utilisateur
            if callback_ui:
                user_approved = callback_ui(confirmation_msg, command, is_safe)
            else:
                user_approved = messagebox.askyesno(
                    "⚠️ Confirmation d'exécution",
                    confirmation_msg,
                    icon='warning' if not is_safe else 'question'
                )

            if user_approved:
                # Déterminer shell type
                shell_type = "powershell" if "Get-" in command or "Set-" in command else "cmd"

                # Exécuter
                result = self.execute_command(command, shell_type)
                result["command"] = command
                result["user_approved"] = True
                results.append(result)
            else:
                results.append({
                    "command": command,
                    "user_approved": False,
                    "stdout": "",
                    "stderr": "❌ Exécution refusée par l'utilisateur",
                    "success": False
                })

        return results

    def get_execution_stats(self) -> Dict:
        """Statistiques d'exécution"""
        total = len(self.execution_history)
        successful = sum(1 for ex in self.execution_history if ex["success"])

        return {
            "total_executions": total,
            "successful": successful,
            "failed": total - successful,
            "success_rate": (successful / total * 100) if total > 0 else 0
        }


# Test simple
if __name__ == "__main__":
    tool_system = ToolCallSystem()

    # Test parsing
    test_response = """
Pour diagnostiquer ce problème, exécutez:

```cmd
systeminfo
```

Et aussi:
```powershell
Get-NetAdapter | Where-Object {$_.Status -eq "Up"}
```

Exécuter: `ipconfig /all`
"""

    commands = tool_system.parse_ai_response_for_commands(test_response)
    print(f"Commandes détectées: {len(commands)}\n")

    for cmd in commands:
        print(f"Commande: {cmd['command']}")
        is_safe, msg = tool_system.is_command_safe(cmd['command'])
        print(f"  Sécurité: {msg}\n")
