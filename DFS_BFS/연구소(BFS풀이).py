"""
풀이 과정
1. 바이러스 리스트를 만든다 
2. 3개의 벽을 세울 조합을 만든다 (itertools의 combinations 사용)
3. 벽을 세울 수 있는 경우의 수 만큼 bfs 탐색한다
4. 안전영역이 최대인 경우를 골라서 출력한다
"""
import copy             
from collections import deque
from itertools import combinations

def wall(birus, size):
    m, n = size[0], size[1]
    l1 = []
    for i in range(m):
        for j in range(n):
            if birus[i][j] == 0:
                l1.append((i,j))
    result = list(combinations(l1, 3))
    return result

def birus_bfs(birus, size):
    m, n = size[0], size[1]  #4

    a = [-1,0,0,1]
    b = [0,-1,1,0]
    
    sub = copy.deepcopy(birus)            #다차원 리스트 복사. 2차원 리스트는 copy() 안됨.
    
    l2 = []
    for i in range(m):
        for j in range(n):
            if birus[i][j] == 2:
                l2.append([i,j])
    
    max = 0
    select_wall = wall(birus, size)
    for i in range(len(select_wall)):
        #벽 세우기
        for j in range(3):
            w = select_wall[i][j]
            birus[w[0]][w[1]] = 1
        sub = copy.deepcopy(birus)  
        #marking 할 2차원 리스트
        queue = deque(l2)

        while(1):
            root = queue.popleft()
            x, y = root[0], root[1]
            for s in range(4):
                nx = x + a[s]
                ny = y + b[s]
                if nx < 0 or nx > m-1 or ny < 0 or ny > n-1:
                    continue
                else:
                    a1 = birus[nx][ny]
                    if a1 == 0 and sub[nx][ny] == 0:
                        queue.append([nx,ny])
                        sub[nx][ny] = 2
                    elif a1 == 1 or a1 == 2:
                        continue
            if not queue:
                cnt = 0  
                for s in range(m):
                    cnt += sub[s].count(0)
                if cnt > max:
                    max = cnt
                break
        #벽 허물기
        for j in range(3):
            w = select_wall[i][j]
            birus[w[0]][w[1]] = 0

    return max


size = list(map(int, input().split()))
birus = []
for i in range(size[0]):
    birus.append(list(map(int,input().split())))
result = birus_bfs(birus, size)
print(result)
