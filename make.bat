@echo off
for /r %%i in (Main_Seminar_Dec*.tex) do texify -cp %%i
