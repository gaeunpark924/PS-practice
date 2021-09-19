  
#좌, 우 방향은 문제 내용을 똑같이 구현하였고 사라진 만큼 0을 채우고 상, 하 방향은 행과 열을 바꿔서 계산함
#그리고 재귀로 완전 탐색하여 최대값 찾음
#처음 채점했을 때 2%에서 계속 틀렸다고 나와서 시간이 2시간 정도 최대 이동시킬 수 있는 횟수가 5인데 4로 해서 틀렸었음ㅜ 그것만 고치고 바로 통과!
#반례가 다 통과하는데 처음이 틀리면 사소한 것을 놓쳤을 가능성이 높다...
#https://www.acmicpc.net/problem/12100
from collections import deque
def left(a, board):
    new_board = []
    for i in range(a):
        line = board[i]
        marking = 0
        sub_board = []
        for j in range(a):
            if line[j] != 0:
                if len(sub_board) != 0:
                    if sub_board[-1] == line[j] and marking == 0:
                        sub_board[-1] += line[j]
                        marking = 1
                        continue
                sub_board.append(line[j])
                marking = 0
        for i in range(a-len(sub_board)):
            sub_board.append(0)
        new_board.append(sub_board)
    return new_board
def right(a, board):
    new_board = []
    for i in range(a):
        line = board[i]
        marking = 0
        sub_board = deque([])
        for j in range(a-1, -1, -1):
            if line[j] != 0:
                if len(sub_board) != 0:
                    if sub_board[0] == line[j] and marking == 0:
                        sub_board[0] += line[j]
                        marking = 1
                        continue
                sub_board.appendleft(line[j])
                marking = 0
        for i in range(a-len(sub_board)):
            sub_board.appendleft(0)
        new_board.append(list(sub_board))
    return new_board
def T(a):
    row = len(a)
    col = len(a[0])
    a_ = [[0 for i in range(row)]for j in range(col)]
    for i in range(row):
        for j in range(col):
            a_[j][i] = a[i][j]
    return a_
import copy 
def search(board, move, cnt):
    if cnt == 6:
        mm = 0
        for i in board:
            if max(i) > mm:
                mm = max(i)
        return mm

    if move == 'left':
        new_board = left(a,board) 
    elif move == 'right':
        new_board = right(a,board)
    elif move == 'up':
        board = deque(T(list(board)))
        new_board = left(a,board)
        new_board = deque(T(list(new_board)))
    elif move == 'down':
        board = deque(T(list(board)))
        new_board = right(a,board)
        new_board = deque(T(list(new_board)))
    cnt += 1
    x = search(new_board, 'left', cnt)
    y = search(new_board, 'right', cnt)
    z = search(new_board, 'up', cnt)
    s = search(new_board, 'down', cnt)

    return max(x,y,z,s)
    
def solution(a, board):
    move = ['left','right','up','down']
    result = []
    for i in range(len(move)):
       result.append(search(board, move[i], 1))
    return max(result)
a = int(input())
board_game = deque([])
for i in range(a):
    board_game.append([int(i) for i in input().split()])
print(solution(a, board_game))
