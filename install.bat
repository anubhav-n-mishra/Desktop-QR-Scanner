@echo off
echo Installing QRiftly dependencies...
echo.

REM Check if Python is installed
python --version >nul 2>&1
if errorlevel 1 (
    echo ERROR: Python is not installed or not in PATH
    echo Please install Python 3.7 or higher from https://python.org
    pause
    exit /b 1
)

echo Python found, installing packages...
pip install -r requirements.txt

if errorlevel 1 (
    echo.
    echo ERROR: Failed to install dependencies
    echo Please check your internet connection and try again
    pause
    exit /b 1
)

echo.
echo ✓ Dependencies installed successfully!
echo.
echo You can now run QRiftly with:
echo   python qr_scanner.py
echo.
echo Or build an executable with:
echo   build.bat
echo.
echo To create test QR codes:
echo   python create_test_qr.py
echo.
pause