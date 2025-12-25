#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Script pour corriger les URLs cassées dans programs.json"""

import json
from pathlib import Path

# Dictionnaire massif des corrections d'URLs pour programs.json
URL_FIXES = {
    # ============ ANTIVIRUS ============
    "G DATA Antivirus": "https://www.gdata-software.com/download",
    "F-Secure Antivirus": "https://www.f-secure.com/en/home/free-tools",
    "Avira Free Antivirus": "https://www.avira.com/en/free-antivirus-windows",
    "Immunet": "https://www.immunet.com/index",
    "Panda Free Antivirus": "https://www.pandasecurity.com/en/homeusers/free-antivirus/",
    "Baidu Antivirus": "https://www.baidu.com",  # Discontinued
    "McAfee Total Protection": "https://www.mcafee.com/en-us/antivirus/free.html",
    "Vipre Antivirus": "https://www.vipre.com/products/home-antivirus/",
    "Quick Heal Total Security": "https://www.quickheal.com/free-virus-protection-security-online",
    "Arcabit Antivirus": "https://www.arcabit.com/antivirus-free/",
    "Adaware Antivirus": "https://www.adaware.com/free-antivirus-download",

    # ============ BUREAUTIQUE ============
    "LibreOffice": "https://www.libreoffice.org/download/download/",
    "Apache OpenOffice": "https://www.openoffice.org/download/",
    "OnlyOffice Desktop": "https://www.onlyoffice.com/download-desktop.aspx",
    "Scribus": "https://www.scribus.net/downloads/stable-branch/",
    "SoftMaker FreeOffice": "https://www.freeoffice.com/en/download/applications",
    "Calligra Suite": "https://calligra.org/download/",
    "SimpleNote": "https://simplenote.com/",
    "CherryTree": "https://www.giuspen.com/cherrytree/",
    "HomeBank": "http://homebank.free.fr/downloads.php",
    "Joplin": "https://joplinapp.org/download/",
    "Standard Notes": "https://standardnotes.com/download",
    "Project Libre": "https://www.projectlibre.com/product/projectlibre-open-source",
    "WriteMonkey": "https://writemonkey.com/",
    "Q10": "https://www.baara.com/q10/",
    "AbiWord": "https://www.abisource.com/download/",

    # ============ COMMUNICATION ============
    "Skype": "https://www.skype.com/en/get-skype/",
    "Viber": "https://www.viber.com/download/",
    "Telegram Desktop": "https://desktop.telegram.org/",
    "Messenger": "https://www.messenger.com/desktop",
    "Google Meet": "https://meet.google.com/download",
    "BigBlueButton": "https://bigbluebutton.org/",
    "Pidgin": "https://pidgin.im/download/",

    # ============ COMPRESSION ============
    "Hamster ZIP Archiver": "https://hamstersoft.com/",  # Discontinued
    "TUGZip": "http://www.tugzip.com/",  # Discontinued
    "jZip": "https://www.jzip.com/",
    "IZArc": "https://www.izarc.org/",
    "FreeArc": "https://github.com/sleuthkit/freearc",
    "KGB Archiver": "https://sourceforge.net/projects/kgbarchiver/",
    "B1 Free Archiver": "https://github.com/b1-systems/b1-archiver",
    "ArcThemALL": "http://www.arcthemall.com/",  # Discontinued
    "FilZip": "http://www.filzip.com/",  # Discontinued
    "ExtractNow": "https://www.extractnow.com/",
    "ZipGenius": "https://www.zipgenius.com/",
    "QuickZip": "http://www.quickzip.org/",  # Discontinued
    "CAM UnZip": "http://www.camunzip.com/",  # Discontinued
    "WinMount": "https://www.winmount.com/",
    "UltimateZip": "https://www.ultimatezip.com/",
    "Zip Archiver": "https://www.microsoft.com/store/productId/9WZDNCRDH0D8",
    "Easy 7-Zip": "https://www.e7z.org/",
    "Bandizip": "https://en.bandisoft.com/bandizip/",

    # ============ DÉSINSTALLATEURS ANTIVIRUS ============
    "Kaspersky Removal Tool": "https://support.kaspersky.com/common/uninstall/1464",
    "ESET Uninstaller": "https://support.eset.com/en/kb2289-uninstall-eset-windows-home-products",
    "AVG Remover": "https://www.avg.com/en-us/avg-remover",
    "Bitdefender Uninstall Tool": "https://www.bitdefender.com/consumer/support/answer/28130/",
    "Sophos Removal Tool": "https://support.sophos.com/support/s/article/KB-000036711",
    "Norton Remove Tool": "https://support.norton.com/sp/en/us/home/current/solutions/kb20080710133834EN",
    "Malwarebytes Support Tool": "https://support.malwarebytes.com/hc/en-us/articles/360038524414",
    "Panda Cloud Uninstaller": "https://www.pandasecurity.com/en/support/",
    "F-Secure Uninstallation Tool": "https://www.f-secure.com/en/support",
    "Baidu Antivirus Uninstaller": "https://www.baidu.com",  # Discontinued
    "Emsisoft Commandline Scanner": "https://www.emsisoft.com/en/software/commandline/",
    "Vipre Removal Tool": "https://support.vipre.com/",
    "Webroot Uninstaller": "https://www.webroot.com/",
    "Comodo Removal Tool": "https://www.comodo.com/",
    "Avira Registry Cleaner": "https://www.avira.com/en/support-for-home",
    "Quick Heal Uninstaller": "https://www.quickheal.com/support",
    "IObit Malware Fighter Uninstaller": "https://www.iobit.com/en/advanceduninstaller.php",
    "360 Total Security Uninstaller": "https://www.360totalsecurity.com/",
    "Zemana AntiMalware Uninstaller": "https://www.zemana.com/",

    # ============ DÉVELOPPEMENT ============
    "Visual Studio Code": "https://code.visualstudio.com/download",

    # ============ IA & ASSISTANTS ============
    "Perplexity": "https://www.perplexity.ai/",
    "Grammarly": "https://www.grammarly.com/desktop",
    "ChatGPT Desktop": "https://openai.com/chatgpt/desktop/",
    "Jasper AI": "https://www.jasper.ai/",
    "Jarvis AI": "https://www.jasper.ai/",  # Renamed to Jasper
    "Microsoft Copilot": "https://www.microsoft.com/en-us/microsoft-365/microsoft-copilot",
    "Copy.ai": "https://www.copy.ai/",
    "QuillBot": "https://quillbot.com/",
    "Character.AI": "https://character.ai/",
    "Writesonic": "https://writesonic.com/",
    "Replika": "https://replika.com/",
    "Runway ML": "https://runwayml.com/",
    "Alexa": "https://www.amazon.com/alexa",
    "Bing Chat Desktop": "https://www.bing.com/chat",
    "Wordtune": "https://www.wordtune.com/",
    "Rytr": "https://rytr.me/",
    "Google Bard Desktop": "https://bard.google.com/",
    "Cortana": "builtin",  # Built into Windows

    # ============ IMPRIMANTES & SCAN ============
    "VueScan": "https://www.hamrick.com/vuescan.html",
    "NAPS2": "https://www.naps2.com/download",
    "HP Smart": "https://www.hp.com/us-en/solutions/app.html",
    "Canon IJ Scan Utility": "https://www.canon.com/",
    "Dell Printer Hub": "https://www.dell.com/support/home/",
    "HP Print and Scan Doctor": "https://support.hp.com/us-en/help/hp-print-and-scan-doctor",
    "Lexmark Universal Print Driver": "https://support.lexmark.com/",
    "PaperScan Free": "https://www.paperscan.org/",
    "OKI LPR Utility": "https://www.oki.com/",
    "Konica Minolta Print Service": "https://www.konicaminolta.com/",
    "Microsoft Print to PDF": "builtin",  # Built into Windows
    "Kyocera Print Center": "https://www.kyoceradocumentsolutions.com/",
    "PDF24 PDF Printer": "https://www.pdf24.org/",
    "Bullzip PDF Printer": "https://www.bullzip.com/products/pdf/info.php",
    "Pantum Printer Driver": "https://www.pantum.com/",

    # ============ INTERNET ============
    "qBittorrent": "https://www.qbittorrent.org/download.php",
    "Ares": "http://www.aresultimaversi.com/",  # Discontinued
    "ShareIt": "https://www.ushareit.com/",
    "NetWorx": "https://www.softperfect.com/products/networx/",
    "eMule": "https://www.emule-project.net/home/perl/general.cgi?l=1",
    "Ookla Speedtest": "https://www.speedtest.net/apps/desktop",
    "Xender": "https://www.xender.com/",
    "Angry IP Scanner": "https://angryip.org/download/",
    "Wireshark": "https://www.wireshark.org/download.html",
    "GlassWire Lite": "https://www.glasswire.com/download/",
    "Cyberduck": "https://cyberduck.io/download/",
    "FlashFXP": "https://www.flashfxp.com/download",

    # ============ JEUX ============
    "GOG Galaxy": "https://www.gog.com/galaxy",
    "Itch.io": "https://itch.io/app",
    "Playnite": "https://playnite.link/",
    "RetroArch": "https://www.retroarch.com/?page=platforms",
    "Xbox Game Bar": "builtin",  # Built into Windows 10/11
    "Razer Cortex": "https://www.razer.com/cortex/boost",
    "Xbox App": "https://www.xbox.com/en-US/apps/xbox-app-for-pc",

    # ============ MULTIMÉDIA ============
    "Audacity": "https://www.audacityteam.org/download/",
    "IrfanView": "https://www.irfanview.com/",
    "Kodi": "https://kodi.tv/download/windows/",
    "Jellyfin": "https://jellyfin.org/downloads/",

    # ============ NAVIGATEURS ============
    "UC Browser": "https://www.ucweb.com/",
    "Maxthon": "https://www.maxthon.com/",
    "Tor Browser": "https://www.torproject.org/download/",
    "Slimjet": "https://www.slimjet.com/",
    "Epic Privacy Browser": "https://www.epicbrowser.com/",
    "Cent Browser": "https://www.centbrowser.com/",
    "Avast Secure Browser": "https://www.avast.com/secure-browser",
    "SRWare Iron": "https://www.srware.net/iron/",
    "Falkon": "https://www.falkon.org/download/",
    "Comodo Dragon": "https://www.comodo.com/home/browsers-toolbars/browser.php",
    "Sleipnir": "https://www.fenrir-inc.com/jp/sleipnir/",
    "Iridium Browser": "https://iridiumbrowser.de/",

    # ============ OUTILS ORDIPLUS ============
    "Spybot Search & Destroy": "https://www.safer-networking.org/download/",
    "Adobe Acrobat Reader DC": "https://get.adobe.com/reader/",
    "Malwarebytes": "https://www.malwarebytes.com/mwb-download",

    # ============ PDF ET DOCUMENTS ============
    "IceCream PDF Editor": "https://icecreamapps.com/PDF-Editor/",
    "Nitro PDF Reader": "https://www.gonitro.com/",
    "Nuance Power PDF": "https://www.nuance.com/print-capture-and-pdf-solutions/pdf-and-document-conversion/power-pdf-converter.html",
    "Able2Extract": "https://www.investintech.com/prod_a2e.htm",
    "PDF24 Tools": "https://www.pdf24.org/",
    "DocuSign": "https://www.docusign.com/products/electronic-signature",

    # ============ PACK OFFICE ============
    "Office LTSC 2021": "https://www.microsoft.com/en-us/microsoft-365",

    # ============ PRODUCTIVITÉ ============
    "Obsidian": "https://obsidian.md/download",
    "Any.do": "https://www.any.do/",
    "Remember The Milk": "https://www.rememberthemilk.com/",
    "Microsoft To Do": "https://todo.microsoft.com/",
    "Brain Focus Productivity Timer": "https://brainfocus.io/",
    "Clockify": "https://clockify.me/downloads",
    "Habitica": "https://habitica.com/",
    "Joplin Desktop": "https://joplinapp.org/download/",
    "Be Focused": "https://xwavesoft.com/be-focused-pro.html",
    "Timely": "https://timelyapp.com/",
    "Microsoft OneNote Desktop": "https://www.onenote.com/download",

    # ============ RÉSEAUX SOCIAUX ============
    "Buffer": "https://buffer.com/",
    "Reddit": "https://www.reddit.com/",
    "Pinterest": "https://www.pinterest.com/",
    "Instagram": "https://www.instagram.com/",
    "LinkedIn": "https://www.linkedin.com/",
    "Tumblr": "https://www.tumblr.com/",
    "Station": "https://getstation.com/",
    "Hootsuite": "https://www.hootsuite.com/",
    "Flamingo": "https://flamingo-app.com/",
    "Wavebox": "https://wavebox.io/",
    "Twitterific": "https://twitterrific.com/",
    "Social Media Manager": "https://www.hootsuite.com/",
    "Sprout Social": "https://sproutsocial.com/",
    "Hootsuite Desktop": "https://www.hootsuite.com/",
    "Corebird": "https://corebird.baedert.org/",
    "Agorapulse": "https://www.agorapulse.com/",

    # ============ SERVICES APPLE ============
    "iCloud": "https://support.apple.com/en-us/HT204283",
    "3uTools": "http://www.3u.com/",
    "iMazing": "https://imazing.com/download",
    "Apple Devices": "https://www.microsoft.com/store/productId/9NP83LWLPZ9K",
    "Apple Music Preview": "https://www.apple.com/apple-music/",
    "Apple TV App": "https://www.apple.com/apple-tv-app/",
    "iTools": "https://www.thinkskysoft.com/",
    "iExplorer": "https://macroplant.com/iexplorer",
    "AnyDroid": "https://www.imobie.com/anydroid/",
    "Dr.Fone": "https://drfone.wondershare.com/",

    # ============ STOCKAGE CLOUD ============
    "Box Drive": "https://www.box.com/resources/downloads",
    "Amazon Drive": "https://www.amazon.com/clouddrive/home",
    "MediaFire Desktop": "https://www.mediafire.com/software/",
    "Icedrive": "https://icedrive.net/",
    "Koofr": "https://koofr.eu/",
    "IDrive": "https://www.idrive.com/",
    "Carbonite": "https://www.carbonite.com/",
    "SpiderOak": "https://spideroak.com/",
    "Internxt Drive": "https://internxt.com/drive",

    # ============ STREAMING AUDIO ============
    "Deezer": "https://www.deezer.com/download",
    "Qobuz": "https://www.qobuz.com/us-en/discover",
    "Amazon Music": "https://www.amazon.com/music/player/web",
    "Audible": "https://www.audible.com/",
    "SoundCloud": "https://soundcloud.com/",
    "Apple Music": "https://www.apple.com/apple-music/",
    "Audiomack": "https://audiomack.com/",
    "Pandora": "https://www.pandora.com/",
    "Radio.fr": "https://www.radio.de/",
    "TuneIn Radio": "https://tunein.com/",
    "iHeartRadio": "https://www.iheart.com/",
    "Mixcloud": "https://www.mixcloud.com/",
    "Anghami": "https://www.anghami.com/",
    "JioSaavn": "https://www.jiosaavn.com/",
    "Gaana": "https://gaana.com/",
    "Clementine": "https://www.clementine-player.org/",
    "8tracks": "https://8tracks.com/",  # Discontinued

    # ============ STREAMING VIDÉO ============
    "Netflix": "https://www.netflix.com/",
    "Disney+": "https://www.disneyplus.com/",
    "Apple TV": "https://www.apple.com/apple-tv-app/",
    "Pluto TV": "https://pluto.tv/",
    "Paramount+": "https://www.paramountplus.com/",
    "Crunchyroll": "https://www.crunchyroll.com/",
    "Peacock TV": "https://www.peacocktv.com/",
    "Funimation": "https://www.funimation.com/",
    "Amazon Prime Video": "https://www.primevideo.com/",
    "Tubi": "https://tubitv.com/",
    "Hulu": "https://www.hulu.com/",
    "Vudu": "https://www.vudu.com/",
    "YouTube": "https://www.youtube.com/",
    "Vimeo": "https://vimeo.com/",
    "Molotov TV": "https://www.molotov.tv/",
    "Viki": "https://www.viki.com/",
    "Dailymotion": "https://www.dailymotion.com/",
    "MyCanal": "https://www.canalplus.com/",
    "Restream Desktop": "https://restream.io/",

    # ============ SUITES PROFESSIONNELLES ============
    "Zoho CRM": "https://www.zoho.com/crm/",
    "SAP Business One": "https://www.sap.com/products/erp/s4hana-erp.html",
    "Smartsheet": "https://www.smartsheet.com/",
    "Coda": "https://coda.io/",
    "Monday.com Desktop": "https://monday.com/",
    "ServiceNow": "https://www.servicenow.com/",
    "ERPNext": "https://erpnext.com/",

    # ============ SÉCURITÉ ============
    "Unchecky": "https://unchecky.com/",
    "Kaspersky VPN": "https://www.kaspersky.com/vpn-secure-connection",
    "Comodo Firewall": "https://www.comodo.com/home/internet-security/firewall.php",
    "Hide.me VPN": "https://hide.me/en/software/windows",
    "LastPass": "https://www.lastpass.com/",
    "Cryptomator": "https://cryptomator.org/downloads/",
    "Sticky Password": "https://www.stickypassword.com/",
    "Avira Password Manager": "https://www.avira.com/en/avira-password-manager",
    "Roboform": "https://www.roboform.com/",
    "Enpass": "https://www.enpass.io/downloads/",
    "VeraCrypt": "https://www.veracrypt.fr/en/Downloads.html",
    "Norton Password Manager": "https://my.norton.com/",

    # ============ UTILITAIRES ============
    "HWiNFO64": "https://www.hwinfo.com/download/",
    "Revo Uninstaller": "https://www.revouninstaller.com/products/revo-uninstaller-free/",
    "HWiNFO": "https://www.hwinfo.com/download/",
    "MSI Afterburner": "https://www.msi.com/Landing/afterburner/graphics-cards",

    # ============ UTILITAIRES SYSTÈME ============
    "WinDirStat": "https://windirstat.net/",
    "System Ninja": "https://www.sistemaninja.com/",
    "System Mechanic": "https://www.iolo.com/products/system-mechanic/",
    "Ashampoo WinOptimizer": "https://www.ashampoo.com/en-us/winoptimizer-19",
    "AVG TuneUp": "https://www.avg.com/en-us/avg-pctuneup",
    "Norton Utilities": "https://us.norton.com/products/norton-utilities-ultimate",
}

