from tkinter import *


raiz=Tk()
raiz.title("ventana de pruebas")
raiz.iconbitmap("hongo.ico")
raiz.config(bg="blue")  #la raiz es de color azul
#Hacemos un frame

miFrame=Frame()
#empaquetamos el fram
miFrame.pack(side="right", anchor="w")#side=left,tp,bottom, podemos usar anchor con las opciones =n:North, s=South,e=East,w=West
miFrame.config(bg="red") #el frame es de color rojo
#esta diferencia de color, se percibe cuando reimensionamos la ventana raiz.
miFrame.config(width="650",height="350")
miFrame.pack(fill="y", expand="True") # solo se expande de forma vertical, si queremos en los dos lados es both en lugar de y
miFrame.config(bd=35)#modificamos la medida
miFrame.config(relief="groove")#cambiar al borde, sunken

miFrame.config(cursor="pirate")#se modifica la forma del cursos (hand2 , pirate

raiz.mainloop()