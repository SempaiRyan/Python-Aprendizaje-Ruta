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

#Configurar Grid
ventana.rowconfigure(0,weight=2)
ventana.rowconfigure(1,weight=10)
ventana.columnconfigure(0,weight=1)
ventana.columnconfigure(1,weight=5)


###############
def evento1():
    boton1.config(text="Boton 1 Presionado")


def evento2():
    boton2.config(text="Boton 2 Presionado")

###############
###############
# ============== N ARRIBA,E DERECHA,S ABAJO ,W IZQUIERDA

# BOTONES
boton1=ttk.Button(ventana,text="Boton 1",command=evento1)
boton1.grid(row=0,column=0,sticky="NSWE")



boton2=ttk.Button(ventana,text="Boton 2",command=evento2)
boton2.grid(row=1,column=0,sticky="NSWE")


boton3=ttk.Button(ventana,text="Boton 3")
boton3.grid(row=0,column=1,sticky="NSWE")


boton4=ttk.Button(ventana,text="Boton 4")
boton4.grid(row=1,column=1,sticky="NSWE")





boton1.grid(row=0,column=0)
boton2.grid(row=1,column=0)


ventana.mainloop()














