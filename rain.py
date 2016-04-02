#Please refer to rain_scraper(previously named rain_gauge_chooser.py)
import urllib.request

def parse_page_url_into_lines():
    with urllib.request.urlopen('https://raw.githubusercontent.com/selassid/codeguild/master/sunnyside.rain') as rain_file:
        rain_line_data = [byte_line.decode('utf-8') for byte_line in rain_file]
    # with open('C:\\Users\\Matt\\codeguild\\extras\\opb.rain') as rain_file: #opens and reads p_and_p.txt to memory as var p_and_p
    #     rain_line_data = rain_file.readlines()
    return rain_line_data

def get_date_and_total_rain(rain_line_data):
    raw_dates_and_totals = []
    for line in rain_line_data[11:]:
        items_in_line = line.split()
        date = items_in_line[0]
        amount = items_in_line[1]
        pair = (date,amount)
        raw_dates_and_totals.append(pair)
    dates_and_totals = [tuple(s if s != "-" else "0" for s in tup) for tup in raw_dates_and_totals]
    return dates_and_totals

def print_max_rain_date_and_amount(dates_and_totals):
    date,amount = max(dates_and_totals, key=lambda x:int(x[1]))
    inches = (int(amount)/100)
    print('Currently connected to the ' + rain_line_data[0])
    print('The most rainfall, in a single day, was {} inches on {}.'.format(inches,date))

def date_to_year(date):
    year = date[-4:]
    return year

def date_amount_to_year_amount(date_and_amount):
    amount = date_and_amount[1]
    year = date_to_year(date_and_amount[0])
    return (year, amount)

def dates_to_years(dates_and_totals):
    return [date_amount_to_year_amount(pair) for pair in dates_and_totals]

def convert_to_dict(years_and_amounts):
    d = {}
    for year,amount in years_and_amounts:
        d.setdefault(year, []).append(int(amount))
    return(d)

def display_rainiest_year(years_and_amounts):
    d = convert_to_dict(years_and_amounts)
    e = {k:sum(v) for k,v in d.items()} #sums together all the values for each key
    x = max(e, key=e.get)
    y = (e.get(x) * .01)
    print("{} was the area's wettest year with a total of {} inches of rain.".format(x,y))
    print('')

rain_line_data = parse_page_url_into_lines()
dates_and_totals = get_date_and_total_rain(rain_line_data)
print_max_rain_date_and_amount(dates_and_totals)
years_and_amounts = dates_to_years(dates_and_totals)
convert_to_dict(years_and_amounts)
display_rainiest_year(years_and_amounts)
