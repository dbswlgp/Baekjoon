from collections import deque

N = int(input())
paint = []

for i in range(N):
  paint.append(input())

dx = [0,1,0,-1]
dy = [1,0,-1,0]

def color_nw(paint):
  count = 0
  visited = [[False]*N for _ in range(N)]
  for i in range(N):
    for j in range(N):
      if visited[i][j] == False:
        count += 1
        q = deque([[i,j]])
        visited[i][j] = True
        while q:
          x,y = q.popleft()
          for t in range(4):
            nx = x + dx[t]
            ny = y + dy[t]
            if nx>=0 and nx<=(N-1) and ny>=0 and ny<=(N-1):
              if visited[nx][ny] == False and paint[nx][ny] == paint[x][y]:
                q.append([nx,ny])
                visited[nx][ny] = True
  return count

def color_w(paint):
  count = 0
  visited = [[False]*N for _ in range(N)]
  for i in range(N):
    for j in range(N):
      if visited[i][j] == False:
        count += 1
        q = deque([[i,j]])
        visited[i][j] = True
        while q:
          x,y = q.popleft()
          for t in range(4):
            nx = x + dx[t]
            ny = y + dy[t]
            if nx>=0 and nx<=(N-1) and ny>=0 and ny<=(N-1):
              if visited[nx][ny] == False:
                if paint[x][y] == 'R' or paint[x][y] == 'G':
                  if paint[nx][ny] == 'R' or paint[nx][ny] == 'G':
                    q.append([nx,ny])
                    visited[nx][ny] = True
                else:
                  if paint[nx][ny] == paint[x][y]:
                    q.append([nx,ny])
                    visited[nx][ny] = True
  return count

print(color_nw(paint),color_w(paint))
