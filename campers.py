import json

def check_fields_complete(camper):
    # Verificar si todos los campos obligatorios están completos
    required_fields = ['Nombres', 'Apellidos', 'Direccion', 'Acudiente', 'Contacto', 'Riesgo']
    for field in required_fields:
        if not camper.get(field):
            return False
    return True

def add_campers():
    # Cargar el diccionario existente de campers
    try:
        with open('campers.json', 'r') as archivo:
            data_existing = json.load(archivo)
    except FileNotFoundError:
        data_existing = []
    
    # Solicitar datos del nuevo estudiante
    new_camper_id = int(input('Identificación: '))
    new_camper = {
        "id": new_camper_id,
        "Nombres": input('Nombres: '),
        "Apellidos": input('Apellidos: '),
        "Direccion": input('Dirección: '),
        "Acudiente": input('Acudiente: '),
        "Contacto": {
            "Celular": int(input('Celular: ')),
            "Fijo": int(input('Fijo: '))
        },
        "Riesgo": input('Riesgo: ')
    }
    
    ## Evaluar si el camper pasa a inscrito
    if check_fields_complete(new_camper):
        new_camper["Estado"] = 'En proceso de inscripcion'
        data_existing.append({"campers": [new_camper]})
    else: 
        print("No se puede inscribir faltan datos")
    
    # Escribir los datos actualizados de campers en el archivo JSON
    with open('campers.json', 'w') as archivo:
        json.dump(data_existing, archivo)
    
    # Agregar el ID del nuevo camper a notas.json
    notas_data = []
    try:
        with open('notas.json', 'r') as archivo:
            notas_data = json.load(archivo)
    except FileNotFoundError:
        pass
    
    # Agregar el ID del nuevo camper a cada diccionario dentro de notas_data
    for dict_name, dict_info in notas_data[0].items():
        dict_info.append({"id": new_camper_id})
    
    with open('notas.json', 'w') as archivo:
        json.dump(notas_data, archivo)