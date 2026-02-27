import time

def fibonacci_recursivo(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci_recursivo(n-1) + fibonacci_recursivo(n-2)

def fibonacci_iterativo(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    
    a, b = 0, 1
    for i in range(2, n + 1):
        a, b = b, a + b
    return b

n = int(input("Ingrese un número: "))


inicio = time.time()
resultado_rec = fibonacci_recursivo(n)
fin = time.time()
tiempo_rec = fin - inicio

inicio = time.time()
resultado_it = fibonacci_iterativo(n)
fin = time.time()
tiempo_it = fin - inicio

print("\nResultado Recursivo:", resultado_rec)
print("Tiempo Recursivo:", tiempo_rec, "segundos")

print("\nResultado Iterativo:", resultado_it)
print("Tiempo Iterativo:", tiempo_it, "segundos")