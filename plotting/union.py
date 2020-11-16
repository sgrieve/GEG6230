import matplotlib.pyplot as plt
from matplotlib import rcParams
from shapely.geometry import Point, Polygon

rcParams['font.size'] = 18

poly_l = Polygon([(0,0), (0,20), (20,20), (20,0)])
poly_r = Polygon([(20,0), (20,20), (40,20), (40,0)])

combined = Polygon([(0,0), (0,40), (40,40), (40,0)])

point = Point(20, 0)
circle = point.buffer(10)
union = poly_l.union(circle)


fig = plt.figure(figsize=[12, 6])

for i in range(1, 3):

    ax = plt.subplot(1, 2, i)

    if i == 1:
        plt.fill(*poly_l.exterior.xy, c='tab:blue', alpha=0.7)
        plt.fill(*circle.exterior.xy, c='k', alpha=0.7)

    if i == 2:
        plt.fill(*union.exterior.xy, c='tab:blue', alpha=0.7)

    ax.xaxis.set_ticklabels([])
    ax.xaxis.set_ticks_position('none')
    ax.yaxis.set_ticklabels([])
    ax.yaxis.set_ticks_position('none')

    ax.set_aspect('equal')

    ax.set_xlim((-2.0, 42.0))
    ax.set_ylim((-11.5, 21.5))

plt.suptitle('Union')

plt.tight_layout()
plt.savefig('union.png')
plt.clf()
