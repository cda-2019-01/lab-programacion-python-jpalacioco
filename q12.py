##
## Imprima la suma de la columna 2 por cada letra 
## de la columna 4, ordnados alfabeticamente.
##
## a,114
## b,40
## c,91
## d,65
## e,79
## f,110
## g,35
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
#data_lab_03
columna_3 =[col[3] for col in data_lab_03[0:]]
columna_3 = [col.split(';') for col in columna_3]
claves = []
for fila in columna_3:
    for elemento in fila:
        if elemento not in claves:
            claves.append(elemento)
claves.sort()
#print(claves)
for clave in claves:
    suma = 0
    for fila in data_lab_03:
        col_3 = fila[3].split(';')
        if clave in col_3:
            suma += int(fila[1])
    print(clave+','+str(suma))