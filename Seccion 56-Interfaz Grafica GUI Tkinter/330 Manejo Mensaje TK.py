import tkinter as tk
from tkinter import ttk,messagebox

ventana = tk.Tk()
ventana.geometry('600x400')
ventana.title('Manejo de Componentes')
ventana.iconbitmap('icono.ico')

# Definimos una variable que podremos modificar posteriormente (set), leer(get)
entrada1 = ttk.Entry(ventana, width=30)
entrada1.grid(row=0, column=0)



# Etiqueta (label)
etiqueta1 = tk.Label(ventana, text='Se mostrará el contenido caja de texto')
etiqueta1.grid(row=1, column=0, columnspan=2)



def enviar():
    # Modificamos el texto del label
    etiqueta1.config(text=entrada1.get())

    ## CAJA DE MENSAJES (MESSAGEBOX)
    mensaje1=entrada1.get()
    if mensaje1:
        messagebox.showinfo("Mensaje de iNFO",mensaje1 +"INFORMATIVO")
        messagebox.showerror("Mensaje de ERROR",mensaje1 +"HAY UN PROBLEMA")
        messagebox.showwarning("Mensaje de Alertas",mensaje1+"Alertas uwu")

# Creamos un botón
boton1 = ttk.Button(ventana, text='Enviar', command=enviar)
boton1.grid(row=0, column=1)

ventana.mainloop()
