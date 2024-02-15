import modulo as mod
import os
def letrerito():
    print("------------------------------")
    print("-       ROL COORDINACIÓN     -")
    print("-          ACADÉMICA         -")
    print("------------------------------")

def letrero():
    print("------------------------------")
    print("-         ROL TRAINERS       -")
    print("------------------------------")

def limpiarPantalla():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')
        
def reports():
    repor = input("Digite el número según la sección a la que deseas ingresar: ")
    if repor == '1':
        print("")
        limpiarPantalla()
    elif repor == '2':
        mod.viewMa()
        limpiarPantalla()
    elif repor == '3':
        mod.viewTr()
        limpiarPantalla()
    elif repor == '4':
        print("")
        limpiarPantalla()
    elif repor == '5':
        print("")
        limpiarPantalla()
    elif repor == '6':
        print("")
        limpiarPantalla()
