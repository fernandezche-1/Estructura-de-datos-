"""
Ejemplo interactivo de búsqueda binaria
El usuario puede ingresar datos, generarlos aleatoriamente y buscar valores
"""

from busqueda_binaria import BusquedaBinaria
import random


def mostrar_menu():
    """Muestra el menú principal"""
    print("\n" + "=" * 60)
    print("BÚSQUEDA BINARIA - MENÚ PRINCIPAL")
    print("=" * 60)
    print("1. Ingresar datos manualmente")
    print("2. Generar datos aleatorios")
    print("3. Buscar un valor en el arreglo actual")
    print("4. Mostrar arreglo actual")
    print("5. Ordenar arreglo (necesario para búsqueda binaria)")
    print("6. Salir")
    print("=" * 60)


def ingresar_datos_manual():
    """Permite al usuario ingresar datos manualmente"""
    print("\n--- INGRESO MANUAL DE DATOS ---")
    
    while True:
        try:
            cantidad = int(input("¿Cuántos datos deseas ingresar? "))
            if cantidad <= 0:
                print("❌ La cantidad debe ser mayor a 0. Intenta de nuevo.")
                continue
            break
        except ValueError:
            print("❌ Por favor, ingresa un número válido.")
    
    datos = []
    print(f"\nIngresa {cantidad} número(s):")
    for i in range(cantidad):
        while True:
            try:
                valor = float(input(f"Dato {i+1}: "))
                datos.append(valor)
                break
            except ValueError:
                print("❌ Ingresa un número válido.")
    
    return datos


def generar_datos_aleatorios():
    """Genera datos aleatorios según especificaciones del usuario"""
    print("\n--- GENERACIÓN DE DATOS ALEATORIOS ---")
    
    while True:
        try:
            cantidad = int(input("¿Cuántos datos aleatorios deseas generar? "))
            if cantidad <= 0:
                print("❌ La cantidad debe ser mayor a 0. Intenta de nuevo.")
                continue
            break
        except ValueError:
            print("❌ Por favor, ingresa un número válido.")
    
    while True:
        try:
            min_val = float(input("Valor mínimo: "))
            max_val = float(input("Valor máximo: "))
            if min_val >= max_val:
                print("❌ El valor mínimo debe ser menor que el máximo. Intenta de nuevo.")
                continue
            break
        except ValueError:
            print("❌ Por favor, ingresa números válidos.")
    
    # Generar datos aleatorios (enteros o decimales según el caso)
    if min_val.is_integer() and max_val.is_integer():
        datos = [random.randint(int(min_val), int(max_val)) for _ in range(cantidad)]
    else:
        datos = [round(random.uniform(min_val, max_val), 2) for _ in range(cantidad)]
    
    print(f"\n✅ Se generaron {cantidad} datos aleatorios.")
    return datos


def mostrar_arreglo(arreglo, ordenado=False):
    """Muestra el arreglo de forma formateada"""
    if not arreglo:
        print("⚠️ El arreglo está vacío.")
        return
    
    print("\n--- ARREGLO ACTUAL ---")
    print(f"Tamaño: {len(arreglo)} elementos")
    print(f"Ordenado: {'Sí' if ordenado else 'No'}")
    
    # Mostrar datos en filas de 10 elementos
    for i in range(0, len(arreglo), 10):
        segmento = arreglo[i:i+10]
        indices = [str(j) for j in range(i, min(i+10, len(arreglo)))]
        print(f"Índices: {', '.join(indices):<30}")
        print(f"Valores: {', '.join(str(x) for x in segmento)}")
        print()


