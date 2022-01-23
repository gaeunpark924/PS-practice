
# 백준 7552번 나이트의 이동
# https://www.acmicpc.net/problem/7562
# 2차원 배열에 표시하는 방식
# 큐를 이용하여 bfs 구현
from collections import deque
def bfs_night_move(n,current,reach):
    dx = [-2,-2,-1,1,2,2,-1,1]
    dy = [-1,1,2,2,-1,1,-2,-2]
    queue = deque([[current[0],current[1]]])
    visited=[]
    a[current[0]][current[1]] = 1
    while queue:
        next = queue.popleft()
        visited.append([next[0],next[1]])
        #print([next[0],next[1]],queue,reach)
        if [next[0],next[1]] == reach:
            return a[next[0]][next[1]]-1 #next[2]
        for i in range(8):
            nx = next[0]+dx[i]
            ny = next[1]+dy[i]
            if 0 <= nx < n and 0 <= ny < n:
                if a[nx][ny] == 0:
                    #print([nx,ny])
                    # if nx >= 20 and ny >= 20:
                    #     print([nx,ny])
                    a[nx][ny] = a[next[0]][next[1]] + 1
                    queue.append([nx,ny])
    return

tc = int(input())
for i in range(tc):
    n = int(input())
    current = list(map(int,input().split()))
    reach = list(map(int,input().split()))
    a = [[0]*n for _ in range(n)]
    print(bfs_night_move(n,current,reach))
