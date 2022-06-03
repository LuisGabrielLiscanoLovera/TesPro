@echo off
set /p CommitName="Commit: "
echo Commi es : %CommitName%
 
 python keyC.py
 git add .
 git status 
 git commit -m "%CommitName%"
 git push
 python keyE.py
 python keyD.py
 
for /f "tokens=1-2 delims=:" %%a in ('ipconfig^|find "IPv4"') do set ip=%%b
set ip=%ip:~1%
echo %ip%

python .\manage.py runserver %ip%:4433