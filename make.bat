@echo off
for /r %%i in (Main_Seminar_Gems*.tex) do texify --engine=xelatex %%i
