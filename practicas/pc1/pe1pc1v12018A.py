from random import randint

par1x=randint(0,10)
par1y=randint(0,10)

par2x=randint(0,10)
par2y=randint(0,10)

par3x=randint(0,10)
par3y=randint(0,10)


parbuscadox=randint(0,10)
parbuscadoy=randint(0,10)


primerx=par1x
segundox=par2x
tercerx=par3x

primery=par1y
segundoy=par2y
tercery=par3y

menorx=primerx
#el primer menor
if menorx>segundox:
    menorx=segundox
    segundox=primerx
    primerx=menorx
if menorx>tercerx:
    menorx=tercerx
    tercerx=primerx
    primerx=menorx
#el segundo menor

menorx=segundox
if menorx>tercerx:
    menorx=tercerx
    tercerx=segundox
    segundox=menorx


menory=primery
#el primer menor
if menory>segundoy:
    menory=segundoy
    segundoy=primery
    primery=menory
if menory>tercery:
    menory=tercery
    tercery=primery
    primery=menory
#el segundo menor

menory=segundox
if menory>tercery:
    menory=tercery
    tercery=segundoy
    segundoy=menory


#Para asegurar que está dentro debe cumplirse que
print("las coordenadas: ",par1x,par1y,par2x,par2y,par3x,par3y)
print("El buscado: ",parbuscadox,parbuscadoy)

if parbuscadox>=primerx and parbuscadox<=tercerx:
    if parbuscadoy>=primery and parbuscadoy<=tercery:
        print("Está dentro")
    else:
        print("No está dentro")
else:
    print("No está dentro")

