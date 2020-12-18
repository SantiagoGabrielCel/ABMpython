from Modelo.ComportamientoModleo import *
from Vista.InterfazUnidad6 import *
from tkinter import *



class PrincipalControlador():
    def __init__(self,Raiz):
        self.Raiz = Raiz
        self.ControlVentana = VentanaInterfaz(Raiz)
        self.ControlModelo = Administrador()

        ################################
        # INTERMERDIARIO BOTONES #######
        ###############################
        ##con el .config se soluciono el error de DATATYPE
        self.ControlVentana.Boton1.config(command=self.intermediarAltaDiccionario)
        self.ControlVentana.Boton3.config(command=self.intermediarCreaBD)
        #self.ControlVentana.Boton4.config(command=self.intermediarcreaTabla)
        self.ControlVentana.Boton8.config(command=self.intermediarConsulta)
        self.ControlVentana.Boton5.config(command=self.intermediarBaja)
        self.ControlVentana.Boton6.config(command=self.intermediarModificacion)


    def intermediarCreaBD(self):
        self.ControlModelo.crearBD()

    def intermediarcreaTabla(self):
        self.ControlModelo.crearTabla()

    def intermediarAltaDiccionario(self):

        self.ControlModelo.AltaDiccionario(self.ControlVentana.Tabla,self.ControlVentana.sTitulo, self.ControlVentana.sRuta,
                                           self.ControlVentana.sDescripcion)
    def intermediarConsulta(self):
        self.ControlModelo.fConsulta(self.ControlVentana.Tabla)

    def intermediarBaja(self):
        self.ControlVentana.bajaSecundaria()
        if self.ControlVentana.bSecundariaBtn:
            self.ControlVentana.bSecundariaBtn.config(command=self.bajaSecundaria)



    def intermediarModificacion(self):
        self.ControlModelo.fModifica(self.ControlVentana.nid,self.ControlVentana.sTitulo, self.ControlVentana.sRuta,self.ControlVentana.sDescripcion)

    def bajaSecundaria(self):
        ##print(self.ControlVentana.bSecundaria.nid)
        self.ControlModelo.fBaja(self.ControlVentana.nid)
        if self.ControlModelo.fBaja:
            self.ControlVentana.bSecundaria.destroy()


if __name__ == '__main__':
    Raiz = Tk()
    App = PrincipalControlador(Raiz)
    Raiz.mainloop()
