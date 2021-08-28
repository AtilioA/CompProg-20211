def run():
    nAlunos, t1, t2 = map(int, input().split())

    t1Set = []

    for _ in range(t1):
        t1Set.append(frozenset(input().split(' ')))
    t1Set = frozenset(t1Set)
    for _ in range(t2):
        roldinho = t1Set.intersection([frozenset(input().split(' '))])
        if roldinho:
            continue
        else:
            return 0
    return 1

print(run())
