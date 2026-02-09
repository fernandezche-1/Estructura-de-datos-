class Ventas:
    def __init__(self):
        self.meses = [
            "Enero", "Febrero", "Marzo", "Abril",
            "Mayo", "Junio", "Julio", "Agosto",
            "Septiembre", "Octubre", "Noviembre", "Diciembre"
        ]

        self.departamentos = ["Ropa", "Deportes", "Juguetería"]

        # Arreglo bidimensional con datos iniciales
        self.ventas = [
            [1200, 800, 600],
            [1500, 900, 700],
            [1300, 850, 650],
            [1600, 1000, 900],
            [1700, 1100, 950],
            [1800, 1200, 1000],
            [2000, 1300, 1100],
            [2100, 1400, 1200],
            [1900, 1250, 1050],
            [2200, 1500, 1300],
            [2300, 1600, 1400],
            [2500, 1800, 1600]
        ]

    def insertar(self, mes, departamento, monto):
        fila = self.meses.index(mes)
        columna = self.departamentos.index(departamento)
        self.ventas[fila][columna] = monto

    def buscar(self, mes, departamento):
        fila = self.meses.index(mes)
        columna = self.departamentos.index(departamento)
        return self.ventas[fila][columna]

    def eliminar(self, mes, departamento):
        fila = self.meses.index(mes)
        columna = self.departamentos.index(departamento)
        self.ventas[fila][columna] = 0

    def mostrar_tabla(self):
        print("\nMes          Ropa      Deportes     Juguetería")
        print("-" * 50)
        for i in range(12):
            print(f"{self.meses[i]:12} {self.ventas[i][0]:8} {self.ventas[i][1]:12} {self.ventas[i][2]:12}")


# -------- PROGRAMA PRINCIPAL --------
ventas = Ventas()
opcion = 0

while opcion != 5:
    print("\nMENÚ DE OPCIONES")
    print("1. Insertar venta")
    print("2. Buscar venta")
    print("3. Eliminar venta")
    print("4. Mostrar tabla")
    print("5. Salir")

    opcion = int(input("Seleccione una opción: "))

    if opcion == 1:
        mes = input("Ingrese el mes: ")
        departamento = input("Ingrese el departamento (Ropa, Deportes, Juguetería): ")
        monto = float(input("Ingrese el monto: "))
        ventas.insertar(mes, departamento, monto)
        print("Venta insertada correctamente.")

    elif opcion == 2:
        mes = input("Ingrese el mes: ")
        departamento = input("Ingrese el departamento (Ropa, Deportes, Juguetería): ")
        resultado = ventas.buscar(mes, departamento)
        print("Venta encontrada:", resultado)

    elif opcion == 3:
        mes = input("Ingrese el mes: ")
        departamento = input("Ingrese el departamento (Ropa, Deportes, Juguetería): ")
        ventas.eliminar(mes, departamento)
        print("Venta eliminada correctamente.")

    elif opcion == 4:
        ventas.mostrar_tabla()
}
    elif opcion == 5:
        print("Programa finalizado.")

    else:
        print("Opción no válida.")
