import json

# Cargar el JSON
with open('campers.json', 'r') as archivo:
    data = json.load(archivo)

# Extraer el primer registro
primer_registro = data[0]

# Guardar solo el primer registro de vuelta en el archivo
with open('campers.json', 'w') as archivo:
    json.dump([primer_registro], archivo)
