---
geometry: margin=2.5cm
output: pdf_document
---

# GEG6230 - Advanced Geospatial Science

## Assignment 1 - Data visualisation project

- Contact: Stuart Grieve (s.grieve@qmul.ac.uk)
- Credit: 45% module mark (6.75 credits)
- Page limit: 1 A3 page

You are working as a GIS analyst and have been instructed by your client to assist in the identification of suitable hydro power sites across the Lake District. A number of candidate catchments have been proposed but the client does not understand the data about each catchment as they have never done a GIS course.

Create a one page visualisation, highlighting **some** of the information provided by the client in a more accessible manner. **Your final visualisation should include 2 maps and 2 graphs.**

There are 4 catchments, each with a unique number: `75001, 75004, 75006, 75007`

The following data is available on QMplus for each catchment:

- DEM
- Shapefile boundary
- Landcover statistics and legend
- River daily flow measurements over time
- Precipitation over time
- Day and night temperature over time

The precipitation, temperature and flow data is from the period 1-1-2013 to 31-12-2015, with each day numbered sequentially, e.g. day number 366 will be 1-1-2014.

There is also a general DEM of the area containing all of the catchments, called `Lake_District.tif`.

If you wish, you can find additional information about these catchments from the [National River Flow Archive](https://nrfa.ceh.ac.uk/data/search), using the unique catchment numbers to find the 4 catchments we are interested in.

Factors which may make a catchment good for a hydro power scheme:

- Steep slopes
- High rainfall and discharge
- Consistent rainfall and discharge over the year
- Landcover types which are conducive to high runoff
- Temperatures usually above freezing

**Note that which catchments you choose is unimportant, this assignment will be graded based on the presentation of the data, not the identification of the best catchments for hydro power.**

## Assignment 2 - Data visualisation presentation

- Contact: Stuart Grieve (s.grieve@qmul.ac.uk)
- Credit: 10% module mark (1.5 credits)
- Duration: 5 minutes

Having created your one page visualisation for assignment 1, present this visualisation. You should explain:

- What data you chose to present and why
- What design choices you have made
- What challenges you overcame to present the data

**As this is a Late Summer Resit, there will not be a presentation, but rather you must submit your slides and up to 1000 words of notes outlining what you would have spoken about.**

## Assignment 3 - GIS project

- Contact: Stuart Grieve (s.grieve@qmul.ac.uk)
- Credit: 45% module mark (6.75 credits)
- Page limit: 4 A4 pages + code

You have a dataset of landslide scar outline polygons for the [Coweeta Experimental Catchment](https://coweeta.uga.edu/) in North Carolina, USA. As part of ongoing efforts to better understand landsliding in this area, you need to calculate the factor of safety (`Fs`) of each of these polygons.

Factor of safety is a measure of the balance between driving and resisting forces operating on hillslope material. When `Fs` is below 1 a failure is likely, and values above 1 suggest that the hillslope is stable under current conditions. We calculate the factor of safety as follows:

$$Fs = \frac{ C } { h \rho_s g } + \frac{W \cos{\theta} \tan{\phi}} {\sin{\theta}}$$

Where:

- $C:$ soil cohesion
- $\theta:$ topographic slope
- $\phi:$ friction angle
- $\rho_s:$ soil density
- $h:$ soil depth
- $g:$ gravitational acceleration = $9.81~ms^{-2}$
- $W:$ hydrological constant

You have access to the following datasets on QMplus:

- Coweeta_clip.tif
- Coweeta_slope.tif (in radians)

Alongside a series of numbered polygon shapefiles, called `scar_1.shp` through to `scar_15.shp`. Each of these shapefiles has the following attributes, measured in the field:

- Friction angle (in radians)
- Soil depth
- Soil density
- Hydrological constant


## Tasks

1. Develop a workflow to calculate the factor of safety of all of the scar polygons, using **ArcGIS ModelBuilder**.
1. Develop a workflow to calculate the factor of safety of all of the scar polygons, **using Python**.
1. Create a map (including a caption) showing the variations in factor of safety across some (or all) of the study area.
1. Create a boxplot of the `Fs` values calculated using Python.
1. Write a 1 page discussion of the pros and cons of these two approaches to automation, with regard to reproducibility.

## What to submit

1. A 4 page document containing:
- **Page 1:** An image of the ArcGIS ModelBuilder workflow
- **Page 2:** A map of the calculated factor of safety data for some (or all) of Coweeta, **including a brief caption describing it.**
- **Page 3:** A boxplot of the Fs values for the 15 landslide scars, **including a brief caption describing it.**
- **Page 4:** One written page of discussion of the pros and cons of these two approaches to automation, with regard to reproducibility.

2. A copy of the Jupyter notebook containing the python workflow to calculate `Fs` for each catchment.

**These two files should be placed in a `.zip` file, with your student number as the filename, and submitted.**
