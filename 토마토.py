import copy             # copy 모듈을 가져옴
from collections import deque
def tomato_func(tomato, size):
    m, n = size[1], size[0]  #4

    a = [-1,0,0,1]
    b = [0,-1,1,0]
    
    if all(0 not in l for l in tomato):    #tomato에 0이 없으면
        return 0

    #marking 할 2차원 리스트
    sub = copy.deepcopy(tomato)            #다차원 리스트 복사. 2차원 리스트는 copy() 안됨.

    #bfs 구현할 queue
    queue = deque([])                      #queue
    for i in range(m):
        for j in range(n):
            if tomato[i][j] == 1:
                queue.append([i,j])     
    #queue에서 pop할 게 없으면 다음 layer로
    x = len(queue)

    day = 0
    while(1):
        #같은 queue에 담긴 것만
        for k in range(x):
            root = queue.popleft()
            i, j = root[0], root[1]
            for s in range(4):
                nx = i + a[s]
                ny = j + b[s]
                a1 = 0
                if nx < 0 or nx > m-1 or ny < 0 or ny > n-1:
                    continue
                else:
                    a1 = tomato[nx][ny]
                    if a1 == 0 and sub[nx][ny] == 0:
                        queue.append([nx,ny])
                        sub[nx][ny] = 1
                    elif a1 == 1 or a1 == -1:
                        continue
        x = len(queue)
        day += 1
        if not queue:
            if any(0 in l for l in sub):
                return -1
            else:
                return day-1
     
size = list(map(int, input().split()))
tomato = []
for i in range(size[1]):
    tomato.append(list(map(int,input().split())))
result = tomato_func(tomato, size)

print(result)
