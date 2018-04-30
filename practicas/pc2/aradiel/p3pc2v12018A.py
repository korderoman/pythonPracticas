"""
Juego de la Vida
Generar una matriz aleatoria nxm con ceros y unos en donde 1 representa un organismo vivo y 0 su desaparición.
Un ciclo de vida significa recorrer todas las celdas de la matriz con las siguientes reglas:

a) Si la celda contiene 0  y existe una o dos celdas con 1 en alguno de los cuatro lados, la celda cambia a 1.
b) Si la celda contiene 1 y existen tres o cuatro celdas con 1 en sus cuatro lados, su valor cambia a 0
c) En los otros casos, la celda no cambia de valor

Escriba un programa para simular k ciclos de vida. Muestre la cantidad de organismos vivos al inicio y luego de los k ciclos


"""
import random

filas=int(input("Indique el número de filas"))
columnas=int(input("Indique el número de columnas"))

matriz=[]

for i in range(0,filas):
    matriz.append([])
    for j in range(0,columnas):
        matriz[i].append(random.randint(0,1))

ciclos=0
findeJuego=False
contador=0
ciclos=0

while findeJuego==False:

    for i in range(0,filas):
        for j in range(0,columnas):
            if matriz[i][j]==0:
                # las esquinas
                if i==0 and j==0:
                    if matriz[i+1][j]==1 or matriz[i][j+1]==0:
                        matriz[i][j]=1
                elif i==filas-1 and j==columnas-1:
                    if matriz[i-1][j]==1 or matriz[i][j-1]==1:
                        matriz[i][j]=1
                elif i==0 and j==columnas-1:
                    if matriz[i][j-1]==1 or matriz[i+1][j]==1:
                        matriz[i][j]==1
                elif i==filas-1 and j ==0:
                    if matriz[i][j+1]==1 or matriz[i-1][j]==1:
                        matriz[i][j]==1
                #si está en un punto superior
                elif i==0 and j>0 and j<columnas-1:
                    if matriz[i][j-1]==1 or matriz[i][j+1]==1 or matriz[i+1][j]==1:
                        matriz[i][j]=1
                #si está en un punto inferior
                elif i==filas-1 and j>0 and j<columnas-1:
                    if matriz[i][j-1]==1 or matriz[i][j+1]==1 or matriz[i-1][j]==1:
                        matriz[i][j]=1
                #si está en un punto lateral izquierdo
                elif i>0 and j== 0 and i < filas - 1:
                    if matriz[i+1][j] == 1 or matriz[i][j + 1] == 1 or matriz[i -1 ][j] == 1:
                        matriz[i][j] = 1
                # si está en un punto lateral derecho
                elif i>0 and j ==columnas-1 and i < filas - 1:
                    if matriz[i+1][j] == 1 or matriz[i][j-1] == 1 or matriz[i - 1][j] == 1:
                        matriz[i][j] = 1
                #en cualquier otro punto
                elif i>0 and j>0 and j<columnas-1 and i<filas-1:
                    if matriz[i][j+1] == 1 or matriz[i][j - 1] == 1 or matriz[i - 1][j] == 1 or matriz[i+1][j]==1:
                        matriz[i][j] = 1
            elif matriz[i][j]==1:
                #parte superior
                if i == 0 and j > 0 and j < columnas - 1:
                    if matriz[i][j - 1] == 1 and matriz[i][j + 1] == 1 and matriz[i + 1][j] == 1:
                        matriz[i][j] = 0
                # si está en un punto inferior
                elif i == filas - 1 and j > 0 and j < columnas - 1:
                    if matriz[i][j - 1] == 1 and matriz[i][j + 1] == 1 and matriz[i - 1][j] == 1:
                        matriz[i][j] = 0
                        # si está en un punto lateral izquierdo
                elif i > 0 and j == 0 and i < filas - 1:
                    if matriz[i + 1][j] == 1 and matriz[i][j + 1] == 1 and matriz[i - 1][j] == 1:
                        matriz[i][j] = 0
                # si está en un punto lateral derecho
                elif i > 0 and j == columnas - 1 and i < filas - 1:
                    if matriz[i + 1][j] == 1 and matriz[i][j - 1] == 1 and matriz[i - 1][j] == 1:
                        matriz[i][j] = 0
                #en un punto cualquiera es una combinatoria de 4 en 3 tal que el punto puede mirar up,down,left,right
                elif i>0 and j>0 and j<columnas-1 and i<filas-1:
                    #los 4 son 1
                    if matriz[i][j + 1] == 1 and matriz[i][j - 1] == 1 and matriz[i - 1][j] == 1 and matriz[i + 1][j] == 1:
                        matriz[i][j]=0
                    elif matriz[i][j + 1] == 1 and matriz[i][j - 1] == 1 and matriz[i - 1][j] == 1:
                        matriz[i][j]=0
                    elif matriz[i+1][j] == 1 and matriz[i][j - 1] == 1 and matriz[i + 1][j] == 1:
                        matriz[i][j]=0
                    elif matriz[i][j + 1] == 1 and matriz[i+1][j] == 1 and matriz[i + 1][j] == 1:
                        matriz[i][j]=0
                    elif matriz[i][j + 1] == 1 and matriz[i][j - 1] == 1 and matriz[i + 1][j] == 1:
                        matriz[i][j]=0
    ciclos+=1
    for i in range(0,filas):
        for j in range(0,columnas):
            if matriz[i][j]==1:
                contador+=1
            else:
                contador=0
    if contador==9:
        findeJuego=True
    print("numero de ciclo",ciclos)
    print(matriz)



