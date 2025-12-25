#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Script pour corriger automatiquement les URLs cassées dans portable_apps.json"""

import json
from pathlib import Path

# Dictionnaire des corrections d'URLs
URL_FIXES = {
    # PortableApps.com - URLs directes vers la page de téléchargement
    "7-Zip Portable": "https://portableapps.com/apps/utilities/7-zip_portable",
    "Recuva Portable": "https://portableapps.com/apps/utilities/recuva_portable",
    "IrfanView Portable": "https://portableapps.com/apps/graphics_pictures/irfanview_portable",
    "GIMP Portable": "https://portableapps.com/apps/graphics_pictures/gimp_portable",
    "Inkscape Portable": "https://portableapps.com/apps/graphics_pictures/inkscape_portable",
    "Paint.NET Portable": "https://portableapps.com/apps/graphics_pictures/paint.net_portable",
    "Audacity Portable": "https://portableapps.com/apps/music_video/audacity_portable",
    "XnView Portable": "https://portableapps.com/apps/graphics_pictures/xnview_portable",
    "Wireshark Portable": "https://portableapps.com/apps/utilities/wireshark_portable",
    "FileZilla Portable": "https://portableapps.com/apps/internet/filezilla_portable",
    "Speccy Portable": "https://portableapps.com/apps/utilities/speccy_portable",
    "KeePass Portable": "https://portableapps.com/apps/utilities/keepass_portable",
    "ClamWin Portable": "https://portableapps.com/apps/security/clamwin_portable",
    "CCleaner Portable": "https://portableapps.com/apps/utilities/ccleaner_portable",

    # Total Commander - Dernière version stable
    "Total Commander": "https://totalcmd.net/1105/tcmd1105x64.exe",

    # FreeCommander - URL du site officiel
    "FreeCommander": "https://freecommander.com/en/downloads/",

    # WinDirStat - URL sourceforge (plus stable)
    "WinDirStat Portable": "https://sourceforge.net/projects/windirstat/files/latest/download",

    # K-Lite Codec Pack - URL officielle
    "K-Lite Codec Pack": "https://codecguide.com/download_k-lite_codec_pack_basic.htm",

    # MPC-HC - Fork actif
    "MPC-HC Portable": "https://github.com/clsid2/mpc-hc/releases/latest",

    # OBS Studio - Latest release page
    "OBS Studio Portable": "https://obsproject.com/download",

    # ImageMagick - URL page de téléchargement
    "ImageMagick Portable": "https://imagemagick.org/script/download.php#windows",

    # Greenshot - Latest release page
    "Greenshot Portable": "https://github.com/greenshot/greenshot/releases/latest",

    # UltraVNC - Page de téléchargement officielle
    "UltraVNC Portable": "https://uvnc.com/downloads/ultravnc.html",

    # NetLimiter - Page de téléchargement
    "NetLimiter Portable": "https://www.netlimiter.com/download",

    # Insomnia - Page de téléchargement
    "Insomnia Portable": "https://insomnia.rest/download",

    # mRemoteNG - Latest release
    "mRemoteNG Portable": "https://github.com/mRemoteNG/mRemoteNG/releases/latest",

    # Remote Desktop Manager - Page de téléchargement
    "Remote Desktop Manager": "https://devolutions.net/remote-desktop-manager/home/download",

    # GPU-Z - URL officielle TechPowerUp
    "GPU-Z Portable": "https://www.techpowerup.com/download/techpowerup-gpu-z/",

    # CrystalDiskInfo - Utiliser sourceforge
    "CrystalDiskInfo": "https://sourceforge.net/projects/crystaldiskinfo/files/latest/download",

    # CrystalDiskMark - Utiliser sourceforge
    "CrystalDiskMark": "https://sourceforge.net/projects/crystaldiskmark/files/latest/download",

    # HWiNFO - URL directe portable
    "HWiNFO Portable": "https://www.hwinfo.com/download/",

    # AllDup - Page de téléchargement
    "AllDup Portable": "https://www.alldup.de/en_download_alldup.php",

    # PDF24 Creator - Page de téléchargement
    "PDF24 Creator": "https://www.pdf24.org/en/download.html",

    # Balena Etcher - Latest release
    "Balena Etcher": "https://github.com/balena-io/etcher/releases/latest",

    # Brackets - Projet abandonné, alternative VSCode Portable
    "Brackets Portable": "https://code.visualstudio.com/Download",

    # Deno - Latest release
    "Deno Portable": "https://github.com/denoland/deno/releases/latest",

    # PHP - Page de téléchargement Windows
    "PHP Portable": "https://windows.php.net/download/",

    # Ruby - Latest installer
    "Ruby Portable": "https://github.com/oneclick/rubyinstaller2/releases/latest",

    # Redis - Alternative Memurai (fork Windows)
    "Redis Portable": "https://www.memurai.com/get-memurai",

    # SQLite - Version récente
    "SQLite Portable": "https://www.sqlite.org/download.html",

    # Laragon - URL GitHub correcte
    "Laragon Portable": "https://laragon.org/download/",

    # KeePassXC - Latest
    "KeePassXC Portable": "https://github.com/keepassxreboot/keepassxc/releases/latest",

    # Bitwarden - Page de téléchargement
    "Bitwarden Portable": "https://bitwarden.com/download/",

    # WinMD5 - URL alternative
    "WinMD5 Portable": "https://www.nirsoft.net/utils/hashmyfiles.zip",

    # HashCheck - Latest release
    "HashCheck": "https://github.com/gurnec/HashCheck/releases/latest",

    # Sandboxie - Latest release
    "Sandboxie Portable": "https://github.com/sandboxie-plus/Sandboxie/releases/latest",

    # Comodo Firewall - Page de téléchargement
    "Comodo Firewall": "https://www.comodo.com/home/internet-security/firewall.php",

    # Wise Care 365 - Page de téléchargement
    "Wise Care 365": "https://www.wisecleaner.com/wise-care-365.html",

    # Windows10Debloater - Latest
    "Windows10Debloater": "https://github.com/Sycnex/Windows10Debloater/releases/latest",

    # CleanAfterMe - Nirsoft
    "CleanAfterMe": "https://www.nirsoft.net/utils/cleanaftme.zip",

    # Temp File Cleaner - URL alternative
    "Temp File Cleaner": "https://www.bleachbit.org/download/windows",

    # Disk Cleanup - Intégré à Windows
    "Disk Cleanup": "https://www.microsoft.com/en-us/software-download/windows10"
}

