@echo off
chcp 65001 >nul
title Réorganisation Projet NiTriTe V20.0
color 0E

echo.
echo ╔═══════════════════════════════════════════════════════════╗
echo ║          RÉORGANISATION PROJET NiTriTe V20.0              ║
echo ╚═══════════════════════════════════════════════════════════╝
echo.

REM Créer dossier archives_versions si nécessaire
if not exist "archives_versions" mkdir "archives_versions"
echo ✓ Dossier archives_versions créé
echo.

echo [1/6] Archivage des anciennes versions...
REM Déplacer anciens .spec
if exist "NiTriTe_V17_Portable.spec" move /Y "NiTriTe_V17_Portable.spec" "archives_versions\" >nul
if exist "NiTriTe_V18_Portable.spec" move /Y "NiTriTe_V18_Portable.spec" "archives_versions\" >nul

REM Déplacer anciens scripts
if exist "Lancer_nitrite_v17.bat" move /Y "Lancer_nitrite_v17.bat" "archives_versions\" >nul
if exist "LANCER_NITRITE_V14.bat" move /Y "LANCER_NITRITE_V14.bat" "archives_versions\" >nul
for %%F in (*.bat) do (
    if /I not "%%F"=="BUILD_V20.bat" (
        if /I not "%%F"=="LANCER_NITRITE_V20.bat" (
            if /I not "%%F"=="reorganiser_projet.bat" (
                move /Y "%%F" "archives_versions\" >nul 2>&1
            )
        )
    )
)
echo ✓ Anciennes versions archivées
echo.

echo [2/6] Archivage des logs et builds...
if exist "logs" (
    if not exist "archives_versions\logs" mkdir "archives_versions\logs"
    xcopy /E /I /Y "logs\*" "archives_versions\logs\" >nul 2>&1
    rmdir /s /q "logs" 2>nul
)
if exist "build" rmdir /s /q "build" 2>nul
if exist "release" (
    move /Y "release" "archives_versions\release" >nul 2>&1
)
echo ✓ Logs et builds archivés
echo.

echo [3/6] Archivage de la documentation ancienne...
if exist "docs\archive" (
    if not exist "archives_versions\docs_archive" mkdir "archives_versions\docs_archive"
    xcopy /E /I /Y "docs\archive\*" "archives_versions\docs_archive\" >nul 2>&1
)
if exist "reports" (
    move /Y "reports" "archives_versions\reports" >nul 2>&1
)
if exist "CHANGELOG_V18.5.md" move /Y "CHANGELOG_V18.5.md" "archives_versions\" >nul
if exist "BUILD_SUCCESS.md" move /Y "BUILD_SUCCESS.md" "archives_versions\" >nul
if exist "CORRECTIONS_MODE_PORTABLE.md" move /Y "CORRECTIONS_MODE_PORTABLE.md" "archives_versions\" >nul
echo ✓ Documentation archivée
echo.

echo [4/6] Archivage des backups...
if exist "backups_corrections" (
    move /Y "backups_corrections" "archives_versions\backups" >nul 2>&1
)
if exist "archive" (
    if not exist "archives_versions\archive_racine" mkdir "archives_versions\archive_racine"
    xcopy /E /I /Y "archive\*" "archives_versions\archive_racine\" >nul 2>&1
    rmdir /s /q "archive" 2>nul
)
echo ✓ Backups archivés
echo.

echo [5/6] Nettoyage des fichiers temporaires...
del /F /Q nul 2>nul
del /F /Q .bash_history 2>nul
if exist "__pycache__" rmdir /s /q "__pycache__" 2>nul
if exist "src\__pycache__" rmdir /s /q "src\__pycache__" 2>nul
if exist "src\v14_mvp\__pycache__" rmdir /s /q "src\v14_mvp\__pycache__" 2>nul
echo ✓ Fichiers temporaires supprimés
echo.

echo [6/6] Création structure propre...
if not exist "logs" mkdir "logs"
echo ✓ Structure créée
echo.

echo.
echo ╔═══════════════════════════════════════════════════════════╗
echo ║          ✓ RÉORGANISATION TERMINÉE !                      ║
echo ╚═══════════════════════════════════════════════════════════╝
echo.
echo 📁 Structure finale:
echo    📂 src/              - Code source
echo    📂 data/             - Données et configurations
echo    📂 assets/           - Ressources (icônes, images)
echo    📂 logiciel/         - Outils diagnostiques portables
echo    📂 Script Windows/   - Scripts système Windows
echo    📂 logs/             - Logs d'exécution
echo    📂 archives_versions/ - Anciennes versions et backups
echo    📄 BUILD_V20.bat     - Script de build
echo    📄 LANCER_NITRITE_V20.bat - Script de lancement dev
echo    📄 NiTriTe_V20_Portable.spec - Configuration PyInstaller
echo    📄 README.md         - Documentation
echo.
pause
