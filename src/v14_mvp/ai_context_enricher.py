#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Context Enricher - NiTriTe V20.0
Détection hardware + enrichissement contexte pour réponses personnalisées
"""

import os
import json
import subprocess
import platform
import re
from pathlib import Path
from typing import Dict, List, Optional
from datetime import datetime


class ContextEnricher:
    """
    Enrichit le contexte pour réponses IA ultra-personnalisées
    - Détection hardware (CPU, GPU, RAM, disques)
    - Profil utilisateur (expertise, préférences)
    - Historique problèmes/solutions
    """

    def __init__(self, profiles_dir="data/learning"):
        self.profiles_dir = Path(profiles_dir)
        self.profiles_dir.mkdir(parents=True, exist_ok=True)

        self.profile_path = self.profiles_dir / "user_profiles.json"
        self.current_profile = self.load_user_profile()

        # UI callback pour confirmations
        self.ui_confirm_callback = None

    def set_ui_callback(self, callback_func):
        """Configure callback pour confirmations UI"""
        self.ui_confirm_callback = callback_func

    def detect_full_system(self, force_rescan: bool = False) -> Optional[Dict]:
        """
        Détecte tout le système avec confirmation user

        Args:
            force_rescan: Forcer re-scan même si déjà détecté

        Returns:
            Dict avec specs complètes ou None si refusé
        """
        # Si déjà scanné et pas force_rescan
        if not force_rescan and self.current_profile.get('hardware_detected'):
            last_scan = self.current_profile.get('last_hardware_scan')
            if last_scan:
                print(f"[ContextEnricher] Hardware déjà détecté le {last_scan}")
                return self.current_profile['hardware_detected']

        # Demande confirmation (si callback configuré)
        if self.ui_confirm_callback:
            if not self.ui_confirm_callback(
                "L'agent IA souhaite scanner votre système pour des conseils personnalisés.\n\n"
                "Actions (lecture seule) :\n"
                "- Détecter CPU (wmic cpu)\n"
                "- Détecter GPU (wmic VideoController)\n"
                "- Détecter RAM (wmic memorychip)\n"
                "- Détecter disques (wmic diskdrive)\n\n"
                "Autoriser le diagnostic système ?"
            ):
                print("[ContextEnricher] Diagnostic refusé par utilisateur")
                return None
        else:
            print("[ContextEnricher] WARN: Aucun callback UI, scan sans confirmation")

        system_info = {}

        try:
            # CPU
            system_info['cpu'] = self._detect_cpu()

            # GPU
            system_info['gpu'] = self._detect_gpu()

            # RAM
            system_info['ram'] = self._detect_ram()

            # Disques
            system_info['storage'] = self._detect_storage()

            # OS
            system_info['os'] = self._detect_os()

            # Timestamp
            system_info['detected_at'] = datetime.now().isoformat()

            # Sauvegarde profil
            self.current_profile['hardware_detected'] = system_info
            self.current_profile['last_hardware_scan'] = system_info['detected_at']
            self.save_user_profile()

            print(f"[ContextEnricher] ✅ Système détecté: {system_info['cpu']['name']}, "
                  f"{system_info['ram']['total_gb']:.1f}GB RAM")

            return system_info

        except Exception as e:
            print(f"[ContextEnricher] ERROR detecting system: {e}")
            return None

    def _detect_cpu(self) -> Dict:
        """Détecte CPU via wmic"""
        try:
            output = subprocess.check_output(
                'wmic cpu get name, maxclockspeed, numberofcores, numberoflogicalprocessors',
                shell=True, text=True, timeout=5
            )

            lines = [l.strip() for l in output.strip().split('\n') if l.strip()]
            if len(lines) < 2:
                return {'name': 'Unknown CPU', 'cores': 0, 'threads': 0}

            # Parse ligne de données
            data_line = lines[1]
            parts = data_line.split()

            # Extraction intelligente
            # Format: MaxClockSpeed Name... NumberOfCores NumberOfLogicalProcessors
            max_clock = int(parts[0])
            threads = int(parts[-1])
            cores = int(parts[-2])
            name = ' '.join(parts[1:-2])

            cpu_info = {
                'name': name,
                'max_clock_mhz': max_clock,
                'cores': cores,
                'threads': threads,
                'brand': self._detect_cpu_brand(name),
                'generation': self._detect_cpu_generation(name)
            }

            return cpu_info

        except Exception as e:
            print(f"[ContextEnricher] ERROR detecting CPU: {e}")
            return {'name': 'Detection failed', 'cores': 0, 'threads': 0}

    def _detect_gpu(self) -> Dict:
        """Détecte GPU via wmic"""
        try:
            output = subprocess.check_output(
                'wmic path win32_VideoController get name, driverversion, adapterram',
                shell=True, text=True, timeout=5
            )

            lines = [l.strip() for l in output.strip().split('\n') if l.strip()]
            if len(lines) < 2:
                return None

            # Parse première carte graphique (ligne 1)
            data_line = lines[1]
            parts = data_line.split()

            # AdapterRAM est le premier nombre, DriverVersion contient points
            adapter_ram = 0
            driver_version = ""
            name_parts = []

            for part in parts:
                if part.replace('.', '').isdigit() and '.' in part:
                    driver_version = part
                elif part.isdigit() and int(part) > 1000000:  # RAM en bytes
                    adapter_ram = int(part)
                else:
                    name_parts.append(part)

            name = ' '.join(name_parts)
            vram_gb = adapter_ram / (1024**3) if adapter_ram > 0 else 0

            gpu_info = {
                'name': name,
                'vram_gb': round(vram_gb, 2),
                'driver_version': driver_version,
                'brand': self._detect_gpu_brand(name)
            }

            return gpu_info

        except Exception as e:
            print(f"[ContextEnricher] ERROR detecting GPU: {e}")
            return None

    def _detect_ram(self) -> Dict:
        """Détecte RAM via wmic"""
        try:
            output = subprocess.check_output(
                'wmic memorychip get capacity, speed',
                shell=True, text=True, timeout=5
            )

            lines = [l.strip() for l in output.strip().split('\n') if l.strip()]
            if len(lines) < 2:
                return {'total_gb': 0, 'speed_mhz': 0, 'sticks': 0}

            # Parse chaque barrette
            total_bytes = 0
            speeds = []
            stick_count = 0

            for line in lines[1:]:  # Skip header
                parts = line.split()
                if len(parts) >= 2:
                    try:
                        capacity = int(parts[0])
                        speed = int(parts[1])
                        total_bytes += capacity
                        speeds.append(speed)
                        stick_count += 1
                    except ValueError:
                        continue

            total_gb = total_bytes / (1024**3)
            avg_speed = sum(speeds) / len(speeds) if speeds else 0

            ram_info = {
                'total_gb': round(total_gb, 2),
                'speed_mhz': int(avg_speed),
                'sticks': stick_count,
                'type': self._detect_ram_type(avg_speed)
            }

            return ram_info

        except Exception as e:
            print(f"[ContextEnricher] ERROR detecting RAM: {e}")
            return {'total_gb': 0, 'speed_mhz': 0, 'sticks': 0}

    def _detect_storage(self) -> List[Dict]:
        """Détecte disques via wmic"""
        try:
            output = subprocess.check_output(
                'wmic diskdrive get model, size, interfacetype',
                shell=True, text=True, timeout=5
            )

            lines = [l.strip() for l in output.strip().split('\n') if l.strip()]
            if len(lines) < 2:
                return []

            disks = []
            for line in lines[1:]:  # Skip header
                parts = line.split()
                if len(parts) >= 2:
                    try:
                        # Dernière valeur = size (en bytes)
                        size_bytes = int(parts[-1])
                        interface = parts[-2] if len(parts) >= 3 else "Unknown"
                        model = ' '.join(parts[:-2])

                        size_gb = size_bytes / (1024**3)

                        disk_info = {
                            'model': model,
                            'size_gb': round(size_gb, 2),
                            'interface': interface,
                            'type': self._detect_disk_type(model)
                        }
                        disks.append(disk_info)
                    except ValueError:
                        continue

            return disks

        except Exception as e:
            print(f"[ContextEnricher] ERROR detecting storage: {e}")
            return []

    def _detect_os(self) -> Dict:
        """Détecte OS via platform"""
        return {
            'name': platform.system(),
            'version': platform.version(),
            'release': platform.release(),
            'architecture': platform.architecture()[0]
        }

    # Helper methods pour parsing intelligent

    def _detect_cpu_brand(self, name: str) -> str:
        """Détecte marque CPU"""
        name_lower = name.lower()
        if 'intel' in name_lower:
            return 'Intel'
        elif 'amd' in name_lower:
            return 'AMD'
        return 'Unknown'

    def _detect_cpu_generation(self, name: str) -> Optional[str]:
        """Détecte génération CPU"""
        # Intel: i9-14900K → 14th gen
        intel_match = re.search(r'i[3579]-(\d{1,2})\d{3}', name)
        if intel_match:
            gen = int(intel_match.group(1))
            return f"{gen}th Gen Intel"

        # AMD: Ryzen 9 7950X → 7000 series
        amd_match = re.search(r'ryzen.*?(\d)(\d{3})', name.lower())
        if amd_match:
            series = amd_match.group(1)
            return f"Ryzen {series}000 Series"

        return None

    def _detect_gpu_brand(self, name: str) -> str:
        """Détecte marque GPU"""
        name_lower = name.lower()
        if 'nvidia' in name_lower or 'geforce' in name_lower or 'rtx' in name_lower or 'gtx' in name_lower:
            return 'NVIDIA'
        elif 'amd' in name_lower or 'radeon' in name_lower:
            return 'AMD'
        elif 'intel' in name_lower:
            return 'Intel'
        return 'Unknown'

    def _detect_ram_type(self, speed_mhz: int) -> str:
        """Détecte type RAM selon vitesse"""
        if speed_mhz >= 4800:
            return 'DDR5'
        elif speed_mhz >= 2133:
            return 'DDR4'
        elif speed_mhz >= 800:
            return 'DDR3'
        return 'Unknown'

    def _detect_disk_type(self, model: str) -> str:
        """Détecte type disque (SSD/HDD/NVMe)"""
        model_lower = model.lower()
        if 'nvme' in model_lower or 'pcie' in model_lower:
            return 'NVMe SSD'
        elif 'ssd' in model_lower or 'solid state' in model_lower:
            return 'SATA SSD'
        else:
            return 'HDD'

    # Enrichissement contexte

    def enrich_context(self, user_message: str, conversation_history: List[Dict]) -> Dict:
        """
        Enrichit le contexte pour génération réponse

        Args:
            user_message: Message utilisateur actuel
            conversation_history: Historique [{role, content}, ...]

        Returns:
            Contexte enrichi
        """
        context = {
            'user_profile': self.current_profile,
            'hardware_detected': self.current_profile.get('hardware_detected'),
            'recent_topics': self._extract_topics(conversation_history[-10:]),
            'expertise_level': self._detect_expertise_level(conversation_history),
            'common_issues': self._get_user_patterns(),
            'conversation_length': len(conversation_history)
        }

        return context

    def _extract_topics(self, recent_messages: List[Dict]) -> List[str]:
        """Extrait topics récents de la conversation"""
        topics = []

        # Keywords importants
        topic_keywords = {
            'installation': ['installer', 'télécharger', 'setup'],
            'diagnostic': ['problème', 'erreur', 'bug', 'lent', 'crash'],
            'optimisation': ['optimiser', 'améliorer', 'accélérer', 'performance'],
            'gaming': ['jeu', 'gaming', 'fps', 'lag'],
            'backup': ['sauvegarde', 'backup', 'restaurer'],
            'drivers': ['driver', 'pilote', 'mise à jour']
        }

        for msg in recent_messages:
            content = msg.get('content', '').lower()
            for topic, keywords in topic_keywords.items():
                if any(kw in content for kw in keywords):
                    if topic not in topics:
                        topics.append(topic)

        return topics

    def _detect_expertise_level(self, conversation_history: List[Dict]) -> str:
        """
        Détecte niveau expertise utilisateur

        Returns:
            'beginner', 'intermediate', 'expert', 'power_user'
        """
        # Analyse messages utilisateur
        user_messages = [m['content'] for m in conversation_history if m.get('role') == 'user']

        if not user_messages:
            return 'intermediate'  # Default

        # Indicateurs expertise
        expert_keywords = ['powershell', 'registry', 'cmd', 'terminal', 'script', 'api', 'debug']
        beginner_keywords = ['comment', 'c\'est quoi', 'aide', 'facile', 'simple']

        expert_score = 0
        beginner_score = 0

        for msg in user_messages[-20:]:  # Derniers 20 messages
            msg_lower = msg.lower()
            expert_score += sum(1 for kw in expert_keywords if kw in msg_lower)
            beginner_score += sum(1 for kw in beginner_keywords if kw in msg_lower)

        # Classification
        if expert_score > 5:
            return 'expert'
        elif expert_score > 2:
            return 'power_user'
        elif beginner_score > 3:
            return 'beginner'
        else:
            return 'intermediate'

    def _get_user_patterns(self) -> List[str]:
        """Récupère patterns utilisateur (problèmes fréquents)"""
        return self.current_profile.get('common_patterns', [])

    # Profil utilisateur

    def load_user_profile(self) -> Dict:
        """Charge profil utilisateur depuis disque"""
        if not self.profile_path.exists():
            return self._create_default_profile()

        try:
            with open(self.profile_path, 'r', encoding='utf-8') as f:
                return json.load(f)
        except Exception as e:
            print(f"[ContextEnricher] ERROR loading profile: {e}")
            return self._create_default_profile()

    def save_user_profile(self):
        """Sauvegarde profil utilisateur"""
        try:
            with open(self.profile_path, 'w', encoding='utf-8') as f:
                json.dump(self.current_profile, f, indent=2, ensure_ascii=False)
            print(f"[ContextEnricher] Profil sauvegardé: {self.profile_path}")
        except Exception as e:
            print(f"[ContextEnricher] ERROR saving profile: {e}")

    def _create_default_profile(self) -> Dict:
        """Crée profil par défaut"""
        return {
            'version': '1.0.0',
            'created_at': datetime.now().isoformat(),
            'hardware_detected': None,
            'last_hardware_scan': None,
            'expertise_level': 'intermediate',
            'common_patterns': [],
            'preferences': {
                'detail_level': 'detailed',
                'response_format': 'markdown'
            }
        }

    def build_context_prompt(self, context: Dict) -> str:
        """
        Construit prompt enrichi pour LLM

        Args:
            context: Contexte enrichi

        Returns:
            Prompt formaté
        """
        parts = []

        # Hardware détecté
        hw = context.get('hardware_detected')
        if hw:
            parts.append(f"""
