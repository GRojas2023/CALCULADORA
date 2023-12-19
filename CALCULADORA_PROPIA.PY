from tkinter import *
from tkinter import ttk
import math 

#colocar caracteres en pantalla
def INGRESAR_VALORES(tecla): 
    if tecla >= "0" and tecla <="9" or tecla == "(" or tecla == ")" or tecla == ".":
        TEXTO_2.set(TEXTO_2.get() + tecla)
    
    if tecla == "*" or tecla == "/" or tecla == "+" or tecla == "-":
        if tecla == "*":
            TEXTO_1.set(TEXTO_2.get() + "*")
        elif tecla == "/":
            TEXTO_1.set(TEXTO_2.get() + "/")
        elif tecla == "+":
            TEXTO_1.set(TEXTO_2.get() + "+")
        elif tecla == "-":
            TEXTO_1.set(TEXTO_2.get() + "-")
        TEXTO_2.set("")

    if tecla == "=":
        TEXTO_1.set(TEXTO_1.get() + TEXTO_2.get())
        resultado = eval(TEXTO_1.get())
        TEXTO_2.set(resultado)

#calcular raiz cuadrada de lo que esta en texto_2
def raiz_cuadrada():
    TEXTO_1.set("")
    resultado = math.sqrt(float(TEXTO_2.get()))
    TEXTO_2.set(resultado)


VENTANA_PRINCIPAL = Tk()
VENTANA_PRINCIPAL.title("Calculador IITA")
VENTANA_PRINCIPAL.geometry("+500+80")
VENTANA_PRINCIPAL.columnconfigure(0, weight=1)#HACER QUE LA COLUMNA ABARQUE LA PNTALLA RECORDA USAR STICKY
VENTANA_PRINCIPAL.rowconfigure(0, weight=1)#HACER QUE LA CELDA ABARQUE LA PNTALLA RECORDA USAR STICKY

#ESTILOS DEL MARCO PRINCIPAL
estilos = ttk.Style()
estilos.theme_use('clam')
estilos.configure('MARCO_PRINCIPAL.TFrame', background = "#DBDBDB")


# CONSTRUCCION DEL MARCO PRINCIPAL CON SU UBICACION
MARCO_PRINCIPAL = ttk.Frame(VENTANA_PRINCIPAL, style="MARCO_PRINCIPAL.TFrame")
MARCO_PRINCIPAL.grid(row= 0, column=0 , sticky= (W, N, E, S)) #ANCLAR A LOS LADOS A LA CALCULADORA
#VOLVER A TODAS LAS COLUMNAS ADAPTABLES A LA PANTALLA
MARCO_PRINCIPAL.columnconfigure(0, weight=1)
MARCO_PRINCIPAL.columnconfigure(1, weight=1)
MARCO_PRINCIPAL.columnconfigure(2, weight=1)
MARCO_PRINCIPAL.columnconfigure(3, weight=1)
#VOLVER A TODAS LAS CELDAS ADAPTABLES A LA PANTALLA
MARCO_PRINCIPAL.rowconfigure(0, weight=1)
MARCO_PRINCIPAL.rowconfigure(1, weight=1)
MARCO_PRINCIPAL.rowconfigure(2, weight=1)
MARCO_PRINCIPAL.rowconfigure(3, weight=1)
MARCO_PRINCIPAL.rowconfigure(4, weight=1)
MARCO_PRINCIPAL.rowconfigure(5, weight=1)
MARCO_PRINCIPAL.rowconfigure(6, weight=1)
MARCO_PRINCIPAL.rowconfigure(7, weight=1)

#ESTILO DE LOS LABEL O SEA LA ESCRITURA DE PANTALLA TEXTO 1
estilos_TEXTO1 = ttk.Style()
estilos_TEXTO1.configure("TEXTO1.TLabel", font = "arial 15", anchor = "e")

### CREACION Y POSICION DEL TEXTO 1
TEXTO_1 = StringVar()
TEXTO_1_1 = ttk.Label(MARCO_PRINCIPAL,textvariable= TEXTO_1, style= "TEXTO1.TLabel")
TEXTO_1_1.grid(row=0 ,column=0, columnspan=4, sticky= (W, N, E, S))


#ESTILO DE LOS LABEL O SEA LA ESCRITURA DE PANTALLA TEXTO 2
estilos_TEXTO2 = ttk.Style()
estilos_TEXTO1.configure("TEXTO2.TLabel", font = "arial 40", anchor = "w")


### CREACION Y POSICION DEL TEXTO 2
TEXTO_2 = StringVar()
TEXTO_2_2 = ttk.Label(MARCO_PRINCIPAL, textvariable= TEXTO_2, style= "TEXTO2.TLabel")
TEXTO_2_2.grid(row=1, column=0, columnspan=4, sticky= (W, N, E, S))




#Estilos para los botones
estilos_botones_numeros = ttk.Style()
estilos_botones_numeros.configure("botones_numeros.TButton", font = "arial 22", width = 5 , background = "yellow", relief = "flat")
estilos_botones_numeros.map("botones_numeros.TButton", background =[("active", "#B9B9B9")])

estilos_botones_borrar = ttk.Style()
estilos_botones_borrar.configure("botones_borrar.TButton", font = "arial 22", width = 5 , background = "green", relief = "flat")
estilos_botones_borrar.map("botones_borrar.TButton", foreground = [("active", "red")], background = [("active", "#858585")])

estilos_botones_otros = ttk.Style()
estilos_botones_otros.configure("botones_otros.TButton", font = "arial 22", width = 5 , background = "blue", relief = "flat")
estilos_botones_numeros.map("botones_otros.TButton", background =[("active", "#858585")])



