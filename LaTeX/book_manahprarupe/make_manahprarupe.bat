@echo off
for /r %%i in (Main_Book_ManahPrarupe*.tex) do texify --engine=xetex  -cp %%i
