from  tkinter import *

root=Tk()

miFrame=Frame(root,width=500,height=400)



#una etiqueta requiere que se le diga el padre
miLabel=Label(miFrame,text="Hola Mundo de python",fg="red",font=("comic Sans MS",18)) #fg color de texto
miLabel.place(x=100,y=200) #podriamos usar pack, pero sobreescribe las dimensiones del frame, para ello mejor usamor un place
#forma abreviada o anónima
Label(miFrame,text="Hola Mundo de nuevo").place(x=100,y=50)
#creamos una imagen
miImagen=PhotoImage(file="hongo.png")
Label(miFrame,image=miImagen).place(x=25,y=100)

miFrame.pack()
root.mainloop()