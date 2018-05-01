"""
En el examen de admision a la UNi 2017-II se presentaron 800 postulantes, el examen tiene 20 preguntas, cada pregunta tiene 5 alternativas, las respuestas de las veinte preguntas se guardan en una lista y
 se generan en forma aleatoria. La pregunta buena bonifica con un punto, en blanco cero y mal contestada con -1. Un postulante ingresa si su nota es mayor o igual al promedipo general de todos los postulantes
 , se pide mostrar los 5 primeros puestos en caso de haber empate debe mostrar los postulantes con sus notas


"""
import random
notas=[]
#definimos que correcta es 1 incorrecta 2, y no respondida 0
respuestas=[]


for alumnos in range(0,800):
    #obtenemos sus respuestas
    respuestas.append([])
    for j in range(0,20):
        respuestas[alumnos].append(random.randint(0,2))

for alumnos in range(0,800):
    valor=0
    for j in respuestas[alumnos]:
        if respuestas[alumnos][j]==1:
            valor+=1
        elif respuestas[alumnos][j]==2:
            valor-=1
        elif respuestas[alumnos][j]==0:
            valor+=0
    if valor<0:
        valor=0

    notas.append(valor)

#obtenemos el promedio
suma=0
for i in range(0,800):
    suma+=notas[i]
promedio=suma/len(notas)
ingresantes=0
#cantidad de ingresantes
for i in range(0,800):
    if notas[i]>=promedio:
        ingresantes+=1
print(promedio)
print(ingresantes)
#obtenemos los 5 mejores puestos para ello podemos ordenarlo

for i in range(0,800):
    menor=0;
    for j in range(0,800):
        if notas[i]>notas[j]:
            menor=notas[j]
            notas[j]=notas[i]
            notas[i]=menor
print(notas)

for i in range(0,5):
     print("El puesto numero",i+1, "tiene nota de: ",notas[i])
