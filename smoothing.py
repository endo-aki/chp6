import cv2
import numpy as np 


img = cv2.imread("gry.jpg")

kernel = np.array([
                    [0, 0, 1, 0, 0],
                    [0, 0, 1, 0, 0],
                    [0, 0, 1, 0, 0],
                    [0, 0, 1, 0, 0],
                    [0, 0, 1, 0, 0]
                                         ], np.float32) / 5

smoothing = cv2.filter2D(img, -1, kernel)

cv2.imwrite("tate.jpg", smoothing)



kernel = np.array([
                    [1, 0, 0, 0, 0],
                    [0, 1, 0, 0, 0],
                    [0, 0, 1, 0, 0],
                    [0, 0, 0, 1, 0],
                    [0, 0, 0, 0, 1]
                                         ], np.float32) / 5

smoothing = cv2.filter2D(img, -1, kernel)

cv2.imwrite("naname.jpg", smoothing)



kernel = np.array([
                    [0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0],
                    [1, 1, 1, 1, 1],
                    [0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0]
                                         ], np.float32) / 5

smoothing = cv2.filter2D(img, -1, kernel)

cv2.imwrite("yoko.jpg", smoothing)