def kruskal(nodos, aristas):
    parent = {nodo: nodo for nodo in nodos}

    def find(nodo):
        if parent[nodo] != nodo:
            parent[nodo] = find(parent[nodo])
        return parent[nodo]

    def union(nodo1, nodo2):
        raiz1 = find(nodo1)
        raiz2 = find(nodo2)
        if raiz1 != raiz2:
            parent[raiz2] = raiz1

    aristas.sort(key=lambda x: x[2])
    arbol = []
    costo_total = 0

    for u, v, peso in aristas:
        if find(u) != find(v):
            union(u, v)
            arbol.append((u, v, peso))
            costo_total += peso

    return arbol, costo_total


# Ejemplo
nodos = ['A', 'B', 'C', 'D']
aristas = [
    ('A', 'B', 1),
    ('A', 'C', 4),
    ('B', 'C', 2),
    ('B', 'D', 5),
    ('C', 'D', 3)
]

arbol, costo = kruskal(nodos, aristas)

print("Kruskal (Árbol de expansión mínima):")
print("Aristas:", arbol)
print("Costo total:", costo)