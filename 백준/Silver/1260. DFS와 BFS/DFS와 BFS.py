from collections import deque
N,M,V = map(int,input().split())

graph = [[] for _ in range(N+1)]
visited = [False] * (N+1)
         
for i in range(M):
  a,b = map(int,input().split())
  graph[a].append(b)
  graph[b].append(a)

for i in range(1,N+1):
  graph[i].sort()

def DFS(graph,visited,v):
  visited[v] = True
  print(v,end=' ')
  for i in graph[v]:
    if visited[i] == False:
      DFS(graph,visited,i)

def BFS(graph,visited,v):
  queue = deque()
  queue.append(v)
  visited[v] = True
  while queue:
    v = queue.popleft()
    print(v,end=' ')
    for i in graph[v]:
      if visited[i] == False:
        queue.append(i)
        visited[i] = True

DFS(graph,visited,V)
print()

visited = [False] * (N+1)
BFS(graph,visited,V)