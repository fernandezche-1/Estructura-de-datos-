Este programa en Python implementa un sistema de control de ventas mensuales utilizando una matriz bidimensional (arreglo 3x12).
Permite registrar, consultar, eliminar y visualizar las ventas de tres departamentos a lo largo de doce meses del año.

Los departamentos considerados son:

Ropa

Deportes

Juguetería

Cada fila de la matriz representa un departamento y cada columna corresponde a un mes.

Estructura del programa

El programa está organizado en:

Constantes para departamentos y meses

Una clase principal llamada VentasMensuales

Un menú interactivo para que el usuario use el sistema desde consola

Explicación de la clase y métodos
Clase VentasMensuales

Esta clase administra la matriz de ventas y contiene los métodos para manipularla.

__init__(self)

Inicializa la matriz ventas con valores en cero.
La matriz tiene:

3 filas (departamentos)

12 columnas (meses)
self.ventas = [[0 for _ in range(12)] for _ in range(3)]
visualizar_tabla(self)

Muestra en pantalla una tabla completa con:

Los departamentos en filas

Los meses como encabezados

Las ventas registradas en formato monetario

Sirve para ver de manera clara todas las ventas almacenadas.

insertar_modificar(self)

Permite al usuario:

Elegir un departamento

Elegir un mes

Ingresar el monto de la venta

Si la venta ya existía, el valor se modifica; si no, se inserta.
Usa los métodos index() para localizar la posición correcta en la matriz.

buscar_venta(self)

Permite consultar una venta específica ingresando:

Departamento

Mes

El programa muestra el monto registrado para esa combinación.

eliminar_venta(self)

Permite eliminar una venta específica:

Ubica el departamento y mes

Reemplaza el monto por 0

Esto simula la eliminación del registro dentro de la matriz.

Menú principal

La función menu() muestra un menú interactivo que permite al usuario elegir entre:

Insertar o modificar una venta

Buscar una venta

Eliminar una venta

Visualizar la tabla completa

Salir del programa

El menú se repite hasta que el usuario decide salir.
