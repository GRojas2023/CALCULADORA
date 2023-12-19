from tkinter import *
#from _tkinter import ttk
#import match 


Ventana_Principal= Tk() # Declaracion de la Ventana principal
Ventana_Principal.title("Conversor de DOLAR $$")
Ventana_Principal.geometry("+400+90")


Dolar_Hoy = 950 #Prcio del dolar hoy
FECHA = "10/12/2023"

#cREACION DE TEXTO 1 Y CONFIGURACION
Texto1 = Label(Ventana_Principal, text= f"El precio del dolar hoy es {Dolar_Hoy} FECHA {FECHA}")   #Texto en la Ventana principal precio del dolar
Texto1.config(font=('Arial', 12))
Texto1.grid()


Ventana_Principal.mainloop()
