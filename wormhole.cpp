#include <iostream>
#include <vector>
#include <limits>
#include <sstream>

using namespace std;

// Verificar se um valor está contido em um vetor
bool is_in(vector<bool>::iterator it1, vector<bool>::iterator it2, bool val)
{
    for (vector<bool>::iterator it = it1; it != it2; it++)
    {
        if ((*it) == val)
        {
            return 1;
        }
    }
    return 0;
}

// Template para encontrar índice da primeira ocorrência de um elemento em um vetor
template <typename comparavel>
int index(typename vector<comparavel>::iterator it1, typename vector<comparavel>::iterator it2, comparavel val)
{
    int qtd = 0;
    for (typename vector<comparavel>::iterator it = it1; it != it2; it++)
    {
        if ((*it) == val)
        {
            return qtd;
        }
        qtd++;
    }
    return 0;
}

int sum_inf(int i, int j)
{
    if (j == numeric_limits<int>::max() || i == numeric_limits<int>::max())
    {
        return numeric_limits<int>::max();
    }
    else
    {
        return i + j;
    }
}

class Grafo
{
private:
    vector<vector<pair<int, int>>> adj;
    int nVertices;
    vector<bool> aberto;

public:
    Grafo(int nVertices)
    {
        // Inicializa vértices do grafo e "conjunto" (vetor) aberto
        for (int i = 0; i < nVertices; i++)
        {
            vector<pair<int, int>> k;
            this->aberto.push_back(true);
            this->adj.push_back(k);
        }
        this->nVertices = nVertices;
    };

    void adiciona_aresta(int u, int v, int peso)
    {
        pair<int, int> ida = make_pair(u, peso);
        pair<int, int> volta = make_pair(v, peso);

        this->adj[v].push_back(ida);
        this->adj[u].push_back(volta);
    }

    vector<int> DJ_Kastra_desproibido(int inicio)
    {
        vector<int> dists;

        // Inicializa vetor de distâncias com valores infinitos e 0 para vértice de ínicio
        for (int i = 0; i < this->nVertices; i++)
        {
            dists.push_back(numeric_limits<int>::max());
        }
        dists[inicio] = 0;

        while (is_in(this->aberto.begin(), this->aberto.end(), true))
        {
            int indiceMenor = index<bool>(this->aberto.begin(), this->aberto.end(), true);
            int proximoVertice = 0;
            for (int dist : dists)
            {
                if (this->aberto[proximoVertice] && dist < dists[indiceMenor])
                {
                    indiceMenor = proximoVertice;
                }
                proximoVertice++;
            }
            this->aberto[indiceMenor] = false;

            vector<pair<int, int>> vizinhos = this->adj[indiceMenor];
            for (pair<int, int> vizinho : vizinhos)
            {
                // cout << dists[indiceMenor] << dists[vizinho.first];
                if (this->aberto[vizinho.first])
                {
                    int custo = min(dists[vizinho.first], sum_inf(dists[indiceMenor], vizinho.second));
                    dists[vizinho.first] = custo;
                }
            }
        }
        return dists;
    }
};

int main()
{
    int c, n, m;
    int u, v, w;

    cin >> c;
    for (int i = 0; i < c; i++)
    {
        cin >> n >> m;

        Grafo *g = new Grafo(n);

        for (int i = 0; i < m; i++)
        {
            cin >> u >> v >> w;
            g->adiciona_aresta(u, v, w);
        }

        vector<int> dists = g->DJ_Kastra_desproibido(0);
        // cout << "Case #" << c << ": ";
        // if (dists[T] == numeric_limits<int>::max()) {
        //     cout << "unreachable" << endl;
        // } else {
        for(int i = 0; i < c; i++) {
            cout << dists[i] << ' ';
        }
        cout << dists[i] << endl;

        delete g;
    }

    return 0;
}
