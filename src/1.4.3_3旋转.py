#-*- encoding=utf-8
import cv2
import numpy as np
img = cv2.imread('/home/hanrong/Desktop/opencv/build/Zheng/0.jpeg',0)
rows,cols = img.shape
# 第三个参数表示缩放比例
M = cv2.getRotationMatrix2D((cols/2,rows/2),90,4) 
dst = cv2.warpAffine(img,M,(cols,rows))
cv2.imshow('dst', dst)
cv2.waitKey(0)
cv2.destroyAllWindows()
