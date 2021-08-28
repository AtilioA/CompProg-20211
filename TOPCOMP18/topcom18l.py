G = int(input())

ids_initial = set(list(map(int, input().strip().split(' ')))[1:])

for g in range(G - 1):
    ids = set(list(map(int, input().strip().split(' ')))[1:])

    ids_initial = ids.intersection(ids_initial)

    if(not len(ids_initial)):
        break

if(len(ids_initial)):
    print(f'{len(ids_initial)} amigos em comum!')
else:
    print("IMPOSSIVEL!")
