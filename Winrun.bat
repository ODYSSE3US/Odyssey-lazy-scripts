:Basic_Info
@echo off
color 0a
title "ODYSSEY EASY RUN"

set /p Q=Do you want to Install, Run Or Exit? [I/R/E]
IF %Q% == I goto Check_And_Q
IF %Q% == R goto Start_Script
IF %Q% == E exit

:Check_And_Install
cls


:Start_Script
cls
echo Starting Script...
start python Menus.py
exit