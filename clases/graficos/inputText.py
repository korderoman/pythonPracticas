from  tkinter import *

root=Tk()

miFrame=Frame(root,width=550,height=400)
#orientacion en derecha=e, izquierda=w, arriba=n, sur=s
nombreLabel=Label(miFrame,text="Nombre")
nombreLabel.grid(row=0,column=0,sticky="e",padx=15, pady=10)
cuadroNombre=Entry(miFrame)
cuadroNombre.grid(row=0, column=1)#usaremos grid para posicionar los objetos
cuadroNombre.config(fg="red",justify="center")

passLabel=Label(miFrame,text="Clave")
passLabel.grid(row=3,column=0,padx=15,pady=10)
cuadroPass=Entry(miFrame)
cuadroPass.grid(row=3,column=1,padx=10,pady=10)
cuadroPass.config(show="*") #recuerda que config edita color, etc


apellidoLabel=Label(miFrame,text="Apellido")
apellidoLabel.grid(row=1,column=0,sticky="e",padx=15, pady=10)
cuadroApellido=Entry(miFrame)
cuadroApellido.grid(row=1, column=1)#usaremos grid para posicionar los objetos


direccionLabel=Label(miFrame,text="Direccion")
direccionLabel.grid(row=2,column=0,sticky="e",padx=15, pady=10)
cuadroDireccion=Entry(miFrame)
cuadroDireccion.grid(row=2,column=1)

miFrame.pack()
root.mainloop()