N, M = [int(i) for i in input().split(' ')]
i = 0
ranks = [int(i) for i in input().split(' ')]

while i < N:
    coins, rank = [int(i) for i in input().split(' ')]
    j = 0
    while rank < M and coins >= ranks[rank]:
        coins -= ranks[rank]
        rank+=1
    sum = 0
    j = 0
    while j < rank:
        sum = sum + j + 1
        j+=1
    if i == N - 1:
        print(f'{sum}')
    else:
        print(f'{sum} ', end='')

    i += 1
