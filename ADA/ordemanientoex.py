import json
import os

# ==========================================
# GUARDAR DATOS
# ==========================================

def guardar_datos(nombre_archivo, datos):
    # Obtener la carpeta donde está este archivo .py
    carpeta_actual = os.path.dirname(__file__)

    # Crear ruta completa
    ruta = os.path.join(carpeta_actual, nombre_archivo)

    with open(ruta, "w", encoding="utf-8") as archivo:
        json.dump(datos, archivo, indent=4)


# ==========================================
# LEER DATOS
# ==========================================

def leer_datos(nombre_archivo):
    # Obtener la carpeta donde está este archivo .py
    carpeta_actual = os.path.dirname(__file__)

    # Crear ruta completa
    ruta = os.path.join(carpeta_actual, nombre_archivo)

    with open(ruta, "r", encoding="utf-8") as archivo:
        datos = json.load(archivo)

    return datos


# ==========================================
# LEER VARIOS ARCHIVOS JSON
# ==========================================

def cargar_datos_automaticos(archivos):
    datos_totales = []

    # Obtener la carpeta donde está este archivo .py
    carpeta_actual = os.path.dirname(__file__)

    for nombre in archivos:
        # Crear ruta completa del archivo
        ruta = os.path.join(carpeta_actual, nombre)

        with open(ruta, "r", encoding="utf-8") as archivo:
            datos = json.load(archivo)
            datos_totales.extend(datos)

    return datos_totales


# ==========================================
# INTERCALACIÓN
# ==========================================

def intercalacion(lista1, lista2):
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


# ==========================================
# MEZCLA DIRECTA
# ==========================================

def mezcla_directa(nombre_archivo):
    datos = leer_datos(nombre_archivo)

    datos.sort()

    guardar_datos(nombre_archivo, datos)

    return datos


# ==========================================
# MEZCLA EQUILIBRADA
# ==========================================

def mezcla_equilibrada(nombre_archivo):
    datos = leer_datos(nombre_archivo)

    mitad = len(datos) // 2

    izquierda = sorted(datos[:mitad])
    derecha = sorted(datos[mitad:])

    resultado = intercalacion(izquierda, derecha)

    guardar_datos(nombre_archivo, resultado)

    return resultado