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
lista_1=[]
data_lab_03=open('data.csv')
separador = "\t"
for fila in data_lab_03:
    columna_0 = fila.split(separador)[0].strip()
    lista.append(columna_0)
data_lab_03.close()
lista.sort()
print(lista)
conjunto1 = set(lista)
conjunto=list(conjunto1)
conjunto.sort()
print(conjunto)
print(len(lista))
matriz=[]
for i in range(len(conjunto)):
    matriz.append([])
    for j in range(2):
        matriz[i].append(None)
print(matriz[0][0])
l=0
m=0
for k in conjunto:
    for i in lista:
        print(k+'-'+i)
        if i==k:
            l=1+l
    matriz[m][0]=k
    matriz[m][1]=l
    m=m+1
    l=0
    
print(matriz)