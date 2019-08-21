import numpy as np
from glob import glob
import sys

ID = sys.argv[1]

dates = []
min_t = []
max_t = []

filelist = glob('*.csv')

filelist.sort()

for f in filelist:

    data = np.genfromtxt(f, skip_header=91, skip_footer=1, dtype=str, delimiter=',')
    for d in data:
        dates.append(d[0])
        max_t.append(float(d[8]))
        min_t.append(float(d[9]))

with open('{}/{}_temperatures.csv'.format(ID, ID), 'w') as w:

    w.write('date,maximum_temp,minimum_temp\n')
    for a,b,c in zip(dates,max_t,min_t):
        w.write('{},{},{}\n'.format(a,b,c))
