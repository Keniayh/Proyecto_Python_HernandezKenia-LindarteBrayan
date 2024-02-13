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
add_campers()

def addRuta():
   with open ('rutasEntreno', 'r') as rutas:
       rutica = json.loand(rutas)
    
   newRuta = input("Ingrese el nombre de la nueva ruta, ('ej. Ruta x')")
    
   if newRuta in rutica[newRuta]:
        print("!Oh, lo siento, ya has creado esa Ruta¡")
   else:
       rutica["Rutas"][newRuta]
       x = input("")
       rutica["Rutas"][newRuta] = []
       with open('rutasEntreno.json', 'w') as grupsFiles:
           json.dump(rutica, grupsFiles, indent = 2)
           
       print("La Ruta ha sido creada exitosamente")
addRuta()