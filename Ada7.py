import itertools
import networkx as nx
import matplotlib.pyplot as plt

grafo = {
    "Yucatan": {"Campeche": 180, "Quintana Roo": 200},
    "Campeche": {"Yucatan": 180, "Tabasco": 300},
    "Quintana Roo": {"Yucatan": 200, "Chiapas": 450},
    "Tabasco": {"Campeche": 300, "Veracruz": 250, "Chiapas": 200},
    "Chiapas": {"Tabasco": 200, "Oaxaca": 350, "Quintana Roo": 450},
    "Veracruz": {"Tabasco": 250, "Oaxaca": 200},
    "Oaxaca": {"Veracruz": 200, "Chiapas": 350}
}

def mostrar_grafo():
    for estado, conexiones in grafo.items():
        for destino, costo in conexiones.items():
            print(f"{estado} -> {destino} : {costo} km")

def costo_ruta(ruta):
    total = 0
    for i in range(len(ruta) - 1):
        origen = ruta[i]
        destino = ruta[i + 1]
        if destino in grafo[origen]:
            total += grafo[origen][destino]
        else:
            return float("inf")
    return total

def ruta_sin_repetir():
    estados = list(grafo.keys())
    mejor_ruta = None
    menor_costo = float("inf")

    for perm in itertools.permutations(estados):
        costo = costo_ruta(perm)
        if costo < menor_costo:
            menor_costo = costo
            mejor_ruta = perm

    return mejor_ruta, menor_costo

def ruta_con_repeticion():
    G = nx.Graph()

    for origen in grafo:
        for destino, costo in grafo[origen].items():
            G.add_edge(origen, destino, weight=costo)

    recorrido = list(nx.dfs_preorder_nodes(G, source="Yucatan"))
    costo = costo_ruta(recorrido)

    return recorrido, costo

def dibujar_grafo():
    G = nx.Graph()

    for origen in grafo:
        for destino, costo in grafo[origen].items():
            G.add_edge(origen, destino, weight=costo)

    pos = nx.spring_layout(G)
    etiquetas = nx.get_edge_attributes(G, 'weight')

    nx.draw(G, pos, with_labels=True)
    nx.draw_networkx_edge_labels(G, pos, edge_labels=etiquetas)

    plt.title("Grafo de Estados")
    plt.show()

if __name__ == "__main__":
    print("Relaciones entre estados:\n")
    mostrar_grafo()

    print("\n--- Ruta sin repetir ---")
    ruta, costo = ruta_sin_repetir()
    print("Ruta:", ruta)
    print("Costo total:", costo)

    print("\n--- Ruta con repetición ---")
    ruta2, costo2 = ruta_con_repeticion()
    print("Ruta:", ruta2)
    print("Costo total:", costo2)

    dibujar_grafo()