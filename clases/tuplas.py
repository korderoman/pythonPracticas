"""
Parecida a las listas, pero son inmutables, es decir que no cambian en el tiempo,
no se puede añadir, eliminar. Pero si tienen acciones tales como obtener porciones
que se forman en nuevas tuplas, no periten hacer busquedas, pero si podemos comprobar si existe un elementos o si
¿Que utilidad tiene?
Más rápidas, menos espacio, formatean Strings, pueden utilizarse como claves en un diccionario. (las listas no)

"""

mitupla=("Juan",13,1,1995)
print(mitupla[2])


miLista2=["Juan",13,1,1995]
#podemos convetir una tupla en lista
milista=list(mitupla)
#podemos convertir una lista en tupla
mitupla2=tuple(miLista2)


print(milista)
print(mitupla2)

print("Juan" in mitupla2) #podemos saber si un elemento esta dentro de la tupla o lista
print(mitupla2.count(13)) #count, cuenta cuantas veces existe un elemento en una tupla
#una tupla unitaria
mitupla3=("Juan",)#la coma hace dicha indicacion
#también puede ir sin paréntesis
mitupl4="Juan",13,1,1995
#podemos asignar a las variables los componentes de las tuplas
nombre,dia,mes,agno=mitupla #a esto se le conoce como desempaquetado de tupla


print(nombre)