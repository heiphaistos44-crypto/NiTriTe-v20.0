@echo off
chcp 65001 >nul
title NiTriTe V17 - Installation des Dependances

echo.
echo ========================================
echo   Installation des Dependances
echo   NiTriTe V17 Beta
echo ========================================
echo.

:: Vérifier Python
python --version >nul 2>&1
if errorlevel 1 (
    echo [X] ERREUR: Python n'est pas installe
    echo.
    echo Telechargez Python 3.8-3.12 depuis:
    echo https://www.python.org/downloads/
    echo.
    echo IMPORTANT: Cochez "Add Python to PATH" lors de l'installation
    echo.
    pause
    exit /b 1
)

echo [OK] Python detecte:
python --version
echo.

:: Mise à jour de pip
echo [*] Mise a jour de pip...
python -m pip install --upgrade pip
echo.

:: Installation depuis requirements.txt
if exist requirements.txt (
    echo [*] Installation depuis requirements.txt...
    python -m pip install -r requirements.txt
    echo.
) else (
    echo [!] requirements.txt non trouve
    echo [*] Installation manuelle des dependances...
    echo.

    :: Installation manuelle
    echo [*] Installation de customtkinter...
    python -m pip install customtkinter>=5.2.0

    echo [*] Installation de Pillow...
    python -m pip install Pillow>=10.0.0

    echo [*] Installation de requests...
    python -m pip install requests>=2.31.0

    echo [*] Installation de psutil...
    python -m pip install psutil>=5.9.0

    echo [*] Installation de PyInstaller...
    python -m pip install pyinstaller>=6.0.0

    echo [*] Installation de packaging...
    python -m pip install packaging>=23.0

    echo [*] Installation de tqdm...
    python -m pip install tqdm>=4.66.0

    echo [*] Installation de colorama...
    python -m pip install colorama>=0.4.6
)

:: Vérification finale
echo.
echo ========================================
echo   Verification des installations
echo ========================================
echo.

python -c "import customtkinter; print('[OK] customtkinter:', customtkinter.__version__)"
python -c "import PIL; print('[OK] Pillow')"
python -c "import requests; print('[OK] requests')"
python -c "import psutil; print('[OK] psutil')"
python -c "import PyInstaller; print('[OK] PyInstaller')"

echo.
echo ========================================
echo   Installation terminee !
echo ========================================
echo.
echo Vous pouvez maintenant lancer:
echo - BUILD_PORTABLE_V17_FIXED.bat pour compiler
echo - LANCER_NITRITE_V17.bat pour tester en mode dev
echo.
pause
