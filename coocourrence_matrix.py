# -*- coding: utf-8 -*-
# DISCIPLINA - PROCESSAMENTO DIGITAL DE IMAGENS
# SEMESTRE - 2020.1
# ALUNO - LUCAS ISMAEL CAMPOS MEDEIROS
import subprocess, os
import numpy as np
import matplotlib.pyplot as plt
import cv2
import random
import skimage.feature as skf


# print('Select an image: \n')
img = cv2.imread(r'C:/Users/Lucas Ismael/Documents/PDI_2020/images/'+input('Selected input(.pgm):')+'.pgm',0)
#img = cv2.imread(r'C:/Users/Lucas Ismael/Documents/PDI_2020/images/Lena.pgm',0)
ccmatrix = skf.greycomatrix(img,[1],[0], levels = 256)
imgccmatrix = ccmatrix[:,:,0,0]


print('-------------------------------------' + '\n')
print('| contrast = ' + str(skf.greycoprops(ccmatrix, 'contrast')[0][0]) + '      | \n')
print('-------------------------------------' + '\n')
print('| dissimilarity = ' + str(skf.greycoprops(ccmatrix, 'dissimilarity')[0][0]) + ' |\n')
print('-------------------------------------' + '\n')
print('| homogeneity = ' + str(skf.greycoprops(ccmatrix, 'homogeneity')[0][0]) + ' |\n')
print('-------------------------------------' + '\n')
print('| energy = ' + str(skf.greycoprops(ccmatrix, 'energy')[0][0]) + '      |\n')
print('-------------------------------------' + '\n')
print('| correlation = ' + str(skf.greycoprops(ccmatrix, 'correlation')[0][0]) + '  |\n')
print('-------------------------------------' + '\n')

plt.figure()
plt.subplot(121),plt.imshow(img, cmap='gray'),plt.title('Imagem Original')
plt.xticks([]), plt.yticks([])
plt.subplot(122),plt.imshow(imgccmatrix, cmap='gray'),plt.title('Matriz de co-ocorrência')
plt.xticks([]), plt.yticks([])
plt.show()