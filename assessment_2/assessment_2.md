---
geometry: margin=2.5cm
output: pdf_document
urlcolor: blue
colorlinks: true
---

# GEG6230 - Advanced Geospatial Science - Assignment 2

## GIS project

- Contact: Stuart Grieve (s.grieve@qmul.ac.uk)
- Credit: 50% module mark (7.5 credits)
- Page limit: 4 A4 pages + code
- Deadline: 16/12/20 2pm, via QMplus

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
1. Write a 2 page discussion of the pros and cons of these two approaches to automation, with regard to reproducibility.

## What to submit

1. A 5 page document containing:
- **Page 1:** An image of the ArcGIS ModelBuilder workflow
- **Page 2:** A map of the calculated factor of safety data for some (or all) of Coweeta, **including a brief caption describing it.**
- **Page 3:** A boxplot of the Fs values for the 15 landslide scars, **including a brief caption describing it.**
- **Pages 4-5:** Two written pages of discussion of the pros and cons of these two approaches to automation, with specific regard to reproducibility.

2. A copy of the Jupyter notebook containing the python workflow to calculate `Fs` for each catchment **AND** the code to create the boxplot of Fs values.

**These two files should be placed in a `.zip` file, with your student number as the filename, and submitted to QMplus.**


## References

For the write up on the reproducibility of the methods these two references will help you get started. Both are available as PDFs on QMplus under the week 12 section.

Church, M., Dudill, A., Venditti, J. G., & Frey, P. (2020). Are results in geomorphology reproducible?. Journal of Geophysical Research: Earth Surface, 125(8), e2020JF005553.

Grieve, S. W. D., Clubb, F. J., & Mudd, S. M. (2020). Reproducible topographic analysis. In Developments in Earth Surface Processes (Vol. 23, pp. 339-367). Elsevier.
