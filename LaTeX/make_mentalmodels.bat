@echo off
for /r %%i in (Main_*MentalModels*.tex) do texify -cp %%i