def fix_programs_urls():
    """Corriger les URLs cassees dans programs.json"""
    print("=" * 100)
    print("CORRECTION AUTOMATIQUE DES URLS CASSEES - PROGRAMS.JSON")
    print("=" * 100)
    print()

    # Charger le JSON
    json_path = Path("data/programs.json")
    if not json_path.exists():
        print(f"[ERROR] Fichier non trouve: {json_path}")
        return

    with open(json_path, 'r', encoding='utf-8') as f:
        data = json.load(f)

    fixed_count = 0
    not_found = []

    # Parcourir et corriger
    for category, apps in data.items():
        for app_name, app_info in apps.items():
            if app_name in URL_FIXES:
                old_url = app_info.get('download_url') or app_info.get('url', '')
                new_url = URL_FIXES[app_name]

                if old_url != new_url:
                    # Mettre à jour l'URL
                    if 'download_url' in app_info:
                        app_info['download_url'] = new_url
                    elif 'url' in app_info:
                        app_info['url'] = new_url

                    fixed_count += 1
                    print(f"[FIX] {app_name} ({category})")
                    print(f"  AVANT: {old_url[:70]}...")
                    print(f"  APRES: {new_url[:70]}...")
                    print()

    # Sauvegarder
    backup_path = Path("data/programs.json.backup")
    print(f"[BACKUP] Sauvegarde de l'original vers: {backup_path}")
    with open(backup_path, 'w', encoding='utf-8') as f:
        # Recharger l'original pour le backup
        with open(json_path, 'r', encoding='utf-8') as orig:
            f.write(orig.read())

    print(f"[SAVE] Sauvegarde du fichier corrige...")
    with open(json_path, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=4, ensure_ascii=False)

    print()
    print("=" * 100)
    print("RESULTAT:")
    print("=" * 100)
    print(f"[OK] URLs corrigees: {fixed_count}")
    print(f"[BACKUP] Backup cree: {backup_path}")
    print(f"[FILE] Fichier mis a jour: {json_path}")
    print()
    print("[INFO] Relancez 'python check_programs_urls.py' pour verifier!")

if __name__ == "__main__":
    fix_programs_urls()
