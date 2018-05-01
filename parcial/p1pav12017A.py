"""
Dado dos matrices A de orden n*p y B de orden p*m cada funcion debe recibir como parámetros la matriz y número de filas y número de columnas, se pide:
a) Funcion de lectura de la matriz
b)Función de visualizar la matriz
c)Función para hallar A.B
d) función para ordenar la matriz resultado por columnas


"""
import random
matrizA=[]
matrizB=[]

p=int(input("Ingrese un valor 1"))
m=int(input("Ingrese un valor 2"))
n=int(input("Ingrese un valor 3"))

#una funcion en python se define como
def leerMatriz(filas,columnas,matriz):
    for i in range(0,filas):
        matriz.append([])
        for j in range (0,columnas):
            matriz[i].append(random.randint(1,5))
    return  matriz

def verMatriz(fila,columnas,matriz):
        return matriz[fila][columnas]

def multiplicar(matrizA,matrizB):
    matrizMultiplicada=[]
    valor=0
    for w in range(0, n):
        matrizMultiplicada.append([])
        for z in range(0,m):

            for i in range(0, n):
                for j in range(0, m):
                    # un elemento de la matriz  (valor) almacena la multiplicacion de elemento fila y elemento columna
                    valor += matrizA[i][j] * matrizB[j][i]
            matrizMultiplicada[w].append(valor)
    return matrizMultiplicada

def ordenarMatriz(matrizResultado):
    #no se entiende bien como es eso del resultado por columnas, entenderé que hay que ordenar cada columna
    for i in range(0,n):
        for j in range(0,m):
            print("no seXD")

leerMatriz(n,p,matrizA)
leerMatriz(p,m,matrizB)
matrizResultado=multiplicar(matrizA,matrizB)
ordenarMatriz(matrizResultado)

print(verMatriz(1,2,matrizB))

