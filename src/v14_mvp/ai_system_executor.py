#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
System Executor - NiTriTe V20.0
Exécution sécurisée de commandes système avec confirmation utilisateur
"""

import subprocess
import json
from pathlib import Path
from typing import Dict, Optional, List
from datetime import datetime


class SystemExecutor:
    """
    Exécuteur de commandes système sécurisé
    - Whitelist stricte de commandes safe (lecture seule)
    - Confirmation utilisateur obligatoire
    - Parsing résultats → Conseils personnalisés
    """

    # Whitelist commandes sûres (lecture seule, pas de modification système)
    SAFE_COMMANDS = {
        # === CPU ===
        'cpu_info': {
            'command': 'wmic cpu get name, maxclockspeed, numberofcores, numberoflogicalprocessors',
            'description': 'Informations processeur (nom, vitesse, cœurs)',
            'timeout': 5
        },
        'cpu_usage': {
            'command': 'wmic cpu get loadpercentage',
            'description': 'Charge CPU actuelle (%)',
            'timeout': 5
        },

        # === RAM ===
        'ram_info': {
            'command': 'wmic memorychip get capacity, speed',
            'description': 'Détails barrettes RAM (capacité, vitesse)',
            'timeout': 5
        },
        'ram_usage': {
            'command': 'wmic OS get FreePhysicalMemory, TotalVisibleMemorySize',
            'description': 'Utilisation mémoire RAM (libre/total)',
            'timeout': 5
        },

        # === GPU ===
        'gpu_info': {
            'command': 'wmic path win32_VideoController get name, driverversion, adapterram',
            'description': 'Carte graphique (modèle, driver, VRAM)',
            'timeout': 5
        },

        # === Disques ===
        'disk_info': {
            'command': 'wmic diskdrive get model, size, interfacetype',
            'description': 'Disques installés (modèle, taille, type)',
            'timeout': 5
        },
        'disk_health': {
            'command': 'wmic diskdrive get status',
            'description': 'Santé disques (OK/Degraded/Failed)',
            'timeout': 5
        },
        'disk_usage': {
            'command': 'wmic logicaldisk get name, size, freespace',
            'description': 'Espace disques logiques (C:, D:, etc.)',
            'timeout': 5
        },

        # === Système ===
        'system_info': {
            'command': 'systeminfo',
            'description': 'Informations système complètes',
            'timeout': 10
        },
        'os_version': {
            'command': 'ver',
            'description': 'Version Windows',
            'timeout': 3
        },
        'uptime': {
            'command': 'wmic os get lastbootuptime',
            'description': 'Dernière date démarrage système',
            'timeout': 5
        },

        # === Processus ===
        'process_list': {
            'command': 'tasklist',
            'description': 'Liste processus en cours',
            'timeout': 5
        },
        'process_memory': {
            'command': 'tasklist /v /fo csv',
            'description': 'Processus avec consommation mémoire',
            'timeout': 5
        },

        # === Drivers ===
        'driver_list': {
            'command': 'driverquery /v /fo csv',
            'description': 'Liste drivers installés',
            'timeout': 10
        },

        # === Réseau ===
        'network_adapters': {
            'command': 'wmic nic get name, speed, macaddress',
            'description': 'Adaptateurs réseau',
            'timeout': 5
        },
        'network_config': {
            'command': 'ipconfig /all',
            'description': 'Configuration réseau complète',
            'timeout': 5
        }
    }

    def __init__(self, ui_callback=None):
        """
        Args:
            ui_callback: Fonction pour confirmations UI
                         Signature: callback(message: str) -> bool
        """
        self.ui_callback = ui_callback

        # Logs exécutions
        self.execution_log = []

    def can_execute(self, command_key: str) -> bool:
        """Vérifie si commande est dans whitelist"""
        return command_key in self.SAFE_COMMANDS

    def get_available_commands(self) -> List[str]:
        """Liste commandes disponibles"""
        return list(self.SAFE_COMMANDS.keys())

    def get_command_description(self, command_key: str) -> Optional[str]:
        """Récupère description d'une commande"""
        cmd_data = self.SAFE_COMMANDS.get(command_key)
        return cmd_data['description'] if cmd_data else None

    def execute_with_confirmation(self, command_key: str, reason: str = "") -> Dict:
        """
        Exécute commande après confirmation utilisateur

        Args:
            command_key: Clé de commande (ex: 'cpu_info')
            reason: Raison de l'exécution (affiché à l'utilisateur)

        Returns:
            Dict avec 'success', 'output', 'error', 'cancelled'
        """
        # Vérification whitelist
        if not self.can_execute(command_key):
            return {
                'success': False,
                'error': f"Commande '{command_key}' non autorisée",
                'security_block': True
            }

        cmd_data = self.SAFE_COMMANDS[command_key]

        # Construction message confirmation
        confirmation_msg = self._build_confirmation_message(command_key, cmd_data, reason)

        # Demande confirmation (si callback configuré)
        if self.ui_callback:
            if not self.ui_callback(confirmation_msg):
                return {
                    'success': False,
                    'cancelled': True,
                    'message': 'Exécution annulée par utilisateur'
                }
        else:
            print(f"[SystemExecutor] WARN: Pas de callback UI, exécution sans confirmation")

        # Exécution
        result = self._execute_safe(command_key, cmd_data)

        # Log
        self.execution_log.append({
            'timestamp': datetime.now().isoformat(),
            'command_key': command_key,
            'reason': reason,
            'success': result.get('success', False)
        })

        return result

    def _build_confirmation_message(self, command_key: str, cmd_data: Dict, reason: str) -> str:
        """Construit message de confirmation utilisateur"""
        msg = f"""L'agent IA souhaite exécuter un diagnostic système.

📋 **Diagnostic** : {cmd_data['description']}

💻 **Commande** : {cmd_data['command']}

🎯 **Raison** : {reason if reason else 'Diagnostic général'}

✅ Cette commande est sûre et en lecture seule (aucune modification système).

⏱️ Durée : ~{cmd_data['timeout']} secondes

Autoriser l'exécution ?
"""
        return msg

    def _execute_safe(self, command_key: str, cmd_data: Dict) -> Dict:
        """Exécute commande de manière sécurisée"""
        try:
            output = subprocess.check_output(
                cmd_data['command'],
                shell=True,
                text=True,
                timeout=cmd_data['timeout'],
                stderr=subprocess.STDOUT
            )

            return {
                'success': True,
                'output': output,
                'command_key': command_key,
                'executed_at': datetime.now().isoformat()
            }

        except subprocess.TimeoutExpired:
            return {
                'success': False,
                'error': f"Timeout ({cmd_data['timeout']}s dépassé)",
                'timeout': True
            }

        except subprocess.CalledProcessError as e:
            return {
                'success': False,
                'error': f"Erreur exécution: {e.output}",
                'exit_code': e.returncode
            }

        except Exception as e:
            return {
                'success': False,
                'error': f"Erreur inattendue: {str(e)}"
            }

    # === Parsing & Conseils ===

    def parse_and_advise(self, command_key: str, output: str) -> Dict:
        """
        Parse résultat et génère conseils personnalisés

        Args:
            command_key: Commande exécutée
            output: Sortie brute

        Returns:
            Dict avec 'parsed_data', 'advice', 'severity'
        """
        parsers = {
            'cpu_info': self._parse_cpu_info,
            'cpu_usage': self._parse_cpu_usage,
            'ram_usage': self._parse_ram_usage,
            'disk_usage': self._parse_disk_usage,
            'process_memory': self._parse_process_memory,
            'uptime': self._parse_uptime
        }

        if command_key not in parsers:
            return {
                'parsed_data': None,
                'raw_output': output,
                'advice': 'Résultat brut (aucun parser disponible)'
            }

        # Parse
        parsed = parsers[command_key](output)

        # Génère conseils
        advice = self._generate_advice(command_key, parsed)

        return {
            'parsed_data': parsed,
            'advice': advice,
            'severity': self._detect_severity(command_key, parsed)
        }

    def _parse_cpu_usage(self, output: str) -> Optional[Dict]:
        """Parse wmic cpu get loadpercentage"""
        try:
            lines = [l.strip() for l in output.strip().split('\n') if l.strip()]
            if len(lines) < 2:
                return None

            load_percent = int(lines[1])

            return {
                'load_percent': load_percent,
                'status': 'high' if load_percent > 80 else 'normal'
            }
        except:
            return None

    def _parse_ram_usage(self, output: str) -> Optional[Dict]:
        """Parse wmic OS get FreePhysicalMemory, TotalVisibleMemorySize"""
        try:
            lines = [l.strip() for l in output.strip().split('\n') if l.strip()]
            if len(lines) < 2:
                return None

            parts = lines[1].split()
            free_kb = int(parts[0])
            total_kb = int(parts[1])

            used_kb = total_kb - free_kb
            usage_percent = (used_kb / total_kb) * 100

            return {
                'free_gb': free_kb / (1024**2),
                'total_gb': total_kb / (1024**2),
                'used_gb': used_kb / (1024**2),
                'usage_percent': usage_percent,
                'status': 'critical' if usage_percent > 90 else 'high' if usage_percent > 70 else 'normal'
            }
        except:
            return None

    def _parse_disk_usage(self, output: str) -> Optional[List[Dict]]:
        """Parse wmic logicaldisk get name, size, freespace"""
        try:
            lines = [l.strip() for l in output.strip().split('\n') if l.strip()]
            if len(lines) < 2:
                return None

            disks = []
            for line in lines[1:]:
                parts = line.split()
                if len(parts) >= 3:
                    free_bytes = int(parts[0])
                    name = parts[1]
                    size_bytes = int(parts[2])

                    used_bytes = size_bytes - free_bytes
                    usage_percent = (used_bytes / size_bytes) * 100 if size_bytes > 0 else 0

                    disks.append({
                        'name': name,
                        'total_gb': size_bytes / (1024**3),
                        'free_gb': free_bytes / (1024**3),
                        'used_gb': used_bytes / (1024**3),
                        'usage_percent': usage_percent,
                        'status': 'critical' if usage_percent > 90 else 'warning' if usage_percent > 80 else 'ok'
                    })

            return disks
        except:
            return None

    def _parse_process_memory(self, output: str) -> Optional[List[Dict]]:
        """Parse tasklist /v /fo csv (top 10 processus gourmands)"""
        try:
            import csv
            from io import StringIO

            reader = csv.DictReader(StringIO(output))
            processes = []

            for row in reader:
                try:
                    mem_str = row.get('Mem Usage', '0 K').replace(',', '').replace(' K', '').replace(' ', '')
                    mem_kb = int(mem_str)

                    processes.append({
                        'name': row.get('Image Name', 'Unknown'),
                        'pid': row.get('PID', '0'),
                        'memory_kb': mem_kb,
                        'memory_mb': mem_kb / 1024,
                        'status': row.get('Status', 'Unknown')
                    })
                except:
                    continue

            # Tri par mémoire décroissante, top 10
            processes.sort(key=lambda p: p['memory_kb'], reverse=True)
            return processes[:10]

        except:
            return None

    def _parse_uptime(self, output: str) -> Optional[Dict]:
        """Parse wmic os get lastbootuptime"""
        try:
            lines = [l.strip() for l in output.strip().split('\n') if l.strip()]
            if len(lines) < 2:
                return None

            # Format: 20241227094523.500000+060
            boot_str = lines[1].split('.')[0]  # Ignore millisecondes

            # Parse: YYYYMMDDHHmmss
            year = int(boot_str[0:4])
            month = int(boot_str[4:6])
            day = int(boot_str[6:8])
            hour = int(boot_str[8:10])
            minute = int(boot_str[10:12])
            second = int(boot_str[12:14])

            boot_time = datetime(year, month, day, hour, minute, second)
            uptime_seconds = (datetime.now() - boot_time).total_seconds()
            uptime_days = uptime_seconds / 86400

            return {
                'boot_time': boot_time.isoformat(),
                'uptime_seconds': uptime_seconds,
                'uptime_days': uptime_days,
                'uptime_hours': uptime_seconds / 3600,
                'status': 'long' if uptime_days > 7 else 'normal'
            }
        except:
            return None

    def _parse_cpu_info(self, output: str) -> Optional[Dict]:
        """Parse wmic cpu info"""
        # Déjà fait dans context_enricher, retour simple
        return {'raw': output}

    # === Génération Conseils ===

    def _generate_advice(self, command_key: str, parsed_data: Optional[Dict]) -> str:
        """Génère conseils selon résultats diagnostic"""
        if not parsed_data:
            return "❌ Impossible d'analyser les résultats"

        advisors = {
            'cpu_usage': self._advise_cpu_usage,
            'ram_usage': self._advise_ram_usage,
            'disk_usage': self._advise_disk_usage,
            'process_memory': self._advise_process_memory,
            'uptime': self._advise_uptime
        }

        if command_key in advisors:
            return advisors[command_key](parsed_data)

        return "✅ Diagnostic effectué avec succès"

    def _advise_cpu_usage(self, data: Dict) -> str:
        """Conseils selon charge CPU"""
        load = data['load_percent']

        if load > 90:
            return f"""
⚠️ **CPU Critique** : {load}% de charge

**Actions Immédiates** :
1. Ouvrir Gestionnaire Tâches (Ctrl+Shift+Esc)
2. Trier par "CPU"
3. Identifier processus gourmand (>30%)
4. Fermer si non essentiel

**NiTriTe** :
- Diagnostic → HWMonitor (vérifier température)
- Si >80°C : Problème refroidissement
"""
        elif load > 70:
            return f"⚠️ **CPU Élevé** : {load}% - Normal si tâche lourde en cours. Surveiller si permanent."
        else:
            return f"✅ **CPU Normal** : {load}%"

    def _advise_ram_usage(self, data: Dict) -> str:
        """Conseils selon utilisation RAM"""
        usage = data['usage_percent']
        used_gb = data['used_gb']
        total_gb = data['total_gb']

        if usage > 90:
            return f"""
⚠️ **RAM Critique** : {usage:.1f}% ({used_gb:.1f}/{total_gb:.1f} GB)

**Actions Immédiates** :
1. Fermer applications inutilisées
2. NiTriTe → Optimisations → Nettoyage mémoire
3. Redémarrer PC si uptime > 7 jours

**Solutions Long Terme** :
- Upgrade RAM (minimum 16GB recommandé)
- NiTriTe → Scripts Windows → Optimisation RAM
- Désactiver démarrage auto apps lourdes
"""
        elif usage > 70:
            return f"""
⚠️ **RAM Élevée** : {usage:.1f}% ({used_gb:.1f}/{total_gb:.1f} GB)

Normal si multitâche intensif. Surveiller si ralentissements.

**Optimisations NiTriTe** :
- Optimisations → Désactiver services inutiles
- Scripts Windows → Nettoyage processus
"""
        else:
            return f"✅ **RAM OK** : {usage:.1f}% ({used_gb:.1f}/{total_gb:.1f} GB)"

    def _advise_disk_usage(self, data: List[Dict]) -> str:
        """Conseils selon espace disques"""
        advices = []

        for disk in data:
            name = disk['name']
            usage = disk['usage_percent']
            free_gb = disk['free_gb']

            if usage > 90:
                advices.append(f"""
⚠️ **{name} Critique** : {usage:.1f}% plein ({free_gb:.1f} GB libres)

**Actions** :
1. NiTriTe → Optimisations → Nettoyage disque
2. Vider Corbeille
3. Désinstaller apps inutilisées
4. NiTriTe → Scripts Windows → Nettoyage Windows.old
""")
            elif usage > 80:
                advices.append(f"⚠️ **{name}** : {usage:.1f}% plein - Nettoyage recommandé")
            else:
                advices.append(f"✅ **{name}** : {usage:.1f}% ({free_gb:.1f} GB libres)")

        return '\n\n'.join(advices)

    def _advise_process_memory(self, data: List[Dict]) -> str:
        """Conseils selon processus gourmands"""
        top_5 = data[:5]

        advice = "### 🔝 Top 5 Processus Gourmands (RAM)\n\n"

        for i, proc in enumerate(top_5, 1):
            advice += f"{i}. **{proc['name']}** : {proc['memory_mb']:.1f} MB\n"

        advice += "\n**Conseil** : Fermez les applications non essentielles (Chrome, Discord, etc.)\n"
        advice += "**NiTriTe** : Optimisations → Désactiver services inutiles"

        return advice

    def _advise_uptime(self, data: Dict) -> str:
        """Conseils selon uptime"""
        days = data['uptime_days']

        if days > 14:
            return f"""
⚠️ **Uptime Très Long** : {days:.1f} jours sans redémarrage

**Recommandation** : Redémarrer PC pour :
- Appliquer mises à jour Windows
- Nettoyer mémoire RAM
- Réinitialiser services système

**Action** : Redémarrer maintenant si possible
"""
        elif days > 7:
            return f"⚠️ **Uptime Long** : {days:.1f} jours - Redémarrage recommandé bientôt"
        else:
            return f"✅ **Uptime Normal** : {days:.1f} jours"

    def _detect_severity(self, command_key: str, parsed_data: Optional[Dict]) -> str:
        """Détecte sévérité (info, warning, critical)"""
        if not parsed_data:
            return 'unknown'

        # CPU
        if command_key == 'cpu_usage':
            load = parsed_data.get('load_percent', 0)
            if load > 90:
                return 'critical'
            elif load > 70:
                return 'warning'

        # RAM
        if command_key == 'ram_usage':
            usage = parsed_data.get('usage_percent', 0)
            if usage > 90:
                return 'critical'
            elif usage > 70:
                return 'warning'

        # Disques
        if command_key == 'disk_usage':
            for disk in parsed_data:
                if disk['usage_percent'] > 90:
                    return 'critical'
                elif disk['usage_percent'] > 80:
                    return 'warning'

        # Uptime
        if command_key == 'uptime':
            days = parsed_data.get('uptime_days', 0)
            if days > 14:
                return 'warning'

        return 'info'


# Test
if __name__ == "__main__":
    print("=== Test SystemExecutor ===\n")

    # Callback UI simulation
    def mock_ui_callback(message):
        print(f"\n[UI CONFIRMATION]\n{message}")
        return True  # Auto-accept pour test

    executor = SystemExecutor(ui_callback=mock_ui_callback)

    # Test 1 : RAM usage
    print("=== Test 1 : Diagnostic RAM ===")
    result = executor.execute_with_confirmation(
        'ram_usage',
        reason='Diagnostiquer problème de lenteur'
    )

    if result.get('success'):
        print("\n✅ Exécution réussie")
        parsed = executor.parse_and_advise('ram_usage', result['output'])
        print(f"\nDonnées parsées: {parsed['parsed_data']}")
        print(f"\n{parsed['advice']}")
    else:
        print(f"❌ Erreur: {result.get('error')}")

    # Test 2 : Liste commandes disponibles
    print("\n\n=== Commandes Disponibles ===")
    for cmd_key in executor.get_available_commands()[:5]:
        desc = executor.get_command_description(cmd_key)
        print(f"- {cmd_key}: {desc}")
