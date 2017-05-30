import cv2
import numpy as np 

img = cv2.imread("gry.jpg")

laplacian = cv2.Laplacian(img, -1)

cv2.imwrite("laplacian.jpg", laplacian)


laplacian2 = cv2.Laplacian(img, cv2.CV_32F)

cv2.imwrite("laplacian32.jpg", laplacian2)




