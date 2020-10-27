# -*- coding: utf-8 -*-
# DISCIPLINA - PROCESSAMENTO DIGITAL DE IMAGENS
# SEMESTRE - 2020.1
# ALUNO - LUCAS ISMAEL CAMPOS MEDEIROS
import subprocess, os
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
    intensity_matrix = np.zeros((rows, columns), float)

    for i in range(rows):
        for j in range(columns):
            intensity_matrix[i][j] = int(aux_matrix[i][j])
    return read_header, rows, columns, max_intensity, intensity_matrix


def my_writeimage(*args):
    print('Saving new file: \n')
    file_name = input('Output filename:')+'.pgm'
    with open('/home/lucasismael/PDI_2020/images/'+file_name, 'w') as saida:
        saida.write(str(header))
        saida.write(str(columns) + ' ' + str(rows) + '\n')
        saida.write(str(max_intensity))
        np.savetxt(saida, new_matrix, delimiter=' ', newline='\n', header='', footer='', comments='# ', fmt='%i')
        
def my_histogramequalization(*args):
    intensity_quantity = int(max_intensity)+1
    total_pixels = rows*columns
    r = np.zeros(intensity_quantity, int) #Initializing intensity vector
    for k in range(len(r)):
        r[k] = np.count_nonzero(matrix == k)
    r_prob = r/total_pixels
    cdf = np.cumsum(r_prob)
    eq_map = np.arange(0,intensity_quantity,1,int)
    for l in range(intensity_quantity):
        eq_map[l] = np.ceil(int(max_intensity)*cdf[l])
    new_matrix = np.array(matrix)
    for iz in range(intensity_quantity):
        new_matrix = np.where(matrix != iz, new_matrix, eq_map[iz])
    r_eq = np.zeros(intensity_quantity, int) #Initializing intensity vector
    for h in range(len(r_eq)):
        r_eq[h] = np.count_nonzero(new_matrix == h)
    y = np.arange(0,intensity_quantity,1,int)
    plt.bar(y,r)
    plt.title('Original Histogram')
    plt.figure()    
    plt.bar(y,r_eq)
    plt.title('Equalized Histogram')
    plt.show()
    return new_matrix

def my_negativeimage(*args):
    intensity_quantity = int(max_intensity)+1
    total_pixels = rows*columns
    new_matrix = np.array(matrix)
    eq_map = np.arange(0,intensity_quantity,1,int)
    for l in range(intensity_quantity):
        eq_map[l] = np.ceil(int(max_intensity)-l)
        new_matrix = np.where(matrix != l, new_matrix, eq_map[l])
    #for iz in range(intensity_quantity):
    #    new_matrix = np.where(matrix != iz, new_matrix, eq_map[iz])
    return new_matrix

def my_logfilter(*args):
    new_matrix = np.array(matrix, dtype = np.uint8)
    eq_map = np.arange(0,256,1,float)
    c = int(input('C constant value: '))
    for l in range(256):
        eq_map[l] = c * (np.log10(l + 1))
        new_matrix = np.where(matrix != l, new_matrix, eq_map[l])        
    return new_matrix
    
def my_gammafilter(*args):
    new_matrix = np.array(matrix, dtype = np.uint8)
    eq_map = np.arange(0,256,1,float)
    c = float(input('C constant value: '))
    gamma = float(input('Gamma constant value: '))
    for l in range(256):
        eq_map[l] = c * (np.power(l, gamma))
        new_matrix = np.where(matrix != l, new_matrix, eq_map[l])        
    return new_matrix
    
        

print('Select an image: \n')
header, rows, columns, max_intensity, matrix = my_readimage('/home/lucasismael/PDI_2020/images/'+input('Selected input(.pgm):')+'.pgm')
#new_matrix = my_histogramequalization(header, rows, columns, max_intensity, matrix)
#new_matrix = my_negativeimage(header, rows, columns, max_intensity, matrix)
#new_matrix = my_logfilter(header, rows, columns, max_intensity, matrix)
new_matrix = my_gammafilter(header, rows, columns, max_intensity, matrix)
my_writeimage()


