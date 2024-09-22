from collections import deque

def solution(maps):
    answer = []
    N = len(maps)
    M = len(maps[0])
    
    dx = [0,1,0,-1]
    dy = [1,0,-1,0]
    visited = [[False] * M for _ in range(N)]
    for i in range(N):
        for j in range(M):
            if visited[i][j] == False and maps[i][j] != 'X':
                q = deque()
                q.append([i,j])
                visited[i][j] = True
                count = 0
                while q:
                    x,y = q.popleft()
                    count += int(maps[x][y])
                    for t in range(4):
                        nx = x + dx[t]
                        ny = y + dy[t]
                        if nx>=0 and nx<=N-1 and ny>=0 and ny<=M-1:
                            if visited[nx][ny] == False:
                                if maps[nx][ny] != 'X':
                                    q.append([nx,ny])
                                    visited[nx][ny] = True
                answer.append(count)
    
    answer.sort()
    if len(answer) == 0:
        answer.append(-1)
    return answer