@ECHO OFF
@REM activates virtual env from any location
@REM It takes absolute directory path of this batch file and activates virtual env
if exist %~dp0\venv\Scripts\activate.bat (
	CALL %~dp0\venv\Scripts\activate.bat
) else (
	printf "virtual environment not found"
)