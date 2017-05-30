import cv2
import numpy as np 

img = cv2.imread("gry.jpg")

blured = cv2.GaussianBlur(img, (5,5), 0)

cv2.imwrite("result_Gaussian55.jpg", blured)

kernel_gaussian = np.array([
                            [1,  2, 1],
                            [2,  4, 2],
                            [1,  2, 1]
                            ], np.float32) / 16

img_gaussian = cv2.filter2D(img, -1, kernel_gaussian)

cv2.imwrite("result_Gaussian33.jpg", img_gaussian)



noise = cv2.imread("ngry.jpg")

blured = cv2.GaussianBlur(noise, (5,5), 0)

cv2.imwrite("Gaussian_noise.jpg", blured)