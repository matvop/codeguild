# City of Portland - Hydra Network Rain Gauge scraper
# Retrieves hourly updated rain gauge data from or.water.usgs.gov.
# (internet connection required)
# Supports user selection of a specific rain gauge station.
# Currently outputs the street address selected location,
# date of most rainfall - amount of rain, and the location's wettest year
# and amount of rain for that year
# future revisions may include ability to notify user if
# location has been retired, and that data is for historic purposes

import urllib.request
import os


def parse_index_url():
    """Parses Oregon usgs rain station index page into a list of lines"""
    with urllib.request.urlopen(
            'http://or.water.usgs.gov/non-usgs/bes/') as data_file:
        all_gauges_line_data = [
            byte_line.decode('utf-8') for byte_line in data_file
        ]
    return all_gauges_line_data[120:]


def parse_rain_file_url():
    """Parses the user selected rain station data into a list of lines"""
    url = gauge_dict[select_rain_gauge()][1]
    with urllib.request.urlopen(url) as rain_file:
        rain_lines = [
            byte_line.decode('utf-8') for byte_line in rain_file
        ]
    return rain_lines


def create_rain_gauge_dict():
    html_source_lines = parse_index_url()
    """Creates and returns a list of urls by piecing together .rain file
    names, available in the HTML, with known url prefix. Removes two
    erroneous/retired locations from list."""
    url_prefix = 'http://or.water.usgs.gov/non-usgs/bes/'
    url_search_string = '.rain'
    lines_with_matching_url = [
            line for line in html_source_lines
            if url_search_string in line
    ]
    url_raw = [line[26:] for line in lines_with_matching_url]
    url_list = [line[:-22] for line in url_raw]
    url_list.pop(url_list.index('rover.rain'))
    url_list.pop(url_list.index('swan_island.rain'))
    completed_list_of_urls = [url_prefix + url for url in url_list]
    """Creates a list of rain gauge location names by locating a specific
    string 'Rain Gage<br>' inside the HTML. A list of lines is created from
    the matching html_source_lines. The lines are then cleaned of extra
    characters and returned into a location_list"""
    location_search_string = 'Rain Gage<br>'
    lines_with_rain_gauge_address = [
        line for line in html_source_lines
        if location_search_string in line
    ]
    location_raw = [line[4:] for line in lines_with_rain_gauge_address]
    location_list = [line for line in location_raw]
    # cuts the rest of the junk out of each line
    location_list = [
        i.split('Rain Gage<br>', 1)[0] for i in location_list
    ]
    """Finds the index positions of the lines in the html source line list
    which contain the matching partial string and increases the index pos
    by 1 to reach the line that contains station id"""
    station_number_indices = [
        (i+1) for i, s in enumerate(
            html_source_lines) if 'Rain Gage<br>' in s
    ]
    station_number_lines = [
        html_source_lines[i] for i in station_number_indices
    ]
    station_number_raw = [line[17:] for line in station_number_lines]
    station_number_list = [line[:-6] for line in station_number_raw]
    return {
        z[0]: list(z[1:]) for z in zip(
            station_number_list,
            location_list,
            completed_list_of_urls
        )
    }


def select_rain_gauge():
    """Provides the user with a table of available rain stations by their
    id#, location, and .rain file url. Prompts user for station id#"""
    print('\n{:<15} {:<40} {:<40}'.format('Station id#:', 'Location:',
                                          'URL:\n'))
    for k, v in gauge_dict.items():
        location, url = v
        print('{:<15} {:<40} {:<40}'.format(k, location, url))
    print('')
    return input("""Rain level data is available for the listed locations.

Please enter station id#: """)


def get_date_and_total_rain():
    rain_line_data = parse_rain_file_url()
    print('\nCurrently connected to the ' + rain_line_data[0])
    raw_dates_and_totals = []
    # items_in_line = [line[11:].split() for line in rain_line_data]
    # date = [i[0] for i in items_in_line]
    # amount = [i[1] for i in items_in_line]
    # (date, amount) = [(i, i) for i in items_in_line]
    # print (date, amount)
    # raw_dates_and_totals = [(date, amount) for pair in ]
    for line in rain_line_data[11:]:
        items_in_line = line.split()
        date = items_in_line[0]
        amount = items_in_line[1]
        pair = (date, amount)
        raw_dates_and_totals.append(pair)
    dates_and_total_rain = [tuple(
        s if s != "-" else "0" for s in pair)
            for pair in raw_dates_and_totals]
    return dates_and_total_rain


def date_amount_to_year_amount(date_and_amount):
    """brings in the date_and_amount tuple and returns only the year and """
    amount = date_and_amount[1]
    year = date_and_amount[0][-4:]
    return (year, amount)


def print_max_rain_date_and_amount(dates_and_totals):
    date, amount = max(dates_and_totals, key=lambda x: int(x[1]))
    inches = (int(amount) * .01)
    print(
        'The most rainfall, in a single day, was {} inches on {}.'.format(
            inches, date))


def display_rainiest_year(dates_and_totals):
    years_and_amounts = [date_amount_to_year_amount(pair) for pair in dates_and_totals]
    # convert the tuples to a dict
    d = {}
    for year, amount in years_and_amounts:
        d.setdefault(year, []).append(int(amount))
    # sum together all the values for each key in the dict
    e = {year: sum(amount) for year, amount in d.items()}
    # find the year with max amount of rain
    x = max(e, key=e.get)
    # find the amount of rain for that year
    y = (e.get(x) * .01)
    print(
        "{} was the area's wettest year with a total of {} inches of rain.\n"
        .format(x, y)
    )

gauge_dict = create_rain_gauge_dict()
run = True
while run:
    os.system('cls')
    dates_and_totals = get_date_and_total_rain()
    print_max_rain_date_and_amount(dates_and_totals)
    display_rainiest_year(dates_and_totals)
    yayornay = input(
        'Would you like to check another station? [y/n]: ').lower()
    if yayornay == 'y':
        run = True
    else:
        run = False
