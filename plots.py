import matplotlib.pyplot as plt
import pandas as pd

def to_graph():
    cve = pd.read_csv('cve.csv')
    plt.bar(cve["date"], cve["total"])
    plt.xticks(rotation=45)
    plt.title('Reported CVEs')
    plt.xlabel('Date')
    plt.ylabel('Number Of CVEs')
    plt.show()