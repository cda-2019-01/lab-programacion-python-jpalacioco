##
## Imprima una tabla en formato CSV que contenga por cada clave 
## de la columna 5, la correspondiente cantidad de registros 
## asociados (filas en el archivo)
##
## aaa,13
## bbb,16
## ccc,23
## ddd,23
## eee,15
## fff,20
## ggg,13
## hhh,16
## iii,18
## jjj,18
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
#data_lab_03
columna_4 =[z[4] for z in data_lab_03[0:]]
columna_4
#Split
claves = []
columna_4 = [z.split(';') for z in columna_4]
# encontrar las claves unicas
for fila in columna_4:
    for elemento in fila:
        lista_elemento = elemento.split(':')[0]
        #print(lista_elemento)
        if lista_elemento not in claves:
            claves.append(lista_elemento)
claves.sort()
            #print(claves)
#
respuesta_csv = []
for clave in claves:
    contador_numeros = 0
    for fila in columna_4:
        for elemento in fila:
            clave_aux = elemento.split(':')[0]
            numero_aux = elemento.split(':')[1]
            if clave == clave_aux:
                contador_numeros +=1 # equivale a realizar la operación matemática
    print(clave+','+str(contador_numeros))
    respuesta_csv.append([clave, contador_numeros])
import csv
with open('q10.csv', 'w') as f:
    x = csv.writer(f,
                   delimiter = ',',
                   quoting=csv.QUOTE_NONNUMERIC)
    for r in respuesta_csv:
        x.writerow(r)