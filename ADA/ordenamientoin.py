# ==========================================
# LIBRERÍA DE ORDENACIÓN INTERNA
# ==========================================

# ==========================================
# MÉTODO BURBUJA
# ==========================================

def burbuja(arr):

    datos = arr.copy()

    n = len(datos)

    for i in range(n):

        for j in range(0, n - i - 1):

            if datos[j] > datos[j + 1]:

                datos[j], datos[j + 1] = datos[j + 1], datos[j]

    return datos


# ==========================================
# MÉTODO INSERCIÓN
# ==========================================

def insercion(arr):

    datos = arr.copy()

    for i in range(1, len(datos)):

        clave = datos[i]

        j = i - 1

        while j >= 0 and clave < datos[j]:

            datos[j + 1] = datos[j]

            j -= 1

        datos[j + 1] = clave

    return datos


# ==========================================
# MÉTODO SELECCIÓN
# ==========================================

def selection_sort(arr):

    datos = arr.copy()

    for i in range(len(datos)):

        min_idx = i

        for j in range(i + 1, len(datos)):

            if datos[j] < datos[min_idx]:

                min_idx = j

        datos[i], datos[min_idx] = datos[min_idx], datos[i]

    return datos


# ==========================================
# MÉTODO SHELL SORT
# ==========================================

def shell_sort(arr):

    datos = arr.copy()

    gap = len(datos) // 2

    while gap > 0:

        for i in range(gap, len(datos)):

            temp = datos[i]

            j = i

            while j >= gap and datos[j - gap] > temp:

                datos[j] = datos[j - gap]

                j -= gap

            datos[j] = temp

        gap //= 2

    return datos


# ==========================================
# MÉTODO QUICK SORT
# ==========================================

def quick_sort(arr):

    if len(arr) <= 1:
        return arr

    pivote = arr[len(arr) // 2]

    izquierda = [x for x in arr if x < pivote]
    centro = [x for x in arr if x == pivote]
    derecha = [x for x in arr if x > pivote]

    return quick_sort(izquierda) + centro + derecha


# ==========================================
# MÉTODO HEAPIFY
# ==========================================

def heapify(arr, n, i):

    mayor = i

    izq = 2 * i + 1

    der = 2 * i + 2

    if izq < n and arr[izq] > arr[mayor]:

        mayor = izq

    if der < n and arr[der] > arr[mayor]:

        mayor = der

    if mayor != i:

        arr[i], arr[mayor] = arr[mayor], arr[i]

        heapify(arr, n, mayor)


# ==========================================
# MÉTODO HEAP SORT
# ==========================================

def heap_sort(arr):

    datos = arr.copy()

    n = len(datos)

    for i in range(n // 2 - 1, -1, -1):

        heapify(datos, n, i)

    for i in range(n - 1, 0, -1):

        datos[i], datos[0] = datos[0], datos[i]

        heapify(datos, i, 0)

    return datos


# ==========================================
# MÉTODO COUNTING SORT
# ==========================================

def counting_sort(arr, exp):

    n = len(arr)

    salida = [0] * n

    conteo = [0] * 10

    for i in arr:

        indice = i // exp

        conteo[indice % 10] += 1

    for i in range(1, 10):

        conteo[i] += conteo[i - 1]

    i = n - 1

    while i >= 0:

        indice = arr[i] // exp

        salida[conteo[indice % 10] - 1] = arr[i]

        conteo[indice % 10] -= 1

        i -= 1

    for i in range(n):

        arr[i] = salida[i]


# ==========================================
# MÉTODO RADIX SORT
# ==========================================

def radix_sort(arr):

    datos = arr.copy()

    maximo = max(datos)

    exp = 1

    while maximo // exp > 0:

        counting_sort(datos, exp)

        exp *= 10

    return datos