from tkinter import *
import BancoPalabra
import Funciones
from PIL import ImageTk, Image
from tkinter import messagebox

ListaImagenes = []
IndexImg = 0

# Se encarga de hacer un reinicio al programa
def Re_Iniciar():
 global IndexImg, PalabraElegida
 PalabraElegida = Funciones.Palabra_Seleccionada()
 Funciones.Palabra_En_Guiones(Palabra, PalabraElegida)
 IndexImg = -1
 Eliminar_Parte_Del_Cuerpo()

# Esta funcion es una funcion intermedia entre el boton y las acciones que se deben realizar al presionar el
# boton verificar 
def Comunicadora(PalabraElegida, Palabra, entrada):
    if Funciones.Verificar_Letra(PalabraElegida, Palabra, entrada) == False:
        Eliminar_Parte_Del_Cuerpo()
    elif "-" not in Palabra.get():
        Terminar("True")
    Entrada.delete(0, END)

# Esta funcion va cambiando de imagen siempre y cuando el input del usuario no se encuentre dentro de la palabra a adivinar
def Eliminar_Parte_Del_Cuerpo():
    global IndexImg
    IndexImg += 1
    Imagen.configure(image = ListaImagenes[IndexImg])
    if IndexImg == len(ListaImagenes) - 1:
        Terminar(False)

def Terminar(Ganado: bool):
    if not Ganado:
        messagebox.showerror("Partida Perdida", "Usted ha perdido. La palabra correcta era " + PalabraElegida)
    else:
        messagebox.showinfo("Partida Ganada", "Felicidades. Ha adivinado la palabra correcta")
    Re_Iniciar()

# Diseño de ventana principal 
root = Tk()
root.title("Hangman Game")
root.geometry("500x550")
root.configure(background = "white")
root.resizable(False, False)
root.iconbitmap(".icon\\HangmanImg.ico")

img1 = PhotoImage(file = BancoPalabra.RutasImagenes[0])
img2 = PhotoImage(file = BancoPalabra.RutasImagenes[1])
img3 = PhotoImage(file = BancoPalabra.RutasImagenes[2])
img4 = PhotoImage(file = BancoPalabra.RutasImagenes[3])
img5 = PhotoImage(file = BancoPalabra.RutasImagenes[4])
img6 = PhotoImage(file = BancoPalabra.RutasImagenes[5])
img7 = PhotoImage(file = BancoPalabra.RutasImagenes[6])
ListaImagenes.extend([img1, img2, img3, img4, img5, img6, img7])

Imagen = Label(root, height = 300, width = 300, image = img1, background = "white")
Imagen.pack(side = "top", anchor = "center")

Palabra = StringVar(value = "")
PalabraL = Label(root, font = ("Arial", 30), textvariable = Palabra, background = "white")
PalabraL.pack(side = "top", anchor = "center")

Entrada = Entry(root, bd = 5, background = "white",  width = 5, font = ("Arial", 20), justify = "center")
Entrada.pack(ipady = 10)

Verificacion = Button(root, text = "Verificar", background = "black", bd = 0, font = ("Calibri", 15), fg = "white", height = 1, pady = 1, padx = 3, command = lambda: Comunicadora(PalabraElegida, Palabra, Entrada.get().lower()))
Verificacion.pack(pady = 15)

PalabraElegida = Funciones.Palabra_Seleccionada()
Funciones.Palabra_En_Guiones(Palabra, PalabraElegida)

root.mainloop()