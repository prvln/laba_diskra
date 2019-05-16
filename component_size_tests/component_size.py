import time
t0 = time.clock()
a = []
z = []
out = []
l = 0
res = 0

counter = 0

for i in open('test6.in'):
    a.append(i[:-1])
    b = i
    z += b.split()

for i in open('test6.out'):
    a.append(i[:-1])
    b = i
    out += b.split()

n = int(z[0])                       #int(input("Введите кол-во вершин: "))
m = int(z[1])                       #int(input("Введите кол-во рёбер: "))
v = int(z[2])                       #int(input("Введите кол-во пар номеров смежных вершин: "))

counter = n**0.24
if counter < 4:
    counter = 4
print(counter,'kkkk')

out = int(out[0])

mas_x = []                          # массив х1,...,xn
mas_y = []                          # массив у1,...,yn

arr = [[0] * n for i in range(n)]

for i in range(3,len(z)):           # разбиваем на 2 массива х и у
    if i % 2 !=0:
        mas_x.append(int(z[i]))
    else:
        mas_y.append(int(z[i]))

for i in range(m):
    arr[mas_x[i]][mas_y[i]] = -1
    arr[mas_y[i]][mas_x[i]] = -1

for i in range(n):
    if arr[v][i] == -1:
        arr[v][i] = 1
    if arr[i][v] == -1:
        arr[i][v] = 1
    

while l < counter:
    for i in range(n):
        
        for j in range(n):
            
            if arr[i][j] == 1:
                
                for k in range(n):
                    
                    if arr[k][j] == -1:
                        arr[k][j] = 1
                        
                    if arr[i][k] == -1:
                        arr[i][k] = 1
    l+=1

for i in range(n):
    for j in range(n):
        if arr[i][j] == 1:
            res+=1
            break
print(res)

if res == out:
    print("YEZZ!")
else:
    print("NO")

print(time.clock() - t0,"sec")

'''
def print_arr():
    for i in arr:
        print(i)
    print("\n")
'''
