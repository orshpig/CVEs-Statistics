import matplotlib.pyplot as plt
import pandas as pd

def to_graph():
    cve = pd.read_csv('cve.csv')
    date = cve['date']
    indexes = [index for index, date in enumerate(date)]
    dates = [date for index, date in enumerate(date)]
    dates = list(map(str, dates))
    plt.bar(dates, cve['total'])
    plt.xticks(ticks=indexes, labels=dates, rotation=45)
    plt.title('Reported CVEs')
    plt.xlabel('Dates')
    plt.ylabel('Number Of CVEs')
    plt.show()
