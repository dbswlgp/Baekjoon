N = int(input())

fruit = list(map(int,input().split()))

answer = 1

if N == 1:
  print(answer)
else:
  fruit1 = 0
  fruit2 = 0
  count = 0
  for i in range(N):
    if fruit1 == 0:
      fruit1 = fruit[i]
      fruit1_start = i
      fruit1_end = i
      count += 1
    elif fruit[i] == fruit1:
      count += 1
      fruit1_end = i
    elif fruit2 == 0:
      fruit2 = fruit[i]
      fruit2_start = i
      fruit2_end = i
      count += 1
    elif fruit[i] == fruit2:
      count += 1
      fruit2_end = i
    else:
      answer = max(answer,count)
      if fruit1_end < fruit2_end:
        count -= (fruit1_end - fruit1_start)
        fruit1, fruit1_start, fruit1_end = fruit2, fruit1_end+1, fruit2_end
      else:
        count -= (fruit2_end - fruit1_start)
        fruit1_start = fruit2_end + 1
      fruit2 = fruit[i]
      fruit2_start = i
      fruit2_end = i
  
  answer = max(answer,count)
  print(answer)