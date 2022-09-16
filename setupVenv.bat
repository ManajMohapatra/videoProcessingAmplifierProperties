@ECHO OFF
@REM  It creates virtual environment with system packages

py -m venv %~dp0\venv
CALL activateVenv.bat
CALL updatePythonLibraries.bat