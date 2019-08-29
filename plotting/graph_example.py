import matplotlib.pyplot as plt
from matplotlib import rcParams

rcParams['font.size'] = 14

plt.plot(5,7,'o', label='Data point')

plt.xlim(0,10)
plt.ylim(0,10)
plt.xlabel('X axis\nThe independent variable (The cause)')
plt.ylabel('Y axis\nThe dependent variable (The effect)')
plt.legend(title='Legend')
plt.tight_layout()
plt.savefig('parts_of_graph.png')
