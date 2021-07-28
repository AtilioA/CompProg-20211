from heapq import heappop
from heapq import heappush

operations = 0

n, k = input().strip().split()

k = int(k)
n = int(n)

A = list(map(int, input().strip().split()))
B = []
# Cria heap
for a in A:
    heappush(B, a)

def procuraSeTemMenor(A, k):
    for i in A:
        if (i < k):
            return True
    return False

def filtroMaiorIgual(x):
    return x >= k

while (len(B) > 1):
    if not procuraSeTemMenor(B, k):
        break

    fstmenor = heappop(B) # pega o primeiro menor
    sndmenor = heappop(B) # pega o segundo menor
    docinho = fstmenor + (2*sndmenor) # formula de sweetness
    operations = operations + 1 # numero de iteracoes necessarias
    heappush(B, docinho)

if (len(list(filter(filtroMaiorIgual, B))) != len(B)):
    print(-1)
else:
    print(operations)
