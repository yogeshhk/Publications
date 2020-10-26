@echo off
for /r %%i in (Main_Talk_*.tex) do texify -cp %%i
