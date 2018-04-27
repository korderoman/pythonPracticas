


matriz=[]

filas=int(input("Ingrese el numero de filas"))
columnas=int(input("Ingrese el número de columnas"))

"""
for i in range(0,filas):
    matriz2=[]
    matriz.append(matriz2)
    for j in range(0,columnas):
        valor=int(input("INgrese un numero"))
        matriz2.append(valor)


"""
for i in range(0,filas):
    for j in range(0,columnas):
        matriz[i][j]=int(input("Ingrese un valor"))

print(matriz)





