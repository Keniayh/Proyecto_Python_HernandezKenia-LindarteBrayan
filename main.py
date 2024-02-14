import os
import json
from pprint import pprint
import campers as moca
import modulo as mod
import fuctionMenu as lejo
import notas as nt

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
            x = True
            while x == True:
                lejo.letrerito()
                print("Has ingresado a la sección de Trainers.")
                print("¿Qué deseas hacer?")
                print("1. Crear nuevo Trainer \t2. Asignar horario \t3.Ver Trainers \n4. Volver al menú anterior")
                optionTr = input("Digite el número según la opción a la deseas ingresar: ")
                if optionTr == '1':
                    mod.add_trainers()
                elif optionTr == '2':
                    print("")
                elif optionTr == '3':
                    print("")
                elif optionTr == '4':
                    x = False
    elif optionsAC == '2':
        while True:
            lejo.letrerito()
            print("Has ingresado a la sección de Campers")
            print("¿Qué deseas hacer?")
            print("1. Incripciones \t2. Matriculas \n3. Editar información \t4.Notas \n5. Volver al menú anterior \t6. Salir ")
            optionsA = input("Digite el número según la opción a la que deseas ingresar: ")
            limpiarPantalla()
            if optionsA == '1':
                print("Favor ingresar datos del estudiante: ")
                moca.add_campers()
            elif optionsA == '2':
                print("aun no")
            elif  optionsA == '3':
                print("")
            elif optionsA == '4':
                nt.add_notas()
            elif optionsA == '5':
                break
            else:
                if optionsA == '6':
                    fin = False
    elif optionsAC == '3':

        print("Has ingresado a la sección de Rutas de entrenamiento")
        print("¿Qué deseas hacer?")
        print("1. Motrar Rutas \t 2. Crear rutas de entrenamiento")
        optionR = input("Digite el número según la opción a la que deseas ingresar: ")
        if optionR == '1':
            mod.viewR()
        elif optionR == '2':
            print("Has ingresado a la sección de crear rutas.")
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
