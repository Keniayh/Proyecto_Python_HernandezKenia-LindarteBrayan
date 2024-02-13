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
    
    
# Ejemplo de uso
add_trainers()
