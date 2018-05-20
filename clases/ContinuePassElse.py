"""
La instruccion continue saltar a la siguiente iteracion de bucle si etsamos en nu ubcle que debe dar 10 vueltas
pero en la vueta 5 lee esta instruccion, obvia esta linea y salta a la 6ta, se usa mucho en la definición de clases
El pass se usa para las clases
"""

for letra in "python":
    if letra=="h":#al detectar la h saltará y no será impresa
        continue
    print(letra)



#instruccion pass que devuelve un null

class Miclase:
    pass #deja el traajo a medias

