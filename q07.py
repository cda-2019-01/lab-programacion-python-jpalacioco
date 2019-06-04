##
## Genere una lista de tuplas, donde cada tupla contiene en la primera 
## posicion, el valor de la segunda columna; la segunda parte de la 
## tupla es una lista con las letras de la primera columna que aparecen
## asociadas a dicho valor de la segunda columna. Esto es:
##
##    ('0', ['C'])
##    ('1', ['E', 'B', 'D', 'A', 'A', 'E'])
##    ('2', ['A', 'E', 'D'])
##    ('3', ['A', 'B', 'D', 'E', 'E'])
##    ('4', ['E', 'B'])
##    ('5', ['B', 'C', 'D', 'D', 'E', 'E', 'E'])
##    ('6', ['C', 'E', 'A', 'B'])
##    ('7', ['A', 'C', 'E', 'D'])
##    ('8', ['E', 'E', 'A', 'B'])
##    ('9', ['A', 'B', 'E', 'C'])
##
##
## import csv
data_lab_07=open('data2.csv', 'r').readlines()
data_lab_07 = [z.replace('\n', '') for z in data_lab_07]
data_lab_07 = [z.split(',') for z in data_lab_07]
#extrae columnas 0 y 1
columna_0 = [z[0] for z in data_lab_07[0:]]
columna_1 = [z[1] for z in data_lab_07[1:]]
numeros = []
for numero in columna_1:
    if numero not in numeros:
        numeros.append(numero)
numeros.sort()
#recorre los 2 vectores probando la condición
#print(range(len(numeros)))
respuesta = []
for VA in numeros:
    letra_filtrada = [columna[0] for columna in data_lab_07 if columna[1] == VA]
    respuesta.append((VA, letra_filtrada))
print(respuesta)