import BancoPalabra
from random import randint as rd

# Seleccionar palabra de banco de palabras al azar
def Palabra_Seleccionada():
    PalabraElegida = BancoPalabra.Lista_Palabras[rd(0, len(BancoPalabra.Lista_Palabras)-1)]
    return PalabraElegida

# Transfomra la variable Texto en una cadena de guiones de acuerdo a longitud de la palabra elegida 
def Palabra_En_Guiones(variableTexto, PalabraElegida):
    ListaCaracteres = list(PalabraElegida)
    ListaCaracteres = list(map(lambda x: "-", ListaCaracteres))
    variableTexto.set("".join(ListaCaracteres))

# Verifica que una letra ingresada este dentro de la palabra elegida 
def Verificar_Letra(PalabraElegida, variableTexto, Entrada):
    if Entrada in PalabraElegida:
        Sustituir_Letras(PalabraElegida, variableTexto, Entrada)
        return True
    else:
        return False

# Sustituye los guiones en las posiciones donde se encuentren las letra ingresadas
def Sustituir_Letras(PalabraElegida, variableTexto, Entrada):
    Caracteres = list(variableTexto.get())
    for i in range(len(PalabraElegida)):
        if Entrada == PalabraElegida[i]:
            Caracteres[i] = PalabraElegida[i]
    variableTexto.set("".join(Caracteres))