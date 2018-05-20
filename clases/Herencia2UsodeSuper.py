class Persona():

    def __init__(self,nombre,edad,lugar_residencia):
        self.nombre=nombre
        self.edad=edad
        self.lugar_residencia=lugar_residencia

    def descripcion(self):
        print("Nombre: ",self.nombre," Edad: ",self.edad," Lugar de residencia: ",self.lugar_residencia)




class Empleado(Persona):
    def __init__(self,salario,antiguedad, nombre_empleado,edad_empleado,residencia_empleado):
        #llamamos al constructor de la clase padre
        super().__init__(nombre_empleado,edad_empleado,residencia_empleado)
        self.salario=salario
        self.antiguedad=antiguedad
    #un empleado es una persona
    def descripcion(self):
        super().descripcion()#con esto llamamos al metodo del padre
        print("Salario: ",self.salario,"Antiguedad: ",self.antiguedad)

Antonio=Persona("Antonio",55,"España")
Antonio.descripcion()

#ahora hacemos un empleado
#Si hacemos Emily.descripcion nos manda error su usamos Emily=Empleado(1500,15), para ello debemo de agregar super
#en el constructor

Emily=Empleado(1500,15,"Emily",31,"Perú")
Emily.descripcion()

#en python existe la funcion isInstance equivalente a typeof, con ello podemos saber el tipo de la instancia

print(isinstance(Emily,Persona))
print(isinstance(Emily,Empleado))