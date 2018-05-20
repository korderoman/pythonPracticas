


class Coche():
    largoChasis=250
    anchoChasis=120
    ruedas=4
    enmarcha=False


    def arrancar(self): #self es el this, solo que en otros lenguajes es implícito, pero python requiere que se ponga de forma explícito
        self.enmarcha=True

    def estado(self):
        if(self.enmarcha):
            return "El coche está en marcha"
        else:
            return "El coche está parado"

#instancia, no se requiere el new
miCoche=Coche();

print(miCoche.largoChasis)
miCoche.arrancar()#el metodo arrancar con el parámetro self, está llamando al objeto micochey su propiedad en marcha y modifcandolo
print(miCoche.estado())



class Coche2():
    #sintaxis del constructor, siempre es el mismo para cualquier clase
    def __init__(self):
        #el encapsulamiento se da con __
        self.__largoChasis = 250
        self.__anchoChasis = 120
        self.__ruedas = 4 #encapsulado
        self.__enmarcha = False

    def arrancamos(self,arracamos):
        self.__enmarcha=arracamos

        if self.__enmarcha:
            chequeo=self.__chequeo_interno()

        if self.__enmarcha and chequeo:
            return "El cochis está en marcha"
        elif self.__enmarcha and chequeo==False:
            return "Algo ha ido mal en el chequeo no podemos arrancar"
        else:
            return "El coche está parado"
    #para restringir como uso interno, es decir encapsulado el método debe estar con __
    def __chequeo_interno(self):
        print("realizando chequeo interno")
        self.gasolina="ok"
        self.aceite="ok"
        self.puertas="cerradas"

        if self.gasolina=="ok" and self.aceite=="ok" and self.puertas=="cerradas":
            return True
        else:
            return False

miCoche2=Coche2()
#ruedas ya no es accesible miCoche2.ruedas ni miCoche2.__ruedas

print(miCoche2.arrancamos(True))