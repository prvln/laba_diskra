a = []
z = []
out = []

L = 0

for i in open('test1.in'):
    a.append(i[:-1])
    b = i
    z += b.split()

for i in open('test6.out'):
    a.append(i[:-1])
    b = i
    out += b.split()

n = int(z[0])           #int(input("Введите кол-во вершин: "))
m = int(z[1])           #int(input("Введите кол-во рёбер: "))
v = int(z[2])           #int(input("Введите кол-во пар номеров смежных вершин: "))

out = int(out[0])

mas_x = []              # массив х1,...,xn
mas_y = []              # массив у1,...,yn


for i in range(3,len(z)):             # разбиваем на 2 массива х и у
    if i % 2 !=0:
        mas_x.append(int(z[i]))
    else:
        mas_y.append(int(z[i]))

print(out)
