m = input("Input start: ")
n = input("Input finish: ")
W = 26
H = 26

alfa = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

bukva_1 = m[0]
chislo_1 = m[1:]

bukva_2 = n[0]
chislo_2 = n[1:]

for i in range(len(alfa)):
    if bukva_1 == alfa[i]:
        bukva_1 = i + 1

    if bukva_2 == alfa[i]:
        bukva_2 = i + 1

bukva_1 = int(bukva_1)
bukva_2 = int(bukva_2)
chislo_1 = int(chislo_1)
chislo_2 = int(chislo_2)

h = [[0 for j in range(26)] for i in range(26)]

def lee(bukva_1, chislo_1, bukva_2, chislo_2):

    dx = [2, 1, -1, -2, -2, -1, 1, 2]
    dy = [1, 2, 2, 1, -1, -2, -2, -1]

    d = 0
    h[bukva_1][chislo_1] = 0
    for y in range(26):
        for x in range(26):
            if h[y][x] == d:
                for k in range(8):
                    iy = y + dy[k]
                    ix = x + dx[k]
                    if iy >= 0 & iy < H & ix >= 0 & ix < W:
                        pass
lee(bukva_1, chislo_1, bukva_2, chislo_2)
