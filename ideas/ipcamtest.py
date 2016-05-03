import cv2
import urllib.request
import requests
from requests.auth import HTTPBasicAuth
import numpy as np

# use the method below to retrieve recorded byte file and playback
# in place of the stream url
# '.cgi?date=1&clock=1&resolution=[640]x[360]'
# stream = urllib.request.urlopen('http://50.73.56.89/axis-cgi/mjpg/video.cgi?date=1&clock=1&resolution=640x400&compression=15')
# stream = urllib.request.urlopen('http://esoteric.ddns.net:8181/axis-cgi/mjpg/video.cgi?date=1&clock=1&resolution=640x400&compression=15')
# http://50.73.56.89/mjpg/video.mjpg
# http://sudo:281281@esoteric.ddns.net:8181/mjpg/video.mjpg
url = 'http://esoteric.ddns.net:8181/axis-cgi/mjpg/video.cgi?date=1&clock=1&resolution=640x400&compression=15'
stream = requests.get(url, auth=('sudo', '281281'), stream=True)

bytes = b''
while True:
    bytes += stream.raw.read(1024)
    a = bytes.find(b'\xff\xd8')
    b = bytes.find(b'\xff\xd9')
    if a != -1 and b != -1:
        jpg = bytes[a:b + 2]
        # print(jpg)
        bytes = bytes[b + 2:]
        image = cv2.imdecode(np.fromstring(jpg, dtype=np.uint8),
                         cv2.IMREAD_COLOR)
        cv2.imshow('MJPG Network Camera Stream', image)
        # with open('C:\\Users\\Matt\\Desktop\\test.mjpg', 'wb') as output:
        #     output.write(i)
        if cv2.waitKey(1) == 27:
            exit(0)


# cap = cv2.VideoCapture(url)
# # Define the codec and create VideoWriter object
# fourcc = cv2.VideoWriter_fourcc(*'MJPG')
# out = cv2.VideoWriter('output.avi',fourcc, 20.0, (640,400))
#
# while(cap.isOpened()):
#     ret, frame = cap.read()
#     if ret==True:
#         frame = cv2.flip(frame,0)
#         # write the flipped frame
#         out.write(frame)
#         cv2.imshow('frame',frame)
#         if cv2.waitKey(1) == 27:
#             exit(0)
#     else:
#         break
#
# # Release everything if job is finished
# cap.release()
# out.release()
# cv2.destroyAllWindows()

# """READING FROM MJPG FILE"""
# import cv2
# import urllib
# import numpy as np
#
# stream = open('C:\\Users\\Matt\\Desktop\\test.mjpg', 'rb')
# print(stream)
# bytes = b''
# while True:
#     bytes += stream.read(1024)
#     a = bytes.find(b'\xff\xd8')
#     b = bytes.find(b'\xff\xd9')
#     if a != -1 and b != -1:
#         jpg = bytes[a:b+2]
#         bytes = bytes[b+2:]
#         i = cv2.imdecode(np.fromstring(jpg, dtype=np.uint8), cv2.IMREAD_COLOR)
#         cv2.imshow('i', i)
#         if cv2.waitKey(1) == 27:
#             exit(0)
