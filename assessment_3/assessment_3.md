---
geometry: margin=2.5cm
output: pdf_document
---

# GEG6230 - Advanced Geospatial Science - Assignment 3

## GIS project

- Contact: Stuart Grieve (s.grieve@qmul.ac.uk)
- Credit: 45% module mark (6.75 credits)
- Page limit: 3 A4 pages + code
- Deadline: TBD, via QMplus

You have a dataset of landslide scar outline polygons for the [Coweeta Experimental Catchment](coweeta lter link) in North Carolina, USA. As part of ongoing efforts to better understand landsliding in this area, you need to calculate the factor of safety (`Fs`) of each of these polygons.

Factor of safety is a measure of the balance between driving and resisting forces operating on hillslope material. When `Fs` is below 1 a failure is likely, and values above 1 suggest that the hillslope is stable under current conditions. We calculate the factor of safety as follows:

$$Fs = \frac{ C \cos{\theta} \tan{\phi}} {h \rho_s g \sin{\theta}} $$

Where:

- $C:$ soil cohesion
- $\theta:$ topographic slope
- $\phi:$ friction angle
- $\rho_s:$ soil density = $N$
- $h:$ soil depth
- $g:$ gravitational acceleration = $9.81~ms^{-2}$

You have access to the following datasets on QMplus:

- soil_cohesion.tif
- Coweeta_DEM.tif
- Coweeta_slope.tif

Alongside a series of numbered polygon shapefiles, called `scar_1.shp` through to `scar_N.shp`. Each of these shapefiles has the following attributes, measured in the field:

- Friction angle
- Soil depth


## Tasks

1. Develop a workflow to calculate the factor of safety of all of the scar polygons, using **ArcGIS ModelBuilder**.
1. Develop a workflow to calculate the factor of safety of all of the scar polygons, **using Python**.
1. Create a map (including a caption) showing the variations in factor of safety across some (or all) of the Coweeta catchment.
1. Write a 1 page discussion of the pros and cons of these two approaches to automation, with regard to reproducibility.

## What to submit

1. A 3 page document containing:
- **Page 1:** An image of the ArcGIS ModelBuilder workflow
- **Page 2:** A map of the calculated factor of safety data for some (or all) of Coweeta, **including a brief caption describing it.**
- **Page 3:** One written page of discussion of the pros and cons of these two approaches to automation, with regard to reproducibility.

2. A copy of the Jupyter notebook containing the python workflow to calculate `Fs` for each catchment.

**These two files should be placed in a `.zip` file, with your student number as the filename, and submitted to QMplus.**

## Feedback

You will be given time in class to begin this assignment, where you will be able to discuss your ideas with Stuart, as well as your classmates.

If you require further help you can attend Stuart's Advice and Feedback hours (without an appointment):

- Tuesday 14:00-15:00
- Thursday 10:00-11:00

Or at any other time by appointment, email Stuart (s.grieve@qmul.ac.uk) to arrange one.
