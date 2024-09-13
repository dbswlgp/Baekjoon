def fact(N):
    if N == 1:
        return 1
    return N * fact(N-1)


N = int(input())

ques = list(map(int,input().split()))
q_type = ques[0]

if q_type == 1:
    if N == 1:
        print(1)
    else:
        answer = []
        k = ques[1]
        used = [False] * (N+1)
        pos = 1
        while True:
            fact_result = fact(N-pos)
            count = (k // fact_result)
            k -= (count * fact_result)
            if k == 0:
                count -= 1
            for i in range(1,N+1):
                if used[i] == True:
                    continue
                if count == 0:
                    used[i] = True
                    answer.append(i)
                    break
                if used[i] == False:
                    count -= 1
            pos += 1
            if k == 1:
                for i in range(1,N+1):
                    if used[i] == False:
                        answer.append(i)
                break
            if k == 0:
                for i in range(N,0,-1):
                    if used[i] == False:
                        answer.append(i)
                break
        for i in range(N):
            print(answer[i],end=' ')
else:
    sequ = []
    for i in range(1,len(ques)):
        sequ.append(ques[i])
    used = [False] * (N+1)
    answer = 1
    pos = 1
    while True:
        count = 0
        num = sequ[pos-1]
        for i in range(1,N+1):
            if i == num:
                used[i] = True
                break
            if used[i] == False and used[i] != num:
                count += 1
        if pos == N:
            break
        answer += (fact(N-pos) * count)
        pos += 1

    print(answer)
