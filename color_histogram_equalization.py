# -*- coding: utf-8 -*-
# DISCIPLINA - PROCESSAMENTO DIGITAL DE IMAGENS
# SEMESTRE - 2020.1
# ALUNO - LUCAS ISMAEL CAMPOS MEDEIROS

import cv2
import numpy as np
import math
from matplotlib import pyplot as plt

def RGB_TO_HSI(img):

    with np.errstate(divide='ignore', invalid='ignore'):

        #Load image with 32 bit floats as variable type
        bgr = np.float32(img)/255

        #Separate color channels
        blue = bgr[:,:,0]
        green = bgr[:,:,1]
        red = bgr[:,:,2]

        #Calculate Intensity
        def calc_intensity(red, blue, green):
            return np.divide(blue + green + red, 3)

        #Calculate Saturation
        def calc_saturation(red, blue, green):
            minimum = np.minimum(np.minimum(red, green), blue)
            saturation = 1 - (3 / (red + green + blue + 0.001) * minimum)

            return saturation

        #Calculate Hue
        def calc_hue(red, blue, green):
            hue = np.copy(red)

            for i in range(0, blue.shape[0]):
                for j in range(0, blue.shape[1]):
                    hue[i][j] = 0.5 * ((red[i][j] - green[i][j]) + (red[i][j] - blue[i][j])) / \
                                math.sqrt((red[i][j] - green[i][j])**2 +
                                        ((red[i][j] - blue[i][j]) * (green[i][j] - blue[i][j])))
                    hue[i][j] = math.acos(hue[i][j])

                    if blue[i][j] <= green[i][j]:
                        hue[i][j] = hue[i][j]
                    else:
                        hue[i][j] = ((360 * math.pi) / 180.0) - hue[i][j]

            return hue

        #Merge channels into picture and return image
        hsi = cv2.merge((calc_hue(red, blue, green), calc_saturation(red, blue, green), calc_intensity(red, blue, green)))
        return hsi
    
img = cv2.imread(r'C:/Users/Lucas Ismael/Documents/PDI_2020/images/naruto.png')
cv2.imshow("src", img)

(b, g, r) = cv2.split(img)

blueEQ = cv2.equalizeHist(b)
greenEQ = cv2.equalizeHist(g)
redEQ = cv2.equalizeHist(r)

finalEQ = cv2.merge((blueEQ, greenEQ, redEQ))
cv2.imshow("final", finalEQ)

# plt.figure()
# plt.imshow(img_hsi)
# plt.figure()
# plt.imshow(img_hsi[:, :,0], cmap='gray')
# plt.figure()
# plt.imshow(img_hsi[:, :,1], cmap='gray')
# plt.figure()
# plt.imshow(img_hsi[:, :,2], cmap='gray')

#plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
# plt.show()