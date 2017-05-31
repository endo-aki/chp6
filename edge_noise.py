import cv2
import numpy as np 

noise = cv2.imread("ngry.jpg")

kernel_x = np.array([
                            [ 0,  0,  0],
                            [ -1,  0,  1],
                            [ 0,  0,  0]
                            ], np.float32)	

result = cv2.filter2D(noise, -1, kernel_x)

result = cv2.convertScaleAbs(result)

cv2.imwrite("x1_noise.jpg", result)



kernel_Sobel_x = np.array([
                            [ -1,  0,  1],
                            [ -2,  0,  2],
                            [ -1,  0,  1]
                            ], np.float32)	

result = cv2.filter2D(noise, -1, kernel_Sobel_x)

result = cv2.convertScaleAbs(result)

cv2.imwrite("SobelX_noise.jpg", result)


img =cv2.imread("Gaussian_noise.jpg")

result = cv2.filter2D(img, -1, kernel_Sobel_x)

result = cv2.convertScaleAbs(result)

cv2.imwrite("Gaussian_noise_edge.jpg", result)