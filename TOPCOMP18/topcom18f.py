N = int(input())

for i in range(N):
    expression = input().split(' and ')

    trueson = set([letter for letter in expression if len(letter) == 1])
    falseta = set([letter[-1] for letter in expression if len(letter) != 1])

    inter = len(trueson.intersection(falseta))

    if (inter):
        print("trivialmente falsa")
    else:
        print("nem trivialmente verdadeira, nem trivialmente falsa")
