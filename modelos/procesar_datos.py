import csv

file_path = 'datos/validacionZonal20230821.csv'

def read_csv(file_path):
    data = []
    with open(file_path, 'r', newline='', encoding='utf-8') as csv_file:
        csv_reader = csv.reader(csv_file)
        header = next(csv_reader)  # Leer la primera fila como encabezado
        for row in csv_reader:
            data.append(row)
    return header, data