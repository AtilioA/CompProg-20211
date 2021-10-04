def check_query(s, l, r):
    # Particiona lista, começando de l e indo até r (ambos inclusive)
    partialS = s[l-1:r]

    # Checa se cada elemento é igual ao próximo
    # Nesse caso guarda 'os elementos atuais' numa lista, mas só precisamos da quantidade de iguais
    equals = [partialS[i] for i in range(len(partialS) - 1) if partialS[i]==partialS[i + 1]]

    # Retorna quantidade de elementos iguais
    return len(equals)


s = input()
m = int(input())
for query in range(m):
    l, r = map(int, input().split())
    print(check_query(s, l, r))

