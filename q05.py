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
data_lab_05=open('data2.csv', 'r').readlines()
data_lab_05 = [z.replace('\n', '') for z in data_lab_05]
data_lab_05 = [z.split(',') for z in data_lab_05]
columna_0 =[z[0] for z in data_lab_05[0:]]
columna_0
letras = []
for letra in columna_0:
    if letra not in letras:
        letras.append(letra)
letras.sort()
letras
## se quiere seleccionar las filas donde letras cumpla la condicion
for VA in letras:
    letra_filtrada = [columna[1] for columna in data_lab_05 if columna[0] == VA]
    minimo = min(letra_filtrada)
    maximo = max(letra_filtrada)
    print(VA+',',maximo+',',minimo)