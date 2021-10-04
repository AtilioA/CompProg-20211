a = input()
s = input()

sortedS = sorted(s, reverse=True)
replacedA = list(a)

for c in sortedS:
    for i, originalDigit in enumerate(replacedA):
        if c > originalDigit:
            replacedA[i] = c
            break

print("".join(replacedA))
