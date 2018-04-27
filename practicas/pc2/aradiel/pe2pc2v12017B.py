"""Para el partido Peru-Colombia la Federación Peruana a dispuesto la venta una cierta cantidad de boletos disponibles
(Norte y Sur, Oriente y Occidente) cuyos precios son (59,190,290). Escriba un programa para organizar las ventas en línea
cada persona debe presentar su dni , el programa debe de leer y agregar a un vector el dni.
En caso que el DNI exista el programa debe enviar un mensaje, muestre un mensaje rechazando la venta de boletos.
Si la venta se realiza lea la cantidad de boletos que se compra (no debe ser mayor de 4), tipo de boleto, cuando la
cantidad llegue a cero muestre yb nebsaje por cada categoría y finalice el programa, el programa debe de mostrar la cantidad
de boletos vendidos, no vendidos por cada categoría, su monto y el monto total general.
"""
import random

bnorte=random.randint(1,10)
bsur=random.randint(1,10)
boccidente=random.randint(1,10)
boriente=random.randint(1,10)

continuar=True
pnorte=59
psur=59
poriente=190
poccidente=290

listaDni=[]
listaDni.append(11111111)
while continuar:
    dni=int(input("Ingrese su dni"))
    for i in range(0,len(listaDni)):
        if listaDni[i]!=dni:
            listaDni.append(dni)
            locacion=input("Elija su locacion: (no)rte,(su)r,(or)iente,(oc)cidente")
            cantidad=int(input("Indique la cantidad"))
            while cantidad>4:
                cantidad=int(input("Indique una cantidad no mayor de 4"))
            if bnorte!=0 and bsur!=0 and boriente!=0 and boccidente!=0:
                if locacion=="no":
                    if bnorte>=cantidad and bnorte!=0:
                        bnorte-=cantidad
                    elif bnorte<cantidad and bnorte!=0:
                         resta=cantidad-bnorte
                         print("Queda solo", resta," boletos")
                    elif bnorte==0:
                            print("No nos quedan boletos")
                            continuar=False
            else:

                #elif locacion=="su":
                #elif locacion == "or":
                #elif locacion == "oc":
        else:
            print("Usted ya no puede comprar más boletos")


