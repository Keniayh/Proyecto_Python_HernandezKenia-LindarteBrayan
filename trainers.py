import json

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
    
    
# Ejemplo de uso
add_trainers()
