@ECHO OFF
if defined VIRTUAL_ENV (CALL %~dp0\deactivateVenv.bat)
rmdir venv /s /Q