##
## Imprima la cantidad de registros por letra para la 
## primera columna, ordenados alfabeticamente.
##
## A,8
## B,7
## C,5
## D,6
## E,14
##
import csv
lista=[]
data_lab_03=open('data.csv')
separador = "\t"
for fila in data_lab_03:
    columna_0 = fila.split(separador)[0].strip()
    lista.append(columna_0)
data_lab_03.close()
lista.sort()
conjunto1 = set(lista)
conjunto=list(conjunto1)
conjunto.sort()
matriz=[]
for i in range(len(conjunto)):
    matriz.append([])
    for j in range(2):
        matriz[i].append(None)
l=0
m=0
for k in conjunto:
    for i in lista:
        if i==k:
            l=1+l
    matriz[m][0]=k
    matriz[m][1]=l
    m=m+1
    l=0
for elemento in matriz:   
    print(elemento[0]+','+str(elemento[1]))