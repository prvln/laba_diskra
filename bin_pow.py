def pow_l(x, n):
    result = 1
    while n != 0:
        if n % 2 != 0:
            result *= x
            n -= 1
        else:
            x *= x
            n /= 2
    return result

def pow_h(base, degree, module):
    degree = bin(degree)[2:]
    r = 1
 
    for i in range(len(degree) - 1, -1, -1):
       r = (r * pow_l(base,int(degree[i]))) % module
       base = pow_l(base, 2) % module
 
    return r

p = 332636593    #int(input('Введите кольцо: '))
x = 2348726364    #int(input('Введите х: '))
a =  123456789   #int(input('Введите а: '))
b =  744329   #int(input('Введите b: '))
c =  3899631002   #int(input('Введите c: '))
d =  375476873   #int(input('Введите d: '))

# Ответ: 3216689

print((a * pow_h(x,d,p) + b* pow_h(x,c,p) + c * pow_h(x,b,p) + d)%p)

