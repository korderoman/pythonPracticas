"""
Estructuras que extraen valores de una función y se almacenan en objetos iterables (que se pueden recorrer
Son mas eficientes que las funciones tradicionales
muy útiles con listas de valores infinitos
Bajos determinados escenarios, será muy útil que un generador devuelva los valores de uno en uno
Un generador usar la palabra reservada yield


"""

#haremos que nos genere una función de números pares

def generarPares(limite):
    num=1
    milista=[]
    while num<limite:
        milista.append(num*2)
        num+=1
    return milista

print(generarPares(10))


def generarPares2(limite):
    num = 1

    while num < limite:
        yield num*2
        num += 1

devuelvePares=generarPares2(10)

for i in devuelvePares:
    print(i)


#Ahora con la instruccion yield from
#Simplifica el código del generador en caso tengamos que usar bucles anidados.

#*el asterisoc en python significa que no se sabe cuantos argumentos se incluiran y que estos se entregaran en forma de tupla

def devuelveCiudades(*ciudades):
    for e in ciudades:
        yield e


ciudadesDevueltas=devuelveCiudades("Madrid","Barcelona","Bilbao","Valencia")
    #next imprime uno a uno
print(next(ciudadesDevueltas))
print(next(ciudadesDevueltas))


#si quisieramos acceder a las letras

def devuelveCiudades2(*ciudades):
    for e in ciudades:
        for subelemento in e:
            yield subelemento

ciudadesDevueltas2=devuelveCiudades2("Madrid","Barcelona","Bilbao","Valencia")

print(next(ciudadesDevueltas2))
print(next(ciudadesDevueltas2))




def devuelveCiudades3(*ciudades):
    for e in ciudades:
        yield from e #devuelve lo mismo que la funcion 2

ciudadesDevueltas3=devuelveCiudades3("Madrid","Barcelona","Bilbao","Valencia")

print(next(ciudadesDevueltas3))
print(next(ciudadesDevueltas3))