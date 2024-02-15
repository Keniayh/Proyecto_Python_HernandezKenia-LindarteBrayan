import json
from pprint import pprint

def check_fields_complete(camper):
    required_fields = ['Nombres', 'Apellidos', 'Dirección', 'Acudiente', 'Contacto', 'Riesgo']
    for field in required_fields:
        if not camper.get(field):
            return False
    return True

#CRUD RUTAS

def newRuta():
    try:
        with open ('rutasEntreno.json', 'r') as archivo:
            rutas = json.load(archivo)
    except FileNotFoundError:
        rutas = []
    a = int(input("Ingrese el número  de rutas que desea crear: "))
    
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
    nombre = input('Nombres: ')
    grupo_por_defecto = nombre[0].upper() + "1"  # Tomar la inicial y añadir "1"
    new_trainer = {
        "Nombres": nombre,
        "Apellidos": input('Apellidos: '),
        "id": int(input('Identificación: ')),
        "Contacto": int(input("Número de telefono: ")),
        "Horario": {
            "Grupo": grupo_por_defecto,
            "Area_Entrenamiento": input("Area de entrenamiento: "),
            "Time": input("Ingrese la hora de inicio (HH:MM) - hora final (HH:MM): ") 
        },
    }
    
    # Agregar al nuevo trainer a la lista existente
    data_existing.append(new_trainer)
    
    # Escribir los datos en el archivo JSON
    with open('trainers.json', 'w') as archivo:
        json.dump(data_existing, archivo)
#VISUALIZAR A LOS TRAINERS 

def viewTr():
    try:
        with open('trainers.json', 'r') as archivo:
            data = json.load(archivo)
        for item  in data:
            trainers = item.get('trainers', [])
            for trainer in trainers:
                print(f"ID: {trainer.get('id', 'No disponible')}")
                print(f"Nombres: {trainer.get('Nombres', 'No disponible')}")
                print(f"Apellidos: {trainer.get('Apellidos', 'No disponible')}")
                print("-" * 30)
    except FileNotFoundError:
        print("El archivo 'trainers.json' no existe")
       
    
#PASAR LOS APROBADOS DEL JSON DE CAMPER AL JSON DE MATRICULADOS

def matriculas():
    try:
        with open('campers.json', 'r') as archivo:
            data = json.load(archivo)
    except FileNotFoundError:
        data = []
    try:
        with open('matriculados.json', 'r') as archivo:
            matri = json.load(archivo)
    except FileNotFoundError:
        matri = {}
        
    campAprobados = []
    #iterar sobre las listas de campers
    for campersLista in data:
        #iterar sobre las campers en la lista actual
        for entry in campersLista.get('campers',[{"Estado": "No especificado"}]):
            if entry["Estado"] == "aprobado":
                if entry.get("Estado") == "aprobado":
                    #agrega al camper aprobado a la lista
                    campersLista.append(entry)
    
    #agrega campers aprobados a matriculados.json
    for i, camper in enumerate(campersLista, star = 1):
        matri[f'camper_{i}'] = camper
    #filtra campers no approvados y acualiza campers.json
    for campersLista in data:
        campersLista['campers'] = [entry for entry in campersLista['campers']if entry not in campAprobados]
        
    with open('campers.json', 'w') as archivo:
        json.dump(data, archivo, indent = 2)
    
    with open('campers.json', 'w') as archivo:
        json.dump(matri, archivo, indent = 2)  
        
matriculas()
#VER LOS CAMPRS MATRICULADOS, POR ENDE APROBADOS 
def viewMa():
    try:
        with open('matriculados.json','r') as archivo:
            matriculados =json.load(archivo)
        #accede a la info de camper matriculado
        for key, camper in matriculados.items():
            print(f"Camper ID: {key}")
            for field, value in camper.items():
                print(f" {field}: {value}")
            print("\n" + "-"*30)
    except FileNotFoundError:
        print("El archivo 'matriculados.json' está vacio")

#def viewM():
    
#   with open('matriculados.json', 'r') as archivo:
#       matriculadosA = json.load(archivo)
        
#    pprint(matriculadosA)

