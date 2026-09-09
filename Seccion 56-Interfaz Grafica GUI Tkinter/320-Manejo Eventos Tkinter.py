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
ventana.geometry('600x400')   # Tamaño en pixeles
ventana.title('Hola Mundo')   # Título de la ventana
ventana.iconbitmap('icono.ico')  # Ícono de la aplicación

print("\n")  # Espacio visual

# ===========================


def evento_click():


    boton1.config(text="Boton Presionado")


    print("Ejecucion del evento Click")

    # ========== Creamos un nuevo boton y mopstramos
    boton2=ttk.Button(ventana, text="Nuevo Boton")
    boton2.pack()


# ==============================
# 3. Crear un botón
# ==============================
boton1 = ttk.Button(ventana, text='Dar click',command=evento_click)

boton1.pack()  # Mostrar el botón en la ventana

print("\n")  # Espacio visual


# ==============================
# 4. Iniciar el loop principal
# ==============================
ventana.mainloop()
