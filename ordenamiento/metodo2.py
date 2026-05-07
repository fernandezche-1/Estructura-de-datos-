from tkinter import *
from tkinter import ttk, messagebox
import json


# ==================================================
# CARGAR DATOS JSON
# ==================================================

def cargar_json():

    try:

        with open("datos.json", "r") as archivo:

            datos = json.load(archivo)

            return datos

    except:

        messagebox.showerror(
            "Error",
            "No se pudo leer el archivo JSON"
        )

        return None


# ==================================================
# GUARDAR DATOS JSON
# ==================================================

def guardar_json(lista1, lista2):

    datos = {

        "lista1": lista1,
        "lista2": lista2

    }

    with open("datos.json", "w") as archivo:

        json.dump(datos, archivo, indent=4)


# ==================================================
# INTERCALACION
# ==================================================

def intercalacion(lista1, lista2):

    lista1.sort()
    lista2.sort()

    resultado = []

    i = 0
    j = 0

    while i < len(lista1) and j < len(lista2):

        if lista1[i] < lista2[j]:

            resultado.append(lista1[i])
            i += 1

        else:

            resultado.append(lista2[j])
            j += 1

    while i < len(lista1):

        resultado.append(lista1[i])
        i += 1

    while j < len(lista2):

        resultado.append(lista2[j])
        j += 1

    return resultado


# ==================================================
# MEZCLA DIRECTA
# ==================================================

def mezcla_directa(lista):

    if len(lista) > 1:

        medio = len(lista) // 2

        izquierda = lista[:medio]
        derecha = lista[medio:]

        mezcla_directa(izquierda)
        mezcla_directa(derecha)

        i = 0
        j = 0
        k = 0

        while i < len(izquierda) and j < len(derecha):

            if izquierda[i] < derecha[j]:

                lista[k] = izquierda[i]
                i += 1

            else:

                lista[k] = derecha[j]
                j += 1

            k += 1

        while i < len(izquierda):

            lista[k] = izquierda[i]
            i += 1
            k += 1

        while j < len(derecha):

            lista[k] = derecha[j]
            j += 1
            k += 1


# ==================================================
# MEZCLA EQUILIBRADA
# ==================================================

def mezcla_equilibrada(lista):

    if len(lista) <= 1:

        return lista

    mitad = len(lista) // 2

    izquierda = mezcla_equilibrada(lista[:mitad])
    derecha = mezcla_equilibrada(lista[mitad:])

    return mezclar(izquierda, derecha)


def mezclar(izquierda, derecha):

    resultado = []

    i = 0
    j = 0

    while i < len(izquierda) and j < len(derecha):

        if izquierda[i] < derecha[j]:

            resultado.append(izquierda[i])
            i += 1

        else:

            resultado.append(derecha[j])
            j += 1

    resultado.extend(izquierda[i:])
    resultado.extend(derecha[j:])

    return resultado


# ==================================================
# EJECUTAR
# ==================================================

def ejecutar():

    datos = cargar_json()

    if datos is None:
        return

    lista1 = datos["lista1"]
    lista2 = datos["lista2"]

    metodo = combo.get()

    if metodo == "Intercalacion":

        resultado = intercalacion(lista1, lista2)

    elif metodo == "Mezcla Directa":

        mezcla_directa(lista1)

        resultado = lista1

    elif metodo == "Mezcla Equilibrada":

        resultado = mezcla_equilibrada(lista1)

    else:

        messagebox.showwarning(
            "Aviso",
            "Seleccione un metodo"
        )

        return

    salida.config(
        text=str(resultado)
    )


# ==================================================
# VENTANA
# ==================================================

ventana = Tk()

ventana.title("Ordenamiento con JSON")
ventana.geometry("700x500")
ventana.config(bg="#0F172A")


# ==================================================
# TITULO
# ==================================================

titulo = Label(
    ventana,
    text="ORDENAMIENTO CON ARCHIVOS JSON",
    bg="#0F172A",
    fg="white",
    font=("Arial", 22, "bold")
)

titulo.pack(pady=20)


# ==================================================
# COMBOBOX
# ==================================================

combo = ttk.Combobox(
    ventana,
    values=[
        "Intercalacion",
        "Mezcla Directa",
        "Mezcla Equilibrada"
    ],
    state="readonly",
    width=30,
    font=("Arial", 12)
)

combo.pack(pady=20)


# ==================================================
# BOTON
# ==================================================

boton = Button(
    ventana,
    text="EJECUTAR",
    bg="#2563EB",
    fg="white",
    font=("Arial", 14, "bold"),
    width=20,
    height=2,
    command=ejecutar
)

boton.pack(pady=20)


# ==================================================
# RESULTADO
# ==================================================

salida = Label(
    ventana,
    text="Resultado...",
    bg="#1E293B",
    fg="#22C55E",
    font=("Consolas", 16, "bold"),
    width=40,
    height=6
)

salida.pack(pady=30)


# ==================================================
# FOOTER
# ==================================================

footer = Label(
    ventana,
    text="Python + JSON + Tkinter",
    bg="#0F172A",
    fg="gray",
    font=("Arial", 10)
)

footer.pack(side="bottom", pady=10)


# ==================================================
# INICIO
# ==================================================

ventana.mainloop()