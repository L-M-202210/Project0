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

# ------------------
# ------------------
# Command or Control
# ------------------
# ------------------

# Separadora de list

def separador(palabra):
    a = ""
    for i in range(0,len(palabra)-1):
        a += palabra[i]
    return a

# Existe la variable

def existeVariable(variable,variables):
    existe = False
    if variables.contains(variable) == True:
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

def revisorCreadorVariable(linea,variables):
    sintaxisFunction =  False
    if linea[0] == '(defvar':
        if type(float(linea[1])) == float or type(int(linea[1])) == int:
            pass
        else:
            separada = separador(linea[2])
            if type(int(separada)) == int and linea[2][-1] == ')':
                sintaxisFunction = True
    variables.append(linea[1])
    return sintaxisFunction

def revisorAsignacionVariable(linea):
    sintaxisAsignador = False
    if linea[0] == '(=':
        if type(float(linea[1])) == float or type(int(linea[1])) == int:
            pass
        else:
            separada = separador(linea[2])
            if type(int(separada)) == int and linea[2][-1] == ')':
                sintaxisAsignador = True
    return sintaxisAsignador

# Revisa un movimiento

def revisorMovimiento(linea,variables):
    sintaxisMovement = False
    separada = separador(linea[1])
    if linea[0] + str(type(int(separada))) + linea[1][-1] == '(move' + str(int) + ')':
        sintaxisMovement = True
    elif linea[0] == '(move':
        separada = separador(linea[1])
        if existeVariable(separada,variables) == True and linea[1][-1] == ')':
            sintaxisMovement = True
    elif linea[0] == '(turn':
        if linea[1] == ':left)' or linea[1] == ':right)' or linea[1] == ':around)':
            sintaxisMovement = True
    elif linea[0] == '(face':
        if linea[1] == ':north)' or linea[1] == ':south)' or linea[1] == ':east)' or linea[1] == (':west)'):
            sintaxisMovement = True
    elif linea[0] == '(put':
        if linea[1] == 'Balloons' or linea[1] == 'Chips':
            separada = separador(linea[2])
            if type(int(separada)) == int and linea[2][-1]:
                sintaxisMovement = True
            elif existeVariable(separada,variables) == True and linea[2][-1] == ')':
                sintaxisMovement = True
    elif linea[0] == '(pick':
        if linea[1] == 'Balloons' or linea[1] == 'Chips':
            separada = separador(linea[2])
            if type(int(separada)) == int and linea[2][-1] == ')':
                sintaxisMovement = True
            elif existeVariable(separada,variables) == True and linea[2][-1] == ')':
                sintaxisMovement = True
    elif linea[0] == '(move-dir':
        if type(int(linea[1])) == int:
            if linea[2] == ':north)' or linea[2] == ':south)' or linea[2] == ':east)' or linea[2] == (':west)'):
                sintaxisMovement = True
        elif existeVariable(linea[1],variables) == True: 
            if linea[2] == ':north)' or linea[2] == ':south)' or linea[2] == ':east)' or linea[2] == (':west)'):   
                sintaxisMovement = True
    elif linea[0] == '(run-dirs':
        for direction in linea:
            if direction == ':north)' or direction == ':south)' or direction == ':east)' or direction == ':west)':
                sintaxisMovement = True
    elif linea[0] == '(move-face':
        if type(int(linea[1])) == int:
            if linea[2] == ':north)' or linea[2] == ':south)' or linea[2] == ':east)' or linea[2] == (':west)'):
                sintaxisMovement = True
        elif existeVariable(linea[1],variables) == True:
            if linea[2] == ':north)' or linea[2] == ':south)' or linea[2] == ':east)' or linea[2] == (':west)'):
                sintaxisMovement = True
    elif linea[0] == '(skip)':
        sintaxisMovement = True
    return sintaxisMovement

# funcion acumuladora

def funcionRevisoraAcumuladora(linea,variables):
    sintaxis = False
    if revisorCreadorVariable(linea,variables) == True:
        sintaxis = True
    elif revisorAsignacionVariable(linea) == True:
        sintaxis = True
    elif revisorMovimiento(linea,variables) == True:
        sintaxis = True
    return sintaxis


# -----------------
# -----------------
# Control Structure
# -----------------
# -----------------

# funcion condicion facing

