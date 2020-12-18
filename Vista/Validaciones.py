import re

def fValidar(cadena):
    patron = re.compile(r'^[A-Za-z]+(?:[ _-][A-Za-z]+)*$')
    try:
        if(patron.match(cadena) != None):
            return "Valido"
        else:
            return "No valido"
    except:
        return "No valido"

