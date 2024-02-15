import modulo as mod
import main as lok
def letrerito():
    print("------------------------------")
    print("-       ROL COORDINACIÓN     -")
    print("-          ACADÉMICA         -")
    print("------------------------------")

def letrero():
    print("------------------------------")
    print("-         ROL TRAINERS       -")
    print("------------------------------")

def reports():
    repor = input("Digite el número según la sección a la que deseas ingresar: ")
    if repor == '1':
        print("")
        lok.limpiarPantalla()
    elif repor == '2':
        mod.viewMa()
        lok.limpiarpantalla()
    elif repor == '3':
        mod.viewTr()
        lok.limpiarPantalla()
    elif repor == '4':
        print("")
        lok.limpiarPantalla()
    elif repor == '5':
        print("")
        lok.limpiarPantalla()
    elif repor == '6':
        print("")
        lok.limpiarPantalla()



