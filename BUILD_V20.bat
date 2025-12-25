@echo off
chcp 65001 >nul
title Build NiTriTe V20.0 Portable
color 0A

echo.
echo ╔═══════════════════════════════════════════════════════════╗
echo ║          BUILD NiTriTe V20.0 PORTABLE                     ║
echo ╚═══════════════════════════════════════════════════════════╝
echo.

REM Nettoyer les builds précédents
echo [1/5] Nettoyage des builds précédents...
if exist "dist" rmdir /s /q "dist"
if exist "build" rmdir /s /q "build"
echo ✓ Nettoyage terminé
echo.

REM Vérifier Python
echo [2/5] Vérification de Python...
py -3.12 --version >nul 2>&1
if errorlevel 1 (
    echo ✗ Python 3.12 non trouvé!
    pause
    exit /b 1
)
echo ✓ Python 3.12 trouvé
echo.

REM Vérifier les dépendances
echo [3/5] Vérification des dépendances...
py -3.12 -c "import customtkinter, psutil, requests, PIL, google.generativeai" >nul 2>&1
if errorlevel 1 (
    echo ✗ Dépendances manquantes! Installation...
    py -3.12 -m pip install customtkinter psutil requests Pillow google-generativeai
)
echo ✓ Dépendances OK
echo.

REM Build avec PyInstaller
echo [4/5] Build PyInstaller en cours...
echo.
py -3.12 -m PyInstaller NiTriTe_V20_Portable.spec --noconfirm
echo.

REM Copier assets
echo [5/5] Copie des assets...
if not exist "dist\assets" (
    xcopy /E /I /Y "assets" "dist\assets"
)
echo ✓ Assets copiés
echo.

REM Vérifier le résultat
if exist "dist\NiTriTe_V20_Portable.exe" (
    echo.
    echo ╔═══════════════════════════════════════════════════════════╗
    echo ║          ✓ BUILD RÉUSSI !                                 ║
    echo ╚═══════════════════════════════════════════════════════════╝
    echo.
    echo 📦 Fichier: dist\NiTriTe_V20_Portable.exe
    for %%A in ("dist\NiTriTe_V20_Portable.exe") do echo 📊 Taille: %%~zA octets
    echo.
) else (
    echo.
    echo ╔═══════════════════════════════════════════════════════════╗
    echo ║          ✗ BUILD ÉCHOUÉ !                                 ║
    echo ╚═══════════════════════════════════════════════════════════╝
    echo.
)

pause
