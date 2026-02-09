import random
import time
import sys

# =============================
# INICIO DE MEDICIÓN DE TIEMPO
# =============================
inicio_tiempo = time.time()

TOTAL_ALUMNOS = 100_000
TOTAL_MATERIAS = 10_000

# Crear matriz: filas = materias, columnas = alumnos
# (Advertencia: esto consume MUCHA memoria)
matriz = [
    [random.randint(0, 10) for _ in range(TOTAL_ALUMNOS)]
    for _ in range(TOTAL_MATERIAS)
]

# Entrada del usuario
alumno = int(input("Ingresa el número del alumno (1 a 100000): "))
materia = int(input("Ingresa el número de la materia (1 a 10000): "))

if not (1 <= alumno <= TOTAL_ALUMNOS and 1 <= materia <= TOTAL_MATERIAS):
    print("Alumno o materia fuera de rango")
    sys.exit()

# Rangos visibles (tabla parcial)
col_inicio = max(0, alumno - 4)
col_fin = min(TOTAL_ALUMNOS, alumno + 3)

fila_inicio = max(0, materia - 4)
fila_fin = min(TOTAL_MATERIAS, materia + 3)

# =============================
# IMPRESIÓN EN FORMATO TABLA
# =============================
print("\nTABLA DE CALIFICACIONES (Vista Parcial)\n")

# Encabezado
print("Materia \\ Alumno", end="  ")
for a in range(col_inicio, col_fin):
    print(f"A{a+1:^7}", end=" ")
print()

print("-" * (20 + (col_fin - col_inicio) * 9))

# Filas (materias)
for m in range(fila_inicio, fila_fin):
    print(f"Materia {m+1:<6} ", end="")
    for a in range(col_inicio, col_fin):
        valor = matriz[m][a]
        if m == materia - 1 and a == alumno - 1:
            print(f"[{valor:^5}]", end=" ")
        else:
            print(f" {valor:^5} ", end=" ")
    print()

# =============================
# FIN DE MEDICIÓN DE TIEMPO
# =============================
fin_tiempo = time.time()

# Resultado puntual
print("\nRESULTADO BUSCADO")
print("------------------------------")
print(f"Alumno {alumno}")
print(f"Materia {materia}")
print(f"Calificación: {matriz[materia-1][alumno-1]}")

print("\nTIEMPO DE EJECUCIÓN")
print("------------------------------")
print(f"{fin_tiempo - inicio_tiempo:.4f} segundos")