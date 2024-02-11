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
        print("1. Trainers \t2. Campers \t3. Rutas de entrenamiento  \t4. Reportes \t 5. Volver al menú principal")
        optionsAC = input(int(("Ingresa el número según el área a la cual deseas ingresar: ")))
        if optionsAC == "1":
            print("Has ingresado a la sección de Trainers.")
            print("¿Qué deseas hacer?")
            print("1. Crear nuevo Trainer \t2. Asignar horario \t3.Ver Trainers \t4.Regresar al inicio")
        elif optionsAC == "2":
            print("Has ingresado a la sección de Campers")
            print("¿Qué deseas hacer?")
            print("1. Matriculas \t2. Editar información \t3.Notas \t ")
        elif optionsAC == "3":
            print("Has ingresado a la sección de Rutas de entrenamiento")
            print("¿Qué deseas hacer?")
            print("1. Visualizar las Rutas \t 2. Crear nuevas rutas de entrenamiento")            
    elif rta == 2:
        print("-------------------------")
        print("-      ROL TRAINER      -")
        print("-------------------------")
        print("")
        print("¿Qué deseas hacer?")
        print("1. Horario \t2. Volver al inicio")
        optionsT = input(int("Ingresa el número según el área a la cual deseas ingresar: "))
        if optionsT == "1":
            print("Has ingresado a la sección de Horarios")
            print("Completa la siguiente información para saber tu hoario de trabajo")
            limpiarPantalla()
            print("Ingresa tus datos:")
            trainerN = input("Ingresa tu/s nombre/s: ")
            trainerA = input("Ingresa tu/s apellido/s: ")
    else:
        if rta == "3":
            fin = False
