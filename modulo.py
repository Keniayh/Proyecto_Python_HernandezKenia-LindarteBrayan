import json
from pprint import pprint
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
#CRUD RUTAS

def newRuta():
    try:
        with open ('rutasEntreno.json', 'r') as archivo:
            rutas = json.load(archivo)
    except FileNotFoundError:
        rutas = []
    a = int(input("Ingrese el número ed notas que desea crear: "))
    
    for i in range (a):
        new_Ruta = {
            "nombre ruta": input(f"Nombre ruta {i+1} :")
        }
        rutas.append(new_Ruta)
        
    with open ('rutasEntreno.json', 'w') as archivo:
        json.dump(rutas, archivo, indent = 4)
#VISUALIZAR RUTAS


def viewR():
    with open("rutasEntreno.json", 'r') as archivo:
        rutas = json.load(archivo)
    #print(json.dumps(rutas, indent = 4))
    #imprime el contenido del json como una lista en el terminal
    pprint(rutas)

   
#CRUD TRAINERS

def add_trainers():
    # Cargar el diccionario existente
    try:
        with open('trainers.json', 'r') as archivo:
            data_existing = json.load(archivo)
    except FileNotFoundError:
        data_existing = []
    
    # Solicitar datos del nuevo trainer
    new_trainer = {
        "id": int(input('Identificación: ')),
        "Nombres": input('Nombres: '),
        "Apellidos": input('Apellidos: '),
        "Contacto": int(input("Número de telefono: ")),
        "Horario": {
            "Grupo": input("Grupo: "),
            "Area_Entrenamiento": input("Area de entrenamiento: "),
            "Time": input("Ingrese la hora de inicio (HH:MM) - hora final (HH:MM): ") 
        },
    }
    
    # Agregar el nuevo estudiante a la lista existente
    data_existing.append(new_trainer)
    
    # Escribir los datos en el archivo JSON
    with open('trainers.json', 'w') as archivo:
        json.dump(data_existing, archivo)

def matriculados():
    try:
        with open('campers.json', 'r') as archivo:
            data = json.load(archivo)
    except FileNotFoundError:
        data = []
    try:
        with open('matriculados.json', 'r') as archivo:
            matri = json.load(archivo)
    except FileNotFoundError:
        matri = []
    
    for entry in data[7].get('campers',["Estado"]):
        if entry["Estado"] == "aprobado":
            

#def horarioTrainers():