import os
import json
import campers as moca
import modulo as mod
import fuctionMenu as lejo
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
   
    rta = input("Ingresa el número según el rol: ")
    limpiarPantalla()

    if rta == '1':
        nameModCA = input("Ingresa tu nombre: ")

        limpiarPantalla()
        lejo.letrerito()

        print("")
        print(" Bienvenido ", nameModCA)
        print("¿A qué área deseas ingresar: ")
        print("1. Trainers \t2. Campers \n3. Rutas de entrenamiento  \t4. Reportes \t 5. Volver al menú principal")
        optionsAC = input("Ingresa el número según el área a la cual deseas ingresar: ")
        limpiarPantalla()
        if optionsAC == '1':
            lejo.letrerito()
            print("Has ingresado a la sección de Trainers.")
            print("¿Qué deseas hacer?")
            print("1. Crear nuevo Trainer \t2. Asignar horario \t3.Ver Trainers \t4.Regresar al inicio")
        elif optionsAC == '2':
            lejo.letrerito()
            print("Has ingresado a la sección de Campers")
            print("¿Qué deseas hacer?")
            print("1. Incripciones \t2. Matriculas \n3. Editar información \t4.Notas \t ")
            optionsA = input("Digite el número según la opción a la que deseas ingresar: ")
            limpiarPantalla()
            if optionsA == '1':
                print("Favor ingresar datos del estudiante: ")
                moca.add_campers()
        elif optionsAC == '3':
            print("Has ingresado a la sección de Rutas de entrenamiento")
            print("¿Qué deseas hacer?")
            print("1. Visualizar las Rutas \t 2. Crear nuevas rutas de entrenamiento")
            optionR = input("Digite el número según la opción a la que deseas ingresar: ")
            if optionR == '1':
                print(" aun no")
            elif optionR == '2':
                print("Ingresa el nombre de la  nueva ruta que deseas crear")
                mod.newRuta()
    elif rta == '2':
        lejo.letrero()
        print("")
        print("¿Qué deseas hacer?")
        print("1. Horario \t2. Volver al inicio")
        optionsT = input("Ingresa el número según el área a la cual deseas ingresar: ")

        limpiarPantalla()
        if optionsT == '1':
            lejo.letrero()
            print("Has ingresado a la sección de Horarios")
            print("Completa la siguiente información para saber tu horario de trabajo")
            limpiarPantalla()
            print("Ingresa tu número de identificación.")
            trainerN = input("Número de identificación: ")
    else:       
        if rta == '3':
            fin = False
