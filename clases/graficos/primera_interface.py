from  tkinter import *

raiz=Tk()

#Podemos guardar nuestro archivo como pyw. para que se ejecute sin lanzar la consola de python

#una ventana en ejecución debe de estar en un bucle infinito
raiz.title("Ventana de pruebas")
raiz.resizable(1,0) #no redimensionable 0=false, 1=true
raiz.iconbitmap("hongo.ico") #cambiar el logo de la ventana
raiz.geometry("650x650") #medidas de la ventana
raiz.config(bg="blue") #Color de fondo de la ventana
raiz.mainloop() #siempre va al final
