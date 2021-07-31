from collections import deque
def searchMaze(maze, centerx, centery, queue, mark, a, b):
    mark[centerx][centery] = 1
    while(1):                                                                                         
        for i in range(-1,2):
            for j in range(-1,2):
                if abs(i) + abs(j) == 1 and centerx+i>=0 and centery+j>=0:              #상하좌우 4개 index 비교 #[-1]은 index error가 발생하지 않아서 0 이상인 조건 추가
                    try:                                                                #index error 처리     
                        a1 = maze[centerx+i][centery+j]
                    except IndexError:
                        break
                    if a1 == 1 and mark[centerx+i][centery+j] == 0:                     #방문한 곳은 제외
                        queue.append((centerx+i, centery+j))       
                        mark[centerx+i][centery+j] = marking(mark, centerx+i, centery+j)    #mark 2차원 리스트에 방문한 순서 저장****************
                        if centerx+i == a-1 and centery+j == b-1:       #종점을 방문하면 함수 종료
                            return mark
        centerx, centery = queue.popleft()                                           
    return
def marking(mark, x,y):                                    #상하좌우 비교해서 최소값에 1을 더해서 리턴
    markingMin = 0
    for i in range(-1,2):
        for j in range(-1,2):
            if abs(i) + abs(j) == 1 and x+i>=0 and y+j>=0:
                try:
                    a1 = mark[x+i][y+j]
                except IndexError:
                    break
                if a1 != 0:
                    if markingMin == 0 or a1 < markingMin:
                        markingMin = a1
    return markingMin+1

a, b = map(int, input().split())
li1 = []
for i in range(a):
    x = list(map(int,input()))
    li1.append(x)

queue = deque([])

mark = [[0]*b for _ in range(a)]

mark = searchMaze(li1, 0,0, queue, mark, a, b)
print(mark[a-1][b-1])
