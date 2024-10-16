N = int(input())

dp = [[0]*10 for _ in range(N+1)]

if N == 1:
  print(10)
else:
  for j in range(0,10):
    dp[1][j] = 1
  for i in range(2,N+1):
    dp[i][0] = sum(dp[i-1])%10007
    for j in range(1,10):
      dp[i][j] = dp[i][j-1] - dp[i-1][j-1]

  print(sum(dp[N])%10007)
