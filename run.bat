cd source
call build.bat

move server.exe ..\dist >nul
move client.exe ..\dist >nul

start "" ".\ngrok.exe" tcp 12345
start "" "..\dist\server.exe"
start "" "..\dist\client.exe"