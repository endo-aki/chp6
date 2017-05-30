import cv2
import numpy as np 

img = cv2.imread("koudou.jpg")

img_gry = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

cv2.imwrite("koudou.jpg", img_gry)