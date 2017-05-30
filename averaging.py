import cv2
import numpy as np 

img = cv2.imread("koudou.jpg")

img_gry = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

kernel = np.ones((5,5),np.float32)/25

result = cv2.filter2D(img_gry,-1,kernel)

cv2.imwrite("result_averaging.jpg", result)


img = cv2.imread("gry.jpg")

blur = cv2.blur(img, (3,3))

cv2.imwrite("result_averaging3x3.jpg", blur)


noise = cv2.imread("ngry.jpg")

blured = cv2.blur(noise, (5,5))

cv2.imwrite("averaging_noise.jpg", blured)