N = int(input())
costsStones = list(map(int, input().split()))

cost = 0
for i, stoneCost in enumerate(costsStones[:-2]):
    # print(stoneCost)
    if type(costsStones) == list and len(costsStones) > 1:
        hi = stoneCost
        hi1 = costsStones[i + 1]
        hi2 = costsStones[i + 2]
        print(f'hi = {hi}, hi+1 = {hi1}, hi+2 = {hi2} | ', end='')
        print(f'hi - hi1 = {abs(hi - hi1)}, hi - hi2 = {abs(hi - hi2)}')
        if abs(hi - hi1) <= abs(hi - hi2):
            cost += abs(hi - hi1)
        else:
            costsStones = costsStones[i + 2]
            cost += abs(hi - hi2)
print(cost)


