import sys
from collections import deque

input = sys.stdin.readline

N,M = map(int,input().split())
j_map = []

for i in range(N):
  j_map.append(input())

dx = [0,1,0,-1]
dy = [1,0,-1,0]

max_distance = 0
for i in range(N):
  for j in range(M):
    start_visited = [[False]*M for _ in range(N)]
    if j_map[i][j] == 'L' and start_visited[i][j] == False:
      start_visited[i][j] = True
      q = deque()
      dist = 0
      q.append([i,j,dist])
      visited = [[False]*M for _ in range(N)]
      visited[i][j] = True
      while q:
        x,y,dist = q.popleft()
        for t in range(4):
          nx = x + dx[t]
          ny = y + dy[t]
          if nx>=0 and nx<=N-1 and ny>=0 and ny<=M-1:
            if visited[nx][ny] == False and j_map[nx][ny] == 'L':
              q.append([nx,ny,dist+1])
              visited[nx][ny] = True
      max_distance = max(max_distance,dist)
      
print(max_distance)
      