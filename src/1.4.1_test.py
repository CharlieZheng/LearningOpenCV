#-*- encoding=utf-8 -*-

import cv2
import numpy as np

img = np.zeros((400, 400,3), np.uint8)
# 蓝色通道
img[:, :,0] =0x00 
 # 绿色
img[:, :,1] =0xcc
 # 红色
img[:, :,2] =0x99

img[100:300,100:300,0]=0xff

img[100:300,100:300,1]=0x5c

img[100:300,100:300,2]=0x5c
cv2.imshow('img', img)

hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV) 

# 范围0~180
hueOut= hsv[0, 0, 0]
print('hsv色调 %d' %hueOut)
# 范围0~255
saturationOut =hsv[0, 0, 1]
print ('hsv饱和度 %d' %saturationOut) 
# 范围0~255
valueOut =hsv[0, 0, 2]
print ('hsv亮度 %d' %valueOut)

hueIn = hsv[200, 200, 0]
print ('hsv蓝色 %d' %hueIn)
saturationIn =hsv[200, 200, 1]
print ('hsv绿色 %d' %saturationIn)
valueIn =hsv[200, 200, 2]
print ('hsv红色 %d' %valueIn)

cv2.imshow('hsv', hsv)

#mask = cv2.inRange(hsv, np.array([hueOut, saturationOut, valueOut]), np.array([hueOut, saturationOut, valueOut]))

mask = cv2.inRange(hsv, np.array([hueIn, saturationIn, valueIn]), np.array([hueIn, saturationIn, valueIn]))

cv2.imshow('mask', mask)

res = cv2.bitwise_and(img, img, mask = mask)
cv2.imshow('res', res)

key = cv2.waitKey(0) & 0xff
if (key == 27):
	cv2.destroyAllWindows()
