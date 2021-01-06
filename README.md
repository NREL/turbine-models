# Documentation for NREL Wind Turbine Power Curve Archive
## Welcome to the repository for the wind turbine power curve archive.

The intention of this branch of the repositiory is to provide all the files for the documentation built with Sphinx and hosted on GitHub Pages. This keeps them seperate from the tabular data files stored on the master branch.

## Structure
The /docs directory has all the .html files needed for building the site.
.nojekyll, make.bat, and Makefile are all needed to run Sphinx on Windows. I use Anaconda Prompt in a virtual environment that has Sphinx installed.

The /source directory has all the source .rst files which are needed to create the html files for the site. There is one for each turbine model as well as the index outlining the structure of the site.

Plots for each turbine model that are shown on each turbine's page are included in multiple locations as a result of the source and build setup.

Once you run the batch file with the command 'make html' from the directory containing the make.bat, the html files will appear in the directory:
docs/build/html.
