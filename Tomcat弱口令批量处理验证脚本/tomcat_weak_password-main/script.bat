setlocal enabledelayedexpansion
for /f "tokens=1-3 delims=," %%i in (ip.txt) do (
    set name=%%i
    start cmd /c  python tomcat_weak_password.py -u !name!

)