#botonera
Boton0 = ttk.Button(MARCO_PRINCIPAL, text="0", style= "botones_numeros.TButton", command=lambda: INGRESAR_VALORES("0"))
Boton1 = ttk.Button(MARCO_PRINCIPAL, text="1", style= "botones_numeros.TButton", command=lambda: INGRESAR_VALORES("1"))
Boton2 = ttk.Button(MARCO_PRINCIPAL, text="2", style= "botones_numeros.TButton", command=lambda: INGRESAR_VALORES("2"))
Boton3 = ttk.Button(MARCO_PRINCIPAL, text="3", style= "botones_numeros.TButton", command=lambda: INGRESAR_VALORES("3"))
Boton4 = ttk.Button(MARCO_PRINCIPAL, text="4", style= "botones_numeros.TButton", command=lambda: INGRESAR_VALORES("4"))
Boton5 = ttk.Button(MARCO_PRINCIPAL, text="5", style= "botones_numeros.TButton", command=lambda: INGRESAR_VALORES("5"))
Boton6 = ttk.Button(MARCO_PRINCIPAL, text="6", style= "botones_numeros.TButton", command=lambda: INGRESAR_VALORES("6"))
Boton7 = ttk.Button(MARCO_PRINCIPAL, text="7", style= "botones_numeros.TButton", command=lambda: INGRESAR_VALORES("7"))
Boton8 = ttk.Button(MARCO_PRINCIPAL, text="8", style= "botones_numeros.TButton", command=lambda: INGRESAR_VALORES("8"))
Boton9 = ttk.Button(MARCO_PRINCIPAL, text="9", style= "botones_numeros.TButton", command=lambda: INGRESAR_VALORES("9"))

Boton_borrar = ttk.Button(MARCO_PRINCIPAL, text=chr(9003), style="botones_borrar.TButton")
Boton_borrar_todo = ttk.Button(MARCO_PRINCIPAL, text="C", style="botones_borrar.TButton")
Boton_parentesis1 = ttk.Button(MARCO_PRINCIPAL, text="(", style="botones_otros.TButton", command=lambda: INGRESAR_VALORES("("))
Boton_parentesis2 = ttk.Button(MARCO_PRINCIPAL, text=")", style="botones_otros.TButton", command=lambda: INGRESAR_VALORES(")"))
Boton_punto = ttk.Button(MARCO_PRINCIPAL, text=".", style="botones_otros.TButton", command=lambda: INGRESAR_VALORES("."))

Boton_division = ttk.Button(MARCO_PRINCIPAL, text= chr(247), style="botones_otros.TButton" , command= lambda: INGRESAR_VALORES("/"))
Boton_multiplicar = ttk.Button(MARCO_PRINCIPAL, text="*", style="botones_otros.TButton", command= lambda: INGRESAR_VALORES("*"))
Boton_resta = ttk.Button(MARCO_PRINCIPAL, text="-", style="botones_otros.TButton", command= lambda: INGRESAR_VALORES("-"))
Boton_suma = ttk.Button(MARCO_PRINCIPAL, text="+", style="botones_otros.TButton", command= lambda: INGRESAR_VALORES("+"))

Boton_igual = ttk.Button(MARCO_PRINCIPAL, text="=", style="botones_otros.TButton", command= lambda: INGRESAR_VALORES("="))
Boton_raiz = ttk.Button(MARCO_PRINCIPAL, text="√", style="botones_otros.TButton", command= lambda: raiz_cuadrada())


#posicion de los botones
Boton_parentesis1.grid(row= 2, column= 0, sticky= (W, N, E, S))
Boton_parentesis2.grid(row= 2, column= 1, sticky= (W, N, E, S))
Boton_borrar_todo.grid(row= 2, column= 2, sticky= (W, N, E, S))
Boton_borrar.grid(row= 2, column= 3, sticky= (W, N, E, S))

Boton7.grid(row= 3, column= 0, sticky= (W, N, E, S))
Boton8.grid(row= 3, column= 1, sticky= (W, N, E, S))
Boton9.grid(row= 3, column= 2, sticky= (W, N, E, S))
Boton_division.grid(row= 3, column= 3, sticky= (W, N, E, S))

Boton4.grid(row= 4, column= 0, sticky= (W, N, E, S))
Boton5.grid(row= 4, column= 1, sticky= (W, N, E, S))
Boton6.grid(row= 4, column= 2, sticky= (W, N, E, S))
Boton_multiplicar.grid(row= 4, column= 3, sticky= (W, N, E, S))

Boton1.grid(row= 5, column= 0, sticky= (W, N, E, S))
Boton2.grid(row= 5, column= 1, sticky= (W, N, E, S))
Boton3.grid(row= 5, column= 2, sticky= (W, N, E, S))
Boton_suma.grid(row= 5, column= 3, sticky= (W, N, E, S))

Boton0.grid(row= 6, column= 0, columnspan=2 , sticky= (W, N, E, S))
Boton_punto.grid(row= 6, column= 2, sticky= (W, N, E, S))
Boton_resta.grid(row= 6, column= 3, sticky= (W, N, E, S))

Boton_igual.grid(row= 7, column= 0, columnspan=3 , sticky= (W, N, E, S))
Boton_raiz.grid(row= 7, column= 3, sticky= (W, N, E, S))

#configuracion de las separaciones de los botones
for child in MARCO_PRINCIPAL.winfo_children():
    child.grid_configure(ipady= 10, padx=1, pady=1)


VENTANA_PRINCIPAL.mainloop()