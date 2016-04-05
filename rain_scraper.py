# City of Portland - Hydra Network Rain Gauge scraper
# Retrieves hourly updated rain gauge data from or.water.usgs.gov.
# (internet connection required)
# Supports user selection of a specific rain gauge station.
# Currently outputs the street address selected location,
# date of most rainfall - amount of rain, and the location's wettest year
# and amount of rain for that year
# possible revisions: average rainfall for chosen date, ability to notify
# user if location has been retired, weather prediction

import urllib.request
import os


def parse_index_url():
    """Parse Oregon usgs rain station index page into a list of lines"""
    with urllib.request.urlopen(
    'http://or.water.usgs.gov/non-usgs/bes/') as data_file:
        all_gauges_line_data = [byte_line.decode('utf-8')
                                for byte_line in data_file]
    return all_gauges_line_data[120:]


def parse_rain_file_url():
    """Parse user selected rain station file into a list of lines"""
    print('Rain level data is available for the listed locations.\n')
    url = gauge_dict[input('Please enter station id#: ')][1]
    with urllib.request.urlopen(url) as rain_file:
        rain_lines = [byte_line.decode('utf-8')
                      for byte_line in rain_file]
    return rain_lines


def create_station_list():
    """Find the index positions lines in the html source which contain the
    string. Increases the index pos by 1 to reach the station id line"""
    station_indices = [(i+1) for i, s in enumerate(html_source_lines) if
                       'Rain Gage<br>' in s]
    station_number_lines = [html_source_lines[i] for i in station_indices]
    station_number_raw = [line[17:] for line in station_number_lines]
    return [line[:-6] for line in station_number_raw]


def create_location_list():
    """Create list of location names - same method. Lines cleaned
    of extra characters and returned into a location_list"""
    location_search_string = 'Rain Gage<br>'
    lines_with_rain_gauge_address = [line for line in html_source_lines
                                     if location_search_string in line]
    location_raw = [line[4:] for line in lines_with_rain_gauge_address]
    location_list = [line for line in location_raw]
    # cuts the rest of the junk out of each line
    return [i.split('Rain Gage<br>', 1)[0] for i in location_list]


def create_url_list():
    """Create and return a list of urls from .rain file names, with known
    url prefix. Remove two erroneous locations from list."""
    url_prefix = 'http://or.water.usgs.gov/non-usgs/bes/'
    url_search_string = '.rain'
    lines_with_matching_url = [line for line in html_source_lines
                               if url_search_string in line]
    url_raw = [line[26:] for line in lines_with_matching_url]
    url_list = [line[:-22] for line in url_raw]
    url_list.pop(url_list.index('rover.rain'))
    url_list.pop(url_list.index('swan_island.rain'))
    return [url_prefix + url for url in url_list]


def create_rain_gauge_dict():
    return {z[0]: list(z[1:]) for z in zip(
            create_station_list(),
            create_location_list(),
            create_url_list())}


def display_gauges():
    """Provide the user with a table of available rain stations by their
    id#, location, and .rain file url."""
    print('\n{:<15} {:<40} {:<40}'.format('Station id#:', 'Location:',
                                          'URL:\n'))
    for k, v in gauge_dict.items():
        location, url = v
        print('{:<15} {:<40} {:<40}'.format(k, location, url))
    print('')


def date_amount_to_year_amount(date_and_amount):
    amount = date_and_amount[1]
    year = date_and_amount[0][-4:]
    return (year, amount)


def date_amount_to_day_month_amount(date_and_amount):
    amount = date_and_amount[1]
    day_month = date_and_amount[0][:-5]
    return (day_month, amount)


def display_rain_info():
    rain_line_data = parse_rain_file_url()
    print('\nCurrently connected to the ' + rain_line_data[0])
    raw_dates_and_totals = []
    for line in rain_line_data[11:]:
        items_in_line = line.split()
        date = items_in_line[0]
        amount = items_in_line[1]
        pair = (date, amount)
        raw_dates_and_totals.append(pair)
    dates_and_totals = [tuple(`i`
        s if s != "-" else "0" for s in pair)
            for pair in raw_dates_and_totals]
    date, amount = max(dates_and_totals, key=lambda x: int(x[1]))
    inches = (int(amount) * .01)
    todays_date = rain_line_data[11][:6]
    matching_dates = []
    todays_date_and_amounts = [date_amount_to_day_month_amount(pair)
                               for pair in dates_and_totals]
    for pair in todays_date_and_amounts:
        if todays_date in pair:
            matching_dates.append(pair)
    historic_rain_today = (sum([int(i[1]) for i in matching_dates]))
    average = int(historic_rain_today/ len(matching_dates))
    avg_converted = str(average * .01)
    print('Historically, for this location, the average rainfall '
          'on ' + todays_date + ' is ' + avg_converted + ' inches.')
    print('The most rainfall, in a single day,'
          ' was {} inches on {}.'.format(inches, date))


def display_rainiest_year():
    years_and_amounts = [date_amount_to_year_amount(pair)
                         for pair in dates_and_totals]
    # years_and_amounts = [(pair[0][-4:], pair[1]) for pair
    #                       in dates_and_totals if len(pair) > 1]
    d = {}
    # convert the tuples to a dict - change amount string to int
    for year, amount in years_and_amounts:
        d.setdefault(year, []).append(int(amount))
    # sum together all the values for each key in the dict
    e = {year: sum(amount) for year, amount in d.items()}
    # find the year with max amount of rain
    x = max(e, key=e.get)
    # find the amount of rain for that year
    y = (e.get(x) * .01)
    print("{} was the area's wettest year with "
          'a total of {} inches of rain.\n'.format(x, y))


html_source_lines = parse_index_url()
gauge_dict = create_rain_gauge_dict()
rain = True
while rain:
    os.system('cls')
    display_gauges()
    display_rain_info()
    yayornay = input('Would you like to check another station? [y/n]: '
                     ).lower()
    if yayornay == 'y':
        rain = True
    else:
        rain = False
