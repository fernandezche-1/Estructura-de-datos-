import time

class Pila:
    def __init__(self):
        self.items = []

    def push(self, dato):
        self.items.append(dato)

    def pop(self):
        if self.items:
            return self.items.pop()

    def mostrar(self):
        return self.items



torreA = Pila()
torreB = Pila()
torreC = Pila()

movimientos = []



def mostrar_torres():

    print("\nEstado actual de las torres:")
    print("A:", torreA.mostrar())
    print("B:", torreB.mostrar())
    print("C:", torreC.mostrar())
    print("---------------------------")



def mover(origen, destino, nombre_origen, nombre_destino):

    elemento = origen.pop()
    destino.push(elemento)

    print(f"Mover disco {elemento} de {nombre_origen} → {nombre_destino}")

    mostrar_torres()

    time.sleep(0.8)   



def ejecutar_movimientos():

    while movimientos:

        origen, destino, no, nd = movimientos.pop(0)

        mover(origen, destino, no, nd)



def hanoi(n, origen, auxiliar, destino, no, na, nd):

    if n == 1:
        movimientos.append((origen, destino, no, nd))
        return

    hanoi(n-1, origen, destino, auxiliar, no, nd, na)

    movimientos.append((origen, destino, no, nd))

    hanoi(n-1, auxiliar, origen, destino, na, no, nd)



print("\nTORRES DE HANOI CON PILAS\n")

n = int(input("Ingrese número de discos: "))


for i in range(n,0,-1):
    torreA.push(i)

mostrar_torres()


hanoi(n, torreA, torreB, torreC, "A", "B", "C")

print("\nIniciando movimientos...\n")

ejecutar_movimientos()

print("\nProceso terminado.")