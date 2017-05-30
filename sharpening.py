import cv2
import numpy as np

img = cv2.imread("gry.jpg")

kernel_sharpe = np.array([
                            [ -1,  -1,  -1],
                            [ -1,   9,  -1],
                            [ -1,  -1,  -1]
                            ])	

result = cv2.filter2D(img, -1, kernel_sharpe)

result = cv2.convertScaleAbs(result)

cv2.imwrite("sharpe.jpg", result)


k = 0.5

op = np.array([
                [-k, -k, -k],
                [-k, 1 + 8 * k, -k],
                [-k, -k, -k]
            ])

result = cv2.filter2D(img, -1, op)

result = cv2.convertScaleAbs(result)

cv2.imwrite("sharpe_k05.jpg", result)


k = 2.0

op = np.array([
                [-k, -k, -k],
                [-k, 1 + 8 * k, -k],
                [-k, -k, -k]
            ])

result = cv2.filter2D(img, -1, op)

result = cv2.convertScaleAbs(result)

cv2.imwrite("sharpe_k20.jpg", result)



from PIL import Image
from scipy import ndimage

color = np.array(Image.open("koudou.jpg"))

color_r = color[:, :, 0]
color_g = color[:, :, 1]
color_b = color[:, :, 2]

result_r = ndimage.convolve(color_r, kernel_sharpe)
result_g = ndimage.convolve(color_g, kernel_sharpe)
result_b = ndimage.convolve(color_b, kernel_sharpe)

result = np.empty(img.shape, dtype='uint8')

result[:, :, 0] = result_r[:, :]
result[:, :, 1] = result_g[:, :]
result[:, :, 2] = result_b[:, :]

Image.fromarray(result).save('sharpe_color.png')