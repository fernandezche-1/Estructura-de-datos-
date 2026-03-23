from blibi import LinkedList


def menu():
    lista = LinkedList()

    while True:
        print("\n--- MENÚ ---")
        print("1. Insertar al inicio")
        print("2. Insertar al final")
        print("3. Insertar en posición")
        print("4. Mostrar lista")
        print("5. Buscar elemento")
        print("6. Eliminar elemento")
        print("7. Longitud de la lista")
        print("8. Invertir lista")
        print("9. Salir")

        opcion = input("Selecciona una opción: ")

        if opcion == "1":
            dato = int(input("Dato: "))
            lista.insert_at_beginning(dato)

        elif opcion == "2":
            dato = int(input("Dato: "))
            lista.insert_at_end(dato)

        elif opcion == "3":
            pos = int(input("Posición: "))
            dato = int(input("Dato: "))
            lista.insert_at_position(pos, dato)

        elif opcion == "4":
            lista.display()

        elif opcion == "5":
            valor = int(input("Valor a buscar: "))
            pos = lista.search(valor)
            if pos != -1:
                print(f"Encontrado en posición {pos}")
            else:
                print("No encontrado")

        elif opcion == "6":
            valor = int(input("Valor a eliminar: "))
            lista.delete(valor)

        elif opcion == "7":
            print("Longitud:", lista.length())

        elif opcion == "8":
            lista.reverse()
            print("Lista invertida")

        elif opcion == "9":
            print("Saliendo...")
            break

        else:
            print("Opción inválida")


if __name__ == "__main__":
    menu()