import tkinter as tk
from tkinter import messagebox

def calcular_area(base, altura):
    return (base * altura) / 2
def validar_entrada(entrada):
    try:
        valor = float(entrada)
        if valor <= 0:
            raise ValueError("El valor debe ser mayor que cero")
        return valor
    except ValueError as e:
        messagebox.showerror("Error", str(e))
        return None

def calcular_y_mostrar_area():
    base = validar_entrada(base_entry.get())
    altura = validar_entrada(altura_entry.get())

    if base is not None and altura is not None:
        area = calcular_area(base, altura)
        messagebox.showinfo("Resultado", f"El área del triángulo es: {area}")

# Crear la ventana principal
root = tk.Tk()
root.title("Calculadora de área de triángulo")

# Crear los widgets
base_label = tk.Label(root, text="Base:")
base_label.grid(row=0, column=0, padx=5, pady=5)
base_entry = tk.Entry(root)
base_entry.grid(row=0, column=1, padx=5, pady=5)

altura_label = tk.Label(root, text="Altura:")
altura_label.grid(row=1, column=0, padx=5, pady=5)
altura_entry = tk.Entry(root)
altura_entry.grid(row=1, column=1, padx=5, pady=5)

calcular_button = tk.Button(root, text="Calcular área", command=calcular_y_mostrar_area)
calcular_button.grid(row=2, column=0, columnspan=2, padx=5, pady=5)

# Iniciar el bucle de eventos de Tkinter
root.mainloop()