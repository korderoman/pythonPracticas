"""
Diseñar un programa que permita leer un número n entero positivo, donde su número de cifras, sea mayor o igual
a tres (validar; debe ser positivo y tenga tres o más cifras). Luego el programa debe modificar n en dos números Num_a y
Num_b, donde:

1. Numa: este formado solo por cifras pares y ordenadas en forma ascendente
2. Secuencia formado por indices
3. Num_b este formado por cifras impares e indicar sus posiciones respectivas.

"""

esValido=False
numero=0
Num_a=[]
Num_b=""
while esValido!=True:
    valor=int(input("Ingrese un número"))
    if valor>99:
        esValido=True
        numero=valor
    else:print("No es un número válido")

numero=str(numero)
posicionesPares=[]
for i in range(len(numero)):
    x= int(numero[i])
    if(x%2==0):
        Num_a.append(x)
        pos=i+1
        posicionesPares.append(pos)
        #Num_a+=str(x)
    else:
       Num_b+=str(x)

Num_a.sort();
numApalabra=""
numPosiciones=""
for i in range(len(Num_a)):
    numApalabra+=str(Num_a[i])
    numPosiciones+=str(posicionesPares[i])
print(numApalabra)
print(numPosiciones)
print(Num_b)