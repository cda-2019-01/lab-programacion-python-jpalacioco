##
## Por cada clave de la columna 5 (cadena de tres letras), obtenga
## el valor mas pequeño y el valor mas grande asociado a esa clave.
##
## aaa,0,6
## bbb,4,7
## ccc,0,1
## ddd,5,5
## eee,0,0
## fff,4,9
## ggg,3,3
## hhh,6,8
## iii,2,7
## jjj,2,5
##
## import csv
data_lab_06=open('data2.csv', 'r').readlines()
data_lab_06 = [z.replace('\n', '') for z in data_lab_06]
data_lab_06 = [z.split(',') for z in data_lab_06]
#data_lab_06
columna_4 =[z[4] for z in data_lab_06[0:]]
#Split
claves = []
columna_4 = [z.split(';') for z in columna_4]
# encontrar las claves unicas
for fila in columna_4:
    for elemento in fila:
        lista_elemento = elemento.split(':')[0]
        if lista_elemento not in claves:
            claves.append(lista_elemento)
claves.sort()
#print(claves)
#
for clave in claves:
    lista_numeros = []
    for fila in columna_4:
        for elemento in fila:
            clave_aux = elemento.split(':')[0]
            numero_aux = elemento.split(':')[1]
            if clave == clave_aux:
                lista_numeros.append(int(numero_aux))
    minimo = min(lista_numeros)
    maximo = max(lista_numeros)
    
    print(clave+',',str(minimo)+',',str(maximo))