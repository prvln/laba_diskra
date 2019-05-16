a = []
z = []
out = []

for i in open('test4.in'):
    a.append(i[:-1])
    b = i
    z += b.split()

for i in open('test4.out'):
    a.append(i[:-1])
    b = i
    out += b.split()

m = int(z[0])                       
n = int(z[1])                      
k = int(z[2]) 

mas_x = []                          # массив х1,...,xn
mas_y = []                          # массив у1,...,yn

for i in range(3,len(z)):           # разбиваем на 2 массива х и у
    if i % 2 !=0:
        mas_x.append(int(z[i]))
    else:
        mas_y.append(int(z[i]))

out = int(out[0])

meow = [[0] * n for i in range(m)]
meow[0][0] = 1

for i in range(k):
    x = mas_x[i]
    y = mas_y[i]
    meow[y][x] = -1
    k -= 1

for i in range(m):
    for k in range(n):
        if meow[i][k] == -1:
            continue
        if i and meow[i-1][k] != -1:
            meow[i][k] += meow[i-1][k]
        if k and meow[i][k-1] != -1:
            meow[i][k] += meow[i][k-1]

otvet = meow[m-1][n-1]

print("Ответ: ",otvet)

if otvet == out:
    print("YEEEZZZZ")
else:
    print("NOOOOOOOOO(((")
