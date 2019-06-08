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
#extrae columnas 0 y 1
columna_0 = [z[0] for z in data_lab_03[0:]]
columna_1 = [z[1] for z in data_lab_03[1:]]
numeros = []
for numero in columna_1:
    if numero not in numeros:
        numeros.append(numero)
numeros.sort()
numeros
#recorre los 2 vectores probando la condición
#print(range(len(numeros)))
respuesta = []
for VA in numeros:
    #print(VA)
    letra_filtrada = [columna[0] for columna in data_lab_03 if columna[1] == VA]
    #print(letra_filtrada)
    respuesta.append(VA+','+str(letra_filtrada))
    print((VA,letra_filtrada))