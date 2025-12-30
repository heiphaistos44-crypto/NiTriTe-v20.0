@echo off
chcp 65001 >nul
title NiTriTe V20.0 - Mode Développement
color 0B

REM Changer vers le répertoire du script
cd /d "%~dp0"

echo.
echo ╔═══════════════════════════════════════════════════════════╗
echo ║          LANCEMENT NiTriTe V20.0                          ║
echo ║          Mode Développement                               ║
echo ╚═══════════════════════════════════════════════════════════╝
echo.

REM Vérifier Python
py -3.12 --version >nul 2>&1
if errorlevel 1 (
    echo ✗ Python 3.12 non trouvé!
    echo.
    echo Veuillez installer Python 3.12 depuis:
    echo https://www.python.org/downloads/
    pause
    exit /b 1
)

echo ✓ Python 3.12 trouvé
echo.
echo 🚀 Lancement de NiTriTe V20.0...
echo.

REM Lancer l'application
py -3.12 -m src.v14_mvp.main_app

REM Si erreur
if errorlevel 1 (
    echo.
    echo ╔═══════════════════════════════════════════════════════════╗
    echo ║          ✗ ERREUR AU LANCEMENT                            ║
    echo ╚═══════════════════════════════════════════════════════════╝
    echo.
    echo Vérifiez que toutes les dépendances sont installées:
    echo   py -3.12 -m pip install -r requirements.txt
    echo.
    pause
)
