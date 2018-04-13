"""
Diseñar un programa que permita validar datos de 3 usuarios por código (100,22,300) y clave (111,222,333). Si el
usuario ingresa correctamente los datos el sistema entonces le permite procesar la prueba  de entrada LP_2018 que
rindieron n estudiantes, diseñar un programa que permita leer por cada estudiante, su código (número de 3 cifras) y su
nota (entre 0-20) y luego hacer un reporte para conocer:

A) un número Cod; formado por la secuencia del codigi
B)Un número de de Nots: formado por la secuencia de notas y
C) Otro número sec: formador por el número de dígitos de cada nota


"""
codProfesores=[100,22,300]
claveProfesores=[111,222,333]

ingresarDatos=False
codDocente=0
claveDocente=0

while ingresarDatos!=True:
    codDocente=int(input("Ingrese su código de docente"))
    claveDocente=int(input("Ingrese su clave "))

    for i in range(3):
        if codProfesores[i]==codDocente:
            if claveProfesores[i]==claveDocente:
                print("Bienvenido profesor")
                ingresarDatos=True

    if ingresarDatos==False:
        print("Clave o usuario incorrecto")


n=int(input("Ingrese la cantidad de estudiantes"))

notaAlumnos=[]
codigoAlumnos=[]
for i in range(n):
    codigo=input("Ingrese el codigo del alumno ")
    nota=input("Ingrese la nota del alumno ")
    codigoAlumnos.append(codigo)
    notaAlumnos.append(nota)
Cod=""
Nots=""
Sec=""


for i in range(n):
    Cod+=codigoAlumnos[i]
    Nots+=notaAlumnos[i]+" "
    digitos=str(len(notaAlumnos[i]))
    Sec+=digitos

print(Cod)
print(Nots)
print(Sec)



