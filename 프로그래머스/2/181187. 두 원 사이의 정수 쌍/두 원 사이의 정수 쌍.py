def point(r):
    edge = 0
    result = 0
    y_start = r
    for x in range(0,r+1):
        for y in range(y_start,-1,-1):
            if y**2 <= r**2-x**2:
                y_start = y
                break
        if y_start**2 == r**2-x**2:
            edge += 1
            result += y_start
        else:
            result += (1+y_start)
    result -= (r-1)
    result *= 4
    result -= 3
    edge -= 1
    edge *= 4
    return result, edge
            
def solution(r1, r2):
    point1,edge1 = point(r1)
    point2,edge2 = point(r2)
    answer = point2 + edge2 - point1
    return answer