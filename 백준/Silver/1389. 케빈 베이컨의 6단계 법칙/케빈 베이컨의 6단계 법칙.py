from collections import deque

N,M = map(int,input().split())

graph = [[] for _ in range(N+1)]

for _ in range(M):
    a,b = map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)

min_kevin = 500000
for i in range(1,N+1):
    kevin = 0
    visited = [False] * (N+1)
    q = deque()
    q.append([i,0])
    visited[i] = True
    while q:
        node, dist = q.popleft()
        kevin += dist
        for v in graph[node]:
            if visited[v] == False:
                q.append([v,dist+1])
                visited[v] = True
    if kevin < min_kevin:
        min_kevin = kevin
        answer = [i]
    elif kevin == min_kevin:
        answer.append(i)

print(answer[0])