# ventana principal
import tkinter as tk
from tkinter import ttk,messagebox


ventana = tk.Tk()
ventana.geometry("300x300")
ventana.title("Login")
ventana.iconbitmap("icono.ico")
ventana.resizable(width=True,height=True)




#configuracion del Grid
ventana.columnconfigure(0,weight=1)
ventana.columnconfigure(1,weight=3)


#Usuario
usuario_etiqueta=ttk.Label(ventana,text="Usuario")
usuario_etiqueta.grid(row=0,column=0,sticky=tk.E,padx=5,pady=5)
usuario_etiqueta=ttk.Entry(ventana)
usuario_etiqueta.grid(row=0,column=1,sticky=tk.W,padx=5,pady=5)


#Password
password_etiqueta=ttk.Label(ventana,text="Password")
password_etiqueta.grid(row=1,column=0,sticky=tk.E,padx=5,pady=5)
password_etiqueta=ttk.Entry(ventana,show="*")
password_etiqueta.grid(row=1,column=1,sticky=tk.W,padx=5,pady=5)


# Boton
botonsito=ttk.Button(ventana,text="Login")
botonsito.grid(row=3,column=0,columnspan=2)

def login():
    messagebox.showinfo("Datos login ",f"User{usuario_etiqueta.get()},"
                                       f"Password{password_etiqueta.get()}")




#ejecutar ventana
ventana.mainloop()