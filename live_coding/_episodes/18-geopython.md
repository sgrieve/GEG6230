---
title: GeoPython
---

We are now going to build on the ideas of geospatial workflows created in ArcGIS's ModelBuilder, and our python skills to explore some of the most popular open source GIS python packages.

## Before we start

We are going to come across a new python datatype today, known as a `dictionary`. This is a special datatype which allows us to link a key to a value:

~~~
dictionary = {'key': 'value'}
print(dictionary['key'])
~~~
{: .language-python}

We access elements from a dictionary, not using an index like we do for lists or arrays, but with its key. Values can be accessed using the corresponding key:

~~~
ages = {'stuart': 30, 'william': 85, 'david': 57}
print(ages['david'])
~~~
{: .language-python}

We can add new key value pairs as follows:

~~~
ages['jimmy'] = 27
~~~
{: .language-python}

If we need to loop over all of the items in a dictionary, we can use the `.items()` function to get each key, value pair in turn:

~~~
for name, age in ages.items():
    print(name, age)
~~~
{: .language-python}

We can create a new, empty dictionary with a pair of curly brackets, and then add new key, value pairs. Note that values can be any python object, including another dictionary:

~~~
newdict = {}
newdict['key 1'] = ['lists', 'can', 'be', 'dict', 'values']
newdict['key 2'] = {'key3': 100}
~~~
{: .language-python}

With these nested structures we can access values inside the internal list or dictionary:

~~~
print(newdict['key 1'][1])
print(newdict['key 2']['key3'])
~~~
{: .language-python}


## Downloading our data

We will be using some data taken from last week's practical, a zipfile containing the data is available on QMplus. **It is important that you put these datasets in folders that you can find from your Jupyter Notebook.**

## Points, lines, and polygons

Lets start with an import from the `shapely` library, which we can use to do vector based GIS analysis:

~~~
from shapely.geometry import Point
~~~
{: .language-python}

We have imported the `Point` class, which unsurprisingly, represents points. We can create a new point as follows:

~~~
mypoint = Point(2, 2)
~~~
{: .language-python}

This point object has a series of attributes describing it, such as:

~~~
print(mypoint.x)
print(mypoint.y)
~~~
{: .language-python}

Which allows us to access a point's x and y coordinate values. Now lets move on to lines, known to shapely as **linestrings**. Again, we need to import the geometry we wish to use:

~~~
from shapely.geometry import LineString
~~~
{: .language-python}

And we can create a LineString as follows:

~~~
myline = LineString([(1, 1), (10, 10)])
~~~
{: .language-python}

LineStrings have a length:

~~~
print(myline.length)
~~~
{: .language-python}

~~~
from shapely.geometry import Polygon
~~~
{: .language-python}

And we can create a Polygon as follows:

~~~
mypolygon = Polygon([(0, 0), (5, 25), (20, 20), (20, 0)])
~~~
{: .language-python}

Polygons have a perimeter(length), area and bounding box:

~~~
print(mypolygon.length)
print(mypolygon.area)
print(mypolygon.bounds)
~~~
{: .language-python}

### Viewing our geometries with matplotlib

We can use matplotlib to quickly observe shapely geometries. Note that when plotting a polygon or linestring, we need to include the `*`, this is a shortcut command that separates out the x and y coordinates into the right format for matplotlib.

~~~
import matplotlib.pyplot as plt

plt.scatter(mypoint.x, mypoint.y)
plt.plot(*mypolygon.exterior.xy)
plt.plot(*myline.xy)
~~~
{: .language-python}


## Analyzing our geometries

Now that we have a point, line and polygon, we can explore some spatial analyses.

### Within

Test if an object is inside another object.

~~~
print(mypoint.within(mypolygon))
~~~
{: .language-python}

This shows us that the point is inside the polygon. What happens if we do the same thing with the line?

~~~
print(myline.within(mypolygon))
~~~
{: .language-python}

What if we swap the order we use the objects in?

~~~
print(mypolygon.within(mypoint))
~~~
{: .language-python}

It tells us `False`, but doesn't tell us anything about the logic of what we are trying to do.

Points can also be within a line:

~~~
print(mypoint.within(mypolygon))
~~~
{: .language-python}

What if something crosses an edge? We'll create a new LineString to test this.

~~~
longline = LineString([(1, 1), (10, 10), (25, 32)])
~~~
{: .language-python}

and we can check that it is indeed crossing the polygon:

~~~
plt.plot(*mypolygon.exterior.xy)
plt.plot(*longline.xy)
~~~
{: .language-python}

So now we can test our idea, this time using the `within` command as the condition in our `if` statement:

~~~
if longline.within(mypolygon):
    print('Overlaps are ok!')
else:
    print('Overlaps do not work')
~~~
{: .language-python}

### Contains

If we want to invert the relationship, we can use `contains` instead of `within`. This works exactly the same as `within`, with the same conditions that all of an object must be inside the other object:

~~~
print(mypolygon.contains(mypoint))
~~~
{: .language-python}

### Intersects

What if we want to identify an overlap between two objects? For this we can use the `intersects` command:

~~~
print(myline.intersects(mypolygon))
print(mypoint.intersects(mypolygon))
~~~
{: .language-python}

This does not require a complete containment of an object in order to return True.

### Crosses

`Crosses` is a stricter identifier of an overlap between two objects, which will return false if an object is comepletely contained within another object. So:

~~~
print(longline.crosses(mypolygon))
print(mypoint.crosses(mypolygon))
~~~
{: .language-python}

`longline` extends outside the polygon, so this returns True, whereas the shorter `myline` is totally within the polygon so returns False.


### Buffering

We can create buffers of our objects using the buffer command:

~~~
pointbuffer = mypoint.buffer(10)
print(type(pointbuffer))
~~~
{: .language-python}

This creates a shapely polygon that we can then use for any standard operation. Lets check what the buffer looks like:

~~~
plt.plot(*pointbuffer.exterior.xy)
plt.scatter(mypoint.x, mypoint.y)
plt.axis('equal')
~~~
{: .language-python}

Buffers sizes are in map units, and can be performed on any shapely geometry:

~~~
linebuffer = myline.buffer(20)
polygonbuffer = mypolygon.buffer(15.5)
~~~
{: .language-python}

We can also use negative buffers to make polygons smaller, but if you give too large a value you will wind up with an empty object:

~~~
negativebuffer = mypolygon.buffer(-3)
~~~
{: .language-python}

### Difference

We can get the difference between two objects, subtracting one from the other, as follows:

~~~
polygonbuffer.difference(longline.buffer(5))
~~~
{: .language-python}

We have to be careful about the order we add our objects here, as shapely will not warn us if we do things backwards.

### Union

Union allows us to add geometries together to get the spatial combination of the pair. Note that the order we add the objects does not matter.

~~~
myunion = longline.buffer(5).union(mypolygon)
plt.plot(*myunion.exterior.xy)
plt.axis('equal')
~~~
{: .language-python}

### Convex hull

A useful technique in spatial analysis is the calculation of a convex hull of a series of points. This is the smallest enclosing polygon around a series of points, and can be used as a way of calculating spatial statistics from a continuous dataset for an area covered by a series of discrete points.

To calculate a convex hull, we need more than one point, thankfully shapely has a geometry object for this:

~~~
from shapely.geometry import MultiPoint
~~~
{: .language-python}

The MultiPoint object is a collection of points, and can be created as follows:

~~~
mymultipoint = MultiPoint([[1, 2], [3, 5], [10, 8], [9, 0], [5, 5], [2, 0], [5,2]])
~~~
{: .language-python}

Or, we can make it using a list of existing points:

~~~
p1 = Point(1, 2)
p2 = Point(3, 5)
p3 = Point(10, 8)
MultiPoint([p1, p2, p3])
~~~
{: .language-python}

Now we can calculate and plot out convex hull:

~~~
convexhull = mymultipoint.convex_hull
for point in mymultipoint:
    plt.scatter(point.x, point.y)
plt.plot(*convexhull.exterior.xy)
~~~
{: .language-python}

### Triangulate

We can calculate the delaunay triangulation of a series of points using the `triangulate` function:

~~~
from shapely.ops import triangulate

triangles = triangulate(mymultipoint)
~~~
{: .language-python}

And then we can display the results:

~~~
for poly in triangles:
    plt.plot(*poly.exterior.xy)
~~~
{: .language-python}


### Nearest

We can find the nearest points between two geometries:

~~~
from shapely.ops import nearest_points

line2 = LineString([(3, 15), (20, 15)])
nearest = nearest_points(myline, line2)

plt.plot(*myline.xy, c='r')
plt.plot(*line2.xy, c='k')

for point in nearest:
    plt.scatter(point.x, point.y, c='b')
~~~
{: .language-python}