## 💻 Système Utilisateur Détecté

**CPU** : {hw['cpu']['name']} ({hw['cpu']['cores']}C/{hw['cpu']['threads']}T @ {hw['cpu']['max_clock_mhz']}MHz)
**GPU** : {hw['gpu']['name'] if hw.get('gpu') else 'Non détecté'} ({hw['gpu']['vram_gb']}GB VRAM)
**RAM** : {hw['ram']['total_gb']}GB {hw['ram']['type']} @ {hw['ram']['speed_mhz']}MHz ({hw['ram']['sticks']} barrette{'s' if hw['ram']['sticks'] > 1 else ''})
**OS** : {hw['os']['name']} {hw['os']['version']}
**Stockage** : {', '.join(f"{d['type']} {d['size_gb']}GB" for d in hw.get('storage', []))}

**⚠️ IMPORTANT : Adapte tes conseils à CE système précis.**
""")

        # Topics récents
        topics = context.get('recent_topics', [])
        if topics:
            parts.append(f"**Topics récents** : {', '.join(topics)}")

        # Expertise
        expertise = context.get('expertise_level', 'intermediate')
        expertise_descriptions = {
            'beginner': 'Débutant - Explique TOUS les termes, privilégie interface graphique',
            'intermediate': 'Intermédiaire - Mix GUI + commandes, explications moyennes',
            'expert': 'Expert - Directement technique, PowerShell/Registry OK',
            'power_user': 'Power User - Très technique, optimisations avancées'
        }
        parts.append(f"**Niveau utilisateur** : {expertise_descriptions.get(expertise, 'Intermédiaire')}")

        return '\n'.join(parts)


# Test
if __name__ == "__main__":
    print("=== Test ContextEnricher ===\n")

    enricher = ContextEnricher()

    # Test détection système (sans callback UI)
    print("Scan système (simulation)...\n")
    system_info = enricher.detect_full_system()

    if system_info:
        print("\n✅ Système détecté:")
        print(f"  CPU: {system_info['cpu']['name']}")
        print(f"  RAM: {system_info['ram']['total_gb']}GB {system_info['ram']['type']}")
        if system_info.get('gpu'):
            print(f"  GPU: {system_info['gpu']['name']}")

    # Test enrichissement contexte
    print("\n=== Test enrichissement contexte ===")
    conversation = [
        {'role': 'user', 'content': 'Mon PC est lent'},
        {'role': 'assistant', 'content': 'Je vais diagnostiquer...'},
        {'role': 'user', 'content': 'Comment optimiser gaming?'}
    ]

    context = enricher.enrich_context("Installer Chrome", conversation)
    print(f"\nTopics détectés: {context['recent_topics']}")
    print(f"Expertise: {context['expertise_level']}")

    # Test build prompt
    prompt = enricher.build_context_prompt(context)
    print(f"\n=== Prompt enrichi ===\n{prompt[:500]}...")
