n = int(input("Введите n:"))

i = 0


ch = [1]*n
n_ch = [0]*n


while i != n-1:

    for x in range(0,n-1):
       for j in range(x+1, n):
            n_ch[j] += ch[x]

    ch = [0]*n
    i+=1
    print(i)


    if i == n-1:
        break

    for x in range(1, n):
            for j in range(0, x):
                ch[j] += n_ch[x]
    n_ch = [0]*n
    i += 1
    print(i)

result = (sum(ch) + sum(n_ch)) % 10000000

print(result)

