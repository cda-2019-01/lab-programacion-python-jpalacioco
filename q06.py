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
#data_lab_06
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
for clave in claves:
    lista_numeros = []
    for fila in columna_4:
        for elemento in fila:
            clave_aux = elemento.split(':')[0]
            numero_aux = elemento.split(':')[1]
            if clave == clave_aux:
                lista_numeros.append(int(numero_aux))
    #print(lista_numeros)
    minimo = min(lista_numeros)
    maximo = max(lista_numeros)
    
    print(clave+','+str(minimo)+','+str(maximo))