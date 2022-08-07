@echo off
for /r %%i in (Main*Making*.tex) do texify -cp %%i
