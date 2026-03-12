import tkinter as tk

# -------- CLASE COLA --------

class Cola:

    def __init__(self):
        self.items = []

    def encolar(self, dato):
        self.items.append(dato)

    def desencolar(self):
        if self.items:
            return self.items.pop(0)

    def mostrar(self):
        return self.items

    def vacia(self):
        return len(self.items) == 0


# -------- COLAS --------

colaA = Cola()
colaB = Cola()
colaC = Cola()

cola_global = Cola()

turno = 0
tiempo_total = 0


# tiempos de servicio
tiempo_servicio = {
    "A":6,
    "B":2,
    "C":4
}


# -------- DIBUJAR --------

def dibujar():

    canvas.delete("all")

    colas = [
        colaA.mostrar(),
        colaB.mostrar(),
        colaC.mostrar()
    ]

    nombres = [
        "Servicio A (Largo)",
        "Servicio B (Rápido)",
        "Servicio C (Normal)"
    ]

    colores = ["#EF5350","#42A5F5","#66BB6A"]

    y = 80

    for i in range(3):

        canvas.create_text(
            120,
            y,
            text=nombres[i],
            font=("Arial",12,"bold")
        )

        x = 300

        for cliente in colas[i]:

            canvas.create_rectangle(
                x,
                y-15,
                x+50,
                y+20,
                fill=colores[i],
                width=2
            )

            canvas.create_text(
                x+25,
                y+2,
                text=str(cliente),
                font=("Arial",10,"bold")
            )

            x += 60

        y += 80


# -------- LLEGADA CLIENTE --------

def llegar():

    global turno, tiempo_total

    servicio = entrada.get().upper()

    if servicio not in ["A","B","C"]:
        estado.config(text="Ingrese A, B o C")
        return

    turno += 1

    tiempo = tiempo_servicio[servicio]

    cliente = f"{servicio}{turno}"

    cola_global.encolar((cliente,tiempo))

    if servicio == "A":
        colaA.encolar(cliente)

    elif servicio == "B":
        colaB.encolar(cliente)

    elif servicio == "C":
        colaC.encolar(cliente)

    espera = tiempo_total

    tiempo_total += tiempo

    estado.config(
        text=f"Cliente {cliente} agregado | Espera estimada: {espera} min"
    )

    dibujar()


# -------- ATENDER --------

def atender():

    global tiempo_total

    if cola_global.vacia():
        estado.config(text="No hay clientes")
        return

    cliente, tiempo = cola_global.desencolar()

    servicio = cliente[0]

    if servicio == "A":
        colaA.desencolar()

    elif servicio == "B":
        colaB.desencolar()

    elif servicio == "C":
        colaC.desencolar()

    tiempo_total -= tiempo

    estado.config(
        text=f"Atendiendo {cliente} | Duración {tiempo} min"
    )

    dibujar()


# -------- INTERFAZ --------

ventana = tk.Tk()
ventana.title("Sistema de Colas - Seguros")
ventana.geometry("900x520")
ventana.config(bg="#ECEFF1")


titulo = tk.Label(
    ventana,
    text="Simulación de Colas con 1 Módulo de Atención",
    font=("Arial",18,"bold"),
    bg="#ECEFF1"
)

titulo.pack(pady=10)


canvas = tk.Canvas(
    ventana,
    width=850,
    height=300,
    bg="white",
    highlightthickness=2
)

canvas.pack()


frame = tk.Frame(ventana,bg="#ECEFF1")
frame.pack(pady=10)

tk.Label(
    frame,
    text="Servicio (A,B,C):",
    font=("Arial",11),
    bg="#ECEFF1"
).grid(row=0,column=0)


entrada = tk.Entry(frame,width=5)
entrada.grid(row=0,column=1,padx=5)


btn_llegar = tk.Button(
    frame,
    text="Llegada Cliente",
    command=llegar,
    bg="#42A5F5",
    fg="white",
    font=("Arial",10,"bold")
)

btn_llegar.grid(row=0,column=2,padx=10)


btn_atender = tk.Button(
    frame,
    text="Atender Cliente",
    command=atender,
    bg="#66BB6A",
    fg="white",
    font=("Arial",10,"bold")
)

btn_atender.grid(row=0,column=3,padx=10)


estado = tk.Label(
    ventana,
    text="Sistema listo",
    font=("Arial",12),
    bg="#ECEFF1"
)

estado.pack(pady=10)


dibujar()

ventana.mainloop()