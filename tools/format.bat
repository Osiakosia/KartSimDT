@echo off

echo ========================================
echo KartSimDT Code Formatter
echo ========================================

echo.
echo [1/2] Running Ruff (auto-fix)...
ruff check . --fix

if errorlevel 1 exit /b 1

echo.
echo [2/2] Running Black...
black .

if errorlevel 1 exit /b 1

echo.
echo ========================================
echo Formatting completed.
echo ========================================