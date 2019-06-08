##
## Imprima la suma de la columna 2 por cada letra de la 
## primera columna, ordneados alfabeticamente.
##
## A,37
## B,36
## C,27
## D,23
## E,67
##
import csv
lista=[]
data_lab_03=open('data.csv')
separador = "\t"
for fila in data_lab_03:
    fila_actual=fila.split(separador)
    fecha_actual=fila_actual[2].split('-')
    fecha_formato=[fecha_actual[2],fecha_actual[1],fecha_actual[0]]
    fila_actual[2]="/".join(fecha_formato)
    
    columna_4=fila_actual[3].split(',')
    fila_actual[3]=";".join(columna_4)
    
    columna_5=fila_actual[4].split(',')
    fila_actual[4]=";".join(columna_5)
    
    lista.append(",".join(fila_actual))
data_lab_03.close()
data_lab_03=lista
data_lab_03 = [z.replace('\n', '') for z in data_lab_03]
data_lab_03 = [z.split(',') for z in data_lab_03]
columna_0 =[z[0] for z in data_lab_03[0:]]
letras = []
for letra in columna_0:    
    if letra not in letras:
        letras.append(letra)
letras.sort()
#letras
for letra in letras:
    suma = 0
    for fila in data_lab_03:
        columna_0 = fila[0]
        columna_1 = fila[1]
        if letra == columna_0:
            suma = suma + int(columna_1)
    print(str(letra)+','+str(suma))