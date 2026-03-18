@echo off
for /r %%i in (Main_*MSP*.tex) do texify --engine=luatex  -cp %%i
