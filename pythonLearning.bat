@echo off
cd /d "C:\Users\atiqu\Desktop\Python Learning"

:: Open Windows Terminal: left pane -> hx main.py ; right pane -> run watcher
wt.exe new-tab cmd /k "cd /d C:\Users\atiqu\Desktop\Python Learning && hx main.py" ^
; split-pane -V cmd /k "cd /d C:\Users\atiqu\Desktop\Python Learning && python.exe watch.py"
exit /b
