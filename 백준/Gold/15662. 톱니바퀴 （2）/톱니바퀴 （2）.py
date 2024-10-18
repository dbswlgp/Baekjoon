T = int(input())

gear = []
for i in range(T):
  gear.append(list(input()))

def clockwise(n):
  gear[n][0],gear[n][1],gear[n][2],gear[n][3],gear[n][4],gear[n][5],gear[n][6],gear[n][7] = gear[n][7],gear[n][0],gear[n][1],gear[n][2],gear[n][3],gear[n][4],gear[n][5],gear[n][6]

def counterclockwise(n):
  gear[n][0],gear[n][1],gear[n][2],gear[n][3],gear[n][4],gear[n][5],gear[n][6],gear[n][7] = gear[n][1],gear[n][2],gear[n][3],gear[n][4],gear[n][5],gear[n][6],gear[n][7],gear[n][0]

K = int(input())
for _ in range(K):
  num,d = map(int,input().split())
  num -= 1
  turn = True
  direction = d
  if T == 1:
    if direction == 1:
      clockwise(0)
    else:
      counterclockwise(0)
  for i in range(num,0,-1):
    if gear[i][6] != gear[i-1][2]:
      if direction == 1:
        clockwise(i)
        direction = -1
      else:
        counterclockwise(i)
        direction = 1
    else:
      if direction == 1:
        clockwise(i)
      else:
        counterclockwise(i)
      turn = False
      break
  if turn:
    if direction == 1:
      clockwise(0)
    else:
      counterclockwise(0)
  turn = True
  direction = d
  if num != T-1:
    if direction == 1:
      if gear[num][3] != gear[num+1][6]:
        direction = -1
    else:
      if gear[num][1] != gear[num+1][6]:
        direction = 1
    if direction != d:    
      for i in range(num+1,T-1):
        if gear[i][2] != gear[i+1][6]:
          if direction == 1:
            clockwise(i)
            direction = -1
          else:
            counterclockwise(i)
            direction = 1
        else:
          if direction == 1:
            clockwise(i)
          else:
            counterclockwise(i)
          turn = False
          break
      if turn:
        if direction == 1:
          clockwise(T-1)
        else:
          counterclockwise(T-1)

count_gear = 0
for i in range(T):
  if gear[i][0] == '1':
    count_gear += 1

print(count_gear)
  
      
      