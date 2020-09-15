import fiona
from shapely.geometry import mapping, Polygon
import math

# Define a polygon feature geometry with one attribute
schema = {
    'geometry': 'Polygon',
    'properties': {'scar_id': 'int', 'soil_depth': 'float',
                   'cohesion': 'float', 'soil_dens': 'int',
                   'hydro_const': 'float', 'frict_ang': 'float'}
}


with fiona.open('simpler.shp') as shp:

    for i, s in enumerate(shp, start=1):

        q = s['geometry']['coordinates'][0]
        if len(q) == 1:
            q = q[0]

        attrs = list(s['properties'].values())

        poly = Polygon(q)

        # Write a new Shapefile
        with fiona.open('scars/scar_{}.shp'.format(i),
                        'w', 'ESRI Shapefile', schema) as c:
            c.write({
                'geometry': mapping(poly),
                'properties': {'scar_id': i, 'soil_depth': attrs[0],
                               'cohesion': attrs[1], 'soil_dens': attrs[2],
                               'hydro_const': attrs[3], 'frict_ang': math.radians(attrs[4])}
            })
