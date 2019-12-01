@echo off
for /r %%i in (Main*Yog*.tex) do texify -cp %%i
