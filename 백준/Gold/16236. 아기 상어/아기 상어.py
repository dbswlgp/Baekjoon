from collections import deque

N = int(input())

maps = []
for i in range(N):
  maps.append(list(map(int,input().split())))
  for j in range(N):
    if maps[i][j] == 9:
      shark_x = i
      shark_y = j
      maps[i][j] = 0

dx = [-1,0,1,0]
dy = [0,-1,0,1]

size_of_shark = 2
count_eat = 0
time = 0

while True:
  q = deque()
  q.append([shark_x,shark_y,0])
  visited = [[False]*N for _ in range(N)]
  visited[shark_x][shark_y] = True
  fish_list = []
  short_dist = 0
  while q:
    x,y,dist = q.popleft()
    if maps[x][y] != 0 and maps[x][y] < size_of_shark:
      if short_dist == 0:
        short_dist = dist
        fish_list.append([x,y])
      else:
        if dist != short_dist:
          break
        fish_list.append([x,y])
    for t in range(4):
      nx = x + dx[t]
      ny = y + dy[t]
      if nx>=0 and nx<=N-1 and ny>=0 and ny<=N-1:
        if visited[nx][ny] == False:
          if maps[nx][ny] <= size_of_shark:
            q.append([nx,ny,dist+1])
            visited[nx][ny] = True
  if len(fish_list) == 0:
    break
  else:
    fish_list.sort()
    x = fish_list[0][0]
    y = fish_list[0][1]
    maps[x][y] = 0
    time += short_dist
    count_eat += 1
    shark_x = x
    shark_y = y
    if count_eat == size_of_shark:
      size_of_shark += 1
      count_eat = 0
      
print(time)
