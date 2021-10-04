from collections import defaultdict


class Grafo:
    def __init__(self, nVertices):
        self.adjs = defaultdict(list)
        self.nVertices = nVertices
        # Inicializa todos os vértices
        for vertice in range(nVertices):
            self.adjs[vertice] = []
        # <<Conjuntos>> para Dijkstra
        self.fechado = [False] * nVertices
        self.aberto = [True] * nVertices

    def adiciona_aresta(self, u, v, peso):
        self.adjs[u].append((v, peso))
        self.adjs[v].append((u, peso))

    def dijkstra(self, inicio):
        distV = list(map(lambda x: 0 if x == inicio else float("inf"), range(self.nVertices)))
        # print(distV)

        self.adjs[inicio]
        while True in self.aberto:
            indiceMenor = self.aberto.index(True)
            # print(f"Aberto: {self.aberto}")
            # print(f"Fechado: {self.fechado}")
            # print(f"Distancias: {distV}")
            for dist in distV:
                if self.aberto[distV.index(dist)] and dist < distV[indiceMenor]:
                    indiceMenor = distV.index(dist)
                # print(f"Indice Menor: {indiceMenor}, dist: {distV.index(dist)}")
            # print(indiceMenor)
            self.aberto[indiceMenor] = False
            self.fechado[indiceMenor] = True

            vizinhos = [x for x in self.adjs[indiceMenor] if self.aberto[x[0]]]
            for vizinho in vizinhos:
                custo = min(distV[vizinho[0]], distV[indiceMenor] + vizinho[1])
                distV[vizinho[0]] = custo

        return distV


N = int(input())
for i in range(N):
    n, m, S, T = map(int, input().split(' '))
    g = Grafo(n)
    for j in range(m):
        u, v, w = map(int, input().split(' '))
        g.adiciona_aresta(u, v, w)
    # print(g.adjs.items())
    # print(f"Distância do vértice {inicio} para todos os outros: \n{g.dijkstra(inicio)}")
    distST = g.dijkstra(S)[T]
    print(f"Case #{N}: ", end='')
    if distST == float('inf'):
        print('unreachable')
    else:
        print(distST)
