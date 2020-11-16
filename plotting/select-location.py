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
        for a, b in zip(x, y):
            if (a > 0.1 and a < 0.8) and (b > 0.01 and b < 0.6):
                ax.plot(a, b, 'ro')

    ax.xaxis.set_ticklabels([])
    ax.xaxis.set_ticks_position('none')
    ax.yaxis.set_ticklabels([])
    ax.yaxis.set_ticks_position('none')
    ax.set_aspect('equal')

plt.suptitle('Select [by location]')

plt.tight_layout()

plt.savefig('select-location.png')
plt.clf()
