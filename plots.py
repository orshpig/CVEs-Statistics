import matplotlib.pyplot as plt
import pandas as pd

def to_graph():
    cve = pd.read_csv('cve.csv')
    date = cve['date']
    total = cve['total']
    indexes = [index for index, date in enumerate(date)]
    dates = [date for index, date in enumerate(date)]
    dates = list(map(str, dates))
    fig, ax = plt.subplots(figsize=(10, 12))
    plt.bar(dates, total)
    plt.xticks(ticks=indexes, labels=dates, rotation=25)
    plt.title('Reported CVEs')
    plt.xlabel('Dates')
    plt.ylabel('Number Of CVEs')
    for i in range(len(dates)):
        ax.text(dates[i], total[i], total[i], size=10, horizontalalignment='center', verticalalignment='top')
    plt.show()
