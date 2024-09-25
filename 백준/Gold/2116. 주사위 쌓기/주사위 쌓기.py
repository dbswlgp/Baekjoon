N = int(input())

dice = []
for i in range(N):
    dice.append(list(map(int,input().split())))


answer = 0
for i in range(6):
    temp = 0
    num = dice[0][i]
    index = i
    for j in range(N-1):
        if index == 0 or index == 5:
            a = max(dice[j][1:5])
            temp += a
        elif index == 1 or index == 3:
            b = max(dice[j][0],dice[j][2],dice[j][4],dice[j][5])
            temp += b
        else:
            c = max(dice[j][0],dice[j][1],dice[j][3],dice[j][5])
            temp += c
        
        index = dice[j+1].index(num)
        if index == 0:
            index = 5
        elif index == 5:
            index = 0
        elif index == 1:
            index = 3
        elif index == 3:
            index = 1
        elif index == 2:
            index = 4
        else:
            index = 2
        num = dice[j+1][index]

    if index == 0 or index == 5:
        temp += max(dice[N-1][1:5])
    elif index == 1 or index == 3:
        temp += max(dice[N-1][0],dice[N-1][2],dice[N-1][4],dice[N-1][5])
    else:
        temp += max(dice[N-1][0],dice[N-1][1],dice[N-1][3],dice[N-1][5])

    answer = max(answer,temp)
    
print(answer)