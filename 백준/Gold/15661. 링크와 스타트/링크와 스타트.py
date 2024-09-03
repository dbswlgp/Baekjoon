import sys
from itertools import combinations

input = sys.stdin.readline

N = int(input())
player = [i for i in range(1,N+1)]

ability = []
for _ in range(N):
  ability.append(list(map(int,input().split())))

for i in range(N):
  for j in range(i+1,N):
    ability[i][j] += ability[j][i]


answer = 20000
for p in range(2,N//2+1):
  for start in list(combinations(player,p)):
    start = set(start)
    link = set(player) - start
    start = list(start)
    link = list(link)
    start_power = 0
    link_power = 0
    for i in range(p):
      for j in range(i+1,p):
        start_power += ability[start[i]-1][start[j]-1]
    for i in range(N-p):
      for j in range(i+1,N-p):
        link_power += ability[link[i]-1][link[j]-1]
    answer = min(answer,abs(start_power-link_power))
  if answer == 0:
    break

print(answer)



