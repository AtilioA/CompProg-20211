x1r, y1r, x2r, y2r, xp, yp = map(int, input().split())
rangeX = range(x1r, x2r, -1) if x2r < x1r else range(x1r, x2r)
rangeY = range(y1r, y2r, -1) if y2r < y1r else range(y1r, y2r)
if xp in rangeX and yp in rangeY:
    print("Dentro", end='')
else:
    print("Fora", end='')
