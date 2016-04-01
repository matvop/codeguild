import urllib.request


# retired_location_search_string = ''
# for line in truncated_html_source_lines:
#     if all(s in line for s in search_string):
#         occurances += 1
# print(occurances)
# retired_location = [s for s in truncated_html_source_lines if retired_location_search_string in s]
def parse_index_url_into_lines():
    with urllib.request.urlopen('http://or.water.usgs.gov/non-usgs/bes/') as data_file:
        all_gauges_line_data = [byte_line.decode('utf-8') for byte_line in data_file]
    return all_gauges_line_data

def create_list_of_urls(truncated_html_source_lines):
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
    line_num = 0
    location_list = []
    location_search_string = 'Rain Gage<br>'
    matching_location = [s for s in truncated_html_source_lines if location_search_string in s]
    for line in matching_location:
        decoded_line = matching_location[line_num]
        location_raw = decoded_line[4:]
        location_list.append(location_raw[:-6])
        line_num += 1
    location_list = [i.split('<', 1)[0] for i in location_list]
    return location_list

html_source_lines = parse_index_url_into_lines()
truncated_html_source_lines = html_source_lines[120:]
rain_gauge_dict = dict(zip(create_list_of_locations(truncated_html_source_lines),create_list_of_urls(truncated_html_source_lines)))
