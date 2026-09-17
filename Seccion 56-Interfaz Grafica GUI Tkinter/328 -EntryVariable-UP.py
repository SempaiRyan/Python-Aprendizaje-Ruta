# ==============================
# 1. Importar librerías necesarias
# ==============================
import tkinter as tk
from tkinter import ttk

print("\n")  # Espacio visual


# ==============================
# 2. Crear ventana principal
# ==============================
ventana = tk.Tk()
ventana.geometry('600x400')
ventana.title('Manejo de Grid')
ventana.iconbitmap('icono.ico')

print("\n")  # Espacio visual


# ==============================
# 3. Crear variable y caja de texto- SET , LEER GET
# ==============================
entrada_var1 = tk.StringVar(value='Valor por default')
entrada1 = ttk.Entry(ventana, width=30, textvariable=entrada_var1)
entrada1.grid(row=0, column=0)

print("\n")  # Espacio visual


# ==============================
# 4. Definir función del botón
# ==============================
def enviar():
    # Recuperamos la información a partir de la variable asociada con la caja de texto
    boton1.config(text=entrada_var1.get())
    # Modificación: utilizamos la variable de texto y el método set
    entrada_var1.set('Cambio...')
    # Recuperamos la información
    print(entrada_var1.get())
    print(entrada1.get())

print("\n")  # Espacio visual


# ==============================
# 5. Crear botón y asociar función
# ==============================
boton1 = ttk.Button(ventana, text='Enviar', command=enviar)
boton1.grid(row=0, column=1)

print("\n")  # Espacio visual


# ==============================
# 6. Iniciar el loop principal
# ==============================
ventana.mainloop()
