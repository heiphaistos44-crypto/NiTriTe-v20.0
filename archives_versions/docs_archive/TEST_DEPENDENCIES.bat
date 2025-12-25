@echo off
chcp 65001 >nul
title NiTriTe V17 - Test des Dependances

echo.
echo ========================================
echo   Test des Dependances - NiTriTe V17
echo ========================================
echo.

:: Tester Python
echo [*] Test de Python...
python --version
if errorlevel 1 (
    echo [X] Python non trouve
    pause
    exit /b 1
)
echo.

:: Tester les modules Python
echo [*] Test des modules Python...
echo.

python -c "import sys; print('Python:', sys.version)"
if errorlevel 1 goto :error

python -c "import customtkinter; print('[OK] customtkinter')"
if errorlevel 1 (
    echo [X] customtkinter manquant
    echo [*] Installation...
    pip install customtkinter
)

python -c "import PIL; print('[OK] PIL / Pillow')"
if errorlevel 1 (
    echo [X] Pillow manquant
    echo [*] Installation...
    pip install Pillow
)

python -c "import requests; print('[OK] requests')"
if errorlevel 1 (
    echo [X] requests manquant
    echo [*] Installation...
    pip install requests
)

python -c "import psutil; print('[OK] psutil')"
if errorlevel 1 (
    echo [X] psutil manquant
    echo [*] Installation...
    pip install psutil
)

python -c "import PyInstaller; print('[OK] PyInstaller')"
if errorlevel 1 (
    echo [X] PyInstaller manquant
    echo [*] Installation...
    pip install pyinstaller
)

echo.
echo ========================================
echo   Toutes les dependances sont OK !
echo ========================================
echo.
pause
exit /b 0

:error
echo.
echo [X] ERREUR lors du test
echo.
pause
exit /b 1
