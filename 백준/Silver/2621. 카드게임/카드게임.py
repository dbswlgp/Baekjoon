def same_color(color):
    for i in range(4):
        if color[i] != color[i+1]:
            return False
    return True

def consecutive_number(num):
    for i in range(len(num)-1):
        if num[i] != num[i+1] - 1:
            return False
    return True

def same_number(num):
    for i in range(len(num)-1):
        if num[i] != num[i+1]:
            return False
    return True

color = [0] * 5
num = [0] * 5

for i in range(5):
    color[i],num[i] = input().split()
    num[i] = int(num[i])

score = 0
num.sort()


if same_color(color):
    if consecutive_number(num):
        score = max(num) + 900
    else:
        score = max(num) + 600
if (same_number(num[:4])) or (same_number(num[1:])):
    if same_number(num[:4]):
        score = max(score,num[0]+800)
    else:
        score = max(score,num[4]+800)
elif (same_number(num[:3]) or same_number(num[1:4]) or same_number(num[2:])):
    if same_number(num[:3]):
        if same_number(num[3:]):
            score = max(score,num[0]*10 + num[3] + 700)
        else:
            score = num[0] + 400
    if same_number(num[1:4]):
        if same_number([num[0]]+[num[4]]):
            score = max(score,num[1]*10 + num[0] + 700)
        else:
            score = num[1] + 400
    if same_number(num[2:]):
        if same_number(num[:2]):
            score = max(score,num[2]*10 + num[0] + 700)
        else:
            score = max(score,num[2] + 400)
elif consecutive_number(num):
    score = max(score,max(num)+500)
elif num[0] == num[1]:
    if num[2] == num[3]:
        score = max(score,max(num[0],num[2])*10 + min(num[0],num[2]) + 300)
    elif num[3] == num[4]:
        score = max(score,max(num[0],num[3])*10 + min(num[0],num[3]) + 300)
    else:
        score = max(score,num[0] + 200)
elif num[1] == num[2]:
    if num[3] == num[4]:
        score = max(score,max(num[1],num[3])*10 + min(num[1],num[3]) + 300)
    else:
        score = max(score,num[1] + 200)
elif num[2] == num[3]:
    score = max(score,num[2] + 200)
elif num[3] == num[4]:
    score = max(score,num[3] + 200)
else:
    score = max(score,max(num) + 100)

print(score)

