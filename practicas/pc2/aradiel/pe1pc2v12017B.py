"""
Escriba un programa que coloca números aleatorios de un cifra de una cifra en los cuatro bordes de una matríz.
Después rellene los elementos del interior de la matriz, con números aleatorios, de una cifra, tales que cada
uno sea menor o igual al promedio de todos los elementos de los bordes.
Al inicio no interesan los valores que se asignan los elemento interiores, pues serán sustituidos.
"""
import  random
matriz=[]
filas=int(input("Ingrese el número de filas"))
columnas=int(input("Ingrese el número de columnas:"))
suma=0
promedio=0
for i in range(0,filas):
    matriz.append([])
    for j in range(0,columnas):
        if i==0 or i==filas-1 or j==0 or j==columnas-1:
            valor=random.randint(1,9)
            suma+=valor
            matriz[i].append(valor)

        else:
            matriz[i].append(0)

promedio=suma/(filas*columnas)
print(promedio)
promedio=round(promedio)

for i in range(0,filas):
    for j in range(0,columnas):
        if(matriz[i][j]==0):
            matriz[i][j]=random.randint(0,promedio)

#print(matriz[0][1])
print(matriz)




