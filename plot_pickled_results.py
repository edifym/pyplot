import pickle
import matplotlib.pyplot as plt

dicts = [('dict-15m', 15), ('dict-30m', 30), ('dict-45m', 45), ('dict-60m', 60), ('dict-75m', 75), ('dict-all', 240)]
for dict, time in dicts:
    values_dict = {}
    with open(f'{dict}.pkl', 'rb') as handle:
        values_dict = pickle.load(handle)

    total_results = 0
    for key in values_dict.keys():
        total_results += values_dict[key]

    fig, ax = plt.subplots()
    fig.set_size_inches(6, 8)

    times = list(values_dict.keys())
    times.sort()

    print(f'total results: {total_results} {min(times)} {max(times)}')

    prevalence = []
    for t in times:
        prevalence.append(values_dict[t])


    width = 0.35  # the width of the bars: can also be len(x) sequence

    print(f'{times}\n{prevalence}')

    ax.plot(times, prevalence)
    ax.set_ylabel('occurances')
    ax.set_xlabel('µs')
    ax.set_xlim(100, 380)
    ax.set_title(f'Execution distribution at {time} minutes')
    #ax.set_ylim(ymin=0)

    #plt.show()
    plt.savefig(f'{dict}.png')