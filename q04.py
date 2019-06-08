##
## Imprima la cantidad de registros por cada mes.
##
## 01,3
## 02,4
## 03,2
## 04,4
## 05,3
## 06,3
## 07,5
## 08,6
## 09,3
## 10,2
## 11,2
## 12,3
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
# extrae el campo Date
fecha =[z[2] for z in data_lab_03[0:]]
fecha = [VA.split('/') for VA in fecha]
#fecha
mes = [VA[1] for VA in fecha]
#mes
mes_f = []
for i in mes:
    if i not in mes_f:
        mes_f.append(i)
mes_f.sort()
#mes_f
contador_reg = 0
registros =[]
for i in mes_f:
    contador_reg = 0
    for j in mes:   
        if i == j:
            contador_reg = contador_reg + 1
    registros.append(contador_reg)
contador_reg = 0
#registros
respuesta = []
for i in range(len(mes_f)):
    respuesta.append([mes_f[i], registros[i]])
    print(str(mes_f[i])+","+str(registros[i]))