print(matriz)





"""
#Si la posicion es cero, existen varias condiciones, en especial en las esquinas
            if matriz[i][j]==0:
                if i-1<0 and j-1<0:
                    if matriz[i+1][j] == 1 or matriz[i][j+ 1] == 1:  # esquina superior izquierda
                        matriz[i][j] == 1
                elif i-1<0 and j+1>columnas:
                    if matriz[i+1][j] == 1 or matriz[i][j - 1] == 1:  # esquina superior derecha
                        matriz[i][j] == 1
                elif i-1>=0 and j-1<0 and i+1<columnas:
                    if matriz[i-1][j]==1 or matriz[i+1][j]==1 or matriz[i][j+1]==1:
                        matriz[i][j]=0
                
                elif i+1>filas and j-1<0:
                    if matriz[i - 1][j] == 1 or matriz[i][j+ 1] == 1:  # esquina inferior izquierda
                        matriz[i][j] == 1
                elif i+1>filas and j+1>columnas:
                    if matriz[i - 1][j] == 1 or matriz[i][j - 1] == 1:  # esquina inferior derecha
                        matriz[i][j] == 1
                elif i+1>filas and j-1>0 and j+1<columnas:
                    if matriz[i][j-1]==1 or matriz[i][j+1]==1 or matriz[i-1][j]==1:
                        matriz[i][j]==1
                elif  i-1>=0 and j-1>=0 and j<columnas and i<filas:
                    if matriz[i+1][j] == 1 or matriz[i - 1][j] == 1 or matriz[i][j+1] == 1 or matriz[i][j - 1] == 1:
                        matriz[i][j] = 1
                
            elif matriz[i][j]==1:
                if i-1>=0 and j-1<0:
                    if matriz[i][j] == 1 or matriz[i - 1][j] == 1 or matriz[i][j] == 1 or matriz[i][j - 1] == 1:
                        matriz[i][j] = 0
                elif  i-1>=0 and j-1>=0 and j<columnas and i<filas:
                    if matriz[i][j] == 1 or matriz[i - 1][j] == 1 or matriz[i][j] == 1 or matriz[i][j - 1] == 1:
                        matriz[i][j] = 0

"""