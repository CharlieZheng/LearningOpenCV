import cv2
import numpy as np
from matplotlib import pyplot as plt
img = cv2.imread('/home/hanrong/Desktop/opencv/build/Zheng/2.jpeg')
edges = cv2.pyrDown(img, img)
img2 = cv2.pyrUp(img, img)
plt.subplot(131),plt.imshow(img)
plt.title('Original Image'), plt.xticks([]), plt.yticks([])
plt.subplot(132),plt.imshow(edges)
plt.title('Edge Image'), plt.xticks([]), plt.yticks([])
plt.subplot(133),plt.imshow(img2)
plt.title('Edge Image'), plt.xticks([]), plt.yticks([])
plt.show()
