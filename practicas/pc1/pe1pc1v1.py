"""Realizar el siguiente menu:
    MENU de OPCIONES
    ________________
    (O)rdenar 5 números
    (F)recuencia de notas
    (S)alir
    Elija una Opción

    Donde:
    Ordenar: escriba un programa que lea 5 números reales, dos de ellos por lo menos negativos. luego el programa debe
    ordenar en forma ascendente los números positivos siempre y cuando existan por lo menos 2.

    frecuencia:
    Diseñar un programa que permita el ingreso de las notas de n (n>=10) alumnos de un determinado curso, luego muestre
    las 3 notas más altas y el número de alumnos que poseer dichas notas
"""
a=""
while a!="s":
    print("MENU DE OPCIONES")
    print("------------------")
    print("(O)rdenar 5 números \n(F)recuencia de notas \n(S)alir \nElija una opción")

    opcion=input();
    opcion=opcion.lower() #a minusculas, asi evitamos cualquier incidente de parte del usuario

    if(opcion=="o"):
        n1=int(input("Ingrese el primer número"))
        n2=int(input("Ingrese el primer número"))
        n3=int(input("Ingrese el primer número"))
        n4=int(input("Ingrese el primer número"))
        n5=int(input("Ingrese el primer número"))

        esmenor=n1
        #La técnica de resolución consiste en comparar uno por uno los números en cascada
        #primero n1 vs todos
        if n1>n2:
            esmenor=n2
            n2=n1
            n1=esmenor
        if n1>n3:
            esmenor=n3
            n3=n1
            n1=esmenor
        if n1>n4:
            esmenor=n4
            n4=n1
            n1=esmenor
        if n1>n5:
            esmenor=n5
            n5=n1
            n1=esmenor
        #ahora n2 vs los que estén delante de el
        if(n2>n3):
            esmenor=n3
            n3=n2
            n2=esmenor
        if (n2 > n4):
            esmenor = n4
            n4 = n2
            n2 = esmenor
        if (n2 > n5):
            esmenor = n5
            n5 = n2
            n2 = esmenor
        #ahora n3 vs los que estén delante de el

        if n3>n4:
            esmenor=n4
            n4=n3
            n3=esmenor
        if n3>n5:
            esmenor=n5
            n5=n3
            n3=esmenor
        #Ahora con 4, con 5 no pues no tiene números adelante
        if n4>n5:
            esmenor=n5
            n5=n4
            n4=esmenor
        print("Los números de menor a mayor son: ",n1,n2,n3,n4,n5)
        #Fin de pregunta de ordenamiento

    elif opcion=="f":

            #deicidimos arbitrariamente que el número sea 10 ya que cumple la condicion
            nota1=int(input("Ingrese la nota"))
            nota2 = int(input("Ingrese la nota"))
            nota3 = int(input("Ingrese la nota"))
            nota4 = int(input("Ingrese la nota"))
            nota5 = int(input("Ingrese la nota"))
            nota6 = int(input("Ingrese la nota"))
            nota7 = int(input("Ingrese la nota"))
            nota8 = int(input("Ingrese la nota"))
            nota9 = int(input("Ingrese la nota"))
            nota10 = int(input("Ingrese la nota"))

            mayor=nota10
            if (nota10 <= nota1):
                mayor = nota1
                nota1 = nota10
                nota10 = mayor

            if (nota10 <= nota2):
                mayor = nota2
                nota2 = nota10
                nota10 = mayor

            if (nota10 <= nota3):
                mayor = nota3
                nota3 = nota10
                nota10 = mayor

            if (nota10 <= nota4):
                mayor = nota4
                nota4 = nota10
                nota10 = mayor

            if (nota10 <= nota5):
                mayor = nota5
                nota5 = nota10
                nota10 = mayor

            if (nota10 <= nota6):
                mayor = nota6
                nota6 = nota10
                nota10 = mayor

            if (nota10 <= nota7):
                mayor = nota7
                nota7 = nota10
                nota10 = mayor

            if (nota10 <= nota8):
                mayor = nota8
                nota8 = nota10
                nota10 = mayor

            if (nota10 <= nota9):
                mayor = nota9
                nota9 = nota10
                nota10 = mayor

            #nota 9

            if (nota9 <= nota1):
                mayor = nota1
                nota1 = nota9
                nota9 = mayor

            if (nota9 <= nota2):
                mayor = nota2
                nota2 = nota9
                nota9 = mayor

            if (nota9 <= nota3):
                mayor = nota3
                nota3 = nota9
                nota9 = mayor

            if (nota9 <= nota4):
                mayor = nota4
                nota4 = nota9
                nota9 = mayor

            if (nota9 <= nota5):
                mayor = nota5
                nota5 = nota9
                nota9 = mayor

            if (nota9 <= nota6):
                mayor = nota6
                nota6 = nota9
                nota9 = mayor

            if (nota9 <= nota7):
                mayor = nota7
                nota7 = nota9
                nota9 = mayor

            if (nota9 <= nota8):
                mayor = nota8
                nota8 = nota9
                nota9 = mayor


            #con 8
            if (nota8 < nota1):
                mayor = nota1
                nota1 = nota8
                nota8 = mayor
            if (nota8 < nota2):
                mayor = nota2
                nota2 = nota8
                nota8 = mayor
            if (nota8 < nota3):
                mayor = nota3
                nota3 = nota8
                nota8 = mayor
            if (nota8 < nota4):
                mayor = nota4
                nota4 = nota8
                nota8 = mayor
            if (nota8 < nota5):
                mayor = nota5
                nota5 = nota8
                nota8 = mayor
            if (nota8 < nota6):
                mayor = nota6
                nota6 = nota8
                nota8 = mayor
            if (nota8 < nota7):
                mayor = nota7
                nota7 = nota8
                nota8 = mayor

                # con 7
            if (nota7 < nota1):
                mayor = nota1
                nota1 = nota7
                nota7 = mayor
            if (nota7 < nota2):
                mayor = nota2
                nota2 = nota7
                nota7 = mayor
            if (nota7 < nota3):
                mayor = nota3
                nota3 = nota7
                nota7 = mayor
            if (nota7 < nota4):
                mayor = nota4
                nota4 = nota7
                nota7 = mayor
            if (nota7 < nota5):
                mayor = nota5
                nota5 = nota7
                nota7 = mayor
            if (nota7 < nota6):
                mayor = nota6
                nota6 = nota7
                nota7 = mayor

            # con 6
            if (nota6 < nota1):
                mayor = nota1
                nota1 = nota6
                nota6 = mayor
            if (nota6 < nota2):
                mayor = nota2
                nota2 = nota6
                nota6 = mayor
            if (nota6 < nota3):
                mayor = nota3
                nota3 = nota6
                nota6 = mayor
            if (nota6 < nota4):
                mayor = nota4
                nota4 = nota6
                nota6 = mayor
            if (nota6 < nota5):
                mayor = nota5
                nota5 = nota6
                nota6 = mayor

            # con 5
            if (nota5 < nota1):
                mayor = nota1
                nota1 = nota5
                nota5 = mayor
            if (nota5 < nota2):
                mayor = nota2
                nota2 = nota5
                nota5 = mayor
            if (nota5 < nota3):
                mayor = nota3
                nota3 = nota5
                nota5 = mayor
            if (nota5 < nota4):
                mayor = nota4
                nota4 = nota5
                nota5 = mayor

            # con 4
            if (nota4 < nota1):
                mayor = nota1
                nota1 = nota4
                nota4 = mayor
            if (nota4 < nota2):
                mayor = nota2
                nota2 = nota4
                nota4 = mayor
            if (nota4 < nota3):
                mayor = nota3
                nota3 = nota4
                nota4 = mayor
            # con 3
            if (nota3 < nota1):
                mayor = nota1
                nota1 = nota3
                nota3 = mayor
            if (nota3 < nota2):
                mayor = nota2
                nota2 = nota3
                nota3 = mayor
            # con 3
            if (nota2 < nota1):
                mayor = nota1
                nota1 = nota2
                nota2 = mayor


            #Ya con los numeros ordenados

            #print("Las notas de: ",nota1,nota2,nota3,nota4,nota5,nota6,nota7,nota8,nota9,nota10," Los mayores son: ",nota8,nota9,nota10)
           # print("La frecuencia de las notas son: ", contador8, contador9, contador10)
            contadormax1 = 1
            contadormax2 = 1
            contadormax3 = 1
            max1=nota10
            max2=nota9
            max3=nota8

            if max1==nota9:
                contadormax1+=1
                max2=nota8
                max3=nota7
            if max1==nota8:
                contadormax1+=1
                max2=nota7
                max3=nota6
            if max1==nota7:
                contadormax1+=1
                max2 = nota6
                max3 = nota5
            if max1 == nota6:
                contadormax1 += 1
                max2 = nota5
                max3 = nota4
            if max1 == nota5:
                contadormax1 += 1
                max2 = nota4
                max3 = nota3
            if max1 == nota4:
                contadormax1 += 1
                max2 = nota3
                max3 = nota2
            if max1 == nota3:
                contadormax1 += 1
                max2 = nota2
                max3 = nota1
            if max1 == nota2:
                contadormax1 += 1
                max2 = nota1
                max3 = 0
            if max1 == nota1:
                contadormax1 += 1
                max2 = 0
                max3 = 0
            print(max2)
            if max2 == nota8:
                contadormax2 += 1
                max3 = nota7

            if max2 == nota7:
                contadormax2 += 1
                max3 = nota6

            if max2 == nota6:
                contadormax2 += 1
                max3 = nota5

            if max2 == nota5:
                contadormax2 += 1
                max3 = nota4

            if max2 == nota4:
                contadormax2 += 1
                max3 = nota3

            if max2 == nota3:
                contadormax2 += 1
                max3 = nota2

            if max2 == nota2:
                contadormax2 += 1
                max3 = nota1

            if max2 == nota1:
                contadormax2 += 1
                max3 = 0



            print("Los mayores son", max1,max2,max3," y sus frecuencias son ",contadormax1,contadormax2,contadormax3)


    elif opcion=="s":
        a="s"

