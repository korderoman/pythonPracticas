"""
La asociación el buen samaritano desea recabar fondos para la construcción de su local, para ello realiza una rifa
de 1000 tickets, el precio de cada ticket es S/. 5.00 nuevos soles. Para el primer premio se entrega  al sacar el tercer
ticket el segundo premio se entrega al sacar el segundo ticket. Se pide determinar lo sgte:
    los tickets vendido y su monto
    el ticket(s) ganador del primer y segundo premio y su posición de los tickets
"""
import  random

tickets=[]
ticketsCopia=[]
for i in range(0,1000):
    tickets.append(i+1)
ticketsCopia=tickets.copy()
print(len(ticketsCopia))
ticketsVendidos=1000;
total=ticketsVendidos*5
posicion1=0
posicion2=0
posicion3=0

posicion3Copia=0
posicion2Copia=0
posicion1Copia=0

for i in range(0,3):
    TercerPremio = random.randint(1, 1000)
for i in range(0,3):
    segundoPremio=random.randint(1,1000)
for i in range(0,3):
    primerPremio=random.randint(1,1000)

#obtenemos el tercer premio
for i in range(1,1000):
    if tickets[i]==TercerPremio:
        posicion3=i
        for j in range(0,1000):
            if ticketsCopia[j]==TercerPremio:
                posicion3Copia=j
# obtenemos el segundo premio, debemos de retirar el tercer premio
tickets.pop(posicion3)

for i in range(1,999):
    if(tickets[i]==segundoPremio and TercerPremio!=segundoPremio):
        posicion2=i
        for j in range(0,1000):
            if ticketsCopia[j]==segundoPremio:
                posicion2Copia=j
tickets.pop(posicion2)
#obtenemos el primer premio
for i in range(1,998):
    if tickets[i]==primerPremio and primerPremio!=segundoPremio and primerPremio!=TercerPremio:
        posicion1=i
        for j in range(0,1000):
            if(ticketsCopia[j]==primerPremio):
                posicion1Copia=j

print("EL ganador del primer premio es el ticket número: ",primerPremio," y su posicion es: ",posicion1Copia)
print("El ganador del segundo premio es el ticket número: ",segundoPremio, " y su posicion es: ",posicion2Copia)