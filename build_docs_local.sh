# builds Sphinx documentation localy
# runs napoleon extension to properly pre-parse Google style docstrings
cd ./docs
sphinx-apidoc -f -o ./source ../apitalker
make html
cd ..   