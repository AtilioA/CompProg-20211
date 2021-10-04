nPiles = int(input())
piles = map(int, input().split())

nJuicy = int(input())
labelsJuicy = map(int, input().split())

minhocas = []
grupo = 1

for pile in piles:
    for _ in range(pile):
        minhocas.append(grupo)
    grupo += 1

for label in labelsJuicy:
    print(minhocas[label - 1])

