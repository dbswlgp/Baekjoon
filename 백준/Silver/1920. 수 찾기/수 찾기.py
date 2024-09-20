N = int(input())
arr1 = list(map(int,input().split()))
M = int(input())
arr2 = list(map(int,input().split()))

arr1.sort()
for num in arr2:
    start = 0
    end = N-1
    find = False
    while start <= end:
        mid = (start+end)//2
        if arr1[mid] == num:
            print(1)
            find = True
            break
        elif arr1[mid] > num:
            end = mid - 1
        else:
            start = mid + 1
    if not find:
        print(0)