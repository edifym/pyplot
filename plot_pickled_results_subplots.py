import pickle
import matplotlib.pyplot as plt

fig = plt.figure()
fig.set_size_inches(12, 12)
fig.subplots_adjust(hspace=0.35, wspace=0.35)

dicts = [('dict-15m', 15), ('dict-30m', 30), ('dict-60m', 60), ('dict-90m', 90), ('dict-120m', 120), ('dict-all', 240)]
i = 1
for dict, time in dicts:
    values_dict = {}
    with open(f'{dict}.pkl', 'rb') as handle:
        values_dict = pickle.load(handle)

    total_results = 0
    for key in values_dict.keys():
        total_results += values_dict[key]

    times = list(values_dict.keys())
    times.sort()

    print(f'total results: {total_results} {min(times)} {max(times)}')

    prevalence = []
    for t in times:
        prevalence.append(values_dict[t])

    width = 0.35  # the width of the bars: can also be len(x) sequence

    print(f'{times}\n{prevalence}')

    ax = fig.add_subplot(2, 3, i)
    ax.plot(times, prevalence)
    ax.set_ylabel('no. of occurances')
    ax.set_xlabel('runtime (µs)')
    ax.set_xlim(145, 630)
    ax.set_title(f'{time} minutes')
    #ax.set_ylim(ymin=0)

    i += 1

plt.tight_layout()
plt.savefig(f'dict-subplots.png')
