"""
Los diccionarios
    Son estructuras de datos que nos permiten almacenar valores de diferente tipo (enteros, cadenas de texto, decimales)
    e incluso listas y otros diccionarios.
    La principal característica de los diccionarios es que los datos se almacenan asociados a una clave de tal forma que se
    se crea una asociación de tipo clave:valor para cada elementos almacenado.
    Los elementos almacenados no está ordenandos. El orden es indiferente a la hora de almacenar información en un diccionario. (HashSet en Java)
    Los diccionarios van entre llaves

"""
midiccionario={"Alemania":"Berlin","Peru":"Lima","Francia":"París","Reino Unido":"Londres","España":"Madrid"}

#podemos acceder a través de la clave

print(midiccionario["Francia"])

#agregar elementos a un diccionario
midiccionario["Italia"]="Lisboa"

print(midiccionario)
#podemos sobrescribir un valor
midiccionario["Italia"]="Roma"
print(midiccionario)

#eliminar una elemento del diccionario

del midiccionario["Reino Unido"]
print(midiccionario)

#un diccionario puede tener diferentes tipos de datos
midiccionario2={"Alemania":"Berlin",23:"Jordan","edad":35}
print(midiccionario2)
#Tambien a una clave se le pueden asignar muchos valores
midiccionario3={23:"Jordan","Nombre":"Michael","Equipo":"Chicago","anillos":[1991,1992,1993,1996,1997,1998]}
print(midiccionario3)
#tambien podemos guardar un diccionario dentro de otro diccionario
midiccionario3={23:"Jordan","Nombre":"Michael","Equipo":"Chicago","anillos":{"temporadas":[1991,1992,1993,1996,1997,1998]}}
#metodos de un diccionario que nos devuelve las claves
print(midiccionario.keys())
#los valores
print(midiccionario.values())
#la longitud del diccionario
print(len(midiccionario))

