# Se importa la libreria de tkinter con todas sus funciones
from tkinter import *
from tkinter import messagebox

# -----------------------------
# funciones de la app 
# -----------------------------

def sumar():
    try:
        num1 = int(a.get())
        num2 = int(b.get())
        resultado = num1 + num2
        c.set(resultado)
        t_resultados.delete("1.0", END)
        t_resultados.insert(END, f"{num1} + {num2} = {resultado}")
    except:
        t_resultados.delete("1.0", END)
        t_resultados.insert(END, "Error: valores no válidos")

def borrar():
    # Limpia los valores y resultados sin cerrar la app
    a.set("")
    b.set("")
    c.set(0)
    t_resultados.delete("1.0", END)

def salir():
    # Muestra confirmación antes de cerrar
    respuesta = messagebox.askokcancel("Confirmación", "La app se cerrará. ¿Deseas continuar?")
    if respuesta:
        ventana_principal.destroy()

# -----------------------------
# ventana principal de la app
# -----------------------------

ventana_principal = Tk()
ventana_principal.title("Santiago Angel Ramon (kangelox_draw)")
ventana_principal.geometry("800x500")
ventana_principal.resizable(0, 0)
ventana_principal.config(bg="black")

# --------------------------
# variables globales
# --------------------------
a = StringVar()
b = StringVar()
c = IntVar()

# -------------------------
# frame_1
# -------------------------
frame_1 = Frame(ventana_principal)
frame_1.config(bg="ivory2", width=780, height=240)
frame_1.place(x=10, y=10)

titulo = Label(frame_1, text="Colegio San Jose de Guanenta")
titulo.config(bg="yellow", fg="blue", font=("Arial", 16))
titulo.place(x=250, y=10)

logo = PhotoImage(file="img/btn-suma.png")
label_logo = Label(frame_1, image=logo)
label_logo.place(x=10, y=10)

subtitulo1 = Label(frame_1, text="Especialidad en sistemas")
subtitulo1.config(bg="yellow", fg="blue", font=("Arial", 12))
subtitulo1.place(x=300, y=50)

subtitulo2 = Label(frame_1, text="Suma de dos enteros")
subtitulo2.config(bg="ivory2", fg="blue", font=("Arial", 15))
subtitulo2.place(x=300, y=70)

label_a = Label(frame_1, text="a =")
label_a.config(bg="ivory2", fg="blue", font=("Arial", 20))
label_a.place(x=300, y=120)

label_b = Label(frame_1, text="b =")
label_b.config(bg="ivory2", fg="blue", font=("Arial", 20))
label_b.place(x=300, y=160)

entry_a = Entry(frame_1, width=4, textvariable=a)
entry_a.config(font=("Arial", 20), justify=CENTER)
entry_a.place(x=487, y=120)

entry_b = Entry(frame_1, width=4, textvariable=b)
entry_b.config(font=("Arial", 20), justify=CENTER)
entry_b.place(x=487, y=160)

# -----------------------------
# frame_2
# -----------------------------
frame_2 = Frame(ventana_principal)
frame_2.config(bg="ivory2", width=780, height=120)
frame_2.place(x=10, y=260)

# Botón para sumar
img_bt_sumar = PhotoImage(file="img/boton_sumar.png")
bt_sumar = Button(frame_2, image=img_bt_sumar, width=105, height=105, command=sumar)
bt_sumar.place(x=116, y=7)

# Botón para borrar (solo limpia los campos)
img_bt_borrar = PhotoImage(file="img/boton_borrar.png")
bt_borrar = Button(frame_2, image=img_bt_borrar, width=105, height=105, command=borrar)
bt_borrar.place(x=337, y=7)

# Botón para salir (muestra confirmación)
img_bt_salir = PhotoImage(file="img/boton_salir.png")
bt_salir = Button(frame_2, image=img_bt_salir, width=105, height=105, command=salir)
bt_salir.place(x=558, y=7)

# -----------------------------
# frame 3: resultados
# -----------------------------
frame_3 = Frame(ventana_principal)
frame_3.config(bg="ivory2", width=780, height=120)
frame_3.place(x=10, y=390)

t_resultados = Text(frame_3, width=50, height=3)
t_resultados.config(bg="green", fg="white", font=("Courier", 20))
t_resultados.pack()

# -----------------------------
# iniciar la app
# -----------------------------
ventana_principal.mainloop()