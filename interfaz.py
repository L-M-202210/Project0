# --------------------
# Carga el archivo txt
# --------------------

def loadArchive():
    """
    Esta funcion carga el archivo txt
    """
    archive = input("Introduzca la direccion de su archivo: ")
    archivo = open(archive,mode='r')
    return archivo

# --------------------------------------
# Funciones revisoras de linea de codigo
# --------------------------------------

# Existe la variable

def existeVariable(variable,variables):
    existe = False
    if variable.contains(variable) == True:
        existe = True
    return existe

# Existe la funcion

def existeFunction(funcion,funciones):
    existe = False
    if funciones.contains(funcion) == True:
        existe = True
        return existe

# Revisa la creacion de una funcion

def revisorCreadorFunction(linea):
    pass

# Revisa la creacion de una variable

def revisorCreadorVariable(linea):
    sintaxisFunction =  False
    if linea[0] + linea[1] == '(defvar':
        if type(float(linea[2])) == float or type(int(linea[2])) == int:
            pass
        else:
            if type(float(linea[3])) == float:
                pass
            elif type(int(linea[3])) == int and linea[4] == ')':
                sintaxisFunction = True
    return sintaxisFunction

def revisorAsignacionVariable(linea):
    sintaxisAsignador = False
    if linea[0] + linea[1] == '(=':
        if type(float(linea[2])) == float or type(int(linea[2])) == int:
            pass
        else:
            if type(float(linea[3])) == float:
                pass
            elif type(int(linea[3])) == int and linea[4] == ')':
                sintaxisAsignador = True
    return sintaxisAsignador

# Revisa un movimiento

def revisorMovimiento(linea,variables):
    sintaxisMovement = False
    if linea[0] + linea[1] + str(type(int(linea[2]))) + linea[3] == '(move' + str(int) + ')':
        sintaxisMovement = True
        return sintaxisMovement
    elif linea[0] + linea[1] == '(move':
        if existeVariable(linea[2],variables) == True and linea[3] == ')':
            sintaxisMovement = True
            return sintaxisMovement
    elif linea[0] + linea[1] == '(turn':
        if linea[2] + linea[3] == ':left)' or linea[2] + linea[3] == ':right)' or linea[2] + linea[3] == ':around)':
            sintaxisMovement = True
            return sintaxisMovement
    elif linea[0] + linea[1] == '(face':
        if linea[2] + linea[3] == ':north)' or linea[2] + linea[3] == ':south)' or linea[2] + linea[3] == ':east)' or linea[2] + linea[3] == (':west)'):
            sintaxisMovement = True
            return sintaxisMovement
    elif linea[0] + linea[1] == '(put':
        if linea[2] == 'Balloons' or linea[2] == 'Chips':
            if type(int(linea[3])) == int:
                sintaxisMovement = True
                return sintaxisMovement
            elif existeVariable(linea[3],variables) == True and linea[4] == ')':
                sintaxisMovement = True
                return sintaxisMovement
    elif linea[0] + linea[1] == '(pick':
        if linea[2] == 'Balloons' or linea[2] == 'Chips':
            if type(int(linea[3])) == int and linea[4] == ')':
                sintaxisMovement = True
                return sintaxisMovement
            elif existeVariable(linea[3],variables) == True and linea[4] == ')':
                sintaxisMovement = True
                return sintaxisMovement
    elif linea[0] + linea[1] == '(move-dir':
        if type(int(linea[2])) == int:
            if linea[3] + linea[4] == ':north)' or linea[3] + linea[4] == ':south)' or linea[3] + linea[4] == ':east)' or linea[3] + linea[4] == (':west)'):
                sintaxisMovement = True
                return sintaxisMovement
        elif existeVariable(linea[2],variables) == True: 
            if linea[3] + linea[4] == ':north)' or linea[3] + linea[4] == ':south)' or linea[3] + linea[4] == ':east)' or linea[3] + linea[4] == (':west)'):   
                sintaxisMovement = True
                return sintaxisMovement



    elif linea[0] + linea[1] == '(run-dirs':
        return sintaxisMovement
    elif linea[0] + linea[1] == '(move-face':
        return sintaxisMovement
    elif linea[0] + linea[1] + linea[2] == '(skip' +')':
        return sintaxisMovement

# ----------------
# Funcion revisora
# ----------------

def main():
    pass
