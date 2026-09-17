# ==============================
# 1. Importar librerías necesarias
# ==============================
import tkinter as tk
from tkinter import ttk, messagebox, Menu


# ==============================
# 2. Crear ventana principal
# ==============================
ventana = tk.Tk()
ventana.geometry('600x400')
ventana.title('Manejo de Componentes')
ventana.iconbitmap('icono.ico')


# ==============================
# 3. Crear caja de texto (Entry)
# ==============================
entrada1 = ttk.Entry(ventana, width=30)
entrada1.grid(row=0, column=0)


# ==============================
# 4. Crear etiqueta (Label)
# ==============================
etiqueta1 = tk.Label(ventana, text='Se mostrará el contenido caja de texto')
etiqueta1.grid(row=1, column=0, columnspan=2)


# ==============================
# 5. Definir función del botón
# ==============================
def enviar():
    etiqueta1.config(text=entrada1.get())
    mensaje1 = entrada1.get()
    if mensaje1:
        messagebox.showinfo("Mensaje INFO", mensaje1 + " INFORMATIVO")


# ==============================
# 6. Definir función para crear menú
# ==============================
def crear_menu():
    # Configurar menú principal
    menu_principal = Menu(ventana)

    # Crear submenú Archivo
    sub_menu_archivo = Menu(menu_principal, tearoff=0)
    sub_menu_archivo.add_command(label="Nuevo")
    sub_menu_archivo.add_command(label="Salir", command=ventana.quit)

    # Agregar submenú al menú principal
    menu_principal.add_cascade(label="Archivo", menu=sub_menu_archivo)

    #Sub menu ayuda
    sub_menu=Menu(menu_principal,tearoff=0)

    #Agg nueva opcion
    sub_menu.add_command(label="Acerca de ", )

    menu_principal.add_cascade(menu=sub_menu,label="Ayuda")


    # Mostrar menú en la ventana principal
    ventana.config(menu=menu_principal)


# ==============================
# 7. Crear botón y asociar función
# ==============================
boton1 = ttk.Button(ventana, text='Enviar', command=enviar)
boton1.grid(row=0, column=1)


# ==============================
# 8. Crear menú y arrancar loop
# ==============================
crear_menu()
ventana.mainloop()
