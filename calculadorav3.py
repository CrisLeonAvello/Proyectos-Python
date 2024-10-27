import tkinter as tk

ventana = tk.Tk()
ventana.title("Calculadora Básica PYTHON")
ventana.geometry("600x350") 

ventana.configure(bg="#FF7F50")

label_num1 = tk.Label(ventana, text="Ingresa el primer dígito:", bg="#f0f0f0", font=("Arial", 16))
label_num1.grid(row=0, column=0, padx=5, pady=5)

entry_num1 = tk.Entry(ventana, font=("Arial", 16))
entry_num1.grid(row=0, column=1, padx=5, pady=5)

label_num2 = tk.Label(ventana, text="Ingresa el segundo dígito:", bg="#f0f0f0", font=("Arial", 16))
label_num2.grid(row=1, column=0, padx=5, pady=5)

entry_num2 = tk.Entry(ventana, font=("Arial", 16))
entry_num2.grid(row=1, column=1, padx=5, pady=5)

def operar(opcion):
    try:
        a = float(entry_num1.get())
        b = float(entry_num2.get())

        if opcion == "suma":
            resultado = a + b
        elif opcion == "resta":
            resultado = a - b
        elif opcion == "multiplicacion":
            resultado = a * b
        elif opcion == "division":
            if b != 0:
                resultado = a / b
            else:
                resultado = "Error: NO existe la división de 0"
        else:
            resultado = "La operación no es válida"

        label_resultado.config(text=f"Resultado: {resultado}")
    except ValueError:
        label_resultado.config(text="Por favor, ingresa valores válidos")

boton_suma = tk.Button(ventana, text="Suma", command=lambda: operar("suma"), bg="#4CAF50", fg="white", font=("Arial", 16))
boton_suma.grid(row=2, column=0, padx=5, pady=5)

boton_resta = tk.Button(ventana, text="Resta", command=lambda: operar("resta"), bg="#2196F3", fg="white", font=("Arial", 16))
boton_resta.grid(row=2, column=1, padx=5, pady=5)

boton_multi = tk.Button(ventana, text="Multiplicación", command=lambda: operar("multiplicacion"), bg="#FF9800", fg="white", font=("Arial", 16))
boton_multi.grid(row=3, column=0, padx=5, pady=5)

boton_division = tk.Button(ventana, text="División", command=lambda: operar("division"), bg="#F44336", fg="white", font=("Arial", 16))
boton_division.grid(row=3, column=1, padx=5, pady=5)

label_resultado = tk.Label(ventana, text="El resultado es: ", bg="#f0f0f0", font=("Arial", 16))
label_resultado.grid(row=4, column=0, columnspan=2, padx=5, pady=5)

ventana.grid_rowconfigure(0, weight=1)
ventana.grid_rowconfigure(1, weight=1)
ventana.grid_rowconfigure(2, weight=1)
ventana.grid_rowconfigure(3, weight=1)
ventana.grid_columnconfigure(0, weight=1)
ventana.grid_columnconfigure(1, weight=1) 

ventana.mainloop()
