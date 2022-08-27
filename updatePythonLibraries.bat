@echo off
if not defined VIRTUAL_ENV (CALL %~dp0\activateVenv.bat)
if defined VIRTUAL_ENV (pip install -r %~dp0\requirements.txt)