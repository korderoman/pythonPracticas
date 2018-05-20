edad=7

#esto nos evita estar usando el and, la condicion se lee de izquierda a derecha
#siempre y cuando sean en la misma condicion
if 0<edad<100:
    print("Edad es correcta")
else:
    print("Edad incorrecta")


"""
El operador in nos permite evaluar varias condiciones, se listan entre paréntesis o se puede incluir una lista

"""

print("Asignaturas Optativas Año 2017")
print("Informática gráfica - Pruebas de Software - Usabilidad y Accesibilidad")
asignatura=input("Escribe la Asignatura escogida")

if asignatura in ("Informática Gráfica","Pruebas de Software","Usabilidad y accesibilidad"):
    print("Aisgnatura elegida" + asignatura)
else:
    print("No existe esa asignatura")
