import json

def add_notas():
    # Cargar el diccionario existente de campers
    try:
        with open('campers.json', 'r') as archivo:
            data_existing = json.load(archivo)
    except FileNotFoundError:
        data_existing = []
    try:
        # Cargar los datos existentes de notas.json
        with open('notas.json', 'r') as archivo:
            notas_data = json.load(archivo)
    except FileNotFoundError:
        notas_data = []
    
    # Solicitar el ID del estudiante
    id_estudiante = int(input('Ingrese el ID del estudiante: '))
    
    # Buscar el estudiante por su ID y agregar las notas teórica y práctica
    for entry in notas_data[0].get('prueba_campers_inicial', []):
        if entry["id"] == id_estudiante:
            # Solicitar la primera nota teórica al usuario
            entry["nota_teorica"] = int(input(f'Ingrese nota teórica para el estudiante {id_estudiante}: '))
            # Solicitar la segunda nota práctica al usuario
            entry["nota_practica"] = int(input(f'Ingrese nota práctica para el estudiante {id_estudiante}: '))
            # Calcular y mostrar el promedio después de que se ingresen ambas notas
            promedio = (entry["nota_teorica"] + entry["nota_practica"]) / 2
            print(f'El promedio es: {promedio}')
            # Agregar el promedio como un nuevo campo en el diccionario
            entry["promedio"] = promedio

          # Buscar el estudiante por su ID y cambiar estado 
            for camper_list in data_existing:
                for camper in camper_list.get('campers', []):
                    if camper["id"] == id_estudiante:
                        if promedio >= 60:
                            camper["Estado"] = "aprobado"
                            break  # Terminar el bucle una vez que se haya encontrado y actualizado el estado
                
            break
    # Escribir los datos actualizados en campers.json
    with open('campers.json', 'w') as archivo:
        json.dump(data_existing, archivo)
    
    # Escribir los datos actualizados en notas.json
    with open('notas.json', 'w') as archivo:
        json.dump(notas_data, archivo)

# Ejemplo de uso
add_notas()

