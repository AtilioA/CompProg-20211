R = 10
C = 20
heatmap = [['░' for i in range(20)] for i in range(10)]

valuesSensor = input().split(', ')
valuesSensor = [list(map(int, value.split(' '))) for value in valuesSensor]

def determineHeatChar(heat):
    if heat == 1:
        return '▒'
    elif heat == 2:
        return '▓'
    elif heat == 3:
        return '█'
    else:
        return '░'

for value in valuesSensor:
    heatChar = determineHeatChar(value[2])
    heatmap[value[1]][value[0]] = heatChar

for y in heatmap:
    for char in y:
        print(char, end='')
    print()
