

punto=","
palabra=""
palabraLen=""
p1=""
p2=""
p3=""
p4=""
p5=""
p6=""
p7=""
p8=""
cont1=0
cont2=0
cont3=0
cont4=0
cont5=0
cont6=0
cont7=0
cont8=0

contLen=0
letral=""
letrae=""
letran=""


while punto!=".":
    letra=input("Ingrese una letra")
    interruptor="z"
    palabra+=letra


    if letra == "l":
        p1 = letra
        letral=letra
        interruptor=""
        cont1+=1
    elif letra == "e" and p2=="":
        p2 = letra
        letrae=letra
        interruptor=""
        cont2+=1
    elif letra == "n":
        p3 = letra
        letran=letra
        interruptor=""
        cont3+=1
    elif letra == "g":
        p4 = letra
        cont4+=1
    elif letra == "u":
        p5 = letra
        cont5+=1
    elif letra == "a":
        p6 = letra
        cont6+=1
    elif letra == "j":
        p7 = letra
        cont7+=1
    elif p2!="" and letra=="e":
        p8 = letra
        cont2+=1
        interruptor=""
        letrae=letra

    palabraLen = "" + letral + interruptor + letrae + letran
    if interruptor != "":
        letral = ""
        letrae = ""
        letran = ""
    print(palabraLen)
    if p1!="" and p7=="":
        palabra = "" + p1 + p2 + p3 + p4 + p5 + p6 + p7
    elif p7!="":
        palabra=""+ p1 + p2 + p3 + p4 + p5 + p6 + p7+p8
    print(palabra)


    if palabraLen=="len":
        contLen+=1

    if palabra=="lenguaje":
        print("La cantidad de veces que aparece la letra: l,e,n,g,u,a,j es:",cont1,cont2,cont3,cont4,cont5,cont6,cont7," respectivamente")
        print("La cantidad de veces que aparece la secuencia len es: ", contLen)
        punto="."



