import tkinter as tk


class Cola:

    def __init__(self):
        self.items = []

    def encolar(self, dato):
        self.items.append(dato)

    def desencolar(self):
        if self.items:
            return self.items.pop(0)

    def vacia(self):
        return len(self.items) == 0

    def mostrar(self):
        return self.items



datosA = [3,4,2,8,12]
datosB = [6,2,9,11,3]

colaA = Cola()
colaB = Cola()
colaR = Cola()

indice = 0



def dibujar():

    canvas.delete("all")

    colas = [datosA, datosB, colaR.mostrar()]
    nombres = ["Cola A", "Cola B", "Resultado"]

    colores = ["#4FC3F7", "#FF8A65", "#81C784"]

    y = 50

    for i in range(3):

        canvas.create_text(
            100,
            y+15,
            text=nombres[i],
            font=("Arial",13,"bold")
        )

        x = 220

        for elemento in colas[i]:

            canvas.create_rectangle(
                x,y,
                x+50,y+35,
                fill=colores[i],
                outline="black",
                width=2
            )

            canvas.create_text(
                x+25,
                y+17,
                text=str(elemento),
                font=("Arial",11,"bold")
            )

            x += 60

        y += 80



def sumar_paso():

    global indice

    if indice >= len(datosA):
        estado.config(text="Proceso terminado")

        return

    a = datosA[indice]
    b = datosB[indice]

    suma = a + b

    colaR.encolar(suma)

    lista_resultados.insert(
        tk.END,
        f"{a} + {b} = {suma}"
    )

    estado.config(
        text=f"Sumando {a} + {b}"
    )

    indice += 1

    dibujar()

    ventana.after(1500, sumar_paso)



def iniciar():

    global indice

    indice = 0

    colaR.items = []

    lista_resultados.delete(0, tk.END)

    dibujar()

    ventana.after(1200, sumar_paso)



ventana = tk.Tk()
ventana.title("Simulación Visual de Suma de Colas")
ventana.geometry("950x650")
ventana.config(bg="#FAF8F8")

titulo = tk.Label(
    ventana,
    text="Simulación del Algoritmo: Suma de Colas (FIFO)",
    font=("Arial",18,"bold"),
    bg="#ECEFF1"
)
titulo.pack(pady=10)

canvas = tk.Canvas(
    ventana,
    width=820,
    height=300,
    bg="white",
    highlightthickness=2,
    highlightbackground="gray"
)
canvas.pack()

estado = tk.Label(
    ventana,
    text="Presione iniciar simulación",
    font=("Arial",12),
    bg="#ECEFF1"
)
estado.pack(pady=5)

btn = tk.Button(
    ventana,
    text="Iniciar Simulación",
    command=iniciar,
    bg="#42A5F5",
    fg="white",
    font=("Arial",11,"bold")
)
btn.pack(pady=5)



frame = tk.Frame(ventana, bg="#ECEFF1")
frame.pack(pady=10)

tk.Label(
    frame,
    text="Resultados de las sumas",
    font=("Arial",12,"bold"),
    bg="#ECEFF1"
).pack()

lista_resultados = tk.Listbox(
    frame,
    width=35,
    height=6,
    font=("Arial",11)
)
lista_resultados.pack()


dibujar()

ventana.mainloop()