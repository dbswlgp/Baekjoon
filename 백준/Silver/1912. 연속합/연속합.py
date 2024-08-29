n = int(input())
array = list(map(int,input().split()))

dp = [0] * n
dp[0] = array[0]

for i in range(1,n):
  dp[i] = max(0,dp[i-1]) + array[i]

print(max(dp))