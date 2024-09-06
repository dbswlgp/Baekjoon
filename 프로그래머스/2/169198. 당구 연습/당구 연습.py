def east(m,n,startX,startY,ballX,ballY):
    return (m-startX+m-ballX)**2 + abs(startY-ballY)**2

def west(m,n,startX,startY,ballX,ballY):
    return (startX+ballX)**2 + abs(startY-ballY)**2
    
def south(m,n,startX,startY,ballX,ballY):
    return (startY+ballY)**2 + abs(startX-ballX)**2
    
def north(m,n,startX,startY,ballX,ballY):
    return (n-startY+n-ballY)**2 + abs(startX-ballX)**2

def solution(m, n, startX, startY, balls):
    answer = []
    for ballX,ballY in balls:
        min_dist = 2000**2 + 1000**2
        if startX == ballX:
            if ballY > startY:
                min_dist = min(min_dist,south(m,n,startX,startY,ballX,ballY))
            else:
                min_dist = min(min_dist,north(m,n,startX,startY,ballX,ballY))
        else:
            min_dist = min(min_dist,south(m,n,startX,startY,ballX,ballY))
            min_dist = min(min_dist,north(m,n,startX,startY,ballX,ballY))
        if startY == ballY:
            if ballX > startX:
                min_dist = min(min_dist,west(m,n,startX,startY,ballX,ballY))
            else:
                min_dist = min(min_dist,east(m,n,startX,startY,ballX,ballY))
        else:
            min_dist = min(min_dist,west(m,n,startX,startY,ballX,ballY))
            min_dist = min(min_dist,east(m,n,startX,startY,ballX,ballY))
        answer.append(min_dist)
        
    return answer