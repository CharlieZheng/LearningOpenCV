import cv2
import numpy as np
img = cv2.imread('/home/hanrong/Desktop/opencv/build/Zheng/0.jpeg')
res = cv2.resize(img,None,fx=2, fy=2, interpolation = cv2.INTER_CUBIC)
cv2.imshow('scale1', res)
#OR
height, width = img.shape[:2]
res = cv2.resize(img,(2*width, 2*height), interpolation = cv2.INTER_CUBIC)
cv2.imshow('scale2', res)
while (1):
	key = cv2.waitKey(0) & 0xff
	if (key == 27) :break
cv2.destroyAllWindows()
