import time

a = []
z = []
L = 0

for i in open('test1.in'):
    a.append(i[:-1])
    b = i
    z += b.split()

p = int(z[0])           #int(input("Введите р: "))
x = int(z[1])           #int(input("Введите x: "))
n = int(z[2])           #int(input("Введите кол-во пар чисел n: "))

mas_x = []              # массив х1,...,xn
mas_y = []              # массив у1,...,yn

def evklid(p2, p):
    if p == 0:
        return p2, 1, 0
    else:
        d, x, y = evklid(p, p2 % p)
        return  d, y, x - y * (p2 // p)

def lagranz(mas_x, y, x, p, L):
    for j in range(len(mas_y)):
        p1 = 1
        p2 = 1
        for i in range(len(mas_x)):
            if i != j:
                p1 *= x - mas_x[i]
                p2 *=  mas_x[j] - mas_x[i]
                
                p1 = p1 % p
                p2 = p2 % p
        print(p1)
        print(p2)
                
        q = evklid(p2, p)
        p2 = int(q[1])
        L += (mas_y[j] * p1 * p2) % p
    print("Ответ:",L % p)

t0 = time.clock()

for i in range(3,len(z)):             # разбиваем на 2 массива х и у
    if i % 2 !=0:
        mas_x.append(int(z[i]))
    else:
        mas_y.append(int(z[i]))


lagranz(mas_x, mas_y, x, p, L)
    
print(time.clock() - t0,"sec")
