@echo off
for /r %%i in (Main_Tweet*.tex) do texify -cp %%i
