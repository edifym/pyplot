import numpy as np
import matplotlib.pyplot as plt

fig, ax = plt.subplots()
fig.set_size_inches(12, 8)
#plt.subplots_adjust(left=0.05, bottom=0.05, right=0.95, top=0.95, wspace=0, hspace=0)


se = [int(line.rstrip('\n')) for line in open('se_all.txt')]
fs = [int(line.rstrip('\n')) for line in open('fs_all.txt')]
ind = np.arange(len(se))  # the x locations for the groups

print(se)
print(fs)

diffs = []
for i in range(len(se)):
    res = (fs[i] - se[i]) / se[i] * 100
    print(f'{i} {len(se)} {len(fs)} {se[i]} {fs[i]} {res}')
    diffs.append(res)

print(diffs)

x = np.linspace(-5,5,100)

ax.plot(fs, diffs, 'bo')
ax.set_ylabel('FS difference with SE in %')
ax.set_xlabel('runtime (µs)')
#ax.set_ylim(0, 80)
ax.set_xscale('log')
ax.set_title(f'Difference between FS and SE mode plotted against runtime')

#plt.show()
plt.savefig('all_fs_vs_se_plots.png')
