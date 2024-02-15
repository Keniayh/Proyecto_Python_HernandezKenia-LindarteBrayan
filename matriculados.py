import json

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
        matri = {}
        
    campAprobados = []
    count = 0
    # Iterar sobre las listas de campers
    for campersLista in data:
        # Iterar sobre las campers en la lista actual
        for entry in campersLista.get('campers', []):
            if entry.get("Estado") == "aprobado":
                # Agregar al camper aprobado a la lista y contar hasta 33
                count += 1
                campAprobados.append(entry)
                if count >= 33:
                    break
        if count >= 33:
            break
    
    # Agregar el nombre del entrenador y el valor del atributo "Area_Entrenamiento"
    nombre_entrenador = "Jolver"  # Nombre del entrenador
    area_entrenamiento = "area de entrenamiento"  # Área de entrenamiento del entrenador

    # Crear el diccionario final
    matriculas = {
        "trainer": {
            "Nombre": nombre_entrenador,
            "Area_Entrenamiento": area_entrenamiento,
            "estudiantes": {}
        }
    }

    # Agregar los campers aprobados por orden a estudiantes
    for i, camper in enumerate(campAprobados, start=1):
        matriculas["trainer"]["estudiantes"][f'camper_{i}'] = camper

    # Actualizar matriculados.json sin modificar campers.json
    with open('matriculados.json', 'w') as archivo:
        json.dump(matriculas, archivo, indent=2)


