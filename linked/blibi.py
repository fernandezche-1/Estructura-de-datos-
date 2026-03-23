class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    # Insertar al inicio
    def insert_at_beginning(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    # Insertar al final
    def insert_at_end(self, data):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            return

        current = self.head
        while current.next:
            current = current.next

        current.next = new_node

    # Insertar en una posición específica
    def insert_at_position(self, position, data):
        if position == 0:
            self.insert_at_beginning(data)
            return

        new_node = Node(data)
        current = self.head
        index = 0

        while current and index < position - 1:
            current = current.next
            index += 1

        if current is None:
            print("Posición fuera de rango")
            return

        new_node.next = current.next
        current.next = new_node

    # Mostrar lista
    def display(self):
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")

    # Buscar un valor
    def search(self, value):
        current = self.head
        position = 0

        while current:
            if current.data == value:
                return position
            current = current.next
            position += 1

        return -1

    # Eliminar un nodo
    def delete(self, value):
        current = self.head

        # Si es el primero
        if current and current.data == value:
            self.head = current.next
            return

        prev = None
        while current and current.data != value:
            prev = current
            current = current.next

        if current is None:
            print("Valor no encontrado")
            return

        prev.next = current.next

    # Obtener longitud
    def length(self):
        current = self.head
        count = 0

        while current:
            count += 1
            current = current.next

        return count

    # Invertir lista
    def reverse(self):
        prev = None
        current = self.head

        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node

        self.head = prev