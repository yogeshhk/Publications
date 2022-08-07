@echo off
for /r %%i in (Main*Victory*.tex) do texify -cp %%i
