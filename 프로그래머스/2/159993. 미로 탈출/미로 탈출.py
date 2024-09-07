from collections import deque

def short_dist(start,end,maps):
    N = len(maps)
    M = len(maps[0])
    visited = [[False]*M for _ in range(N)]
    dx = [0,1,0,-1]
    dy = [1,0,-1,0]
    for i in range(N):
        for j in range(M):
            if maps[i][j] == start:
                q = deque()
                q.append([i,j,0])
                visited[i][j] = True
                while q:
                    x,y,dist = q.popleft()
                    if maps[x][y] == end:
                        return dist
                    for t in range(4):
                        nx = x + dx[t]
                        ny = y + dy[t]
                        if nx>=0 and nx<=N-1 and ny>=0 and ny<=M-1:
                            if visited[nx][ny] == False and maps[nx][ny] != 'X':
                                q.append([nx,ny,dist+1])
                                visited[nx][ny] = True
    return 0


def solution(maps):
    lever = short_dist('S','L',maps)
    exit = short_dist('L','E',maps)
    if lever == 0 or exit == 0:
        return -1
    else:
        return lever + exit