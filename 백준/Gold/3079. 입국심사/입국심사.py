import sys

input = sys.stdin.readline

N,M = map(int,input().split())

time = []

for _ in range(N):
  time.append(int(input()))

start = 0
end = max(time)*1000000000

answer = 0
while start<=end:
  mid = (start+end)//2
  audit_count = 0
  for i in range(N):
    audit_count += (mid//time[i])
  if audit_count >= M:
    answer = mid
    end = mid - 1
  else:
    start = mid + 1

print(answer)