def fix_urls():
    """Corriger toutes les URLs cassées"""
    print("=" * 80)
    print("CORRECTION AUTOMATIQUE DES URLS CASSEES")
    print("=" * 80)
    print()

    # Charger le JSON
    json_path = Path("data/portable_apps.json")
    with open(json_path, 'r', encoding='utf-8') as f:
        data = json.load(f)

    fixed_count = 0
    not_found = []

    # Parcourir et corriger
    for category, apps in data.items():
        for app_name, app_info in apps.items():
            if app_name in URL_FIXES:
                old_url = app_info['url']
                new_url = URL_FIXES[app_name]

                if old_url != new_url:
                    app_info['url'] = new_url
                    fixed_count += 1
                    print(f"[FIX] {app_name}")
                    print(f"  AVANT: {old_url[:80]}...")
                    print(f"  APRES: {new_url[:80]}...")
                    print()

    # Sauvegarder
    backup_path = Path("data/portable_apps.json.backup")
    print(f"Sauvegarde de l'original vers: {backup_path}")
    with open(backup_path, 'w', encoding='utf-8') as f:
        # Recharger l'original pour le backup
        with open(json_path, 'r', encoding='utf-8') as orig:
            f.write(orig.read())

    print(f"Sauvegarde du fichier corrige...")
    with open(json_path, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=2, ensure_ascii=False)

    print()
    print("=" * 80)
    print("RESULTAT:")
    print("=" * 80)
    print(f"URLs corrigees: {fixed_count}")
    print(f"Backup cree: {backup_path}")
    print(f"Fichier mis a jour: {json_path}")
    print()
    print("Relancez 'python test_portable_urls.py' pour verifier!")

if __name__ == "__main__":
    fix_urls()
