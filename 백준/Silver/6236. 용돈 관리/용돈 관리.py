N,M = map(int,input().split())

use = []
for i in range(N):
    use.append(int(input()))
    
start = max(use)
end = sum(use)

answer = 0
while start <= end:
    K = (start+end)//2
    balance = 0
    withdraw = 0
    for i in range(N):
        if balance < use[i]:
            balance = K
            withdraw += 1
        balance -= use[i]
    if withdraw <= M:
        end = K - 1
        answer = K
    else:
        start = K + 1
        
print(answer)
        