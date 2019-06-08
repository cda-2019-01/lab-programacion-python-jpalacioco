##
## Imprima por cada fila, la columna 1 y la suma de los valores
## de la columna 5
##
## E,22
## A,14
## B,14
## ....
## C,8
## E,11
## E,16
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
# procesar cada una  de las filas
for fila in data_lab_03:
    columna_0 = fila[0]
    columna_4 = fila[4].split(';')
    suma = 0
    for elemento in columna_4:
        suma += int(elemento.split(':')[1])
    print(columna_0 +','+str(suma))