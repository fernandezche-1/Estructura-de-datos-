def floyd_warshall(matriz):
    n = len(matriz)
    dist = [fila[:] for fila in matriz]

    for k in range(n):
        for i in range(n):
            for j in range(n):
                dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])

    return dist


# Ejemplo
INF = float('inf')
matriz = [
    [0, 3, INF, 7],
    [8, 0, 2, INF],
    [5, INF, 0, 1],
    [2, INF, INF, 0]
]

resultado = floyd_warshall(matriz)

print("Floyd-Warshall:")
for fila in resultado:
    print(fila)