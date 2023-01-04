import pandas as pd
import requests
import plots
from datetime import date, datetime

# Sends a request to the NVD API according to the dates provided by the user
def request():
    total = []
    index = 1
    print('Work in progress, it might take some time...')
    for date in date_list:
        if index < len(date_list):
            next_date = date_list[index]
            response = requests.get(f'https://services.nvd.nist.gov/rest/json/cves/2.0/?pubStartDate={date}T00:00:01.000&pubEndDate={next_date}T00:00:00.000')
            json_data = response.json()
            monthly_total = json_data["totalResults"]
            total.append(str(monthly_total))
            index += 1
        else:
            continue

# Check if the user input is a yearly range, if yes it summarize the CVEs number per year.
    if user_input == '1':
        int_total = [eval(i) for i in total]
        new_total = []
        count = 0
        place = 0
        for i in int_total:
            place += 1
            if place <= 11:
                count += i
            else:
                place = 0
                new_total.append(str(count))
                count = 0

# Summarize the CVEs of 12 months to create total amount per 1 year.
        year_list = [i.strftime("%Y") for i in pd.date_range(start=start_year, end=end_year, freq='Y')]
        new_total[0:0] = ['total']
        year_list[0:0] = ['date']
        data = zip(year_list, new_total)

 # Create a YEARLY CSV based on the data provided by the user input and its API response.
        with open('cve.csv', 'w') as my_file:
            for (year_list, new_total) in data:
                my_file.write("{0},{1}\n".format(year_list, new_total))
# Using the function that creates the YEARLY graph from the CSV file.
        plots.to_graph()

# Check if the user input is a monthly range
    elif user_input == '2':
        total[0:0] = ['total']
        dates_to_graph[0:0] = ['date']
        data = zip(dates_to_graph, total)
        # Create a monthly CSV based on the data provided by the user input and its API response.
        with open('cve.csv', 'w') as my_file:
            for (dates, total) in data:
                my_file.write("{0},{1}\n".format(dates, total))
        # Using the function that creates a monthly graph from the CSV file.
        plots.to_graph()

# Check if the user input is a daily range
    elif user_input == '3':
        total[0:0] = ['total']
        date_list[0:0] = ['date']
        data = zip(date_list, total)
# Create a daily CSV based on the data provided by the user input and its API response.
        with open('cve.csv', 'w') as my_file:
            for (dates, total) in data:
                my_file.write("{0},{1}\n".format(dates, total))
# Using the function that creates a daily graph from the CSV file.
        plots.to_graph()




date_format = '%Y-%m'
max_year = 2023
max_date = datetime.today()
min_date = datetime.strptime('2015-01', date_format)

#Get user input for the graph type.
user_input = input("""Available graph types: 
1) Yearly | 2) Monthly | 3) Daily 
Your Choice: """)

# Get user input for the dates range

if user_input == '1':
    start_year = int(input('From year (YYYY): '))
    end_year = int(input('Until year (YYYY): '))

    if start_year >= 2015 and start_year < max_year and end_year > 2015 and end_year <= max_year:
        start_year = date(start_year, 1, 1)
        end_year = date(end_year+1, 1, 1)
# Splits the years to months and using the request function.
        date_list = [i.strftime("%Y-%m-%d") for i in pd.date_range(start=start_year, end=end_year, freq='MS')]
        request()
    else:
        print(f'Years must be after 2015 and before {max_year}')


elif user_input == '2':
    start_monthly = input('From date (YYYY-MM): ')
    end_monthly = input('Until date (YYYY-MM): ')
    start = datetime.strptime(start_monthly, date_format)
    end = datetime.strptime(end_monthly, date_format)

    if (start < max_date >= end) and (start >= min_date <= end):
# Splits the range to months and using the request function.
        date_list = [i.strftime("%Y-%m-%d") for i in pd.date_range(start=start, end=end, freq='MS')]
        dates_to_graph = [i.strftime("%Y-%m") for i in pd.date_range(start=start, end=end, freq='MS')]
        request()
    else:
        print(f'Years must be after 2015 and ends before {max_date}')


elif user_input == '3':
    print('NOTE: The maximal range is 120 days.')
    start_daily = input('From date (YYYY-MM-DD): ')
    end_daily = input('Until date (YYYY-MM-DD): ')

    start = datetime.strptime(start_daily, '%Y-%m-%d')
    end = datetime.strptime(end_daily, '%Y-%m-%d')

    if (start < max_date >= end) and (start >= min_date <= end):
# Splits the daily ranges to days and using the request function.
        date_list = [i.strftime("%Y-%m-%d") for i in pd.date_range(start=start, end=end, freq='D')]
        if len(date_list) > 120:
            print('120 days limit')
        else:
            request()
    else:
        print(f'Years must be after 2015 and ends before {max_date}')

