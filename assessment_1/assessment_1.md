---
geometry: margin=2.5cm
output: pdf_document
urlcolor: blue
colorlinks: true
---

# GEG6230 - Advanced Geospatial Science - Assignment 1

## Data visualisation project (Assignment 1)

- Contact: Stuart Grieve (s.grieve@qmul.ac.uk)
- Credit: 50% module mark (7.5 credits)
- Page limit: 1 A3 page
- Deadline: 2pm TBD, via QMplus

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
