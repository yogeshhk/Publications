@echo off
for /r %%i in (Main_*Gems*.tex) do texify -cp %%i
