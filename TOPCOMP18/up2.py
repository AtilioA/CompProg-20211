p1, p2 = map(int, input().split())
m = (p1 + p2) / 2
if m >= 7:
    print(f'{m} - Aprovado', end='')
elif m < 5:
    print(f'{m} - Reprovado', end='')
else:
    print(f'{m} - De Recuperacao', end='')
