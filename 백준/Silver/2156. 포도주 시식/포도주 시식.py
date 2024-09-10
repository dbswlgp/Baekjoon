N = int(input())

wine = [0]
for i in range(N):
  wine.append(int(input()))

dp = [0] * (N+1)

dp[1] = wine[1]
if N>=2:
  dp[2] = wine[1] + wine[2]
if N>=3:
  dp[3] = max(wine[1]+wine[3],wine[2]+wine[3])

for i in range(4,N+1):
  dp[i] = max(max(dp[:i-1]),max(dp[:i-2])+wine[i-1])+wine[i]

print(max(dp))
