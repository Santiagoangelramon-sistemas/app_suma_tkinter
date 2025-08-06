# Se importa la libreria de tkinter con todas sus funciones
from tkinter import *  

#-------------------------------------------------------------
# Funciones de la app
#-------------------------------------------------------------



#-------------------------------------------------------------
# Ventana principal de la app
#-------------------------------------------------------------

# Se declara una variable llamada ventana_principal, que adquiere la caracteristicas de un objeto de tipo Tk()

vetana_principal = Tk()

# Titulo de la ventana 
vetana_principal.title("Santiago Angel Ramon")

# Tamaño de la ventana
vetana_principal.geometry("800x500")

# Desahibilar el boton de maximizar pamtalla 
vetana_principal.resizable(0,0)
 
# Color de la pantalla
vetana_principal.config(bg="black")

#------------------------------------------------------------
#Variables globales
#------------------------------------------------------------
a = StringVar()
b = StringVar()
c = IntVar()

#------------------------------------------------------------
#Frame1 - Entrada de datos
#------------------------------------------------------------

frame_1 = Frame(vetana_principal)
frame_1.config(bg="ivory2", width=780, height=240)
frame_1.place(x=10, y=10)

# Imagen - Logo de la app
logo = PhotoImage(file="img/btn-suma.png")
Label_logo = Label(frame_1, image=logo)
Label_logo.place(x=10, y=10)

# Etiqueta del titulo de app
titulo = Label(frame_1, text="Colegio San Jose de Guanenta")
titulo.config(bg="yellow", fg="blue", font=("Arial", 16))
titulo.place(x=390,y=10)

# Etiqueta de subtitulo 1 de la app
subtitulo1 = Label(frame_1, text="Especialidad de sistemas")
subtitulo1.config(bg="yellow", fg="blue", font=("Arial", 12))
subtitulo1.place(x=390,y=40)

# Etiqueta de subtitulo 2 de la app
subtitulo2 = Label(frame_1, text="Suma De Dos Enteros")
subtitulo2.config(bg="ivory2", fg="blue", font=("Arial", 15), anchor=CENTER)
subtitulo2.place(x=487, y=90)

# Etiqueta del primer valor
label_a = Label(frame_1, text="a = ")
label_a.config(bg="ivory2", fg="blue", font=("Arial", 20), anchor=CENTER)
label_a.place(x=390, y=120)

# Entry para el primer valor -a
entry_a = Entry(frame_1, width=4, textvariable=a)
entry_a.config(font=("Arial", 20), justify=CENTER)
entry_a.focus_set()
entry_a.place(x=487, y= 120)

# Etiqueta del segundo valor -b
label_b = Label(frame_1, text= "b = ")
label_b.config(bg="ivory2", fg="blue", font=("Arial", 20), anchor=CENTER)
label_b.place(x=585, y=120)

# Entry para el segundo valor -b
entry_b = Entry(frame_1, width=4, textvariable=a)
entry_b.config(font=("Arial", 20), justify=CENTER)
entry_b.focus_set()
entry_b.place(x=682, y= 120)

#------------------------------------------------------------
#Frame2 - Operaciones
#------------------------------------------------------------

frame_2 = Frame(vetana_principal)
frame_2.config(bg="ivory2", width=780, height=120)
frame_2.place(x=10, y=260)

# boton para sumar
img_bt_sumar = PhotoImage(file= "img/boton_sumar.png")
bt_sumar = Button(frame_2, image = img_bt_sumar, width=105, height=105)
# bt_sumar = Button (frame_2, text="Sumar", width=10)
bt_sumar.place(x=116, y=7)

# boton para borrar entrada y resultados
img_bt_borrar = PhotoImage(file= "img/boton_borrar.png")
bt_borrar= Button(frame_2, image = img_bt_borrar, width=105, height=105)
# bt_sumar = Button (frame_2, text="Sumar", width=10)
bt_borrar.place (x=337, y=7)

# boton para salir
img_bt_salir = PhotoImage(file= "img/boton_salir.png")
bt_salir= Button(frame_2, image = img_bt_salir, width=105, height=105)
# bt_sumar = Button (frame_2, text="Sumar", width=10)
bt_salir.place (x=558, y=7)



#------------------------------------------------------------
#Frame3 - Resultados
#------------------------------------------------------------

frame_3 = Frame(vetana_principal)
frame_3.config(bg="ivory2", width=780, height=100)
frame_3.place(x=10, y=390)

# Area de texto

t_resultados = Text(frame_3, width=50, height=3)
t_resultados.config(bg="green", fg="white", font=("Courier", 20))
t_resultados.pack()
# Metodo principal que despliega la ventana en pantalla
vetana_principal.mainloop()