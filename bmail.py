from collections import defaultdict, deque


# Grafo direcionado com lista de adjacências
class Graph:
    def __init__(self, nVertices):
        # default dictionary para armazenar o grafo
        self.graph = defaultdict(list)
        self.nVertices = nVertices
        # Inicializa listas de adjacências dos vértices
        for i in range(nVertices):
            self.graph[i] = []

    def adiciona_aresta(self, u, v):
        self.graph[u].append(v)

    # Fazer BFS de um grafo e printar
    def BFS(self, inicio):
        # Marca os vértices como não visitados
        visitado = [False] * (len(self.graph) + 1)

        # Cria uma fila para o BFS
        # (deque = Double Ended Queue)
        filaDeVertices = deque()

        # Marca o vértice de entrada e enfileira-o
        filaDeVertices.append(inicio)
        visitado[inicio] = True

        # Enquanto a fila tiver vértices
        while filaDeVertices:
            print(f"Fila atual: {filaDeVertices}")
            # Desenfileira um vértice e printa
            desenfileirado = filaDeVertices.popleft()
            print(f"Vértice visitado: {desenfileirado}")

            # Pega os adjacentes ao vértice desenfileirado
            # Se não estiver visitado, marca-o e enfileira-o
            # Nova iteração com a nova fila até que terminem os vizinhos
            for adj in self.graph[desenfileirado]:
                print(f"Adjacentes a {desenfileirado}:")
                print(adj)

                if visitado[adj] is False:
                    print(f"{adj} foi marcado e enfileirado.")
                    visitado[adj] = True
                    filaDeVertices.append(adj)
                else:
                    print(f"{adj} já foi marcado.")
            print()

    def BFS_print(self, inicio):
        visitado = [False] * (len(self.graph) + 1)
        visitado[inicio] = True

        filaDeVertices = deque()
        filaDeVertices.append(inicio)

        while filaDeVertices:
            desenfileirado = filaDeVertices.popleft()
            print(f"{desenfileirado:3}\n")

            for adj in self.graph[desenfileirado]:
                if visitado[adj] is False:
                    visitado[adj] = True
                    filaDeVertices.append(adj)
                    


n = int(input())
pi = map(int, input().split(' '))

# Inicializa um grafo e adiciona arestas
g = Graph(n)
for i, p in enumerate(pi):
    g.adiciona_aresta(i, p)

print(f"\nGrafo: {g.graph.items()}")

verticeInicial = 0
print(f"\nRealizando busca em amplitude (breadth-first traversal)\
      começando do vértice {verticeInicial}:\n")
g.BFS(verticeInicial)
g.BFS_print(verticeInicial)
