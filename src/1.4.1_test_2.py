#-*- encoding=utf-8 -*-
import cv2
import numpy as np


img = cv2.imread('/home/hanrong/Desktop/opencv/build/Zheng/0.jpeg')

cv2.imshow('img', img)

hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV) 


cv2.imshow('hsv', hsv)

mask = cv2.inRange(hsv, np.array([13, 153, 163]), np.array([15, 162, 180]))

#mask = cv2.inRange(hsv, np.array([hueIn, saturationIn, valueIn]), np.array([hueIn, saturationIn, valueIn]))

cv2.imshow('mask', mask)

res = cv2.bitwise_and(img, img, mask = mask)
cv2.imshow('res', res)

key = cv2.waitKey(0) & 0xff
if (key == 27):
	cv2.destroyAllWindows()
