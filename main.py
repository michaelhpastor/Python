import sys

from modelos.procesar_datos import read_csv
from datetime import datetime


def converHora(hora):
    hora = datetime.strptime(hora, "%H:%M:%S").time()
    return hora


hora_min = "00:00:00"
hora_max = "00:00:00"
prueba = "3:08:42"
prueba = converHora(prueba)
hora_min = converHora(hora_min)
hora_max = converHora(hora_max)
co = 1
file_path = "datos/validacionZonal20230821.csv"
header, data = read_csv(file_path)

print("Encabezado:", header)
print("primera fila",data[690655][5])

for x in data:
    temp = x[5][8:10]
    horTemp = str(x[5][11:])
    horTemp = converHora(horTemp)
    if(horTemp == prueba):
        print(horTemp)
    if temp == "21":
        if co == 1:
            hora_max = horTemp
            hora_min = horTemp
            co = co - 1
        else:
            if hora_min > horTemp:
                hora_min = horTemp
            if hora_max < horTemp:
                hora_max = horTemp

print("max: ", hora_max)
print("min: ", hora_min)