## Loading shapefiles

What we have done so far is pretty cool, but it'll be better if we can use actual GIS data. To do this we are going to use the library `fiona`, and also the `shape` function from shapely:

~~~
import fiona
from shapely.geometry import shape
~~~
{: .language-python}

We can open a shapefile using the `with` statement combined with `fiona.open`:

~~~
with fiona.open('example_data/lake.shp') as shapefile:
    lake = shape(shapefile[0]['geometry'])
~~~
{: .language-python}

This creates a shapely geometry from the geometry in the shapefile, allowing us to do all the operations we have learned before:

~~~
print('The area of the lake is:', lake.area)
print('The perimeter of the lake is:', lake.length)
~~~
{: .language-python}

This is simple, because we know there is only one geometry in the shapefile, but in lots of cases, we will have more than one object in a shapefile, such as in `trees.shp`:

~~~
tree_points = []
with fiona.open('example_data/trees.shp') as shapefile:
    for tree in shapefile:
        tree_points.append(shape(tree['geometry']))

trees = MultiPoint(tree_points)
tree_triangles = triangulate(trees)

for tree in trees:
    plt.scatter(tree.x, tree.y, zorder=1)

for poly in tree_triangles:
    plt.plot(*poly.exterior.xy, color='k', zorder=0)
~~~
{: .language-python}

## Creating a new shapefile

We can save the shapely geometries we create during our analyses using `fiona`. Lets start by saving a buffer of the lake:

~~~
from shapely.geometry import mapping

schema = {'geometry': 'Polygon', 'properties': {'id': 'int'}}

with fiona.open('lake_buffer.shp', 'w', 'ESRI Shapefile', schema) as c:
    c.write({'geometry': mapping(lake.buffer(300)), 'properties': {'id': 1}})
~~~
{: .language-python}

We can save multiple geometries into a single shapefile using a for loop to iterate over a list of geometries, such as our tree triangles:

~~~
schema = {'geometry': 'Polygon', 'properties': {'id': 'int'}}

with fiona.open('tree_triangles.shp', 'w', 'ESRI Shapefile', schema) as c:
    for i, poly in enumerate(tree_triangles):
        c.write({'geometry': mapping(poly), 'properties': {'id': i}})
~~~
{: .language-python}

## Working with rasters

We can load raster data into python and combine it with shapefiles in order to calculate zonal statistics or sample values based on a location. To do this we need to use the `rasterstats` module, alongside the `rasterio` module, which we use to load raster data:

~~~
import rasterio
from rasterstats import point_query, zonal_stats
~~~
{: .language-python}

We will use the slope raster from the ModelBuilder practical for these next few examples. We will load it into Python using `rasterio`, in a form similar to how we load shapefiles with `fiona`:

~~~
with rasterio.open('example_data/Slope.tif') as dataset:
    trans = dataset.transform
    array = dataset.read(1)
~~~
{: .language-python}

We create 2 new variables `trans`, which stores the geographic transform information (also called **affine** in some contexts). This is used to map the grid of raster values, `array`, onto a geographic location. The statement `.read(1)` indicates we want to read the first band of the raster dataset, in cases where we are working with multiband data we can select the band of interest using its number.

We can then use `point_query` to get the raster values at a series of spatial locations:

~~~
pts = point_query('example_data/sample_points.shp', array, affine=trans)
~~~
{: .language-python}

`rasterstats` is able to take vector data as shapefiles, or as shapely points, or as a list of shapely points:

~~~
sample_list = []
with fiona.open('example_data/sample_points.shp') as shapefile:
    for point in shapefile:
        sample_list.append(shape(point['geometry']))

pts2 = point_query(sample_list, , array, affine=trans)
~~~
{: .language-python}

`rasterstats` can also do zonal statistics using either a polygon shapefile:

~~~
stats = zonal_stats('example_data/catchment_1.shp', array, affine=trans)
print(stats)
~~~
{: .language-python}

or a shapely polygon:

~~~
with fiona.open('example_data/catchment_1.shp') as shapefile:
    catchment = shape(shapefile[0]['geometry'])

stats = zonal_stats(catchment, array, affine=trans)
print(stats)
~~~
{: .language-python}

We can access individual stats as follows:

~~~
print(stats[0]['mean'])
~~~
{: .language-python}

We can also specify which stats we want to calculate, from the following list:

- min
- max
- mean
- count
- sum
- std
- median
- majority
- minority
- unique
- range
- nodata
- percentile

