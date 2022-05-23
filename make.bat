:: The medium article should be in a folder (called `name`) and be called 
:: main.md. Images should be placed in a resources subfolder.

@ECHO OFF

set name=%1

:: create one image per equation and acreate a temp file with the equations 
:: replaced by images
python md-equations.py %name%

:: upload all images
git add --all
git commit -m "article update"
git push

echo ...
echo Waiting for the upload to be taken into account by ever systems
echo ...
timeout -T 10 -NOBREAK

:: publish temp file to medium
mdium publish %name%/tmp.md

:: delete temp file
del %name%/tmp.md