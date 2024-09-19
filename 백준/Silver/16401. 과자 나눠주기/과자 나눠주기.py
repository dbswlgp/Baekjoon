import sys

input = sys.stdin.readline
M,N = map(int,input().split())

snack = list(map(int,input().split()))

start = 1
end = 1000000000

answer = 0
while start <= end:
    mid = (start+end)//2
    snack_count = 0
    for i in range(len(snack)):
        snack_count += (snack[i]//mid)
    if snack_count >= M:
        start = mid + 1
        answer = mid
    else:
        end = mid - 1

if answer == 0:
    print(0)
else:
    print(answer)