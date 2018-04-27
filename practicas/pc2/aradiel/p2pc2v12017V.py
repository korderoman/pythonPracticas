"""
Leer una serie de caracteres, por cada caracter leído formar una esperial, la esprial debe estar formada por las vocalores
minúsculas, la serie termina cuando ingresa un punto, indicar las frecuencias de cada vocal


"""

continuar=True
espiral=[]
conta=0
conte=0
conti=0
conto=0
contu=0
while continuar==True:
    letra=input("Ingrese una letra")
    if(letra=="a" or letra=="e" or letra=="i" or letra=="o" or letra=="u"):
        espiral.append(letra)
        if letra=="a":
            conta+=1
        if letra=="e":
            conte+=1
        if letra=="i":
            conti+=1
        if letra=="o":
            conto+=1
        if letra=="u":
            contu+=1
    elif letra==".":
        continuar=False

print("La espiral es: ",espiral)
print("Las frecuencias son de a,e,i,o,u respectivamente", conta,conte,conti,conto,contu)