def conditionalFacing(linea):
    sintaxisConditional = False
    if linea[0] == '(facing-p':
        if linea[1] == 'north)':
            sintaxisConditional = True
        elif linea[1] == 'south)':
            sintaxisConditional = True
        elif linea[1] == 'east)':
            sintaxisConditional = True
        elif linea[1] == 'west)':
            sintaxisConditional = True
    return sintaxisConditional

# funcion condicion can-put

def conditionalCanPut(linea,variables):
    sintaxisConditional = False
    if linea[0] == '(can-put-p':
        if linea[1] == 'Balloons' or linea[1] == 'Chips':
            separada = separador(linea[2])
            if type(int(separada)) == int and linea[2][-1] == ')':
                sintaxisConditional = True
            elif existeVariable(separada,variables) == True and linea[2][-1] == ')':
                sintaxisConditional = True
    return sintaxisConditional

# funcion can-pick

def conditionalCanPick(linea,variables):
    sintaxisConditional = False
    if linea[0] == '(can-pick-p':
        if linea[1] == 'Balloons' or linea[1] == 'Chips':
            separada = separador(linea[2])
            if type(int(separada)) == int and linea[2][-1] == ')':
                sintaxisConditional = True
            elif existeVariable(separada,variables) == True and linea[2][-1] == ')':
                sintaxisConditional = True
    return sintaxisConditional

# funcion can-move

def conditionalCan(linea):
    sintaxisConditional = False
    if linea[0] == '(can-move-p':
        if linea[1] == ':north)':
            sintaxisConditional = True
        elif linea[1] == ':south)':
            sintaxisConditional = True
        elif linea[1] == ':west)':
            sintaxisConditional = True
        elif linea[1] == ':east)':
            sintaxisConditional = True
    return sintaxisConditional
        
# funcion not cond

def notCond(linea,variables):
    sintaxisConditional = False
    if linea[0] == '(not':
        separada = separador(linea[1])
        if conditionalFacing(separada) == True:
            sintaxisConditional = True
        elif conditionalCanPut(separada,variables) == True:
            sintaxisConditional = True
        elif conditionalCanPick(separada,variables) == True:
            sintaxisConditional = True
        elif conditionalCan(separada) == True:
            sintaxisConditional = True
    return sintaxisConditional

# revisora condicion

def revisorConditional(linea,variables):
    sintaxisConditional = False
    if linea[0] == '(if':
        separada = separador(linea[1])
        if conditionalFacing(separada) == True:
            sintaxisConditional = True
        elif conditionalCanPut(separada,variables) == True:
            sintaxisConditional = True
        elif conditionalCanPick(separada,variables) == True:
            sintaxisConditional = True
        elif conditionalCan(separada) == True:
            sintaxisConditional = True
    return sintaxisConditional
        
# repeat        

def repeat(linea,variables):
    sintaxisRepeat = False
    if linea[0] == '(loop':
        if conditionalFacing(linea[1]) == True:
            if linea[-1][-1] == ')':
                sintaxisRepeat = True
        elif conditionalCanPut(linea[1],variables) == True:
            if linea[-1][-1] == ')':
                sintaxisRepeat = True
        elif conditionalCanPick(linea[1],variables) == True:
            if linea[-1][-1] == ')':
                sintaxisRepeat = True
        elif conditionalCan(linea[1]) == True:
            if linea[-1][-1] == ')':
                sintaxisRepeat = True
    return sintaxisRepeat

# repeattimes

def repeatTimes(linea,variables):
    sintaxisRepeat = False
    if linea[0] == '(repeat':
        if type(int(linea[1])) == int:
            if linea[-1][-1] == ')':
                sintaxisRepeat = True
        elif existeVariable(linea[1]) == True: 
            if linea[-1][-1] == ')':    
                sintaxisRepeat = True
    return sintaxisRepeat

# ----------------
# Funcion revisora
# ----------------

def main():
    sintaxis = False
    archivo = loadArchive()
    linea = archivo.readline().split()
    variables = []
    funciones = []
    while linea[0] != "":
        if  funcionRevisoraAcumuladora(linea,variables) == False:
            break
        else:
            if revisorConditional(linea,variables) == False:
                break 
            else:
                if repeat(linea,variables) == False:
                    break
                else:
                    if repeatTimes(linea,variables) == False:
                        break
                    else:
                        sintaxis = True
        linea.readline().split()
    archivo.close()
    return sintaxis