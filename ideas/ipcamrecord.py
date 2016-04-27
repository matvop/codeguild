import cv2
import urllib.request
import requests
from requests.auth import HTTPBasicAuth
import numpy as np


url = 'http://esoteric.ddns.net:8181/axis-cgi/mjpg/video.cgi?date=1&clock=1&resolution=640x400&compression=15'
r = requests.get(url, auth=('sudo', '281281'), stream=True)
cap = cv2.VideoCapture(url)
# Define the codec and create VideoWriter object
fourcc = cv2.VideoWriter_fourcc('M','J','P','G')
out = cv2.VideoWriter('output.avi',fourcc, 5.0, (640,400))

while(cap.isOpened()):
    ret, frame = cap.read()
    if ret==True:
        frame = cv2.flip(frame,0)
        # write the flipped frame
        out.write(frame)
        cv2.imshow('frame',frame)
        if cv2.waitKey(1) == 27:
            exit(0)
    else:
        break

# Release everything if job is finished
cap.release()
out.release()
cv2.destroyAllWindows()
