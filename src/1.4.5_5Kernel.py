import numpy as np
import cv2
#kernel = np.ones((5,5),np.uint8)
#kernel=cv2.getStructuringElement(cv2.MORPH_RECT,(5,5))
#kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE,(5,5))
kernel = cv2.getStructuringElement(cv2.MORPH_CROSS,(5,5))
print(kernel)
