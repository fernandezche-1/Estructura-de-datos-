import heapq

def shell_sort(arr):
    n = len(arr)
    gap = n // 2
    
    while gap > 0:
        for i in range(gap, n):
            temp = arr[i]
            j = i
            while j >= gap and arr[j - gap] > temp:
                arr[j] = arr[j - gap]
                j -= gap
            arr[j] = temp
        gap //= 2
    return arr


def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quick_sort(left) + middle + quick_sort(right)


def heap_sort(arr):
    heapq.heapify(arr)
    return [heapq.heappop(arr) for _ in range(len(arr))]


def radix_sort(arr):
    if len(arr) == 0:
        return arr
    
    max_num = max(arr)
    exp = 1
    
    while max_num // exp > 0:
        counting_sort(arr, exp)
        exp *= 10
    
    return arr


def counting_sort(arr, exp):
    n = len(arr)
    output = [0] * n
    count = [0] * 10
    
    for i in range(n):
        index = arr[i] // exp
        count[index % 10] += 1
    
    for i in range(1, 10):
        count[i] += count[i - 1]
    
    i = n - 1
    while i >= 0:
        index = arr[i] // exp
        output[count[index % 10] - 1] = arr[i]
        count[index % 10] -= 1
        i -= 1
    
    for i in range(n):
        arr[i] = output[i]



def main():
    while True:
        print("\n===== MENÚ DE ORDENAMIENTO =====")
        print("1. ShellSort")
        print("2. QuickSort")
        print("3. HeapSort")
        print("4. RadixSort")
        print("5. Salir")
        
        opcion = int(input("Elige una opción: "))
        
        if opcion == 5:
            print("Saliendo...")
            break
        
        n = int(input("¿Cuántos números deseas ingresar? "))
        lista = []
        
        for i in range(n):
            num = int(input(f"Ingrese número {i+1}: "))
            lista.append(num)
        
        if opcion == 1:
            resultado = shell_sort(lista.copy())
        elif opcion == 2:
            resultado = quick_sort(lista.copy())
        elif opcion == 3:
            resultado = heap_sort(lista.copy())
        elif opcion == 4:
            resultado = radix_sort(lista.copy())
        else:
            print("Opción inválida")
            continue
        
        print("Lista ordenada:", resultado)


if __name__ == "__main__":
    main()