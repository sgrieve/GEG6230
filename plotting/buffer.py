import matplotlib.pyplot as plt
from matplotlib import rcParams
from shapely.geometry import Point, Polygon

rcParams['font.size'] = 18

poly = Polygon([(0,0), (5,25), (20,20), (20,0)])

fig = plt.figure(figsize=[12, 6])

for i in range(1, 3):

    ax = plt.subplot(1, 2, i)
    plt.fill(*poly.exterior.xy, c='tab:blue', alpha=0.7)

    if i == 2:
        buffer = poly.buffer(20)
        plt.fill(*buffer.exterior.xy, c='k', alpha=0.5)
        plt.fill(*poly.exterior.xy, c='tab:blue', alpha=0.7)


    ax.xaxis.set_ticklabels([])
    ax.xaxis.set_ticks_position('none')
    ax.yaxis.set_ticklabels([])
    ax.yaxis.set_ticks_position('none')

    ax.set_xlim(-25, 50)
    ax.set_ylim(-25, 50)

ax.annotate('Buffer', (0.5, 0.93),
            xycoords='figure fraction', ha='center')

plt.axis('equal')
plt.tight_layout()
plt.savefig('buffer.png')
plt.clf()
