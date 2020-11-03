# -*- coding: utf-8 -*-
# DISCIPLINA - PROCESSAMENTO DIGITAL DE IMAGENS
# SEMESTRE - 2020.1
# ALUNO - LUCAS ISMAEL CAMPOS MEDEIROS
import subprocess, os
import numpy as np
import matplotlib.pyplot as plt
import cv2
import random
from PIL import Image, ImageFilter

def my_imgcompare(img1, img2):
     plt.figure()
     plt.subplot(121),plt.imshow(img1, cmap='gray'),plt.title('Imagem Original')
     plt.xticks([]), plt.yticks([])
     plt.subplot(122),plt.imshow(img2, cmap='gray'),plt.title('Imagem Processada')
     plt.xticks([]), plt.yticks([])
     plt.show()
     
def my_spnoise(*args):
    noise_output = np.zeros(img.shape, np.uint8)
    #prob = float(input('a: '))
    prob = 0.05
    thres = 1-prob
    for i in range(img.shape[0]):
        for j in range(img.shape[1]):
            rdn = random.random()
            if rdn < prob:
                noise_output[i][j] = 0
            elif rdn > thres:
                noise_output[i][j] = 255
            else:
                noise_output[i][j] = img[i][j]
    return noise_output

img = cv2.imread(r'C:/Users/Lucas Ismael/Documents/PDI_2020/images/Lena.pgm',0)
noise_image = my_spnoise(img)

n = int(input('Mask size: '))
kernel = np.ones((n, n), float)


mean = cv2.blur(img, (n, n))
#my_imgcompare(img, mean)

median = cv2.medianBlur(noise_image, n)
#my_imgcompare(noise_image, median)

gaussian = cv2.GaussianBlur(img, (n, n), 0)
#my_imgcompare(img, gaussian)

minfilter = cv2.erode(img, kernel)
#my_imgcompare(img, minfilter)

maxfilter = cv2.dilate(img, kernel) 
#my_imgcompare(img, maxfilter)

laplacian = cv2.Laplacian(img,cv2.CV_64F, ksize = n)
my_imgcompare(img, laplacian)
my_imgcompare(img, img+laplacian)
my_imgcompare(img, img-laplacian)
