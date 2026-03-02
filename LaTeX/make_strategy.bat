@echo off
for /r %%i in (Main_*Strategy*.tex) do texify -cp %%i
