##
## Imprima una tabla en formato CSV que contenga por registro,
## la cantidad de elementos de las columnas 4 y 5
## (filas en el archivo)
##
## E,3,5
## A,3,4
## B,4,4
## ...
## C,4,3
## E,2,3
## E,3,3
##
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
respuesta_csv =[]
for fila in data_lab_03:
    columna_0 = fila[0]
    columna_3 = len(fila[3].split(';'))
    columna_4 = len(fila[4].split(';'))
    respuesta_csv.append([columna_0, columna_3, columna_4])
    print(columna_0+','+str(columna_3)+','+str(columna_4))
with open('q11.csv', 'w') as f:
    x = csv.writer(f,
                   delimiter = ',',
                   quoting=csv.QUOTE_NONNUMERIC)
    for r in respuesta_csv:
        x.writerow(r)
f.close()