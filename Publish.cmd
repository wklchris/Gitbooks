@echo off
set /p des="Input discipline of the book (e.g. CS): "
cd %des%

set /p fdname="Input Gitbook folder name (e.g. Gitbook): "
cd %fdname%

if not exist publish\NUL mkdir publish
cd ..

gitbook build %fdname% %fdname%/publish
