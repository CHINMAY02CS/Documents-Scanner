# Importing package to open the url
import urllib.request as request

# Importing the required packages
import numpy as np
import cv2
from PIL import Image
import time

# Creating a variable 'url' to store the url of the IP Webcam
url = 'http://192.168.137.95:8080/shot.jpg'

# we will now be using the urllib to always capture and open the latest image

while True:   # Using 'True' for running the while loop continuously
    img = request.urlopen(url)  # returns the object of the url
    img_bytes = bytearray(img.read()) # converting the image into array
    img_np = np.array(img_bytes, dtype=np.uint8)  # declared the type of data we after storing

    # creating frame for displaying the video
    frame = cv2.imdecode(img_np, -1)   # using flag -1 to bring no change to original image
    frame_cvt = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)  # converting the frame from BGR color code to RGB color code
    frame_blur = cv2.GaussianBlur(frame_cvt, (5, 5), 0)   # smoothing image with (kernel size) , standard deviation
    frame_edge = cv2.Canny(frame_blur, 30, 50)  # detecting the edges with threshold values using Canny Edge detector

    # detecting object by finding contours by retrieving as list by calculating for storage using approximate method
    contours, h = cv2.findContours(frame_edge, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)

    # finding the largest contour
    if contours:
        max_contour = max(contours, key=cv2.contourArea)  # detecting biggest contour using contour area
        x, y, w, h = cv2.boundingRect(max_contour)  # want the rectangle boundary x and y axes and height and width
        if cv2.contourArea(max_contour) > 5000:

            # drawing rectangle with starting and ending points and colors
            cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 255), 2)
            # Comment out the above line if we do not want the frame border to appear in scanned image

            # taking small portion of the frame
            object_only = frame[y: y+h, x: x+w]

            cv2.imshow('Smart Scanner', object_only)   # if you want to scan large area, change 'object_only' to 'frame'
            if cv2.waitKey(1) == ord('s'):  # checking if alphabet 's' is pressed on keyboard

                img_pil = Image.fromarray(object_only)  # the frame consists of array
                # if you want to scan large area, change 'object_only' to 'frame' in above line

                # creating time instance for storing image
                time_str = time.strftime('%Y-%m-%d-%H-%M-%S')  # Year - month - date - Hour - Minute - Second

                img_pil.save(f'{time_str}.pdf')  # storing the image with dynamic name format of time_str
                print(time_str)




