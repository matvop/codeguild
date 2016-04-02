###City of Portland - Hydra Network Rain Gauge scraper
###Retrieves hourly updated rain gauge data from or.water.usgs.gov.
###(internet connection required)
###Supports user selection of a specific rain gauge station.
###Currently outputs the street address selected location,
###date of most rainfall - amount of rain, and the location's wettest year
###and amount of rain for that year
###future revisions may include ability to notify user if
###location has been retired, and that data is for historic purposes

import urllib.request
import os

def parse_index_url_into_lines():
    """Parses Oregon usgs rain station index page into a list of lines"""
    with urllib.request.urlopen(
        'http://or.water.usgs.gov/non-usgs/bes/') as data_file:
        all_gauges_line_data = [
            byte_line.decode('utf-8') for byte_line in data_file
        ]
    return all_gauges_line_data

def parse_rain_file_url_into_lines():
    """Parses the user selected rain station data into a list of lines"""
    with urllib.request.urlopen(get_url()) as rain_file:
        rain_line_data = [
            byte_line.decode('utf-8') for byte_line in rain_file
        ]
    return rain_line_data

def get_url():
    """retrieves the .rain file url by using the users station_num
    input in select_rain_gauge()"""
    url = create_rain_gauge_dict()[select_rain_gauge()][1]
    return url

def select_rain_gauge():
    """Provides the user with a table of available rain stations by their id#,
    location, and .rain file url. Prompts user for station id#"""
    print('\n{:<15} {:<40} {:<40}'.format('Station id#:','Location:','URL:\n'))
    for k, v in create_rain_gauge_dict().items():
        location, url = v
        print('{:<15} {:<40} {:<40}'.format(k, location, url))
    print('')
    return input("""Rain level data is available for the listed locations.

Please enter station id#: """)

def create_list_of_urls(truncated_html_source_lines):
    """Creates and returns a list of urls by piecing together .rain file names,
    available in the HTML, with known url prefix. Removes two erroneous/retired
    locations from list."""
    url_prefix = 'http://or.water.usgs.gov/non-usgs/bes/'
    url_search_string = '.rain'
    lines_with_matching_url = [
        s for s in truncated_html_source_lines if url_search_string in s
    ]
    url_raw = [line[26:] for line in lines_with_matching_url]
    url_list = [line[:-22] for line in url_raw]
    url_list.pop(url_list.index('rover.rain'))
    url_list.pop(url_list.index('swan_island.rain'))
    completed_list_of_urls = [url_prefix + url for url in url_list]
    return completed_list_of_urls

def create_list_of_locations(truncated_html_source_lines):
    """Creates a list of rain gauge location names by locating a specific
    string 'Rain Gage<br>' inside the HTML. A list of lines is created from the
    matching truncated_html_source_lines. The lines are then cleaned of extra
    characters and returned into a location_list"""
    location_search_string = 'Rain Gage<br>'
    lines_with_rain_gauge_address = [
        s for s in truncated_html_source_lines
            if location_search_string in s
    ]
    location_raw = [line[4:] for line in lines_with_rain_gauge_address]
    location_list = [line for line in location_raw]
    location_list = [
        i.split('Rain Gage<br>', 1)[0] for i in location_list
    ] #cuts the rest of the junk out of each line
    return location_list

def create_list_of_station_numbers(truncated_html_source_lines):
    """Finds the index positions of the lines in the html source line list
    which contain the matching partial string and increases the index pos
    by 1 to reach the line that contains station id"""
    station_number_indices = [
        (i+1) for i, s in enumerate(
            truncated_html_source_lines) if 'Rain Gage<br>' in s
    ]
    station_number_lines = [
        truncated_html_source_lines[i] for i in station_number_indices
    ]
    station_number_raw = [line[17:] for line in station_number_lines]
    station_number_list = [line[:-6] for line in station_number_raw]
    return station_number_list

def create_rain_gauge_dict():
    return {
    z[0]:list(z[1:]) for z in zip(
        create_list_of_station_numbers(truncated_html_source_lines),
        create_list_of_locations(truncated_html_source_lines),
        create_list_of_urls(truncated_html_source_lines)
        )
    }

def get_date_and_total_rain(rain_line_data):
    raw_dates_and_totals = []
    # items_in_line = [line[11:].split() for line in rain_line_data]
    # date = [i[0] for i in items_in_line]
    # amount = [i[1] for i in items_in_line]
    # (date,amount) = [(i,i) for i in items_in_line]
    # print (date,amount)
    # raw_dates_and_totals = [(date,amount) for pair in ]
    for line in rain_line_data[11:]:
        items_in_line = line.split()
        date = items_in_line[0]
        amount = items_in_line[1]
        pair = (date,amount)
        raw_dates_and_totals.append(pair)
    dates_and_totals = [tuple(
        s if s != "-" else "0" for s in pair)
            for pair in raw_dates_and_totals]
    return dates_and_totals

def print_max_rain_date_and_amount(dates_and_totals):
    date,amount = max(dates_and_totals, key=lambda x:int(x[1]))
    inches = (int(amount)/100)
    print('\nCurrently connected to the ' + rain_line_data[0])
    print('The most rainfall, in a single day, was {} inches on {}.'.format(
        inches,date
        )
    )

def date_to_year(date):
    year = date[-4:]
    return year

def date_amount_to_year_amount(date_and_amount):
    """brings in the date_and_amount tuple and returns only the year and """
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
    #convert the tuples to a dict
    d = convert_to_dict(years_and_amounts)
    #sum together all the values for each key in the dict
    e = {year:sum(amount) for year,amount in d.items()}
    #find the year with max amount of rain
    x = max(e, key=e.get)
    #find the amount of rain for that year
    y = (e.get(x) * .01)
    print(
    "{} was the area's wettest year with a total of {} inches of rain.\n"
        .format(x,y)
    )

run = True
while run:
    os.system('cls')
    truncated_html_source_lines = parse_index_url_into_lines()[120:]
    rain_gauge_dict = create_rain_gauge_dict()
    rain_line_data = parse_rain_file_url_into_lines()
    dates_and_totals = get_date_and_total_rain(rain_line_data)
    print_max_rain_date_and_amount(dates_and_totals)
    years_and_amounts = dates_to_years(dates_and_totals)
    convert_to_dict(years_and_amounts)
    display_rainiest_year(years_and_amounts)
    yayornay = input(
        'Would you like to check another station? [y/n]: ').lower()
    if yayornay == 'y':
        run = True
    else:
        run = False
