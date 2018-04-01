"""
Diseñar un programa que permita el ingreso de un conjunto no determinado de caracteres, Por cada carácter leído
debe formar la palabra "Lenguaje"

El problema nos pide que ingresemos caracteres hasta que se forme la palabra lenguaje
"""

#Esto definitivamente se realiza mediante un while

p1="";p2="";p3="";p4="";p5="";p6="";p7="";p8="";
palabra=""

while palabra!="lenguaje":
    letra=str(input("Ingrese una letra"))




    if letra=="l":

        p1=letra
    elif letra=="e":
        p2=letra
        p8=letra
    elif letra=="n":
        p3=letra
    elif letra=="g":
        p4=letra
    elif letra=="u":
        p5=letra
    elif letra=="a":
        p6=letra
    elif letra=="j":
        p7=letra
    palabra = "" + p1 + p2 + p3 + p4 + p5 + p6 + p7 + p8
    print(palabra)

print(palabra)

