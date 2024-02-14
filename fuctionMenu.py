
def letrerito():
    print("------------------------------")
    print("-       ROL COORDINACIÓN     -")
    print("-          ACADÉMICA         -")
    print("------------------------------")

def letrero():
    print("------------------------------")
    print("-         ROL TRAINERS       -")
    print("------------------------------")
import json
def mostrar_matriculados():
    try:
        # Cargar el archivo JSON
        with open('matriculados.json', 'r') as file:
            matriculados = json.load(file)

        # Acceder a la información de cada camper matriculado
        for key, camper in matriculados.items():
            print(f"Camper ID: {key}")
            for field, value in camper.items():
                print(f"  {field}: {value}")
            print("\n" + "-"*30)

    except FileNotFoundError:
        print("El archivo 'matriculados.json' no existe.")

# Llamar a la función
mostrar_matriculados()
#def horarioTrainers():



