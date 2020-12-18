
from tkinter import messagebox
import mysql.connector
import peewee

from Vista.InterfazUnidad6 import *
from Vista import Validaciones
import datetime
from Observador import *
from peewee import *




BasePrueba = peewee.SqliteDatabase("baseprueba1.db")
class Base(Model):
    Id = peewee.AutoField()
    Titulo = peewee.TextField()
    Ruta = peewee.TextField()
    Descripcion = peewee.TextField()
    Fecha = peewee.DateField(default=datetime.datetime.now)


    class Meta:
        database = BasePrueba

    def __str__(self) :
        strcadena= " Titulo " + str(self.Titulo)
        return strcadena






class Administrador(TemaConcreto):

    def crearBD(self):

        BasePrueba.connect()
        BasePrueba.create_tables([Base],safe=True)



    #def crearTabla(self):

    def fDecoradora_B(funcion_parametro) :
        def fDecoradora_borra(*args, **kwargs) :
            # Se realizan acciones acá dentro
            print("Se borro informacion")
            print("Inicia ejecucion de " + str(funcion_parametro))
            funcion_parametro(*args, **kwargs)

        return fDecoradora_borra

    ##DECORADOR DE BAJA
    @fDecoradora_B
    def fBaja(self,nid):
            datos = [nid.get()]
            print(datos)
            Elementos = Base(Id=datos)
            Consulta = Elementos.delete().where(Base.Id == datos)
            Consulta.execute()
            messagebox.showinfo("borrado con exito", message="Se borro con exito.")
            ##PATRON OBSERVADOR BAJA
            obs = ConcreteObserverBaja(self)
            val = datos
            self.SetEstado(val)

    ##DECORADOR DE MODIFICACION
    def fDecoradora_M(funcion_parametro) :
        def fDecoradora_Modifica(*args, **kwargs) :
            # Se realizan acciones acá dentro
            print("Se modifico nueva informacion")
            print("Inicia ejecucion de " + str(funcion_parametro))
            funcion_parametro(*args, **kwargs)

        return fDecoradora_Modifica


    @fDecoradora_M
    def fModifica(self,nid,sTitulo,sRuta,sDescripcion):
        cadena = sTitulo.get()
        Validaciones.fValidar(cadena)
        datos = [nid.get()]
        print((datos))
        if(Validaciones.fValidar(cadena) != "No valido"):
            #Elementos = Base(Titulo= sTitulo.get(),Ruta= sRuta.get(),Descripcion=sDescripcion.get())
            ConsultaUp = Base.update(Titulo=cadena,Ruta= sRuta.get(),Descripcion=sDescripcion.get()).where(Base.Id == datos)
            ConsultaUp.execute()
            ##OBSERVADOR MODIFICACION
            obs = ConcreteObserverMod(self)
            val = (datos,cadena,sRuta.get(),sDescripcion.get())
            self.SetEstado(val)

        else:
            messagebox.showerror("campo invalido",message="No acepta numerico.")


    def fConsulta(self,Tabla):
        for i in Base.select():
            Tabla.insert('', 0, values=(i.Id, i.Titulo, i.Ruta, i.Descripcion, i.Fecha))

    ##DECORADOR DE ALTA
    def fDecoradora_A(funcion_parametro) :
        def fDecoradora_alta(*args, **kwargs):
            # Se realizan acciones acá dentro
            print("Se ingreso nueva informacion")
            print("Inicia ejecucion de " + str(funcion_parametro))
            funcion_parametro(*args, **kwargs)

        return fDecoradora_alta


    @fDecoradora_A

    def AltaDiccionario(self,Tabla,sTitulo,sRuta,sDescripcion):
            #VALIDACION#

            sCadena = sTitulo.get()
            if(Validaciones.fValidar(sCadena) != "No valido"):
                ##Declaro esta variable para poder insertar los datos##
                Elementos = Base(Titulo= sCadena, Ruta=sRuta.get(), Descripcion=sDescripcion.get())
                Elementos.save()
                ##Para que aparezca en el treeview


                ###PARA PATRON OBS###
                obs = ConcreteObserverAlta(self)
                val = (sCadena,sRuta.get(),sDescripcion.get())
                self.SetEstado(val)
                for i in Base.select():
                    Tabla.insert('', 0, values=(i.Id, i.Titulo, i.Ruta, i.Descripcion,i.Fecha,i))


            else:
                messagebox.showerror("campo invalido",message="No acepta numerico.")





