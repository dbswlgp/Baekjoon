from itertools import combinations,product

def A_win(dice,A_dice,B_dice):
    win_count = 0
    A_result = [0] * len(A_dice)
    B_result = [0] * len(B_dice)
    
    A_list = []
    for d in A_dice:
        A_list.append(dice[d])
    B_list = []
    for d in B_dice:
        B_list.append(dice[d])
    
    A_result = []
    B_result = []
    
    for A in list(product(*A_list)):
        A_result.append(sum(A))

    for B in list(product(*B_list)):
        B_result.append(sum(B))

    A_result.sort()
    B_result.sort()
    
    B_index = 0
    B_small = 0
    for A_total in A_result:
        for i in range(B_index,len(B_result)):
            if A_total <= B_result[i]:
                B_index = i
                break
            if i == len(B_result)-1:
                B_index = i+1
            B_small += 1
        win_count += B_small
    
    return win_count

'''
          for A_result in list(product(*A_list)):
        A_total = sum(A_result)
        for B_result in list(product(*B_list)):
            B_total = sum(B_result)
            if A_total > B_total:
                win_count += 1
   
   
'''

    
def solution(dice):
    N = len(dice)
    for i in range(N):
        dice[i].sort()
    dice_num = [i for i in range(N)]
    win_best = 0
    for A_dice in list(combinations(dice_num,N//2)):
        A_dice = list(A_dice)
        B_dice = []
        for i in range(N):
            if i not in A_dice:
                B_dice.append(i)
        win_count = A_win(dice,A_dice,B_dice)
        if win_count > win_best:
            win_best = win_count
            answer = A_dice
            
    answer.sort()
    for i in range(N//2):
        answer[i] += 1
    return answer