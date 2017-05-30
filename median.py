import cv2
import numpy as np 

img = cv2.imread("ngry.jpg")

median = cv2.medianBlur(img,5)

cv2.imwrite("median.jpg", median)