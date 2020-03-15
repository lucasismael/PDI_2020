# -*- coding: utf-8 -*-
import numpy as np
import matplotlib.pyplot as plt

def my_readimage(path):
    file = open(path, 'r')

    read_header = file.readline()
    read_wh = file.readline()
    aux0 = read_wh.split()
    columns = int(aux0[0])
    rows = int(aux0[1])
    max_intensity = file.readline()


    aux = file.read().split()
    aux_matrix = np.reshape(aux,(rows, columns))
    intensity_matrix = np.zeros((rows, columns), int)

    for i in range(rows):
        for j in range(columns):
            intensity_matrix[i][j] = int(aux_matrix[i][j])
    return read_header, rows, columns, max_intensity, intensity_matrix

header, rows, columns, max_intensity, matrix = my_readimage('/home/lucasismael/PDI/images/testeM.pgm')
#rows = 64
#columns = 64

total_pixels = rows*columns
y = np.arange(0,256,1,int)
#y = np.arange(0,8,1,int)
r = np.zeros(int(max_intensity)+1, int)
#r = np.array([790,1023,850,656,329,245,122,81])

for k in range(len(r)):
    r[k] = np.count_nonzero(matrix == k)
    
#histograma não equalizado
#plt.bar(y,r)
#plt.show()

r_prob = r/total_pixels
cdf = np.cumsum(r_prob)
eq_out = np.arange(0,256,1,int)
#eq_out = np.arange(0,8,1,int)
for l in range(len(eq_out)):
    eq_out[l] = np.ceil(int(max_intensity)*cdf[l])
    #eq_out[l] = np.ceil(7*cdf[l])
    
#histograma equalizado
#plt.figure()    
#plt.bar(y,eq_out)
#plt.show()
               
        


    


