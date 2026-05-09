@echo off
for /r %%i in (Main_Book_VyuhaRupe*.tex) do texify --engine=xetex  -cp %%i
