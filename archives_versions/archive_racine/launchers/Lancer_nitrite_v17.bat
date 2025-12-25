@echo off
echo.
echo =============================================================
echo   NiTriTe V14 MVP - Maintenance Informatique Pro
echo =============================================================
echo.

REM Se placer dans le dossier du script
cd /d "%~dp0"
echo Repertoire de travail: %CD%
echo.

REM Vérifier Python
python --version >nul 2>&1
if errorlevel 1 (
    echo ERREUR: Python n'est pas installe ou pas dans le PATH
    echo.
    echo Telechargez Python 3.8-3.12:
    echo    https://www.python.org/downloads/
    echo.
    pause
    exit /b 1
)

echo Python detecte
python --version

REM Vérifier que requirements.txt existe
if not exist "requirements.txt" (
    echo ERREUR: requirements.txt introuvable dans %CD%
    echo.
    pause
    exit /b 1
)

REM Installation automatique des dependances principales
echo.
echo Installation/verification des dependances Python...
pip install --upgrade pip
pip install -r requirements.txt
if errorlevel 1 (
    echo.
    echo ECHEC installation des dependances
    pause
    exit /b 1
)
echo Installation des dependances terminee

REM Lancer l'application
echo.
echo =============================================================
echo   LANCEMENT DE L'APPLICATION
echo =============================================================
echo.

python -m src.v14_mvp.main_app

REM Gestion sortie
if errorlevel 1 (
    echo.
    echo =============================================================
    echo   ERREUR: L'APPLICATION S'EST TERMINEE AVEC UNE ERREUR
    echo =============================================================
    echo.
    echo Verifiez :
    echo    - Tous les fichiers sont presents dans src/v14_mvp/
    echo    - Le fichier data/programs.json existe
    echo    - Python 3.8-3.12 est installe
    echo.
    pause
) else (
    echo.
    echo Application fermee normalement
)
pause