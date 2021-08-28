temp, scale = input().split()

temp = float(temp)
scale = scale.lower()

if scale == 'c':
    newTemp = temp * 1.8 + 32
    newScale = 'F'
else:
    newTemp = (temp - 32) / 1.8
    newScale = 'C'

print(f'{newTemp:.2f} ({newScale})', end='')
