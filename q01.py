##
## Imprima la suma de la segunda columna.
##
import csv
columna_2=0
data_lab_03=open('data.csv')
separador = "\t"
for fila in data_lab_03:
    columna_2 = int(fila.split(separador)[1].strip())+int(columna_2)
print(columna_2)
data_lab_03.close()
