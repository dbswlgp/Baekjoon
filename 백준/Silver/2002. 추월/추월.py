N = int(input())

entrance = []
exit = []

for _ in range(N):
  entrance.append(input())

for _ in range(N):
  exit.append(input())

passed = set()
overtake = set()

for i in range(N):
  passed.add(entrance[i])
  for j in range(N):
    if exit[j] == entrance[i]:
      break
    if exit[j] not in passed and exit[j] not in overtake:
      overtake.add(exit[j])

print(len(overtake))
      