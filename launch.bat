@echo off
title RPG
color 1c
SET pyth=C:\Python27\python.exe
echo %cd%
echo.
echo 2016-05-26 14:05 by Emily
echo.
:go
SET file="rpg.py"
%pyth% %file%
pause
goto :go
