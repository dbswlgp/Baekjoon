N = int(input())

if N == 1:
  print(9)
else:
  dp = [[0]*10 for _ in range(N+1)]
  for i in range(0,10):
    dp[1][i] = 1
  for i in range(0,10):
    if i == 0:
      dp[2][i] = dp[1][1]
    elif i == 1:
      dp[2][i] = dp[1][2]
    elif i == 9:
      dp[2][i] = dp[1][8]
    else:
      dp[2][i] = (dp[1][i-1] + dp[1][i+1])
      
  for i in range(3,N+1):
    for j in range(0,10):
      if j == 0:
        dp[i][j] = dp[i-1][1]
      elif j == 9:
        dp[i][j] = dp[i-1][8]
      else:
        dp[i][j] = (dp[i-1][j-1] + dp[i-1][j+1])%1000000000

  print(sum(dp[N])%1000000000)