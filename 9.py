import numpy as np
import sys
from collections import deque

n = int(input("n:"))
s = int(input("s:"))
f = int(input("f:"))

s = s-1
f = f-1
matrix = []

for i in range(0, n):
    lst = input().split()
    lst_int = []
    for j in lst:
        lst_int += [int(j)]
    matrix.append(lst_int)

used = [0] * (n + 1)

q = deque()

q.append(s)
used[s] = 1

while q:
    now = q[0]
    q.popleft()
    for i in range(0, (len(matrix[now]))):
        if (matrix[now][i] != 0):
            if used[i] == 0 or used[i] > used[now] + matrix[now][i]:
                q.append(i)
                used[i] = used[now] + matrix[now][i]

if used[f] == 0:
    print(-1)
else:
    print(used[f]-1)

