@echo off
REM DUP Development Helper Script for Windows

echo ================================================
echo DUP - Drive Upload Program
echo Development Helper Script
echo ================================================
echo.

if "%1"=="" goto help
if "%1"=="install" goto install
if "%1"=="build" goto build
if "%1"=="test" goto test
if "%1"=="clean" goto clean
if "%1"=="run" goto run
goto help

:install
echo Installing DUP in development mode...
python -m pip install -e .
if %errorlevel% neq 0 (
    echo ERROR: Installation failed
    exit /b 1
)
echo.
echo SUCCESS: DUP installed in development mode
echo Run 'dup login' to get started
goto end

:build
echo Building Windows executable...
python build_windows.py
if %errorlevel% neq 0 (
    echo ERROR: Build failed
    exit /b 1
)
echo.
echo SUCCESS: Executable created at dist\dup.exe
echo To create installer, open installer\windows.iss in Inno Setup
goto end

:test
echo Running DUP commands...
echo.
echo Testing version...
dup version
echo.
echo Testing pwd...
dup pwd
echo.
echo Testing ls...
dup ls
echo.
echo All basic tests completed
goto end

:clean
echo Cleaning build artifacts...
if exist build rmdir /s /q build
if exist dist rmdir /s /q dist
if exist dup.spec del /q dup.spec
if exist *.pyc del /s /q *.pyc
if exist __pycache__ rmdir /s /q __pycache__
echo.
echo Cleaned build directories
goto end

:run
echo Running DUP...
python -m dup %2 %3 %4 %5 %6 %7 %8 %9
goto end

:help
echo Usage: dev.bat [command] [options]
echo.
echo Commands:
echo   install   - Install DUP in development mode
echo   build     - Build Windows executable
echo   test      - Run basic tests
echo   clean     - Clean build artifacts
echo   run       - Run DUP (e.g., dev.bat run login)
echo   help      - Show this help message
echo.
echo Examples:
echo   dev.bat install
echo   dev.bat build
echo   dev.bat run login
echo   dev.bat run ls
echo   dev.bat clean
goto end

:end
echo.
echo ================================================
