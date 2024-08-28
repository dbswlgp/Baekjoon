from collections import deque

dx = [0,1,1,1,0,-1,-1,-1]
dy = [1,1,0,-1,-1,-1,0,1]

while True:
  w,h = map(int,input().split())
  if w == 0 and h == 0:
    break
  array = []
  for i in range(h):
    array.append(list(map(int,input().split())))
  visited = [[False]*w for _ in range(h)]
  island = 0
  for i in range(h):
    for j in range(w):
      if array[i][j] == 1:
        if visited[i][j] == False:
          island+=1
          q = deque()
          q.append([i,j])
          while q:
            x,y = q.popleft()
            for t in range(8):
              nx = x + dx[t]
              ny = y + dy[t]
              if nx>=0 and nx<=h-1 and ny>=0 and ny<=w-1:
                if array[nx][ny] == 1:
                  if visited[nx][ny] == False:
                    visited[nx][ny] = True
                    q.append([nx,ny])
  print(island)