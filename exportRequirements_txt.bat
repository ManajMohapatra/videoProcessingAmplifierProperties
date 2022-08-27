@echo off
if not defined VIRTUAL_ENV (CALL %~dp0\activateVenv.bat)
if defined VIRTUAL_ENV (pip freeze > %~dp0\requirements.txt)