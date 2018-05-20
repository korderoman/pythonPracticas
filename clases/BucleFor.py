"""
i recorrera la longitud de la lista, y asumirá los valores que estén dentro de ella

"""

for i in ["Verano","Otoño","Invierno","Primavera"]:
    print("Nuestra estacion es: ", i)

#podemos revisar una palabra
email=False
for i in "elpadredelcordero@gmail.com":
    if i=="@":
        email=True


if email==True:
    print("Correo correcto")
else:
    print("No es correcto")



for u in range(5,10,1): #desde donde, hasta donde, y de cuanto en cuanto
    print(f"valor de la variable {i}") #concatena
