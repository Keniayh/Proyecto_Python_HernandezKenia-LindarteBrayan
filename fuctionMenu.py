import modulo as mod
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
    elif repor == '2':
        mod.viewMa()
    elif repor == '3':
        mod.viewTr()
    elif repor == '4':
        print("")
    elif repor == '5':
        print("")
    elif repor == '6':
        print("")

reports()
