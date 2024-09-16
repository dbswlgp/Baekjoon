from collections import deque

M,N,K = map(int,input().split())

array = [[0]*M for _ in range(N)]

for _ in range(K):
    x1,y1,x2,y2 = map(int,input().split())
    for x in range(x1,x2):
        for y in range(y1,y2):
            array[x][y] = 1

dx = [0,1,0,-1]
dy = [1,0,-1,0]

size = []
visited = [[False]*M for _ in range(N)]
for i in range(N):
    for j in range(M):
        if array[i][j] == 0 and visited[i][j] == False:
            visited[i][j] = True
            q = deque()
            q.append([i,j])
            count = 0
            while q:
                x,y = q.popleft()
                count += 1
                for t in range(4):
                    nx = x + dx[t]
                    ny = y + dy[t]
                    if nx>=0 and nx<=N-1 and ny>=0 and ny<=M-1:
                        if array[nx][ny] == 0 and visited[nx][ny] == False:
                            q.append([nx,ny])
                            visited[nx][ny] = True
            size.append(count)

size.sort()
print(len(size))
for i in range(len(size)):
    print(size[i],end=' ')