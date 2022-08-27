@ECHO OFF
if defined VIRTUAL_ENV (deactivate)
if not defined VIRTUAL_ENV (printf "virtual environment is not active")