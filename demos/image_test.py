import urllib.request
def parse_index_url_into_lines():
    with urllib.request.urlopen(
        'http://al.robotfuzz.com/~al/random/bad3.png') as data_file:
            image_line_data = data_file.readlines()
    print(image_line_data)
parse_index_url_into_lines()
