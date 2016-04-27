import urllib.request
import requests
from requests.auth import HTTPBasicAuth

# use the method below to retrieve recorded byte file and playback
# in place of the stream url
# '.cgi?date=1&clock=1&resolution=[640]x[360]'
# stream = urllib.request.urlopen('http://50.73.56.89/axis-cgi/mjpg/video.cgi?date=1&clock=1&resolution=640x400&compression=15')
# stream = urllib.request.urlopen('http://esoteric.ddns.net:8181/axis-cgi/mjpg/video.cgi?date=1&clock=1&resolution=640x400&compression=15')

url = 'http://esoteric.ddns.net:8181/axis-cgi/mjpg/video.cgi?date=1&clock=1&resolution=640x400&compression=15'
r = requests.get(url, auth=('sudo', '281281'), stream=True)
cap = cv2.VideoCapture(url)
# Define the codec and create VideoWriter object
fourcc = cv2.VideoWriter_fourcc(*'MJPG')
out = cv2.VideoWriter('output.avi',fourcc, 20.0, (640,400))
