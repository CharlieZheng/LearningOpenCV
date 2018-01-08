import cv2
import numpy as np
from matplotlib import pyplot as plt
img = cv2.imread('/home/hanrong/Desktop/opencv/build/Zheng/0.jpeg')


blur = cv2.GaussianBlur(img,(5,5),0)
img[0:100, 0:100] = blur[0:100, 0:100]


#kernel = cv2.getGaussianKernel(img, img.rows, img.cols )
kernel = np.ones((5,5),np.float32)/25
dst = cv2.filter2D(img,-1,kernel)


plt.subplot(131),plt.imshow(img),plt.title('Original')
plt.xticks([]), plt.yticks([])
plt.subplot(132),plt.imshow(blur),plt.title('Blurred')
plt.xticks([]), plt.yticks([])
plt.subplot(133),plt.imshow(dst),plt.title('Blurred')
plt.xticks([]), plt.yticks([])
plt.show()
