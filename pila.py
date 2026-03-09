import tkinter as tk
from tkinter import messagebox

MAX = 8
pila = []

def dibujar_pila():
    canvas.delete("all")

    base_y = 300
    ancho = 120
    alto = 30
    x1 = 90
    x2 = x1 + ancho

    for i, elemento in enumerate(pila):
        y1 = base_y - (i+1)*alto
        y2 = y1 + alto

        canvas.create_rectangle(x1, y1, x2, y2, fill="#4CAF50", outline="black")
        canvas.create_text((x1+x2)/2, (y1+y2)/2, text=elemento, fill="white", font=("Arial",12,"bold"))

    if len(pila) > 0:
        y_tope = base_y - len(pila)*alto
        canvas.create_text(40, y_tope+15, text="TOPE ➜", font=("Arial",10,"bold"), fill="red")

    contador.config(text=f"Elementos: {len(pila)}")

def insertar():
    if len(pila) >= MAX:
        messagebox.showerror("Error","Desbordamiento: pila llena")
        return

    valor = entrada.get().upper()

    if valor == "":
        messagebox.showwarning("Error","Ingresa un valor")
        return

    pila.append(valor)
    entrada.delete(0,tk.END)
    dibujar_pila()

def eliminar():
    valor = entrada.get().upper()

    if valor == "":
        return

    if valor not in pila:

        pila.append(valor)   
        dibujar_pila()

        ventana.after(800, lambda: eliminar_temporal(valor))

    else:
        pila.remove(valor)
        dibujar_pila()

    entrada.delete(0, tk.END)


def eliminar_temporal(valor):
    if valor in pila:
        pila.remove(valor)
        dibujar_pila()

def ver_cima():
    if len(pila)==0:
        messagebox.showinfo("Cima","La pila está vacía")
    else:
        messagebox.showinfo("Cima",f"La cima es {pila[-1]}")

def vaciar():
    pila.clear()
    dibujar_pila()


ventana = tk.Tk()
ventana.title("Simulador de Pila")
ventana.geometry("500x400")
ventana.config(bg="#2c3e50")

titulo = tk.Label(
    ventana,
    text="SIMULADOR DE PILA",
    font=("Arial",16,"bold"),
    bg="#2c3e50",
    fg="white"
)
titulo.pack(pady=10)

frame_control = tk.Frame(ventana,bg="#2c3e50")
frame_control.pack()

entrada = tk.Entry(frame_control,font=("Arial",12),width=10)
entrada.grid(row=0,column=0,padx=10)

btn_insertar = tk.Button(
    frame_control,
    text="Insertar",
    bg="#3498db",
    fg="white",
    width=10,
    command=insertar
)
btn_insertar.grid(row=0,column=1,padx=5)

btn_eliminar = tk.Button(
    frame_control,
    text="Eliminar",
    bg="#e74c3c",
    fg="white",
    width=10,
    command=eliminar
)
btn_eliminar.grid(row=0,column=2,padx=5)

btn_cima = tk.Button(
    frame_control,
    text="Ver cima",
    bg="#9b59b6",
    fg="white",
    width=10,
    command=ver_cima
)
btn_cima.grid(row=1,column=1,pady=10)

btn_vaciar = tk.Button(
    frame_control,
    text="Vaciar",
    bg="#f39c12",
    fg="white",
    width=10,
    command=vaciar
)
btn_vaciar.grid(row=1,column=2)

contador = tk.Label(
    ventana,
    text="Elementos: 0",
    font=("Arial",12),
    bg="#2c3e50",
    fg="white"
)
contador.pack()

canvas = tk.Canvas(
    ventana,
    width=300,
    height=320,
    bg="#ecf0f1",
    highlightthickness=0
)
canvas.pack(pady=10)

ventana.mainloop()