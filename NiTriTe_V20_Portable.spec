# -*- mode: python ; coding: utf-8 -*-
import os
import sys
from PyInstaller.utils.hooks import collect_submodules, collect_all

# Ajouter src/ au path pour que les imports fonctionnent
sys.path.insert(0, os.path.join(os.getcwd(), 'src'))

# Imports cachés critiques pour NiTriTe V20
hiddenimports = [
    # Système et monitoring
    'psutil', 'requests',
    # Interface graphique
    'customtkinter', 'tkinter', 'tkinter.ttk', 'tkinter.font',
    # Images
    'PIL', 'PIL.Image', 'PIL.ImageTk', 'PIL._tkinter_finder',
    # Modules internes
    'importlib', 'importlib.util',
    # Google Generative AI pour l'agent IA
    'google.generativeai', 'google.ai.generativelanguage',
    # Nouvelles pages V20
    'v14_mvp.page_drivers', 'v14_mvp.page_scanvirus',
]

# Ajouter les modules v14_mvp dynamiquement
import glob
v14_mvp_files = glob.glob(os.path.join('src', 'v14_mvp', '*.py'))
for file in v14_mvp_files:
    module_name = os.path.splitext(os.path.basename(file))[0]
    if module_name != '__init__':
        hiddenimports.append(f'v14_mvp.{module_name}')

# Ajouter win32com seulement sur Windows
if sys.platform == 'win32':
    try:
        hiddenimports += ['wmi', 'win32com', 'win32com.client', 'pythoncom']
        hiddenimports += collect_submodules('win32com')
        hiddenimports += collect_submodules('pythoncom')
    except:
        pass  # Ignorer si non disponible

# Ajouter customtkinter submodules
try:
    hiddenimports += collect_submodules('customtkinter')
except:
    pass

a = Analysis(
    [os.path.join('src', 'v14_mvp', 'main_app.py')],
    pathex=[os.path.join(os.getcwd(), 'src')],  # Ajouter src/ au path
    binaries=[],
    datas=[
        ('data', 'data'),
        ('assets', 'assets'),
        ('src', 'src'),
        # Note: archives_compressed n'est PAS inclus dans le build
        # Les archives seront téléchargées automatiquement depuis GitHub Releases au premier lancement
    ],
    hiddenimports=hiddenimports,
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=['matplotlib', 'numpy', 'pandas', 'scipy', 'IPython'],  # Exclure modules non nécessaires
    noarchive=False,
    optimize=0,
)
pyz = PYZ(a.pure)

exe = EXE(
    pyz,
    a.scripts,
    [],
    exclude_binaries=True,  # Mode OnDir - binaries séparés
    name='NiTriTe_V20_Portable',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=False,  # Application GUI, pas de console
    disable_windowed_traceback=False,
    icon='assets/Nitrite_icon1.ico' if os.path.exists('assets/Nitrite_icon1.ico') else None,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
)

coll = COLLECT(
    exe,
    a.binaries,
    a.zipfiles,
    a.datas,
    strip=False,
    upx=True,
    upx_exclude=[],
    name='NiTriTe_V20_Portable'
)
