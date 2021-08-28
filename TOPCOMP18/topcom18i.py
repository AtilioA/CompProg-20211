from itertools import product

def points_in_circle(radius, cx, cy):
    for x, y in product(range(int(radius) + 1), repeat=2):
        if x**2 + y**2 <= radius**2:
            yield from set(((cx + x, cy + y), (cx + x, cy -y), (cx -x, cy + y), (cx -x, cy -y),))


def run():
    g = int(input())
    for _ in range(g):
        a,b,c,d,e = map(int, input().split())
        print(len(list(points_in_circle(a,b,c))))

run()
