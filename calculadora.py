import tkinter as tk

class Calculadora:
    def __init__(self, master):
        self.master = master
        master.title("Calculadora de DOLAR $$ USDC")

        

        # Pantalla
        self.pantalla = tk.Entry(master, width=16, font=('Arial', 20), borderwidth=5)
        self.pantalla.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

        # Botones
        botones = [
            ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
            ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
            ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
            ('0', 4, 0), ('C', 4, 1), ('=', 4, 2), ('+', 4, 3),
        ]

        for texto, fila, columna in botones:
            tk.Button(master, text=texto, font=('Arial', 14), command=lambda t=texto: self.pulsar(t)).grid(row=fila, column=columna, padx=10, pady=10)

    def pulsar(self, valor):
        if valor == '=':
            try:
                resultado = eval(self.pantalla.get())
                self.pantalla.delete(0, tk.END)
                self.pantalla.insert(tk.END, str(resultado))
            except Exception as e:
                self.pantalla.delete(0, tk.END)
                self.pantalla.insert(tk.END, "Error")
        elif valor == 'C':
            self.pantalla.delete(0, tk.END)
        else:
            self.pantalla.insert(tk.END, valor)

# Crear la aplicación
root = tk.Tk()
calculadora = Calculadora(root)

# Mantener la ventana abierta
root.mainloop()
