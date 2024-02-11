import os

def limpiarPantalla():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

fin = True
while fin == True:

    print("-----------------------------")
    print("-       BIENVENIDO A        -")
    print("-        CAMPUSLANDS        -")
    print("-----------------------------")
    print("")
    print("Seleciona el cargo al que perteneces:")
    print("1. Coordinador \t2. Trainer \t3.Salir")
   
    rta = input(int("Ingresa el número según el rol: "))
    limpiarPantalla()

    if rta == "1":
        nameModCA = input("Ingresa tu nombre: ")
        
        print("-------------------------")
        print("-    ROL COORDINACIÓN   -")
        print("-       ACADÉMICA       -")
        print("-------------------------")
        print("")
        print(" Bienvenido ", nameModCA)
        print("¿A qué área deseas ingresar: ")
        print("1. Trainers \t2. Campers \tVolver al inicio")
        opcionesCA = input(int(("Ingresa el número según el área a la cual deseas ingresar: ")))
        
    elif rta == 2:
        print("-------------------------")
        print("-    ROL  ")
        
