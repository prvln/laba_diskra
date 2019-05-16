N = 3
S = 2
F = 1
graph = [[0,1,1],[4,0,1],[2,1,0]]
v = len(graph)

for k in range(0,v):
    for i in range(0,v):
        for j in range(0,v):
            if graph[i,j] > graph[i,k] + graph[k,j]:
                graph[i,j] = graph[i,k] + graph[k,j]
                p[i,j] = p[k,j]


print(graph)
