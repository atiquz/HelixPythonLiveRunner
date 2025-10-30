:: Replace the C:\Users\atiqu\Desktop\Python Learning or C:\Users\atiqu\Desktop\pythonLearning.bat according your specific folder and bat location.

@echo off
cd /d "C:\Users\atiqu\Desktop\Python Learning"

:: If this file is called with "watch" argument, run watcher
if "%~1"=="watch" goto watcher

:: Otherwise, launch Windows Terminal with split panes
wt.exe cmd /k "cd /d C:\Users\atiqu\Desktop\Python Learning && hx main.py" ^
; split-pane -V cmd /k "cd /d C:\Users\atiqu\Desktop\Python Learning && \"C:\Users\atiqu\Desktop\pythonLearning.bat\" watch"
exit /b

:watcher
setlocal
set "file=main.py"
set "lastmod="

:loop
for %%A in ("%file%") do (
    if not "%%~tA"=="%lastmod%" (
        cls
        echo Running main.py ...
        echo ---------------------------------------
        python "main.py"
        echo ---------------------------------------
        set "lastmod=%%~tA"
    )
)
timeout /t 1 >nul
goto loop
