import BancoPalabra
from random import randint as rd

def Palabra_Seleccionada():
# Seleccionar palabra de banco de palabras al azar
    PalabraElegida = BancoPalabra.Lista_Palabras[rd(0, len(BancoPalabra.Lista_Palabras)-1)]
    return PalabraElegida

def Palabra_En_Guiones(variableTexto, PalabraElegida):
# Transfomra la variable Texto en una cadena de guiones de acuerdo a longitud de la palabra elegida 
    ListaCaracteres = list(PalabraElegida)
    ListaCaracteres = list(map(lambda x: "-", ListaCaracteres))
    variableTexto.set("".join(ListaCaracteres))

def Verificar_Letra(PalabraElegida, variableTexto, Entrada):
# Verifica que una letra ingresada este dentro de la palabra elegida 
    if Entrada in PalabraElegida:
        Sustituir_Letras(PalabraElegida, variableTexto, Entrada)
        return True
    else:
        return False

def Sustituir_Letras(PalabraElegida, variableTexto, Entrada):
# Sustituye los guiones en las posiciones donde se encuentren las letra ingresadas
    Caracteres = list(variableTexto.get())
    for i in range(len(PalabraElegida)):
        if Entrada == PalabraElegida[i]:
            Caracteres[i] = PalabraElegida[i]
    variableTexto.set("".join(Caracteres))