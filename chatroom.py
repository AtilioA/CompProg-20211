WORD = 'hello'
s = input()

j = 0
steps = 0
for i in range(len(s)):
    if s[i] == WORD[j]:
        j += 1
        steps += 1

        if steps == 5:
            break

if steps == 5:
    print("YES")
else:
    print("NO")
