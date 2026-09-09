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



###############
def evento1():
    boton1.config(text="Boton 1 Presionado")


def evento2():
    boton2.config(text="Boton 2 Presionado")

###############

boton1=ttk.Button(ventana,text="Boton 1",command=evento1)
boton2=ttk.Button(ventana,text="Boton 2",command=evento2)


boton1.grid(row=0,column=0)
boton2.grid(row=1,column=0)


ventana.mainloop()














