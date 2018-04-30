"""
Para un conjunto de n<=60 alumnos se desea almacenar por cada uno de ellos: código (entero de 3 dígitos) y la nota de 12 controles
Si el promedio de controles se calcula eliminando las 4 notas más bajas, presente el cuadro de mérito indicando:
código, las 12 notas (en el orden en que se tomaron) y el promedio

"""

#sea n=3
import random
codigoAlumnos=[]
notasAlumnos=[[],[],[]]

for i in range(0,3):
    codigoAlumnos.append(random.randint(100,999))

for i in range (0,3):
    for j in range(0,12):
        notasAlumnos[i].append(random.randint(0,20))

#eliminamos las mas bajas

for i in range(0,3):
    for j in range(0,12):
        menor = notasAlumnos[i][j]
        for z in range(0,12):
            if menor<notasAlumnos[i][z]:
                menor=notasAlumnos[i][z]
                notasAlumnos[i][z]=notasAlumnos[i][j]
                notasAlumnos[i][j]=menor

promedios=[]
suma=0
promedio=0
for i in range(0,3):
    suma=0
    for j in range(4,12):
        suma+=notasAlumnos[i][j]

    promedios.append(suma/8)

for i in range(0,3):
    print("El codigo del alumno es: ", codigoAlumnos[i]," sus notas: ",notasAlumnos[i]," y su promedio: ",promedios[i])
