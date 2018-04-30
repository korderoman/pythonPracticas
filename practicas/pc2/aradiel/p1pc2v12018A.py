"""
Generar en forma aleatoria los elementos de una matriz cuadrada en rango de 10 a 50, los elementos de la matriz son
todos diferentes, se pide hallar A elevado a la n.

"""

#La idea inicial es crear una matriz que reciba todos esos datos, y los números aleatorios se hace a través de la
#librería random, esta matriz será una matriz de 3x3

import  random

matrizBruta=[]
matrizDepurada=[]
matrizBase=[[],[],[]]
while len(matrizDepurada)<9:
    valor=random.randint(10,50)
    matrizBruta.append(valor)
    #set elimina elementos duplicados
    #list devuelve el arreglo desordenado como una lista
    matrizDepurada=list(set(matrizBruta))


for i in range(0,3):
    for j in range(0,3):
        matrizBase[i].append(matrizDepurada[j+i*3])

#potencia

matrizPotencia=[]
for w in range(0,9):
    for i in range(0,3):
        for j in range(0,3):
            #un elemento de la matriz  (valor) almacena la multiplicacion de elemento fila y elemento columna
            valor+=matrizBase[i][j]*matrizBase[j][i]
    matrizPotencia.append(valor)
print(matrizBase)
print(matrizPotencia)

