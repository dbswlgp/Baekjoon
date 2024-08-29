def solution(targets):
    answer = 1
    targets.sort(key=lambda x:x[::])
    end = targets[0][1]
    for i in range(1,len(targets)):
        if targets[i][0] < end:
            end = min(end,targets[i][1])
            continue
        else:
            answer += 1
            end = targets[i][1]
    return answer