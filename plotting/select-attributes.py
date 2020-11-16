import random
import matplotlib.pyplot as plt
from matplotlib import rcParams

rcParams['font.size'] = 18

random.seed(10)

x = []
y = []
for i in range(20):
    x.append(random.random())
    y.append(random.random())


fig = plt.figure(figsize=[12, 6])

for i in range(1, 3):

    ax = plt.subplot(1, 2, i)
    ax.plot(x, y, 'ko')

    if i == 2:
        ax.plot(x[10:18], y[10:18], 'ro')

    ax.xaxis.set_ticklabels([])
    ax.xaxis.set_ticks_position('none')
    ax.yaxis.set_ticklabels([])
    ax.yaxis.set_ticks_position('none')
    ax.set_aspect('equal')

plt.suptitle('Select [by attributes]')

plt.tight_layout()
plt.savefig('select-attr.png')
plt.clf()
