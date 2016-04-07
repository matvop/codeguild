import cv2
import urllib.request
import numpy as np

# use the method below to retrieve recorded byte file and playback
# in place of the stream url

stream = urllib.request.urlopen('http://50.73.56.89/axis-cgi/mjpg/video'
                                '.cgi?date=1&clock=1&resolution=640x360')

bytes = b''
while True:
    bytes += stream.read(1024)
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
