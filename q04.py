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
data_lab_03=open('data2.csv', 'r').readlines()
data_lab_03 = [z.replace('\n', '') for z in data_lab_03]
data_lab_03 = [z.split(',') for z in data_lab_03]
# extrae el campo Date
fecha =[z[2] for z in data_lab_03[0:]]
fecha = [VA.split('/') for VA in fecha]
mes = [VA[1] for VA in fecha]
mes_f = []
for i in mes:
    if i not in mes_f:
        mes_f.append(i)
mes_f.sort()
contador_reg = 0
registros =[]
for i in mes_f:
    contador_reg = 0
    for j in mes:   
        if i == j:
            contador_reg = contador_reg + 1
    registros.append(contador_reg)
contador_reg = 0
respuesta = []
for i in range(len(mes_f)):
    respuesta.append([mes_f[i], registros[i]])
print(respuesta)