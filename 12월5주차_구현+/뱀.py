#백준 3190번 뱀
#https://www.acmicpc.net/problem/3190
#뱀의 위치는 deque를 사용해서 저장했고 머리가 늘어나면 append 하고 꼬리가 줄어들면 popleft 해주었습니다.
#코드가 길어져서 뱀이 움직이는 건 moving 함수로 따로 만들었고
#그리고 문제에서 주어지는 보드의 크기가 벽을 포함한 크기라고 생각했는데 그게 아니더라구요
#‘상하좌우 끝에 벽이 있다’고 되어있어서 이해하는데 시간이 좀 걸렸습니다.
#그래서 처음 재귀함수 돌릴 때 n을 2 늘렸더니 통과했습니다.

from collections import deque
import sys
sys.setrecursionlimit(100000000)
def solution(n,k,apple,l,way):
    global time
    snake = deque([[1,1]])
    time = 0
    #처음 방향 오른쪽
    #오른쪽을 0, 위쪽을 1, 왼쪽을 2, 아래쪽을 3
    move(snake,apple,deque(way),0,n+2)
    return time+1
def moving(direction, i, j):
    nx = [0,-1,0,1]
    ny = [1,0,-1,0]
    return [i+nx[direction],j+ny[direction]]
def move(snake,apple,way,direction,n):
    global time
    if way and time == way[0][0]:
        tmp = way[0][1]
        if tmp == 'L':
            direction = (direction+1) % 4
        elif tmp == 'D':
            direction = (direction+3) % 4
        next_move = moving(direction,snake[-1][0],snake[-1][1])
        way.popleft()
    else:
        next_move = moving(direction,snake[-1][0],snake[-1][1])
    if (next_move[0] == 0 or next_move[0] == n-1) or (next_move[1] == 0 or next_move[1] == n-1): #벽에 닿으면
        return
    elif next_move in snake: #몸에 닿으면
        return
    #아무데도 안 닿으면
    if [next_move[0],next_move[1]] in apple:  #사과를 먹으면
        del apple[apple.index([next_move[0],next_move[1]])]
    else: #사과를 먹지 않으면
        snake.popleft()
    snake.append(next_move)
    time += 1  #시간 1초 흐름
    move(snake, apple, way, direction, n)
    return    
n = int(input())
k = int(input())
apple = [list(map(int,input().split())) for _ in range(k)]
l = int(input())
way = []
for i in range(l):
    x, c = input().split()
    way.append([int(x),c])
print(solution(n,k,apple,l,way))
