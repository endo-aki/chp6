import cv2
import numpy as np 

img = cv2.imread("gry.jpg")

blur = cv2.bilateralFilter(img,9,75,75)

cv2.imwrite("bilateral.jpg", blur)



color = cv2.imread("koudou.jpg")

blured = cv2.bilateralFilter(color,9,75,75)

cv2.imwrite("bilateral_color.jpg", blured)



for n in range(2):
	blured = cv2.bilateralFilter(blured,9,75,75)

cv2.imwrite("bilateral_color4.jpg", blured)