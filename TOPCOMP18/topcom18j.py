def calculaPontosX(cestasX):
    if (cestasX // 10 >= 1):
        pontosX = 10 * 3
        cestasX = cestasX - 10
        pontosX = pontosX + (cestasX * 2)
    else:
        pontosX = cestasX * 3

    return pontosX

def calculaPontosY(cestasY):
    if (cestasY // 16 >= 1):
        pontosY = 16 * 3
        cestasY = cestasY - 16
        pontosY = pontosY + (cestasY * 2)
    else:
        pontosY = cestasY * 3

    return pontosY


mediaCestasX1 = int(input())
mediaCestasX2 = int(input())
mediaCestasY1 = int(input())
mediaCestasY2 = int(input())

cestasX = mediaCestasX1 * (30 - 5) + mediaCestasX2 * (30 - 5)
cestasY = mediaCestasY1 * (30 - 8) + mediaCestasY2 * (30 - 8)

pontosX = calculaPontosX(cestasX)
pontosY = calculaPontosY(cestasY)

if pontosY>pontosX:
    print(f'Y Venceu{pontosX}-{pontosY}')
elif pontosY < pontosX:
    print(f'X Venceu{pontosX}-{pontosY}')
else:
    print(f'Empate{pontosX}-{pontosY}')

# X acerta (a) cestas por minuto no primeiro tempo e (b) cestas por minuto no segundo tempo,

# enquanto Y acerta (c) cestas por minuto no primeiro tempo e (d) cestas por minuto no segundo tempo.

# Contudo, o time X não acerta nenhuma cesta durante os últimos 5 minutos de cada tempo
# e o time Y não acerta nenhuma cesta durante os últimos 8 minutos de cada tempo.

# Cada cesta vale 2 ou 3 pontos, dependendo do local de arremesso da bola.

# O time X acerta em média 10 cestas de 3 pontos ao longo de toda a partida, contanto que (a) ou (b) sejam não nulos.

# Já o time Y acerta em média 16 cestas de 3 pontos ao longo de toda a partida, contanto que (c) ou (d) sejam não nulos.
