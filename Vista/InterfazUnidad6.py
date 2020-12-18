from tkinter import *
from tkinter import ttk
from Controlador.Controlador_I import *

from modulo_temas import temas


##from modulo_base_datos import Insertar as Administrador


##CLASE
class VentanaInterfaz():
    def __init__(self,interfaz):
        self.Raiz = interfaz

        self.iniciarinterfaz()
    ##funcion para iniciar la interfaz##
    def iniciarinterfaz(self):
        self.sTitulo = StringVar()
        self.sRuta = StringVar()
        self.sDescripcion = StringVar()
        self.nid = IntVar()
        self.Raiz.geometry("1700x600")
        self.Tabla = ttk.Treeview(self.Raiz, columns=("size", "lastmod"))
        self.Tabla.grid(row=8, column=1, columnspan=1, sticky="nsew")

        self.Tabla["columns"] = ("1", "2", "3", "4","5","6")
        self.Tabla['show'] = 'headings'
        self.Tabla.heading("1", text="id")
        self.Tabla.heading("2", text="Titulo")
        self.Tabla.heading("3", text="Ruta")
        self.Tabla.heading("4", text="Descripción")
        self.Tabla.heading("5", text="Fecha")
        self.Tabla.heading("6", text="Objeto")

        self.Raiz.title("Aplicacion MVC")
        def fEntradas(variable, anchura, fila, columna):
            entrada = Entry(self.Raiz, textvariable=variable, width=anchura)
            entrada.grid(row=fila, column=columna)
            return entrada

        fEntradas(self.sTitulo, 20, 1, 1)
        fEntradas(self.sRuta, 20, 2, 1)
        fEntradas(self.sDescripcion, 20, 3, 1)
        fEntradas(self.nid, 20, 5, 1)
        #fEntradas(self.nid, 20, 7, 1)

        # MARCO
        self.Marco = Frame(self.Raiz, width=1700, height=600)
        self.Marco.place(x=0, y=430)

        Label(self.Raiz, text="Ingrese sus datos", bg="purple", fg="white", font="bold").grid(row=0, column=0,
                                                                                              columnspan=10,
                                                                                              padx=1, pady=1,
                                                                                              sticky=W + E)
        Label(self.Raiz, text="Titulo").grid(row=1, column=0, sticky=W)
        Label(self.Raiz, text="Ruta").grid(row=2, column=0, sticky=W)
        Label(self.Raiz, text="Descripcion").grid(row=3, column=0, sticky=W)
        Label(self.Raiz, text="id").grid(row=5, column=1, sticky=W)
       #Label(self.Raiz, text="id").grid(row=7, column=1, sticky=W)

        ##Botones

        self.Boton1 = Button(self.Raiz, text="Alta", padx=60, pady=1, bg="lightgray", fg="black")
        self.Boton1.grid(row=1, column=2)
        self.Boton3 = Button(self.Raiz, text="Crear Base y tabla", padx=45, pady=1, bg="lightgray", fg="black")
        self.Boton3.grid(row=3, column=2)
        #self.Boton4 = Button(self.Raiz, text="Crear tabla", padx=45, pady=1, bg="lightgray", fg="black")
        #self.Boton4.grid(row=4, column=2)
        self.Boton8 = Button(self.Raiz, text="Consulta todo", padx=65, bg="lightgray", fg="black")
        self.Boton8.grid(padx=20, row=10, column=1)
        self.Boton5 = Button(self.Raiz, text="Dar de baja por id", padx=45, bg="lightgray", fg="black")
        self.Boton5.grid(padx=20, row=5, column=0)
        self.Boton6 = Button(self.Raiz, text="Modifica", padx=45, bg="lightgray", fg="black")
        self.Boton6.grid(padx=20, row=6, column=2)

        self.RbSelecccion = IntVar(value=1)
        self.LblTema = Label(text="Seleccione el tema", bg="black", fg="white", font="bold").grid(padx=20, row=11, column=1)
        self.Rbboton1 = Radiobutton(self.Raiz, text="tema 1", value=1, variable=self.RbSelecccion,
                               command=lambda: temas.EleccionTemas(self.Marco, 1)).grid(padx=20, row=12, column=1)
        self.Rbboton2 = Radiobutton(self.Raiz, text="tema 2", value=2, variable=self.RbSelecccion,
                               command=lambda: temas.EleccionTemas(self.Marco, 2)).grid(padx=20, row=13, column=1)
        self.Rbboton3 = Radiobutton(self.Raiz, text="tema 3", value=3, variable=self.RbSelecccion,
                               command=lambda: temas.EleccionTemas(self.Marco, 3)).grid(padx=20, row=14, column=1)
    ##VENTANA SECUNDARIA baja
    def bajaSecundaria(self):
        self.bSecundaria = Toplevel()
        self.bSecundaria.title="Dar de baja"
        self.bSecundaria.geometry("600x100")
        self.bSecundaria.config(bg="grey")
        self.nid = IntVar()
        bSecundariaLabel = Label(self.bSecundaria, text="Ingrese el id a dar de baja", bg="blue", fg="White", width=88)
        bSecundariaLabel.grid(column=0, row=0, padx=5, pady=5, columnspan=5)
        bSecundariaLabel2 = Label(self.bSecundaria, text="id ")
        bSecundariaLabel2.grid(column=0, row=1,)
        def fEntradas(variable, anchura, fila, columna):
            entrada = Entry(self.bSecundaria, textvariable=variable, width=anchura)
            entrada.grid(row=fila, column=columna)
            return entrada
        fEntradas(self.nid,20,1,1)
        self.bSecundariaBtn = Button(self.bSecundaria, text="Dar de Baja", padx=45, bg="lightgray", fg="black",command=self.bSecundaria.destroy)
        self.bSecundariaBtn.grid(column= 0,row=2,pady=10)
        self.bSecundariaBtn2 = Button(self.bSecundaria, text="Volver", padx=45, bg="lightgray", fg="black",command=self.bSecundaria.destroy)
        self.bSecundariaBtn2.grid(column= 1,row=2,pady=10)



if __name__ == '__main__':
    interfaz = Tk()
    Ventana = VentanaInterfaz(interfaz)
    interfaz.mainloop()
