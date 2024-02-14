import json

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
    
def horario_trainers():
    #Cargar diccionario 
    with open('trainers.json', 'r') as archivo:
        data_existing = json.load(archivo)
    #Solicitar el Id del docente
    id_trainer = int(input('Ingrese el ID del docente: '))
    
    #Buscar al trainer por su ID y modificar su horario
    for trainer in data_existing:
        if trainer.get("id") == id_trainer:
            horario = trainer.get("Horario", {})
            print("Horario:")
            for key, value in horario.items():
                print(f" {key}: {value}")
            #Solicitar nueva informacion 
            new_grupo = input('Nuevo grupo: ')
            new_area_entrenamiento = input('Nueva area de entrenamiento: ')
            #Modificar el valor que ya esta guardado
            trainer["Horario"]["Grupo"] = new_grupo
            trainer["Horario"]["Area_Entrenamiento"] = new_area_entrenamiento
            print("Se modifico con existo")
            break
        
    else: 
        print("Trainer no encontrado")
    #Reescribir los datos actualizados
    with open('trainers.json', 'w')as archivo:
        json.dump(data_existing, archivo)
def see_trainer():
    #Cargar diccionario
    with open('trainers.json', 'r') as archivo:
        data_existing = json.load(archivo)
    #Mostrar los trainers 
    for idx, trainer in enumerate(data_existing):
        print(f" trainer: {idx}")
        print(json.dumps(trainer))
    
# Ejemplo de uso
horario_trainers()