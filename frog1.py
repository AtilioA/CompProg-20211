N = int(input())
hs = list(map(int, input().split()))

# PD table
PDTable = [0] * N

# Initialize PD table
PDTable[0] = 0
PDTable[1] = abs(hs[1] - hs[0])

for i in range(2, N):
    PDTable[i] = min(PDTable[i-2] + abs(hs[i] - hs[i-2]), PDTable[i-1] + abs(hs[i] - hs[i-1]))

print(PDTable[N-1])
