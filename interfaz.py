

# Carga el archivo txt

def loadArchive():
    """
    Esta funcion carga el archivo txt
    """
    archive = input("Introduzca la direccion de su archivo: ")
    archivo = open(archive,mode='r')
    return archivo

# Funciones revisoras de linea de codigo

def revisorFunction(linea):
    sintaxisFunction = True
    if a != 0 :
        sintaxisFunction = False
    return sintaxisFunction
def revisorVariable(linea):
    sintaxisVariable = True
    if a != 0:
        sintaxisVariable = False
    return sintaxisVariable

def revisorLinea(linea):
    return

# Funcion revisora

def revisor():
    sintaxis = True
    texto = loadArchive()
    datos = texto.split(" ")
    while datos[0] != "":
        linea = texto.readline().strip()
        if revisorFunction(linea) == False or revisorVariable(linea) == False or revisorLinea(linea) == False:
            sintaxis = False
            break
    texto.close()
    return sintaxis