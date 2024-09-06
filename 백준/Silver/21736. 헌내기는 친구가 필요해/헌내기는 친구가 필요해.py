from collections import deque

N,M = map(int,input().split())

campus = []
for i in range(N):
  campus.append(input())

visited = [[False]*M for _ in range(N)]
dx = [0,1,0,-1]
dy = [1,0,-1,0]

for i in range(N):
  for j in range(M):
    if campus[i][j] == 'I':
      q = deque()
      q.append([i,j])
      visited[i][j] = True
      meet = 0
      while q:
        x,y = q.popleft()
        if campus[x][y] == 'P':
          meet += 1
        for t in range(4):
          nx = x + dx[t]
          ny = y + dy[t]
          if nx>=0 and nx<=N-1 and ny>=0 and ny<=M-1:
            if visited[nx][ny] == False and campus[nx][ny] != 'X':
              q.append([nx,ny])
              visited[nx][ny] = True
              
if meet == 0:
  print('TT')
else:
  print(meet)
              
          
        