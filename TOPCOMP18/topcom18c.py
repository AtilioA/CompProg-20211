N = int(input())

alunos = []
for _ in range(N):
    alunos.append(list(map(int, input().split(' '))))

def preferenciaAluno(preferencias, a0, a1, a2):
    for i in range(N):
        if (preferencias[a0][i] == a2):
            return True
        if (preferencias[a0][i] == a1):
            return False

def duozaoEstavel(preferencias):
    duplasAlunos = [-1 for i in range(N)]
    alunosDisponiveis = [False for i in range(N)]

    contadorDisponiveis = N
    while (contadorDisponiveis > 0):
        alunoAtual = 0
        while (alunoAtual < N):
            if (alunosDisponiveis[alunoAtual] == False):
                break
            alunoAtual += 1

        i = 0
        while i < N and alunosDisponiveis[alunoAtual] == False:
            try:
                aluno0 = preferencias[alunoAtual][i]
            except:
                return print(-1)
                exit()

            if (duplasAlunos[aluno0 - N] == -1):
                duplasAlunos[aluno0 - N] = alunoAtual
                alunosDisponiveis[alunoAtual] = True
                contadorDisponiveis -= 1

            else:
                a2 = duplasAlunos[aluno0 - N]
                if (preferenciaAluno(preferencias, aluno0, alunoAtual, a2) == False):
                    duplasAlunos[aluno0 - N] = alunoAtual
                    alunosDisponiveis[alunoAtual] = True
                    alunosDisponiveis[a2] = False
            i += 1

    for i in range(N):
        print(duplasAlunos[i])

duozaoEstavel(alunos)
