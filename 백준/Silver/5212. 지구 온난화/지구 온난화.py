import copy

R,C = map(int,input().split())

maps = []
for i in range(R):
  maps.append(list(input()))

maps_after50 = copy.deepcopy(maps)

dx = [0,1,0,-1]
dy = [1,0,-1,0]

for x in range(R):
  for y in range(C):
    if maps[x][y] == 'X':
      water = 0
      for t in range(4):
        nx = x + dx[t]
        ny = y + dy[t]
        if nx>=0 and nx<=R-1 and ny>=0 and ny<=C-1:
          if maps[nx][ny] == '.':
            water += 1
        else:
          water += 1
      if water>=3:
        maps_after50[x][y] = '.'

start_x = R-1
start_y = C-1
end_x = 0
end_y = 0
for i in range(R):
  for j in range(C):
    if maps_after50[i][j] == 'X':
      start_x = min(start_x,i)
      start_y = min(start_y,j)
      end_x = max(end_x,i)
      end_y = max(end_y,j)

for i in range(start_x,end_x+1):
  for j in range(start_y,end_y+1):
    print(maps_after50[i][j],end='')
  print()