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
    intensity_matrix = np.zeros((rows, columns), int)

    for i in range(rows):
        for j in range(columns):
            intensity_matrix[i][j] = int(aux_matrix[i][j])
    return read_header, rows, columns, max_intensity, intensity_matrix

def my_writeimage():
    print('SALVANDO NOVO ARQUIVO')
    file_name = input('Nome do arquivo de saída:')+'.pgm'
    with open(file_name, 'w') as saida:
        saida.write(str(header))
        saida.write(str(columns) + ' ' + str(rows) + '\n')
        saida.write(str(max_intensity))
        np.savetxt(saida, new_matrix, delimiter=' ', newline='\n', header='', footer='', comments='# ', fmt='%i')
        
    
## INÍCIO DO SCRIPT ## 
# LENDO ARQUIVO
print('LEITURA DA IMAGEM')        
header, rows, columns, max_intensity, matrix = my_readimage('/home/lucasismael/PDI_2020/images/'+input('Nome do arquivo de entrada(.pgm):')+'.pgm')
print('--------------------------------------')
# QUANTIDADE DE NÍVEIS DE INTENSIDADE
intensity_quantity = int(max_intensity)+1
#print('QUANTIDADE DE INTENSIDADES: ' + str(intensity_quantity))
# QUANTIDADE DE PIXELS NA IMAGEM
total_pixels = rows*columns
#print('QUANTIDADE DE PIXELS: ' + str(total_pixels))
# CONTANDO A INTENSIDADE DE CADA NÍVEL
#print('CONTAGEM DAS INTENSIDADES')
r = np.zeros(intensity_quantity, int)
for k in range(len(r)):
    r[k] = np.count_nonzero(matrix == k)
# CALCULANDO A PROBABILIDADE DE CADA NÍVEL 
#print('CALCULANDO AS PROBABILIDADES')    
r_prob = r/total_pixels
# CALCULANDO A CDF
#print('CALCULANDO A CDF') 
cdf = np.cumsum(r_prob)
# CONSTRUÍNDO O MAPEAMENTO 
#print('CONSTRUÍNDO O MAPEAMENTO')
eq_map = np.arange(0,intensity_quantity,1,int)
for l in range(len(eq_map)):
    eq_map[l] = np.ceil(int(max_intensity)*cdf[l])
# MAPEANDO OS NOVOS VALORES 
#print('MAPEANDO OS NOVOS VALORES')
new_matrix = np.array(matrix)
for iz in range(len(eq_map)):    
    new_matrix = np.where(matrix != iz, new_matrix, eq_map[iz])

# ESCREVENDO AS INFORMAÇÕES EM UM NOVO ARQUIVO
#print('CONSTRUÍNDO ARQUIVO DE SAÍDA')
my_writeimage()

print('--------------------------------------')
print('PLOTANDO HISTOGRAMAS')
#PLOTANDO HISTOGRAMAS
#histograma não equalizado
y = np.arange(0,intensity_quantity,1,int)
plt.bar(y,r)
plt.title('Histograma Original')
#plt.show()
#histograma equalizado
plt.figure()    
plt.bar(y,eq_map)
plt.title('Histograma Equalizado')
plt.show()



               
        


    