~~~
morestats = zonal_stats(catchment, array, affine=trans, stats='median majority range percentile_98')
~~~
{: .language-python}

## A simple geoprocessing example

We are now going to recreate the first model we built in ModelBuilder, where the aim was to identify all trees that fell within 400m of the road and 300m of the lake.

Lets start by opening a new notebook so that we can start from scratch

Firstly we will import the libraries we will need for this exercise:

~~~
import fiona
from shapely.geometry import shape, mapping, MultiPoint
import matplotlib.pyplot as plt
~~~
{: .language-python}

The we can use fiona to load the three shapefiles we need:

~~~

tree_pts = []
with fiona.open('data/trees.shp') as shapefile:
    for point in shapefile:
        tree_pts.append(shape(point['geometry']))

    trees = MultiPoint(tree_pts)

with fiona.open('data/lake.shp') as shapefile:
    lake = shape(shapefile[0]['geometry'])

with fiona.open('data/road.shp') as shapefile:
    road = shape(shapefile[0]['geometry'])

~~~
{: .language-python}


By buffering the lake and the road, we can then get the `union` of the two buffers, which is the search area for our trees:

~~~
lake_buffer = lake.buffer(300)
road_buffer = road.buffer(400)
buffer_intersect = road_buffer.intersection(lake_buffer)
~~~
{: .language-python}

We can quickly plot these geometries to make sure we are doing the right thing:

~~~
plt.plot(lake_buffer, color='g', alpha=0.2)
plt.plot(road_buffer, color='r', alpha=0.2)
plt.plot(buffer_intersect, color='k')
~~~
{: .language-python}


We can then iterate over all of the points in our multipoint tree variable to find which points are within our search area:

~~~

selected_pts = []

for point in trees:
    if point.within(buffer_intersect):
        selected_pts.append(point)

~~~
{: .language-python}

Finally, we can save our list of points to a new shapefile, and load it in ArcGIS to check that our selection has worked.

~~~

schema = {'geometry': 'MultiPoint', 'properties': {'id': 'int'}}

with fiona.open('selected_trees.shp', 'w', 'ESRI Shapefile', schema) as c:
    for i, point in enumerate(selected_pts):
        c.write({'geometry': mapping(point), 'properties': {'id': i}})

~~~
{: .language-python}


## A real geoprocessing workflow

Now, we are going to start a new notebook and build a python version of the stream power workflow we built using ModelBuilder. Make sure that you can find the stream power files from the previous practical from within your notebook.

We will start by importing the various libraries we will be using:

~~~
import os
import fiona
import rasterio
from glob import glob
from rasterstats import zonal_stats
from shapely.geometry import shape, mapping, Polygon
~~~
{: .language-python}

The `os` library is used to interact with your operating system. We will use it later to format filepaths in a way that will work on any operating system.

Now we are going to use `glob` to get a list of the catchment shapefiles we need to process:

~~~
catchment_files = glob('example_data/catchments/*.shp')
~~~
{: .language-python}

With this list of files, we can write a for loop to iterate over each catchment and perform our stream power calculation. There are comments, marked by the `#` symbol, explaining the new code in this section:

~~~
results = {}

with rasterio.open('example_data/Slope.tif') as dataset:
    trans = dataset.transform
    array = dataset.read(1)

for filename in catchment_files:
    with fiona.open(filename) as shapefile:
        catchment = shape(shapefile[0]['geometry'])

        # Just as we can get the geometry of a shapefile, we can access its
        # attributes with the properties keyword, which allows us to load
        # attribute values into variables.
        K = shapefile[0]['properties']['K']
        Area = shapefile[0]['properties']['Area']

        stats = zonal_stats(catchment, array, affine=trans, stats='mean')
        Slope = stats[0]['mean']

        E = K * (Area ** 0.3) * (Slope ** 0.3)

        # This line is removing the '.shp' extension from the filename string
        filename_no_ext = os.path.splitext(filename)[0]

        # This line is removing the file path, so all that is left is the file
        # name, without an extension
        catchment_name = os.path.basename(filename_no_ext)

        results[catchment_name] = E
~~~
{: .language-python}

We now have a dictionary containing the calculated erosion rate for each of our catchments, lets make a quick bar graph to see what these values look like:

~~~
import matplotlib.pyplot as plt

for key, value in results.items():
    plt.bar(key, value)

plt.ylabel('Erosion rate (m/yr)')
~~~
{: .language-python}
