from tkinter import *

def EleccionTemas(interfaz,Value):
    if (Value == 1):  
        interfaz.configure(background="gray60")
    if (Value == 2 ):
        interfaz.configure(background="slate gray")
    if (Value == 3):
        interfaz.configure(background="dim gray")
        