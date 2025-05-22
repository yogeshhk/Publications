@echo off
for /r %%i in (Main_Book_ThirdBrain_AIRupe.tex) do texify --engine=xetex  -cp %%i
