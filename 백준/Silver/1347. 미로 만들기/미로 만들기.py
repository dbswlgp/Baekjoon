N = int(input())
move = input()

array = [['#']*200 for _ in range(200)]

x = 100
y = 100
array[x][y] = '.'
dx = [0,1,0,-1]
dy = [1,0,-1,0]
d = 1
for m in move:
  if m == 'R':
    d+=1
    if d == 4:
      d = 0
  elif m == 'L':
    d-=1
    if d == -1:
      d = 3
  else:
    x += dx[d]
    y += dy[d]
    array[x][y] = '.'

start_x = 200
start_y = 200
end_x = 0
end_y = 0
for i in range(200):
  for j in range(200):
    if array[i][j] == '.':
      start_x = min(i,start_x)
      start_y = min(j,start_y)
      end_x = max(i,end_x)
      end_y = max(j,end_y)
    
for i in range(start_x,end_x+1):
  for j in range(start_y,end_y+1):
    print(array[i][j],end='')
  print()