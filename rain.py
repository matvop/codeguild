import urllib.request
from collections import defaultdict

def parse_page_url_into_lines():
    with urllib.request.urlopen('http://or.water.usgs.gov/non-usgs/bes/sunnyside.rain') as rain_file:
        rain_line_data = [byte_line.decode('utf-8') for byte_line in rain_file]
    return rain_line_data

def get_date_and_total_rain(rain_line_data):
    raw_dates_and_totals = []
    for line in rain_line_data[11:]:
        items_in_line = line.split()
        date = items_in_line[0]
        amount = int(items_in_line[1])
        pair = (date,amount)
        raw_dates_and_totals.append(pair)
        dates_and_totals = [tuple(s if s != "-" else "0" for s in tup) for tup in raw_dates_and_totals]
    return raw_dates_and_totals

def print_max_rain_date_and_amount(dates_and_totals):
    date,amount = max(dates_and_totals, key=lambda x:int(x[1]))
    inches = (int(amount)*.01)
    print('{} inches of rain fell on {}.'.format(amount,date))

def date_to_year(date):
    year = date[-4:]
    return year

def dates_to_years(dates_and_totals):
    return [date_amount_to_year_amount(pair) for pair in dates_and_totals]

def date_amount_to_year_amount(date_and_amount):
    amount = date_and_amount[1]
    year = date_to_year(date_and_amount[0])
    return (year, amount)

# def combine():
#     d = defaultdict(list)
#     for year,amount in dates_to_years():
#         d[year].append(amount)

rain_line_data = parse_page_url_into_lines()
raw_dates_and_totals = get_date_and_total_rain(rain_line_data)

print_max_rain_date_and_amount(dates_and_totals)
# years_and_amounts = [dict(dates_to_years() for pair in )]
dates_to_years(dates_and_totals)
"""next step - print out the year with the most rain"""
"""set rainfall amount as int, so it doesn't have be set every time"""

# Grouping: dictionary
# dictionary to a list is good way to collect things
