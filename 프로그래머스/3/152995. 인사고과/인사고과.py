def solution(scores):
    wanho_score = scores[0][0] + scores[0][1]
    wanho_a = scores[0][0]
    wanho_b = scores[0][1]
    scores.sort(reverse=True, key=lambda x:(x[0],-x[1]))
    score = []
    high_score = 0
    for i in range(len(scores)):
        high_score = max(high_score,scores[i][1])
        if scores[i][1] == high_score:
            score.append(scores[i][0] + scores[i][1])
        else:
            if scores[i][0] == wanho_a and scores[i][1] == wanho_b:
                return -1

    score.sort(reverse=True)
    answer = score.index(wanho_score) + 1
    
    return answer