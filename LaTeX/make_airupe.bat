@echo off
for /r %%i in (Main_Book_AIRupe*.tex) do texify --engine=xetex  -cp %%i
