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


#primero hacemos el menu global, para ello definimos una variable global de tipo string de salida

salida="ns"

while salida!="s":
    print("########################################")
    print("MENU DE OPCIONES")
    print("(o)rdenar 5 números")
    print("(f)recuencia de notas")
    print("(s)alir")

    opcion=input("Ingrese una opción")
    # Ahora definimos en caso de ser cierto la opción de salida
    if(opcion=="s"):
        print("Usted está saliendo del sistema")
        salida="s"
    #Ahora definimos el caso de hallar el mayo de 5 números
    elif(opcion=="o"):
        n1=int(input("Ingrese el primer número"))
        n2=int(input("Ingrese el segundo número"))
        n3=int(input("Ingrese el tercer número"))
        n4=int(input("Ingrese el cuarto número"))
        n5=int(input("Ingrese el quinto número"))

        #definimos una variable menor y asignamos arbitrariamente un valor
        menor=n1
        #Ahora comparamos la variable con todas las demas, si en caso la variable a comparar resultar menor que "menor
        #entonces esta será el nuevo valor de menor, pero tambien debemos de intercambiar los valores  para cambiar las
        #posiciones

        if menor>n2:
            menor=n2
            n2=n1
            n1=menor
        if menor>n3:
            menor=n3
            n3=n1
            n1=menor
        if menor>n4:
            menor=n4
            n4=n1
            n1=menor
        if menor>n5:
            menor=n5
            n5=n1
            n1=menor
        #Hasta el momento el valor que hemos obtenido es que en la posicion n1 se almacena el menor, ahora el segundo menor
        # se hará comparando n2 con n3,n4,n5, luego n3 con n4 y n5, finalmente n4 con n5

        menor=n2
        if menor>n3:
            menor=n3
            n3=n2
            n2=menor
        if menor>n4:
            menor=n4
            n4=n2
            n2=menor
        if menor>n5:
            menor=n5
            n5=n2
            n2=menor
        #Acabamos de hallar el segundo menor

        menor=n3
        if menor>n4:
            menor=n4
            n4=n3
            n3=menor
        if menor>n5:
            menor=n5
            n5=n3
            n3=menor

        #Ahora con 4
            menor=n4
        if menor>n5:
            menor=n5
            n5=n4
            n4=menor

        print("Los números en forma ascendente son: ",n1,n2,n3,n4,n5)

    elif opcion=="f":
        #procedemos a ordenar los notas, para ello sabemos que las notas pueden ser del 1 al 20, entonces establecemos
        #veinte notas y contabilizamos cuantas notas hay de ellas
        cont20=0 ; cont19 = 0; cont18 = 0;cont17 = 0;cont16 = 0;cont15 = 0;cont14 = 0; cont13 = 0; cont12 = 0
        cont11 = 0; cont10 = 0; cont9 = 0; cont8 = 0; cont7 = 0; cont6 = 0; cont5 = 0; cont4 = 0; cont3 = 0
        cont2 = 0; cont1 = 0;cont0=0

        #La cantidad de alumnos mostrará la cantidad de veces del while
        cantiAlumnos=int(input("Ingrese la cantidad de alumnos"))
        i=1 #el contador de alumnos ya que al menos existirá un alumnos, sino no tiene sentido la opcion
        while i<cantiAlumnos:
            print("Ingrese la nota del alumno: ",i)
            nota=int(input())

            if(nota==20):
                cont20+=1
            if (nota == 19):
                cont19 += 1
            if (nota == 18):
                cont18 += 1
            if (nota == 17):
                cont17 += 1
            if (nota == 16):
                cont16 += 1
            if (nota == 15):
                cont15 += 1
            if (nota == 14):
                cont14 += 1
            if (nota == 13):
                cont13 += 1
            if (nota == 12):
                cont12 += 1
            if (nota == 11):
                cont11 += 1
            if (nota == 10):
                cont10 += 1
            if (nota == 9):
                cont9 += 1
            if (nota == 8):
                cont8 += 1
            if (nota == 7):
                cont7 += 1
            if (nota == 6):
                cont6 += 1
            if (nota == 5):
                cont5 += 1
            if (nota == 4):
                cont4 += 1
            if (nota == 3):
                cont3 += 1
            if (nota == 2):
                cont2 += 1
            if (nota == 1 ):
                cont1 += 1
            if(nota==0):
                cont0+=1
            i+=1
        #hacemos unas posiciones y sus valores
        pos0=0;pos1=1;pos2=2;pos3=3;pos4=4;pos5=5;pos6=6;pos7=7;pos8=8;pos9=9;pos10=10;pos11=11;pos12=12;pos13=13
        pos14=14;pos15=15;pos16=16;pos17=17;pos18=18;pos19=19;pos20=20

        #definimos 3 mayores, recordar que nos piden los 3 mayores
        mayor1=0; mayor2=0;mayor3=0
        primero=0;segundo=0;tercero=0
        #Los cuales iremos hallando sucesivamente en función de sus contadores, es decir, cont20!=0 entonces se
        #se supone que hay un valor de 20
        if cont20>0:
            mayor1=cont20
            primero=pos20
        elif cont19 > 0:
            mayor1 = cont19
            primero = pos19
        elif cont18 > 0:
            mayor1 = cont18
            primero = pos18
        elif cont17 > 0:
            mayor1 = cont17
            primero = pos17
        elif cont16 > 0:
            mayor1 = cont16
            primero = pos16
        elif cont15 > 0:
            mayor1 = cont15
            primero = pos15
        elif cont14 > 0:
            mayor1 = cont14
            primero = pos14
        elif cont13 > 0:
            mayor1 = cont13
            primero = pos13
        elif cont12 > 0:
            mayor1 = cont12
            primero = pos12
        elif cont11 > 0:
            mayor1 = cont11
            primero = pos11
        elif cont10 > 0:
            mayor1 = cont10
            primero = pos10
        elif cont9 > 0:
            mayor1 = cont9
            primero = pos9
        elif cont8 > 0:
            mayor1 = cont8
            primero = pos8
        elif cont7 > 0:
            mayor1 = cont7
            primero = pos7
        elif cont6 > 0:
            mayor1 = cont6
            primero = pos6
        elif cont5 > 0:
            mayor1 = cont5
            primero = pos5
        elif cont4 > 0:
            mayor1 = cont4
            primero = pos4
        elif cont3 > 0:
            mayor1 = cont3
            primero = pos3
        elif cont2 > 0:
            mayor1 = cont2
            primero = pos2
        elif cont1 > 0:
            mayor1 = cont1
            primero = pos1

        elif cont0>0:
            mayor1=cont0
            primero = pos0
        #Aquí hallamos el segundo mayor

        if cont19 and pos19!=primero > 0:
            mayor2 = cont19
            segundo = pos19
        elif cont18 > 0 and pos18!=primero:
            mayor2 = cont18
            segundo = pos18
        elif cont17 >0 and pos17!=primero:
            mayor2 = cont17
            segundo = pos17
        elif cont16 > 0 and pos16!=primero:
            mayor2 = cont16
            segundo = pos16
        elif cont15 > 0 and pos15!=primero:
            mayor2 = cont15
            segundo = pos15
        elif cont14 > 0 and pos14!=primero:
            mayor2 = cont14
            segundo = pos14
        elif cont13 > 0 and pos13!=primero:
            mayor2 = cont13
            segundo = pos13
        elif cont12 > 0 and pos12!=primero:
            mayor2 = cont12
            segundo = pos12
        elif cont11 > 0 and pos11!=primero:
            mayor2 = cont11
            segundo = pos11
        elif cont10 > 0 and pos10!=primero:
            mayor2 = cont10
            segundo = pos10
        elif cont9 > 0 and pos9!=primero:
            mayor2 = cont9
            segundo = pos9
        elif cont8 > 0 and pos8!=primero:
            mayor2 = cont8
            segundo = pos8
        elif cont7 > 0 and pos7!=primero:
            mayor2 = cont7
            segundo = pos7
        elif cont6 > 0 and pos6!=primero:
            mayor2 = cont6
            segundo = pos6
        elif cont5 > 0 and pos5!=primero:
            mayor2 = cont5
            segundo = pos5
        elif cont4 > 0 and pos4!=primero:
            mayor2 = cont4
            segundo = pos4
        elif cont3 > 0 and pos3!=primero:
            mayor2 = cont3
            segundo = pos3
        elif cont2 > 0 and pos2!=primero:
            mayor2 = cont2
            segundo = pos2
        elif cont1 > 0 and pos1!=primero:
            mayor2 = cont1
            segundo = pos1
        elif cont0 > 0 and pos0!=primero:
            mayor2 = cont0
            segundo = pos0

        #Hallamos el tercer mayor

        if cont18>0 and pos18!=primero and pos18!=segundo:
            mayor3=cont18
            tercero=pos18
        elif cont17>0 and pos17!=primero and pos17!=segundo:
            mayor3 = cont17
            tercero = pos17
        elif cont16>0 and pos16!=primero and pos16!=segundo:
            mayor3 = cont16
            tercero = pos16
        elif cont15>0 and pos15!=primero and pos15!=segundo:
            mayor3 = cont15
            tercero = pos15
        elif cont14>0 and pos14!=primero and pos14!=segundo:
            mayor3 = cont14
            tercero = pos14
        elif cont13>0 and pos13!=primero and pos13!=segundo:
            mayor3 = cont13
            tercero = pos13
        elif cont12>0 and pos12!=primero and pos12!=segundo:
            mayor3 = cont12
            tercero = pos12
        elif cont11>0 and pos11!=primero and pos11!=segundo:
            mayor3 = cont11
            tercero = pos11
        elif cont10>0 and pos10!=primero and pos10!=segundo:
            mayor3 = cont10
            tercero = pos10
        elif cont9>0 and pos9!=primero and pos9!=segundo:
            mayor3 = cont9
            tercero = pos9
        elif cont8>0 and pos8!=primero and pos8!=segundo:
            mayor3 = cont8
            tercero = pos8
        elif cont7>0 and pos7!=primero and pos7!=segundo:
            mayor3 = cont7
            tercero = pos7
        elif cont6>0 and pos6!=primero and pos6!=segundo:
            mayor3 = cont6
            tercero = pos6
        elif cont5>0 and pos5!=primero and pos5!=segundo:
            mayor3 = cont5
            tercero = pos5
        elif cont4>0 and pos4!=primero and pos4!=segundo:
            mayor3 = cont4
            tercero = pos4
        elif cont3>0 and pos3!=primero and pos3!=segundo:
            mayor3 = cont3
            tercero = pos3
        elif cont2>0 and pos2!=primero and pos2!=segundo:
            mayor3 = cont2
            tercero = pos2
        elif cont1>0 and pos1!=primero and pos1!=segundo:
            mayor3 = cont1
            tercero = pos1
        elif cont0>0 and pos0!=primero and pos0!=segundo:
            mayor3 = cont0
            tercero = pos0


        print("La mayores notas son:",primero,segundo,tercero," ya la frecuencia es: ",mayor1,mayor2,mayor3)





