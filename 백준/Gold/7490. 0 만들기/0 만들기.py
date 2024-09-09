from itertools import combinations
import copy

def calculate(cal,plus,minus):
  for p in plus:
    cal[p] = '+'
  for m in minus:
    cal[m] = '-'
  num1 = str(cal[0])
  num2 = ''
  op1 = ''
  for i in range(1,len(cal)):
    if cal[i] == '+' or cal[i] == '-':
      if op1 != '':
        if op1 == '+':
          num1 = str(int(num1) + int(num2))
        else:
          num1 = str(int(num1) - int(num2))
        num2 = ''
        op1 = cal[i]
      else:
        op1 = cal[i]
    elif cal[i] != ' ':
      if op1 == '':
        num1 += str(cal[i])
      else:
        num2 += str(cal[i])
  if op1 == '+':
    result = int(num1) + int(num2)
  else:
    result = int(num1) - int(num2)
  if result == 0:
    return cal
  else:
    return False

T = int(input())

for _ in range(T):
  N = int(input())
  cal = [' '] * (2*N-1)
  op = []
  for i in range(len(cal)):
    if i%2 == 0:
      cal[i] = i//2+1
    else:
      op.append(i)
  answer = []
  for i in range(N-1):
    for plus in list(combinations(op,i)):
      except_plus = set(op) - set(plus)
      for j in range(1,N-i):
        for minus in list(combinations(except_plus,j)):
          result = calculate(copy.deepcopy(cal),plus,minus)
          if result != False:
            answer.append(result)
  answer.sort()
  for i in range(len(answer)):
    for j in range(len(answer[i])):
      print(answer[i][j],end='')
    print()
  print()