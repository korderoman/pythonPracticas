"""
Leer una serie de caracteres, hasta encontrar un *, se pide mostrar la frecuencia de cada una de las consonantes minúsculas
"""

seguimos="-"
valor=0
letras=["b","c","d","f","g","h","j","k","m","n","ñ","p","q","r","s","t","v","w","x","y","z"]
contadores=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
while seguimos!="*":
    letra=input("Ingrese una letra por favor")
    if letra=="b":
        contadores[0]+=1
    elif letra=="c":
        contadores[1]+=1
    elif letra=="d":
        contadores[2]+=1
    elif letra=="f":
        contadores[3]+=1
    elif letra=="g":
        contadores[4]+=1
    elif letra=="h":
        contadores[5]+=1
    elif letra=="j":
        contadores[6]+=1
    elif letra=="k":
        contadores[7]+=1
    elif letra=="m":
        contadores[8]+=1
    elif letra=="n":
        contadores[9]+=1
    elif letra=="ñ":
        contadores[10]+=1
    elif letra=="p":
        contadores[11]+=1
    elif letra=="q":
        contadores[12]+=1
    elif letra=="r":
        contadores[13]+=1
    elif letra=="s":
        contadores[14]+=1
    elif letra=="t":
        contadores[15]+=1
    elif letra=="v":
        contadores[16]+=1
    elif letra=="w":
        contadores[17]+=1
    elif letra=="x":
        contadores[18]+=1
    elif letra=="y":
        contadores[19]+=1
    elif letra=="z":
        contadores[20]+=1
    elif letra=="*":
        seguimos="*"

for i in range(len(letras)):
    print("La letra ",letras[i], "tiene una frecuencia de: ",contadores[i])