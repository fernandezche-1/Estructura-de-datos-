from ordenamientoin import *
from ordemanientoex import *

# ==========================================
# PROGRAMA PRINCIPAL
# ==========================================

def menu():

    # Archivos JSON automáticos
    archivos = [
        "datos1.json",
        "datos2.json"
    ]

    # Cargar datos automáticamente
    datos = cargar_datos_automaticos(archivos)

    while True:

        print("\n===================================")
        print("      MENÚ DE ORDENAMIENTOS")
        print("===================================")

        # =================================
        # MÉTODOS INTERNOS
        # =================================

        print("\n--- MÉTODOS DE ORDENAMIENTO INTERNO ---")
        print("1. Burbuja")
        print("2. Insercion")
        print("3. Seleccion")
        print("4. Shell Sort")
        print("5. Quick Sort")
        print("6. Heap Sort")
        print("7. Radix Sort")

        # =================================
        # MÉTODOS EXTERNOS
        # =================================

        print("\n--- MÉTODOS DE ORDENAMIENTO EXTERNO ---")
        print("8. Intercalación")
        print("9. Mezcla Directa")
        print("10. Mezcla Equilibrada")

        # =================================
        # SALIR
        # =================================

        print("\n11. Salir")

        opcion = input("Seleccione una opción: ")

        # =================================
        # INTERNOS
        # =================================

        if opcion == "1":

            print("Resultado:")
            print(burbuja(datos))

        elif opcion == "2":

            print("Resultado:")
            print(insercion(datos))

        elif opcion == "3":

            print("Resultado:")
            print(selection_sort(datos))

        elif opcion == "4":

            print("Resultado:")
            print(shell_sort(datos))

        elif opcion == "5":

            print("Resultado:")
            print(quick_sort(datos))

        elif opcion == "6":

            print("Resultado:")
            print(heap_sort(datos))

        elif opcion == "7":

            print("Resultado:")
            print(radix_sort(datos))

        # =================================
        # EXTERNOS
        # =================================

        elif opcion == "8":

            datos1 = leer_datos("datos1.json")
            datos2 = leer_datos("datos2.json")

            resultado = intercalacion(datos1, datos2)

            print("Resultado:")
            print(resultado)

        elif opcion == "9":

            datos_completos = cargar_datos_automaticos(archivos)

            guardar_datos("datos.json", datos_completos)

            resultado = mezcla_directa("datos.json")

            print("Resultado:")
            print(resultado)

        elif opcion == "10":

            datos_completos = cargar_datos_automaticos(archivos)

            guardar_datos("datos.json", datos_completos)

            resultado = mezcla_equilibrada("datos.json")

            print("Resultado:")
            print(resultado)

        # =================================
        # SALIR
        # =================================

        elif opcion == "11":

            print("Programa finalizado")
            break

        # =================================
        # ERROR
        # =================================

        else:

            print("Opción inválida")


# ==========================================
# EJECUTAR PROGRAMA
# ==========================================

menu()