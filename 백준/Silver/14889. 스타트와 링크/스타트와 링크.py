from itertools import combinations

N = int(input())

power = []
for i in range(N):
    power.append(list(map(int,input().split())))

power_sum = [[0]*N for _ in range(N)]

for i in range(N):
    for j in range(i+1,N):
        power_sum[i][j] = power[i][j] + power[j][i]
        power_sum[j][i] = power_sum[i][j]

num = [i for i in range(N)]

answer = int(1e9)
for case in list(combinations(num,N//2)):
    A = case
    B = list(set(num) - set(A))
    A_total = 0
    B_total = 0
    for i in range(N//2):
        for j in range(i+1,N//2):
            A_total += power_sum[A[i]][A[j]]
    for i in range(N//2):
        for j in range(i+1,N//2):
            B_total += power_sum[B[i]][B[j]]
    answer = min(answer,abs(A_total-B_total))

print(answer)


        