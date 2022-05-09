:: The medium article should be in a folder (called `name`) and be called 
:: main.md. Images should be placed in a resources subfolder.

@ECHO OFF

set name=%1

echo "coucuo"

:: create one image per equation and acreate a temp file with the equations 
:: replaced by images
python md-equations.py %name%

:: upload all images
rem git commit -am "article update"

:: publish temp file to medium
rem mdium publish %name%/tmp.md

:: delete temp file