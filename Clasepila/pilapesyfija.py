class Pila:

    def __init__(self):
        self.items = []

    def push(self, dato):
        self.items.append(dato)

    def pop(self):
        if not self.vacia():
            return self.items.pop()

    def vacia(self):
        return len(self.items) == 0

    def mostrar(self):
        return self.items



def evaluar_posfija(expresion):

    pila = Pila()
    tokens = expresion.split()

    print("\nEvaluando expresión POSFIJA...\n")

    for token in tokens:

        if token.isdigit():

            pila.push(int(token))
            print("Push:", token, "→ Pila:", pila.mostrar())

        else:

            b = pila.pop()
            a = pila.pop()

            if token == '+':
                r = a + b
            elif token == '-':
                r = a - b
            elif token == '*':
                r = a * b
            elif token == '/':
                r = a / b

            pila.push(r)

            print(a, token, b, "=", r, "→ Pila:", pila.mostrar())

    return pila.pop()



def evaluar_prefija(expresion):

    pila = Pila()
    tokens = expresion.split()

    tokens = tokens[::-1]

    print("\nEvaluando expresión PREFIJA...\n")

    for token in tokens:

        if token.isdigit():

            pila.push(int(token))
            print("Push:", token, "→ Pila:", pila.mostrar())

        else:

            a = pila.pop()
            b = pila.pop()

            if token == '+':
                r = a + b
            elif token == '-':
                r = a - b
            elif token == '*':
                r = a * b
            elif token == '/':
                r = a / b

            pila.push(r)

            print(a, token, b, "=", r, "→ Pila:", pila.mostrar())

    return pila.pop()



print("\nEVALUADOR DE EXPRESIONES CON PILAS\n")

print("1. Evaluar expresión POSFIJA")
print("2. Evaluar expresión PREFIJA")

opcion = int(input("\nSeleccione una opción: "))

exp = input("\nIngrese la expresión separada por espacios: ")

if opcion == 1:
    resultado = evaluar_posfija(exp)

elif opcion == 2:
    resultado = evaluar_prefija(exp)

else:
    print("Opción inválida")
    exit()

print("\nResultado final:", resultado)