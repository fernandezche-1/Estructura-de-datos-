import tkinter as tk
from tkinter import messagebox

MAX = 5
pila = []

def actualizar_pila():
    lista.delete(0, tk.END)

    if len(pila) == 0:
        lista.insert(tk.END, "[ vacía ]")
    else:
        for elemento in reversed(pila):
            lista.insert(tk.END, f"| {elemento} |")

    contador.config(text=f"Elementos en la pila: {len(pila)}")

def agregar_elemento():
    if len(pila) == MAX:
        messagebox.showwarning("Pila llena", "La pila está llena")
    else:
        valor = entrada.get()
        if valor == "":
            messagebox.showinfo("Error", "Ingresa un elemento")
            return

        pila.append(valor)
        entrada.delete(0, tk.END)
        actualizar_pila()

def eliminar_elemento():
    if len(pila) == 0:
        messagebox.showwarning("Pila vacía", "La pila está vacía")
    else:
        eliminado = pila.pop()
        messagebox.showinfo("Elemento eliminado", f"Se eliminó: {eliminado}")
        actualizar_pila()

def ver_cima():
    if len(pila) == 0:
        messagebox.showinfo("Cima", "La pila está vacía")
    else:
        messagebox.showinfo("Cima de la pila", f"La cima es: {pila[-1]}")

def vaciar_pila():
    pila.clear()
    messagebox.showinfo("Pila", "La pila ha sido vaciada")
    actualizar_pila()

def verificar_vacia():
    if len(pila) == 0:
        messagebox.showinfo("Estado", "La pila está vacía")
    else:
        messagebox.showinfo("Estado", "La pila no está vacía")

def verificar_llena():
    if len(pila) == MAX:
        messagebox.showinfo("Estado", "La pila está llena")
    else:
        messagebox.showinfo("Estado", "La pila no está llena")

def cantidad():
    messagebox.showinfo("Cantidad", f"La pila tiene {len(pila)} elementos")

# Ventana
ventana = tk.Tk()
ventana.title("Simulación de Pila")
ventana.geometry("350x450")

tk.Label(ventana, text="Elemento:").pack()

entrada = tk.Entry(ventana)
entrada.pack(pady=5)

tk.Button(ventana, text="Agregar elemento", command=agregar_elemento).pack(pady=3)
tk.Button(ventana, text="Eliminar elemento", command=eliminar_elemento).pack(pady=3)
tk.Button(ventana, text="Ver cima", command=ver_cima).pack(pady=3)
tk.Button(ventana, text="Vaciar pila", command=vaciar_pila).pack(pady=3)

tk.Button(ventana, text="¿La pila está vacía?", command=verificar_vacia).pack(pady=3)
tk.Button(ventana, text="¿La pila está llena?", command=verificar_llena).pack(pady=3)
tk.Button(ventana, text="Cantidad de elementos", command=cantidad).pack(pady=3)

contador = tk.Label(ventana, text="Elementos en la pila: 0")
contador.pack(pady=5)

lista = tk.Listbox(ventana, width=20, height=10)
lista.pack(pady=10)

ventana.mainloop()