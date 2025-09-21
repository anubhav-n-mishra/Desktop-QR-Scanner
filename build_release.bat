@echo off
echo 🚀 Building QRiftly for Distribution...
echo.

:: Check if Python is available
python --version >nul 2>&1
if errorlevel 1 (
    echo ❌ Python is not installed or not in PATH
    echo Please install Python from https://python.org
    pause
    exit /b 1
)

:: Install dependencies
echo 📦 Installing dependencies...
pip install opencv-python pyzbar Pillow pyautogui numpy pyinstaller

:: Clean previous builds
if exist "dist" rmdir /s /q "dist"
if exist "build" rmdir /s /q "build"
if exist "*.spec" del "*.spec"

:: Build executable
echo 🔨 Building executable...
pyinstaller --onefile --windowed --name "QRiftly" qr_scanner.py

:: Check if build was successful
if exist "dist\QRiftly.exe" (
    echo.
    echo ✅ Build successful!
    echo 📁 Executable: dist\QRiftly.exe
    for %%A in ("dist\QRiftly.exe") do echo 📊 Size: %%~zA bytes
    echo.
    echo 🎉 Ready for distribution!
) else (
    echo ❌ Build failed!
)

pause