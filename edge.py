import cv2
import numpy as np

img = cv2.imread("gry.jpg")

edge = cv2.Canny(img, 50, 100)

cv2.imwrite("edg.jpg", edge)


kernel_x = np.array([
                            [ 0,  0,  0],
                            [ -1,  0,  1],
                            [ 0,  0,  0]
                            ], np.float32)	

result = cv2.filter2D(img, -1, kernel_x)

result = cv2.convertScaleAbs(result)

cv2.imwrite("x1.jpg", result)


kernel_y = np.array([
                            [ 0,  1,  0],
                            [ 0,  0,  0],
                            [ 0,  -1,  0]
                            ], np.float32)	

result = cv2.filter2D(img, -1, kernel_y)

result = cv2.convertScaleAbs(result)

cv2.imwrite("y1.jpg", result)



kernel_Prewitt_x = np.array([
                            [ -1,  0,  1],
                            [ -1,  0,  1],
                            [ -1,  0,  1]
                            ], np.float32)	

result = cv2.filter2D(img, -1, kernel_Prewitt_x)

result = cv2.convertScaleAbs(result)

cv2.imwrite("PrewX.jpg", result)



kernel_Sobel_x = np.array([
                            [ -1,  0,  1],
                            [ -2,  0,  2],
                            [ -1,  0,  1]
                            ], np.float32)	

result = cv2.filter2D(img, -1, kernel_Sobel_x)

result = cv2.convertScaleAbs(result)

cv2.imwrite("SobelX.jpg", result)



kernel_Prewitt_y = np.array([
                            [ 1,  1,  1],
                            [ 0,  0,  0],
                            [-1, -1, -1]
                            ], np.float32)

result = cv2.filter2D(img, -1, kernel_Prewitt_y)

result = cv2.convertScaleAbs(result)

cv2.imwrite("PrewY.jpg", result)


kernel_Sobel_y = np.array([
                            [ 1,  2,  1],
                            [ 0,  0,  0],
                            [-1, -2, -1]
                            ], np.float32)

result = cv2.filter2D(img, -1, kernel_Sobel_y)

result = cv2.convertScaleAbs(result)

cv2.imwrite("SobelY.jpg", result)



kernel_Sobel_ym = np.array([
                            [-1, -2, -1],
                            [ 0,  0,  0],
                            [ 1,  2,  1]
                            ], np.float32)

result2 = cv2.filter2D(img, -1, kernel_Sobel_ym)

result = cv2.convertScaleAbs(result)

cv2.imwrite("SobelYm.jpg", result2)