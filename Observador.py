

class Tema():
 #Creo lista obs
  ListaObservador = []
  def agregaLista(self,obj):
    self.ListaObservador.append(obj)

  def Notificar(self, valor) :
    for observador in self.ListaObservador:
        observador.Update(valor)
    self.ListaObservador.clear()

  def Quitar(self, obj):
    pass

class TemaConcreto(Tema):

    def __init__(self) :
        self.estado = None
    def SetEstado(self,valor):
        self.estado = valor
        self.Notificar(valor)

    def GetEstado(self):
        return self.estado


class Observador:
    @property
    def Update(self):
        raise NotImplementedError ("A implementar")

class ConcreteObserverAlta(Observador):
     def __init__(self, obj):
         self.observadorA = obj
         self.observadorA.agregaLista(self)
     def Update(self,val):
         print("Actualización dentro de ObservadorConcretoAlta")
         self.estado = self.observadorA.GetEstado()
         print("Informacion ingreso Alta = ", self.estado)


class ConcreteObserverBaja(Observador) :
    def __init__(self, obj) :
        self.observadorA = obj
        self.observadorA.agregaLista(self)

    def Update(self, val) :
        print("Actualización dentro de ObservadorConcretoBaja")
        self.estado = self.observadorA.GetEstado()
        print("Informacion baja id = ", self.estado)


class ConcreteObserverMod(Observador) :
    def __init__(self, obj) :
        self.observadorA = obj
        self.observadorA.agregaLista(self)

    def Update(self, val) :
        print("Actualización dentro de ObservadorConcretoMOD")
        self.estado = self.observadorA.GetEstado()
        print("Informacion MODIFICACADA = ", self.estado)

