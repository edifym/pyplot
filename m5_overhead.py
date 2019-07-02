import numpy as np
import matplotlib.pyplot as plt

fig, ax = plt.subplots()
fig.set_size_inches(6, 8)

times = [float(line.rstrip('\n')) * 1000000 for line in open('m5_overhead.txt')]
avg = sum(times)/len(times)
a = np.array(times)
stddev = np.std(a)
ind = np.arange(1)  # the x locations for the groups
width = 0.35  # the width of the bars: can also be len(x) sequence

print(times, avg, stddev)

rects1 = ax.boxplot(times)

ax.set_ylabel('µs')
ax.set_title('Overhead of dumping stats with m5 binary in µs simulated time')
ax.set_ylim(ymin=0)

#plt.show()
plt.savefig('m5_overhead.png')
