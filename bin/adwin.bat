@echo off 
CD /D "%~dp0"
rem changing title
title Penta~AdminCommandRunner
rem using batch file to run administrative commands on windows
rem %1 ----- to check the command
rem %2 ------ count
rem %3 ----- hostname
echo %1>> cmd.temp
echo %2>> count.temp
echo %3>> hostname.temp

rem ------------------------------------------------------
rem Checking if the script is being ran as admin.if not, it will run itslef as admin
:checkPrivileges
mkdir "%windir%\AdminCheck" 2>nul
if '%errorlevel%' == '0' rmdir "%windir%\AdminCheck" & goto gotPrivileges else goto getPrivileges
:getPrivileges
echo.
echo Getting Administrative Privileges
echo.
runadmin.vbs %0
exit
rem --------------------------------------------------------- 
:gotPrivileges
title Penta~AdminCommandRunner
color 0a
CD /D "%~dp0"
set /p farg=<cmd.temp
set /p sarg=<hostname.temp
set /p targ=<count.temp
set targ_1=%targ:'=%
echo ARGUMENTS RECEIVED:
echo %farg%
echo %sarg%
echo %targ_1%
echo.
del cmd.temp & del count.temp & del hostname.temp
if '%farg%' == 'pn' goto PING
if '%farg%' == 'tr' goto TRACEROUTE
echo Command Interpretation Error!
pause
exit
:PING
echo ACTION:PING
python -c "from pythonping import ping ; ping('%sarg%',verbose=True,count=%targ_1%)"
pause
exit
:TRACEROUTE
echo ACTION:TRACEROUTE
rem writing to a file and running it
echo from icmplib import traceroute>> troute.py
echo hops = traceroute("%sarg%")>> troute.py
echo print('Distance/TTL    Address            Average round-trip time')>> troute.py
echo Last_Distance = ^0>> troute.py
echo for hop in hops:>>troute.py
echo     if Last_Distance + 1 != hop.distance:>> troute.py
echo         print('Some gateways are not responding')>> troute.py
echo     print(f'{hop.distance}               {hop.address}              {hop.avg_rtt} ms')>> troute.py
echo     Last_Distance = hop.distance>>troute.py
python troute.py
del troute.py
pause