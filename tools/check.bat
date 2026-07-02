@echo off

echo ========================================
echo KartSimDT Quality Checks
echo ========================================

echo.
echo [1/4] Ruff
ruff check .

if errorlevel 1 exit /b 1

echo.
echo [2/4] Black
black --check .

if errorlevel 1 exit /b 1

echo.
echo [3/4] MyPy
mypy src

if errorlevel 1 exit /b 1

echo.
echo [4/4] Pytest
pytest -v

echo.
echo ========================================
echo All checks passed.
echo ========================================