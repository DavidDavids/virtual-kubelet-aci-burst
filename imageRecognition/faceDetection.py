#source http://docs.opencv.org/trunk/d7/d8b/tutorial_py_face_detection.html
#this code is to be used for demo purposes only
import sys
import numpy as np
import cv2
from PIL import Image
import glob

sys.path.append('/usr/local/lib/python2.7/site-packages')
image_list = []
for filename in glob.glob('~/Documents/pics/.jpg'): #assuming gif
    im=Image.open(filename)
    image_list.append(im)
#add code to take in a file with multiple pictures
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier('haarcascade_eye.xml')
for imageNum in image_list:
    img = cv2.imread('image_list[imageNum]')
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)
    for (x,y,w,h) in faces:
        cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
        roi_gray = gray[y:y+h, x:x+w]
        roi_color = img[y:y+h, x:x+w]
        eyes = eye_cascade.detectMultiScale(roi_gray)
        for (ex,ey,ew,eh) in eyes:
            cv2.rectangle(roi_color,(ex,ey),(ex+ew,ey+eh),(0,255,0),2)
    cv2.imshow('img',img)
    #
    cv2.waitKey(0)
    cv2.destroyAllWindows()
