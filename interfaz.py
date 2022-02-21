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
    if linea[0] == '(defvar':
        if type(float(linea[1])) == float or type(int(linea[1])) == int:
            pass
        else:
            # problema
            if type(int(linea[2])) == int and linea[3] == ')':
                sintaxisFunction = True
    return sintaxisFunction

def revisorAsignacionVariable(linea):
    sintaxisAsignador = False
    if linea[0] == '(=':
        if type(float(linea[1])) == float or type(int(linea[1])) == int:
            pass
        else:
            # problema
            if type(int(linea[2])) == int and linea[3] == ')':
                sintaxisAsignador = True
    return sintaxisAsignador

# Revisa un movimiento

def revisorMovimiento(linea,variables):
    sintaxisMovement = False
    # problema
    if linea[0] + str(type(int(linea[1]))) == '(move' + str(int) + ')':
        sintaxisMovement = True
        return sintaxisMovement
    elif linea[0] == '(move':
        # problema
        if existeVariable(linea[1],variables) == True and linea[2] == ')':
            sintaxisMovement = True
            return sintaxisMovement
    elif linea[0] == '(turn':
        if linea[1] == ':left)' or linea[1] == ':right)' or linea[1] == ':around)':
            sintaxisMovement = True
            return sintaxisMovement
    elif linea[0] == '(face':
        if linea[1] == ':north)' or linea[1] == ':south)' or linea[1] == ':east)' or linea[1] == (':west)'):
            sintaxisMovement = True
            return sintaxisMovement
    elif linea[0] == '(put':
        if linea[1] == 'Balloons' or linea[1] == 'Chips':
            if type(int(linea[2])) == int:
                sintaxisMovement = True
                return sintaxisMovement
            # problema
            elif existeVariable(linea[2],variables) == True and linea[3] == ')':
                sintaxisMovement = True
                return sintaxisMovement
    elif linea[0] == '(pick':
        if linea[1] == 'Balloons' or linea[1] == 'Chips':
            # problema
            if type(int(linea[2])) == int and linea[3] == ')':
                sintaxisMovement = True
                return sintaxisMovement
            # problema
            elif existeVariable(linea[2],variables) == True:
                sintaxisMovement = True
                return sintaxisMovement
    elif linea[0] == '(move-dir':
        if type(int(linea[1])) == int:
            if linea[2] == ':north)' or linea[2] == ':south)' or linea[2] == ':east)' or linea[2] == (':west)'):
                sintaxisMovement = True
                return sintaxisMovement
        elif existeVariable(linea[1],variables) == True: 
            if linea[2] == ':north)' or linea[2] == ':south)' or linea[2] == ':east)' or linea[2] == (':west)'):   
                sintaxisMovement = True
                return sintaxisMovement
    elif linea[0] == '(run-dirs':
        for direction in linea[1]:
            if direction == ':north)' or direction == ':south)' or direction == ':east)' or direction == ':west)':
                sintaxisMovement = True
                return sintaxisMovement

    elif linea[0] == '(move-face':
        if type(int(linea[1])) == int:
            if linea[2] == ':north)' or linea[2] == ':south)' or linea[2] == ':east)' or linea[2] == (':west)'):
                sintaxisMovement = True
                return sintaxisMovement
        elif existeVariable


    elif linea[0] == '(skip)':
        sintaxisMovement = True
        return sintaxisMovement

# ----------------
# Funcion revisora
# ----------------

def main():
    pass
