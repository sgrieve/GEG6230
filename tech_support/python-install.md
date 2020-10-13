---
geometry: margin=2.5cm
output: pdf_document
urlcolor: blue
colorlinks: true
---

# Installing Python on your own computer

If you wish to try and install Python on your own computer you can follow these instructions from [Software Carpentry](software-carpentry.org) to install on Windows and MacOS.

There are a number of different versions of Python you can choose to install. The only requirement is that you install version 3.x (e.g. 3.7) rather than the older version 2.7.

**Please note that due to the size of the class I am unable to provide individual tech support to students who decide to do this, and that AppsAnywhere remains the preferred way of accessing Python for this course.**

## MacOS

[Watch a Video tutorial](https://www.youtube.com/watch?v=TcSAln46u9U)

1. Open https://www.anaconda.com/products/individual#download-section with your web browser.
1. Download the Anaconda Installer with Python 3 for macOS (you can either use the Graphical or the Command Line Installer).
1. Install Python 3 by running the Anaconda Installer using all of the defaults for installation.

## Windows

[Watch a Video tutorial](https://www.youtube.com/watch?v=xxQ0mzZ8UvA)

1. Open https://www.anaconda.com/products/individual#download-section with your web browser.
1. Download the Anaconda for Windows installer with Python 3. (If you are not sure which version to choose, you probably want the 64-bit Graphical Installer `Anaconda3-...-Windows-x86_64.exe`)
1. Install Python 3 by running the Anaconda Installer, using all of the defaults for installation except make sure to check **Add Anaconda to my PATH environment variable.**


# Installing Geospatial packages

Having successfully installed python using the instructions above, we now need to install some specialist geospatial packages that we will be using during the course.

1. Open the Anaconda Prompt from the start menu in Windows, or open a terminal in MacOS.
1. Enter the command `conda install shapely fiona rasterio rasterstats` and press enter.

This should install all the needed packages for this module. We can test everything has worked correctly:

1. Launch a notebook with the command `jupyter notebook` and once the browser window opens, create a new notebook
1. Inside a notebook cell enter the following python code: `import shapely, fiona, rasterio, rasterstats` and press shift-enter to run the code.
1. If the cell executes without displaying anything on the screen, the install has been successful.
