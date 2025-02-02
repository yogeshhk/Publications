@echo off
for /r %%i in (Main_*Gems*.tex) do texify --engine=luatex -cp %%i