def buscar_valor(arreglo):
    """Permite al usuario buscar un valor en el arreglo usando búsqueda binaria"""
    if not arreglo:
        print("\n⚠️ No hay datos para buscar. Primero ingresa o genera datos.")
        return
    
    # Verificar si el arreglo está ordenado
    esta_ordenado = all(arreglo[i] <= arreglo[i+1] for i in range(len(arreglo)-1))
    
    if not esta_ordenado:
        print("\n⚠️ EL ARREGLO NO ESTÁ ORDENADO.")
        print("La búsqueda binaria SOLO funciona con arreglos ordenados.")
        respuesta = input("¿Deseas ordenar el arreglo automáticamente? (s/n): ").lower()
        if respuesta == 's':
            arreglo.sort()
            print("✅ Arreglo ordenado exitosamente.")
            mostrar_arreglo(arreglo, True)
        else:
            print("❌ No se puede realizar la búsqueda binaria. Usa la opción 5 para ordenar.")
            return
    
    # Solicitar valor a buscar
    print("\n--- BÚSQUEDA DE VALOR ---")
    while True:
        try:
            valor_buscar = input("Ingresa el valor que deseas buscar (o 'cancelar' para volver): ")
            if valor_buscar.lower() == 'cancelar':
                return
            
            # Convertir a número (entero o flotante)
            if '.' in valor_buscar:
                valor_buscar = float(valor_buscar)
            else:
                valor_buscar = int(valor_buscar)
            break
        except ValueError:
            print("❌ Ingresa un número válido o 'cancelar'.")
    
    # Realizar búsqueda binaria
    print(f"\n🔍 Buscando {valor_buscar} en el arreglo...")
    
    # Usar diferentes métodos de búsqueda según lo que quiera el usuario
    print("\n--- MÉTODOS DE BÚSQUEDA DISPONIBLES ---")
    print("1. Búsqueda binaria estándar (primera ocurrencia)")
    print("2. Búsqueda binaria recursiva")
    print("3. Encontrar elemento más cercano")
    print("4. Encontrar TODAS las ocurrencias (si hay duplicados)")
    
    opcion = input("\nElige un método (1-4): ")
    
    resultado = None
    if opcion == '1':
        indice = BusquedaBinaria.buscar_iterativo(arreglo, valor_buscar)
        if indice is not None:
            print(f"\n✅ ¡ÉXITO! El valor {valor_buscar} se encuentra en el índice {indice}")
            print(f"   Valor en esa posición: {arreglo[indice]}")
        else:
            print(f"\n❌ FRACASO. El valor {valor_buscar} NO se encuentra en el arreglo.")
            # Sugerir valores cercanos
            cercano = BusquedaBinaria.buscar_mas_cercano(arreglo, valor_buscar)
            print(f"   💡 Valor más cercano encontrado: {cercano}")
    
    elif opcion == '2':
        indice = BusquedaBinaria.buscar_recursivo(arreglo, valor_buscar)
        if indice is not None:
            print(f"\n✅ ¡ÉXITO! El valor {valor_buscar} se encuentra en el índice {indice}")
            print(f"   Valor en esa posición: {arreglo[indice]}")
        else:
            print(f"\n❌ FRACASO. El valor {valor_buscar} NO se encuentra en el arreglo.")
            cercano = BusquedaBinaria.buscar_mas_cercano(arreglo, valor_buscar)
            print(f"   💡 Valor más cercano encontrado: {cercano}")
    
    elif opcion == '3':
        cercano = BusquedaBinaria.buscar_mas_cercano(arreglo, valor_buscar)
        print(f"\n🔹 El valor más cercano a {valor_buscar} es: {cercano}")
        if cercano == valor_buscar:
            print("   ✅ (El valor existe exactamente en el arreglo)")
        else:
            print("   ⚠️ (El valor no existe exactamente, pero este es el más cercano)")
    
    elif opcion == '4':
        indices = BusquedaBinaria.buscar_todos(arreglo, valor_buscar)
        if indices:
            print(f"\n✅ Se encontraron {len(indices)} ocurrencia(s) del valor {valor_buscar}")
            print(f"   Índices: {indices}")
            for i in indices:
                print(f"   Posición {i}: {arreglo[i]}")
        else:
            print(f"\n❌ El valor {valor_buscar} NO se encuentra en el arreglo.")
            cercano = BusquedaBinaria.buscar_mas_cercano(arreglo, valor_buscar)
            print(f"   💡 Valor más cercano encontrado: {cercano}")
    
    else:
        print("❌ Opción no válida.")


def ordenar_arreglo(arreglo):
    """Ordena el arreglo actual"""
    if not arreglo:
        print("\n⚠️ No hay datos para ordenar. Primero ingresa o genera datos.")
        return arreglo
    
    print("\n--- ORDENAMIENTO DEL ARREGLO ---")
    print(f"Arreglo actual (tamaño: {len(arreglo)})")
    
    respuesta = input("¿Deseas ordenar el arreglo de forma ascendente? (s/n): ").lower()
    if respuesta == 's':
        arreglo.sort()
        print("✅ Arreglo ordenado exitosamente (ascendente).")
        mostrar_arreglo(arreglo, True)
    else:
        print("❌ Ordenamiento cancelado.")
    
    return arreglo


def main():
    """Función principal del programa interactivo"""
    print("=" * 60)
    print("BIENVENIDO AL SISTEMA DE BÚSQUEDA BINARIA")
    print("=" * 60)
    print("\n📌 NOTA IMPORTANTE: La búsqueda binaria SOLO funciona")
    print("   con arreglos ORDENADOS de forma ASCENDENTE.\n")
    
    datos = []
    
    while True:
        mostrar_menu()
        opcion = input("Elige una opción (1-6): ")
        
        if opcion == '1':
            datos = ingresar_datos_manual()
            mostrar_arreglo(datos, False)
        
        elif opcion == '2':
            datos = generar_datos_aleatorios()
            mostrar_arreglo(datos, False)
        
        elif opcion == '3':
            buscar_valor(datos)
        
        elif opcion == '4':
            if datos:
                esta_ordenado = all(datos[i] <= datos[i+1] for i in range(len(datos)-1))
                mostrar_arreglo(datos, esta_ordenado)
            else:
                print("\n⚠️ No hay datos cargados. Usa la opción 1 o 2 primero.")
        
        elif opcion == '5':
            datos = ordenar_arreglo(datos)
        
        elif opcion == '6':
            print("\n👋 ¡Gracias por usar el sistema de búsqueda binaria!")
            break
        
        else:
            print("\n❌ Opción no válida. Por favor, elige una opción del 1 al 6.")
        
        input("\nPresiona Enter para continuar...")


if __name__ == "__main__":
    main()