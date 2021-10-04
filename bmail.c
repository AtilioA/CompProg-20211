#include <stdio.h>
#include <stdlib.h>
#include "bmail_struct.h"

int main()
{
    int i = 0, n = 0, p = 0;

    Grafo *grafo = malloc(sizeof(Grafo));

    scanf("%d", &n);
    cria_grafo(grafo, n);
    printf("Grafo vazio criado com sucesso!\n");
    printf("Inserindo vertices...\n");
    for (int i = 2; i <= n; i++)
    {
        scanf("%d", &p);
        insere_aresta(grafo, i - 1, p - 1);
    }
    printf("test\n");

    busca_prof(grafo);

    // printf("Imprimindo o grafo:\n");
    // imprime_grafo(grafo);
    // printf("\n");

    destroi_grafo(grafo);
    free(grafo);
    // printf("Grafo destruido com sucesso!\n");

    return 0;
}
