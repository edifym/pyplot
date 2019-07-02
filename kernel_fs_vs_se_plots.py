import numpy as np
import matplotlib.pyplot as plt

fig, ax = plt.subplots()
fig.set_size_inches(25.6, 14.4)
plt.subplots_adjust(left=0.05, bottom=0.05, right=0.95, top=0.95, wspace=0, hspace=0)


def autolabel(rects, xpos='center'):
    """
    Attach a text label above each bar in *rects*, displaying its height.

    *xpos* indicates which side to place the text w.r.t. the center of
    the bar. It can be one of the following {'center', 'right', 'left'}.
    """

    ha = {'center': 'center', 'right': 'left', 'left': 'right'}
    offset = {'center': 0, 'right': 1, 'left': -1}
    hoffset = -1

    for rect in rects:
        height = rect.get_height()
        ax.annotate('{}%'.format(height),
                    xy=(rect.get_x() + rect.get_width() / 2, height),
                    xytext=(offset[xpos]*-6, 12 + 9 * hoffset),  # use 3 points offset
                    textcoords="offset points",  # in both directions
                    ha=ha[xpos], va='bottom')
        hoffset = hoffset * -1


se = [float(line.rstrip('\n')) * 1000000 for line in open('se_kernel.txt')]
fs = [float(line.rstrip('\n')) * 1000000 for line in open('fs_kernel.txt')]
names = [line for line in open('kernel_names.txt')]
ind = np.arange(len(se))  # the x locations for the groups
width = 0.35  # the width of the bars: can also be len(x) sequence

print(se)
print(fs)

se_normalized = [100 for val in se]
fs_normalized = []

for i in range(0, len(se)):
    if se[i] == 0 and fs[i] == 0:
        fs_normalized.append(100)
    elif se[i] == 0:
        fs_normalized.append(100)
    else:
        fs_normalized.append(round(fs[i]/se[i]*100, 2))

rects1 = ax.bar(ind - width / 2, se_normalized, width)
rects2 = ax.bar(ind + width / 2, fs_normalized, width)

ax.set_ylabel('% Relative to SE')
ax.set_title('Relative simulated time by emulation mode - kernel benchmarks')
ax.set_xticks(ind)
ax.set_xticklabels(names)
ax.legend(('Syscall Emulation', 'Full System'))

autolabel(rects1, "left")
autolabel(rects2, "right")
plt.xlim(-0.5, 28.5)

#plt.show()
plt.savefig('kernel_fs_vs_se_plots.png')
