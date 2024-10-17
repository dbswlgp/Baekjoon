import sys

S,E,Q = input().split()

comment = []

for line in sys.stdin:
  comment.append(line.strip())

before_start = set()
after_finish = set()

for c in comment:
  if (int(S[0:2]) == int(c[0:2]) and int(S[3:]) >= int(c[3:5])) or (int(S[0:2]) > int(c[0:2])):
    before_start.add(c[6:])
  elif (int(E[0:2]) == int(c[0:2]) and int(E[3:]) <= int(c[3:5])) or (int(E[0:2]) < int(c[0:2])):
    if (int(Q[0:2]) == int(c[0:2]) and int(Q[3:]) >= int(c[3:5])) or (int(Q[0:2]) > int(c[0:2])):
      after_finish.add(c[6:])

answer = before_start & after_finish

print(len(answer))