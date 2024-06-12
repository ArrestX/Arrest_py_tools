@echo off
setlocal enabledelayedexpansion
for /f "tokens=1-3 delims=," %%i in (tmp2.txt) do (
    set name=%%i
    set age=%%j
    set address=%%k
    echo name=!name!   age=!age!   address=!address!
)
pause