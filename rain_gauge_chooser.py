###City of Portland - Hydra Network Rain Gauge scraper
###Retrieves hourly updated rain gauge data from or.water.usgs.gov(internet connection required)
###Supports user selection of a specific rain gauge station
###Currently outputs the street address of the selected location, date of most rainfall and amount of rain, location's wettest year and amount of rain
###future revisions may include ability to notify user if location has been retired, and that data is for historic purposes

import urllib.request
import os

def parse_index_url_into_lines():
    """Parses the main Oregon usgs rain station index webpage into a list of lines"""
    with urllib.request.urlopen('http://or.water.usgs.gov/non-usgs/bes/') as data_file:
        all_gauges_line_data = [byte_line.decode('utf-8') for byte_line in data_file]
    return all_gauges_line_data

def parse_page_url_into_lines():
    """Parses the user selected rain station data into a list of lines"""
    with urllib.request.urlopen(get_url()) as rain_file:
        rain_line_data = [byte_line.decode('utf-8') for byte_line in rain_file]
    return rain_line_data

def get_url():
    """retrives the .rain file url by using the users station_num input in select_rain_gauge()"""
    d = create_rain_gauge_dict()
    station_num = select_rain_gauge(d)
    url = d[station_num][1]
    return url

def select_rain_gauge(rain_gauge_dict):
    """Provides the user with a table of available rain stations by their id# and location, and .rain file url. Prompts the user for station id# and returns response."""
    print('')
    print('{:<15} {:<40} {:<40}'.format('Station id#:','Location:','URL:'))
    print('')
    for k, v in rain_gauge_dict.items():
        location, url = v
        print('{:<15} {:<40} {:<40}'.format(k, location, url))
    print('')
    return input("""Rain level data is available for the listed locations. Please select a station:

    > """)

def create_list_of_urls(truncated_html_source_lines):
    """Creates and returns a list of urls by piecing together .rain filenames, available in the HTML, with known url prefix. Also removes some erroneuos/retired data from the list."""
    line_num = 0
    url_list = []
    url_prefix = 'http://or.water.usgs.gov/non-usgs/bes/'
    url_search_string = '.rain'
    matching_url = [s for s in truncated_html_source_lines if url_search_string in s]
    for line in matching_url:
        decoded_line = matching_url[line_num]
        url_raw = decoded_line[26:]
        url_list.append(url_raw[:-22])
        line_num += 1
    url_list.pop(url_list.index('rover.rain'))
    url_list.pop(url_list.index('swan_island.rain'))
    completed_list_of_urls = [url_prefix + url for url in url_list]
    return completed_list_of_urls

def create_list_of_locations(truncated_html_source_lines):
    """Creates a list of rain gauge location names by locating a specific string 'Rain Gage<br>' inside the HTML. A list lines is created from the matching truncated_html_source_lines. The lines are then cleaned of uneeded characters and returned into a location_list"""
    line_num = 0
    location_list = []
    location_search_string = 'Rain Gage<br>'
    matching_location = [s for s in truncated_html_source_lines if location_search_string in s]
    for line in matching_location:
        decoded_line = matching_location[line_num]
        location_raw = decoded_line[4:]
        location_list.append(location_raw[:-6])
        line_num += 1
    location_list = [i.split('Rain Gage<br>', 1)[0] for i in location_list]
    return location_list

def create_list_of_station_numbers(truncated_html_source_lines):
    station_line_num = 0
    station_number_list = []
    station_number_indices = [(i+1) for i, s in enumerate(truncated_html_source_lines) if 'Rain Gage<br>' in s]
    station_number_lines = [truncated_html_source_lines[i] for i in station_number_indices]
    for line in station_number_lines:
        station_line = station_number_lines[station_line_num]
        station_number_raw = station_line[17:]
        station_number_list.append(station_number_raw[:-6])
        station_line_num +=1
    return station_number_list

def create_rain_gauge_dict():
    return {z[0]:list(z[1:]) for z in zip(create_list_of_station_numbers(truncated_html_source_lines),create_list_of_locations(truncated_html_source_lines),create_list_of_urls(truncated_html_source_lines))}

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

play = True
while play:
    os.system('cls')
    html_source_lines = parse_index_url_into_lines()
    truncated_html_source_lines = html_source_lines[120:]
    rain_gauge_dict = create_rain_gauge_dict()
    rain_line_data = parse_page_url_into_lines()
    dates_and_totals = get_date_and_total_rain(rain_line_data)
    print_max_rain_date_and_amount(dates_and_totals)
    years_and_amounts = dates_to_years(dates_and_totals)
    convert_to_dict(years_and_amounts)
    display_rainiest_year(years_and_amounts)
    yayornay = input('Would you like to check another station? [y/n]: ').lower()
    if yayornay == 'y':
        play = True
    else:
        play = False