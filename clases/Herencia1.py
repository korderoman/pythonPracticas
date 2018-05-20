"""


"""
class Vehiculos():
    def __init__(self,marca,modelo):
        self.marca=marca
        self.modelo=modelo
        self.enmarcha=False
        self.acelera=False
        self.frena=False

    def arrancar(self):
        self.enmarcha=True

    def acelerar(self):
        self.acelera=True

    def frenar(self):
        self.frena=True

    def estado(self):
        print ("Marca: ",self.marca, "\n Modelo: ",self.modelo,"\n ")



#la herencia se incluye entre los parentesis de la clases
class Moto (Vehiculos):
    hacecaballito=""
    def caballito(self):
        self.hacecaballito="voy haciendo el caballito"

    #necesitamos sobreescribir el metodo estado y agregar lo que necesitemos
    def estado(self):
        print("Marca: ", self.marca, "\n Modelo: ", self.modelo, self.hacecaballito )

#creamos una instancia de moto

miMoto=Moto("Honda","CBR")
miMoto.caballito()
miMoto.estado()


class Furgoneta(Vehiculos):
    def carga(self,cargar):
        self.cargado=cargar
        if self.cargado:
            return "La furgoneta está cargada"
        else:
            return "La furgoneta no está cargada"


class VElectricos():
    def __init__(self):
        self.autonomia=100

    def cargarEnergia(self):
        self.cargando=True


#Multiherencia solo se indica dentro de los paréntesis
class BicicletaElectrica(VElectricos,Vehiculos):
    #esta usando el init de VElectricos por ser primero ignorando a los demás
    #la fucnion super va a llamar al mettodo de la clase padre
    pass


#con la multiherencia, los argumentos de los constructores, se definen de la siguiente forma
#se da preferencia a la primera clase que se colocó en el paréntesis, en este caso VElectricos
#y VElectrico no tiene parámetros
miBici=BicicletaElectrica()



miFurgoneta=Furgoneta("Renault","Kangoo")
miFurgoneta.arrancar()
miFurgoneta.estado()
print(miFurgoneta.carga(True))

