##
## Imprima el valor maximo y minimo por cada letra de la columa 1.
##
## A,9,1
## B,9,1
## C,9,0
## D,7,1
## E,9,1
##
## import csv
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
columna_0
letras = []
for letra in columna_0:
    if letra not in letras:
        letras.append(letra)
letras.sort()
letras
## se quiere seleccionar las filas donde letras cumpla la condicion
for VA in letras:
    letra_filtrada = [columna[1] for columna in data_lab_03 if columna[0] == VA]
    #print(letra_filtrada)
    minimo = min(letra_filtrada)
    maximo = max(letra_filtrada)
    print(VA+','+str(maximo)+','+str(minimo))