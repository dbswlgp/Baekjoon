king, stone, N = input().split()
N = int(N)

king_x = abs(int(king[1])-8)
king_y = ord(king[0]) - ord('A')
stone_x = abs(int(stone[1])-8)
stone_y = ord(stone[0]) -ord('A')

move = []
for _ in range(N):
  move.append(input())
  
def possible_move(x,y):
  if x>=0 and x<=7 and y>=0 and y<=7:
    return True
  return False

def stone_exist(king_x,king_y,stone_x,stone_y):
  if king_x == stone_x and king_y == stone_y:
    return True
  return False

for m in move:
  king_nx = king_x
  king_ny = king_y
  stone_nx = stone_x
  stone_ny = stone_y
  if m == 'R':
    king_ny += 1
    stone_ny += 1
  elif m == 'L':
    king_ny -= 1
    stone_ny -= 1
  elif m == 'B':
    king_nx += 1
    stone_nx += 1
  elif m == 'T':
    king_nx -= 1
    stone_nx -= 1
  elif m == 'RT':
    king_nx -= 1
    king_ny += 1
    stone_nx -= 1
    stone_ny += 1
  elif m == 'LT':
    king_nx -= 1
    king_ny -= 1
    stone_nx -= 1
    stone_ny -= 1
  elif m == 'RB':
    king_nx += 1
    king_ny += 1
    stone_nx += 1
    stone_ny += 1
  else:
    king_nx += 1
    king_ny -= 1
    stone_nx += 1
    stone_ny -= 1
  
  if possible_move(king_nx,king_ny):
    if stone_exist(king_nx,king_ny,stone_x,stone_y):
      if possible_move(stone_nx,stone_ny):
        king_x = king_nx
        king_y = king_ny
        stone_x = stone_nx
        stone_y = stone_ny
    else:
      king_x = king_nx
      king_y = king_ny

print(chr(king_y+ord('A')),abs(king_x-8),sep='')
print(chr(stone_y+ord('A')),abs(stone_x-8),sep='')
