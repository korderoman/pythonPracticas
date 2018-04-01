"""Diseñar un programa que permita el ingreso de un conjunto no determinado de números enteros.
Por cada número leído debe preguntar su desea continuar si/no, El programa debe determinar y mostrar el máximo comun divisor
de los dos números más altos
"""
#EL problema nos pide un menu de ingreso de numeros en el que decidamos si continuamos o no
#luego debemos de hallar los dos mayores
#y de esos dos mayores hallar el max común divisor

continuamos="si"
mayor1=0
mayor2=0
while continuamos=="si":
    print("¿Desea continuar? si/no")
    opcion=input()
    #definimos la salida
    if(opcion=="no"):
        continuamos="no"
    elif opcion=="si":
        valor=int(input("Ingrese un número"))
        if valor>mayor1:
            mayor1=valor
        elif valor<mayor1 and valor>mayor2:
            mayor2=valor

    #print("Loa valores son:",mayor1,mayor2)
#COmo ya no desea agregar más numeros y ya tenemos a los mayores, debemos hallar el mcd
mayor=mayor1
menor=mayor2
MCD=0
while menor!=0:
    MCD=menor
    menor=mayor%menor
    mayor=MCD

print("El MCD de: ",mayor1," y ",mayor2," es ",MCD)