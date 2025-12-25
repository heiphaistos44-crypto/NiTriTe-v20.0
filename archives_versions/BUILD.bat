@echo off
chcp 65001 >nul
cls
echo ========================================
echo    NiTriTe V18 - BUILD PORTABLE
echo ========================================
echo.

REM Lancer le script de build Python
py -3.12 build_tools\build_portable_fixed.py

if %ERRORLEVEL% EQU 0 (
    echo.
    echo ========================================
    echo    BUILD TERMINE AVEC SUCCES!
    echo ========================================
    echo.
    echo Executable: dist\NiTriTe_V18_Portable.exe
    echo Package:    release\
    echo.
) else (
    echo.
    echo ========================================
    echo    ERREUR LORS DU BUILD
    echo ========================================
    echo.
)

pause
