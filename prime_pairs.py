'''
Напишите программу, определяющую количество n-значных чисел, таких,
что каждые последовательно взятые две цифры — двузначное простое число.
Например, к таким числам относятся:41,19,197,2313.

Примеры:
2   21
3   52
4   142
8   6962
15  6404362
16  16978702
17  45011932
'''

n = int(input("Введите n: "))

endPrime1 = 5
endPrime3 = 6
endPrime7 = 5
endPrime9 = 5

for i in range(n - 2):
    ePbuff1 = 0
    ePbuff3 = 0
    ePbuff7 = 0
    ePbuff9 = 0

    ePbuff1 = endPrime1 + endPrime3 + endPrime7
    ePbuff3 = endPrime1 + endPrime7
    ePbuff7 = endPrime1 + endPrime3 + endPrime9
    ePbuff9 = endPrime1 + endPrime7

    endPrime1 = ePbuff1
    endPrime3 = ePbuff3
    endPrime7 = ePbuff7
    endPrime9 = ePbuff9

print(endPrime1 + endPrime3 + endPrime7 + endPrime9)
