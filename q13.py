##
## Imprima por cada fila, la columna 1 y la suma de los valores
## de la columna 5
##
## E,22
## A,14
## B,14
## ....
## C,8
## E,11
## E,16
##
data_lab_06=open('data2.csv', 'r').readlines()
data_lab_06 = [z.replace('\n', '') for z in data_lab_06]
data_lab_06 = [z.split(',') for z in data_lab_06]
# procesar cada una  de las filas
for fila in data_lab_06:
    columna_0 = fila[0]
    columna_4 = fila[4].split(';')
    suma = 0
    for elemento in columna_4:
        suma += int(elemento.split(':')[1])
    print(columna_0 +','+str(suma))   
