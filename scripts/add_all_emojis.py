#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Script automatique pour ajouter TOUS les emojis dans pages_full.py
70+ modifications en une seule exécution
"""

import re

# Dictionnaire de tous les remplacements à faire
REPLACEMENTS = [
    # Cartes Statistiques Diagnostic
    ('"CPU"', '"🖥️ CPU"'),
    ('"RAM"', '"💾 RAM"'),
    ('"Disque"', '"💿 Disque"'),
    ('"Réseau"', '"🌐 Réseau"'),

    # Headers de Sections
    ('" Système"', '"💻 Système"'),
    ('" Matériel"', '"🔧 Matériel"'),
    ('" Stockage"', '"💿 Stockage"'),
    #('" Réseau"', '"🌐 Réseau"'),  # Déjà fait ci-dessus
    ('" Outils de Diagnostic"', '"🔧 Outils de Diagnostic"'),

    # Labels Section Matériel
    ('"Processeur"', '"🖥️ Processeur"'),
    ('"Configuration CPU"', '"⚙️ Configuration CPU"'),
    ('"Utilisation CPU"', '"📊 Utilisation CPU"'),
    ('"RAM Totale"', '"💾 RAM Totale"'),
    ('"Génération RAM"', '"💾 Génération RAM"'),
    ('"Utilisation RAM"', '"📊 Utilisation RAM"'),
    ('"GPU"', '"🎮 GPU"'),

    # Boutons Outils Diagnostic
    ('" CrystalDiskInfo"', '"💿 CrystalDiskInfo"'),
    ('" OCCT (Temp & Stress)"', '"🌡️ OCCT (Temp & Stress)"'),
    ('" Test Batterie OrdiPlus"', '"🔋 Test Batterie OrdiPlus"'),
    ('" Test Batterie NiTrite"', '"🔋 Test Batterie NiTrite"'),
    ('" Autoruns"', '"🚀 Autoruns"'),
    ('" Malwarebytes Portable"', '"🛡️ Malwarebytes Portable"'),
    ('" Spybot Search & Destroy"', '"🛡️ Spybot Search & Destroy"'),
    ('" AdwCleaner Portable"', '"🛡️ AdwCleaner Portable"'),
    ('" Wise Disk Cleaner"', '"🧹 Wise Disk Cleaner"'),
    ('" HWMonitor"', '"📊 HWMonitor"'),
    ('" HWinfo"', '"📊 HWinfo"'),
    ('" CrystalDiskMark"', '"⚡ CrystalDiskMark"'),
    ('" CPU-Z"', '"🖥️ CPU-Z"'),
    ('" GPU-Z"', '"🎮 GPU-Z"'),
    ('" Wise Care 365"', '"🔧 Wise Care 365"'),
    ('" Activation Windows/Office"', '"🔑 Activation Windows/Office"'),
    ('" MSCONFIG"', '"⚙️ MSCONFIG"'),
    ('" Gestionnaire des Tâches"', '"📋 Gestionnaire des Tâches"'),
    ('" Dossier Temp"', '"📁 Dossier Temp"'),
    ('" AppData Local"', '"📁 AppData Local"'),
    ('" Tout Mettre à Jour"', '"📥 Tout Mettre à Jour"'),
    ('" Drivers NVIDIA"', '"🎮 Drivers NVIDIA"'),
    ('" Drivers AMD"', '"🎮 Drivers AMD"'),
    ('" Réparer Image Windows"', '"🔧 Réparer Image Windows"'),
    ('" Propriétés Utilisateur"', '"👤 Propriétés Utilisateur"'),
    ('" Système"', '"⚙️ Système"'),  # Pour le bouton, pas le header
    ('" CHKDSK Complet"', '"🔍 CHKDSK Complet"'),

    # Sections Optimisations
    ('" Nettoyage"', '"🧹 Nettoyage"'),
    ('" Vider la corbeille"', '"🗑️ Vider la corbeille"'),
    ('" Fichiers temporaires"', '"🗑️ Fichiers temporaires"'),
    ('" Cache navigateurs"', '"🌐 Cache navigateurs"'),
    ('" Nettoyage disque Windows"', '"💿 Nettoyage disque Windows"'),
    ('" Performance"', '"⚡ Performance"'),
    ('" Optimiser disques"', '"💿 Optimiser disques"'),
    ('" Gestionnaire des tâches"', '"📋 Gestionnaire des tâches"'),
    ('" Nettoyeur de disque"', '"🧹 Nettoyeur de disque"'),
    ('" Options performances"', '"🎮 Options performances"'),
    ('" AtlasOS"', '"🖥️ AtlasOS"'),
    ('" ReviOS"', '"🖥️ ReviOS"'),
    ('" Services"', '"⚙️ Services"'),
    ('" Ouvrir Services"', '"⚙️ Ouvrir Services"'),
    ('" Démarrage"', '"🚀 Démarrage"'),
    ('" Gestionnaire Démarrage"', '"🚀 Gestionnaire Démarrage"'),
]

def add_emojis_to_file(filepath):
    """
    Ajoute tous les emojis dans le fichier
    """
    print(f"[*] Lecture de {filepath}...")

    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    original_content = content
    modifications_count = 0

    print("\n[*] Application des modifications...")

    for old, new in REPLACEMENTS:
        count = content.count(old)
        if count > 0:
            content = content.replace(old, new)
            modifications_count += count
            print(f"  [OK] Modification appliquee ({count} fois)")
        # Ne pas afficher les non-trouvés pour éviter spam

    if content != original_content:
        print(f"\n[*] Sauvegarde des modifications...")
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"[OK] {modifications_count} modifications appliquees avec succes!")
    else:
        print("\n[!] Aucune modification appliquee")

    return modifications_count

if __name__ == "__main__":
    filepath = "C:\\Users\\Utilisateur\\Downloads\\Nitrite-V18.5\\src\\v14_mvp\\pages_full.py"

    print("=" * 80)
    print("  SCRIPT AUTOMATIQUE D'AJOUT D'EMOJIS - NiTriTe V18.5")
    print("=" * 80)

    count = add_emojis_to_file(filepath)

    print("\n" + "=" * 80)
    print(f"  [OK] TERMINE! {count} emojis ajoutes")
    print("=" * 80)
