import json

def add_campers():
    # Cargar el diccionario existente
    try:
        with open('campers.json', 'r') as archivo:
            data_existing = json.load(archivo)
    except FileNotFoundError:
        data_existing = []
    
    # Solicitar datos del nuevo estudiante
    new_camper = {
        "id": int(input('Identificación: ')),
        "Nombres": input('Nombres: '),
        "Apellidos": input('Apellidos: '),
        "Dirección": input('Dirección: '),
        "Acudiente": input('Acudiente: '),
        "Contacto": {
            "Celular": int(input('Celular: ')),
            "Fijo": int(input('Fijo: '))
        },
        "Estado": input('Estado: '),
        "Riesgo": input('Riesgo: ')
    }
    
   # Agregar el nuevo estudiante a la lista existente
    data_existing.append(new_camper)
    
    # Escribir los datos en el archivo JSON
    with open('campers.json', 'w') as archivo:
        json.dump(data_existing, archivo)


def newRuta():
    try:
        with open ('rutasEntreno.json', 'r') as archivo:
            rutas = json.load(archivo)
    except FileNotFoundError:
        rutas = []
   
    new_Ruta = {
        "nombre ruta": input("Nombre ruta: ")
    }
    

    rutas.append(new_Ruta)
    with open ('rutasEntreno.json', 'w') as archivo:
        json.dump(rutas, archivo, indent = 4)
        
newRuta()