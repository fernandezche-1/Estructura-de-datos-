import tkinter as tk
from tkinter import messagebox


class Order:
    def __init__(self, qtty, customer):
        self.customer = customer
        self.qtty = qtty

    def getQtty(self):
        return self.qtty

    def getCustomer(self):
        return self.customer


class Node:
    def __init__(self, info):
        self.info = info
        self.next = None

    def getNext(self):
        return self.next

    def setNext(self, nextNode):
        self.next = nextNode

    def getInfo(self):
        return self.info


class Queue:
    def __init__(self):
        self.front_node = None
        self.rear = None
        self.count = 0

    def size(self):
        return self.count

    def isEmpty(self):
        return self.count == 0

    def front(self):
        if self.isEmpty():
            return None
        return self.front_node.getInfo()

    def enqueue(self, info):
        new_node = Node(info)

        if self.isEmpty():
            self.front_node = new_node
            self.rear = new_node
        else:
            self.rear.setNext(new_node)
            self.rear = new_node

        self.count += 1

    def dequeue(self):
        if self.isEmpty():
            return None

        temp = self.front_node
        self.front_node = self.front_node.getNext()
        self.count -= 1

        if self.front_node is None:
            self.rear = None

        return temp.getInfo()


queue = Queue()

def actualizar_lista():
    lista.delete(0, tk.END)

    node = queue.front_node
    i = 1

    while node != None:
        order = node.getInfo()
        texto = f"{i}. Cliente: {order.getCustomer()} | Cantidad: {order.getQtty()}"
        lista.insert(tk.END, texto)
        node = node.getNext()
        i += 1


def agregar():
    cliente = entry_cliente.get()
    cantidad = entry_cantidad.get()

    if cliente == "" or cantidad == "":
        messagebox.showwarning("Error", "Ingrese todos los datos")
        return

    try:
        cantidad = int(cantidad)
    except:
        messagebox.showerror("Error", "Cantidad debe ser número")
        return

    order = Order(cantidad, cliente)
    queue.enqueue(order)

    entry_cliente.delete(0, tk.END)
    entry_cantidad.delete(0, tk.END)

    actualizar_lista()


def eliminar():
    order = queue.dequeue()

    if order == None:
        messagebox.showinfo("Cola vacía", "No hay pedidos en la cola")
    else:
        messagebox.showinfo(
            "Pedido eliminado",
            f"Cliente: {order.getCustomer()}\nCantidad: {order.getQtty()}"
        )

    actualizar_lista()


def ver_primero():
    order = queue.front()

    if order == None:
        messagebox.showinfo("Cola vacía", "No hay pedidos")
    else:
        messagebox.showinfo(
            "Primer pedido",
            f"Cliente: {order.getCustomer()}\nCantidad: {order.getQtty()}"
        )


ventana = tk.Tk()
ventana.title("Sistema de Pedidos - Cola con Listas Enlazadas")
ventana.geometry("600x450")
ventana.configure(bg="#2c3e50")

titulo = tk.Label(
    ventana,
    text="Sistema Empresarial de Pedidos",
    font=("Arial", 18, "bold"),
    bg="#2c3e50",
    fg="white"
)
titulo.pack(pady=10)


frame_inputs = tk.Frame(ventana, bg="#2c3e50")
frame_inputs.pack()

tk.Label(frame_inputs, text="Cliente", bg="#2c3e50", fg="white").grid(row=0, column=0, padx=5)
entry_cliente = tk.Entry(frame_inputs)
entry_cliente.grid(row=0, column=1, padx=5)

tk.Label(frame_inputs, text="Cantidad", bg="#2c3e50", fg="white").grid(row=1, column=0, padx=5)
entry_cantidad = tk.Entry(frame_inputs)
entry_cantidad.grid(row=1, column=1, padx=5)


frame_botones = tk.Frame(ventana, bg="#2c3e50")
frame_botones.pack(pady=10)

btn_agregar = tk.Button(frame_botones, text="Agregar Pedido", bg="#27ae60", fg="white", width=15, command=agregar)
btn_agregar.grid(row=0, column=0, padx=5)

btn_eliminar = tk.Button(frame_botones, text="Eliminar Pedido", bg="#c0392b", fg="white", width=15, command=eliminar)
btn_eliminar.grid(row=0, column=1, padx=5)

btn_ver = tk.Button(frame_botones, text="Ver Primero", bg="#2980b9", fg="white", width=15, command=ver_primero)
btn_ver.grid(row=0, column=2, padx=5)


lista = tk.Listbox(
    ventana,
    width=70,
    height=15,
    font=("Consolas", 11)
)

lista.pack(pady=10)


ventana.mainloop()