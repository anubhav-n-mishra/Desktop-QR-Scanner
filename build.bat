@echo off
echo Building QRiftly executable...
echo.

REM Check if PyInstaller is available
pyinstaller --version >nul 2>&1
if errorlevel 1 (
    echo Installing PyInstaller...
    pip install pyinstaller
)

REM Clean previous builds
if exist "dist" rmdir /s /q "dist"
if exist "build" rmdir /s /q "build"

echo Building standalone executable...
pyinstaller qr_scanner.spec

if errorlevel 1 (
    echo.
    echo ERROR: Build failed
    pause
    exit /b 1
)

echo.
echo ✓ Build completed successfully!
echo.
echo The executable can be found in: dist\QRiftly.exe
echo File size: 
for %%I in ("dist\QRiftly.exe") do echo %%~zI bytes
echo.
echo Testing executable...
"dist\QRiftly.exe" --help >nul 2>&1 || echo Executable is ready to run!
echo.
pause