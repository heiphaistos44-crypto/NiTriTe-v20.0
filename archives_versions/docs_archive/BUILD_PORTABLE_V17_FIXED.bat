@echo off
chcp 65001 >nul
title NiTriTe V17 - Build Portable (Fixed)

echo.
echo ========================================
echo   NiTriTe V17 - Build Portable
echo ========================================
echo.

:: Vérifier que Python est installé
python --version >nul 2>&1
if errorlevel 1 (
    echo [X] ERREUR: Python n'est pas installe ou n'est pas dans le PATH
    echo [!] Telechargez Python sur https://www.python.org/downloads/
    echo.
    pause
    exit /b 1
)

echo [OK] Python detecte
python --version
echo.

:: Lancer le script de build
echo [*] Lancement du script de build...
echo.
python build_portable_fixed.py

:: Vérifier le résultat
if errorlevel 1 (
    echo.
    echo ========================================
    echo   BUILD ECHOUE
    echo ========================================
    echo.
    pause
    exit /b 1
) else (
    echo.
    echo ========================================
    echo   BUILD REUSSI !
    echo ========================================
    echo.
    echo Executable disponible dans: dist\NiTriTe_V17_Portable.exe
    echo Package portable dans: release\
    echo.
    pause
    exit /b 0
)
