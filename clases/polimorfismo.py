"""
Un objeto puede cambiar de acuerdo al contexto en el que se despliega
dado que python es de tipado dinámico , no representa mucho problema


"""


import  modulo
from modulo import *


print(modulo.suma(1,2))


class Coche():
    def desplazamiento(self):
        print("Me desplazo utilizando 4 ruedas")


class Moto():
    def desplazamiento(self):
        print("Me desplazo utilizando dos ruedas")


class Camion():
    def desplazamiento(self):
        print("Me desplazo utilizando seis ruedas")



miVehiculo=Moto()
miVehiculo2=Coche()
miVehiculo3=Camion()

miVehiculo.desplazamiento()
miVehiculo2.desplazamiento()
miVehiculo3.desplazamiento()


#pero si creamos una funcion que se adapte
def desplazamientoVehiculo(vehiculo):
    vehiculo.desplazamiento()

#el polimorfismo hace que se transforme en un tipo camion, de igual forma si es una moto u otra clase
desplazamientoVehiculo(miVehiculo3)