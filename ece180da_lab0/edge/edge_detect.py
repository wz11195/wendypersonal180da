import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('yaoming.jpg', 0)
edges = cv2.Canny(img, 100, 200, True)

#To save an image to any storage device
#cv2.imwrite('edge_image.jpg', edges)


plt.subplot(121), plt.imshow(img,cmap = 'gray')
plt.title('Orginal Image'), plt.xticks([]), plt.yticks([])
plt.subplot(122), plt.imshow(edges, cmap = 'gray')
plt.title('Edge Image'), plt.xticks([]), plt.yticks([]) 

plt.show()
