# ==============================
# 1. Importar librerías necesarias
# ==============================
import tkinter as tk
from tkinter import ttk

print("\n")  # Espacio visual

#################
ventana= tk.Tk()
ventana.geometry("300x300")
ventana.title("Manejo GRID")
ventana.iconbitmap("icono.ico")


# Justificar texto : justify
# width CANTIDAD DE CARACTERES EN LA CAJA
entrada1=tk.Entry(ventana, width=30,justify=tk.RIGHT)
entrada1.grid(row=0,column=0)

# insert -Insertar un Texto
entrada1.insert(0,"Ingrece una Cadena de texto")
entrada1.insert(5," - ")



ventana.mainloop()




















