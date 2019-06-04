##
## Genere una lista de tuplas, donde cada tupla contiene en la primera 
## posicion, el valor de la segunda columna; la segunda parte de la 
## tupla es una lista con las letras (ordenadas y sin repetir letra) 
## de la primera  columna que aparecen asociadas a dicho valor de la 
## segunda columna. Esto es:
##
## ('0', ['C'])
## ('1', ['A', 'B', 'D', 'E'])
## ('2', ['A', 'D', 'E'])
## ('3', ['A', 'B', 'D', 'E'])
## ('4', ['B', 'E'])
## ('5', ['B', 'C', 'D', 'E'])
## ('6', ['A', 'B', 'C', 'E'])
## ('7', ['A', 'C', 'D', 'E'])
## ('8', ['A', 'B', 'E'])
## ('9', ['A', 'B', 'C', 'E'])
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
    print(VA)
    letra_filtrada = [columna[0] for columna in data_lab_07 if columna[1] == VA]
    letra_filtrada.sort()
    letra_filtrada_unica =[]
    for i in letra_filtrada:
        if i not in letra_filtrada_unica:
            letra_filtrada_unica.append(i)   
    respuesta.append((VA, letra_filtrada_unica))
print(respuesta)