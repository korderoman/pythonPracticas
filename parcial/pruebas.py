import random
num_alumno=[]
notas=[]
x=0
for i in range (0,10):
    x+=1
    num_alumno.append(x)
    print("el alumno numero ", num_alumno[i])
    notas.append([])
    for j in range (0,4):
        nota=random.randint(0,20)
        notas[i].append(nota)
        #print("tiene las siguientes notas: ", notas[j])


print(notas)