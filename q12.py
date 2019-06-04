##
## Imprima la suma de la columna 2 por cada letra 
## de la columna 4, ordnados alfabeticamente.
##
## a,114
## b,40
## c,91
## d,65
## e,79
## f,110
## g,35
##
data_lab_06=open('data2.csv', 'r').readlines()
data_lab_06 = [z.replace('\n', '') for z in data_lab_06]
data_lab_06 = [z.split(',') for z in data_lab_06]
#data_lab_06
columna_3 =[col[3] for col in data_lab_06[0:]]
columna_3 = [col.split(';') for col in columna_3]
claves = []
for fila in columna_3:
    for elemento in fila:
        if elemento not in claves:
            claves.append(elemento)
claves.sort()
#print(claves)
for clave in claves:
    suma = 0
    for fila in data_lab_06:
        col_3 = fila[3].split(';')
        if clave in col_3:
            suma += int(fila[1])
    print(clave+',',suma)