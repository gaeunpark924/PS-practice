#상하좌우
#시뮬레이션
def solution(n,move):
    d = {'R':(0,1),'L':(0,-1),'U':(-1,0),'D':(1,0)}
    start = [1,1]
    for m in move:
        start[0] += d[m][0]
        start[1] += d[m][1]
        if start[0] < 1 or start[0] > n:
            start[0] -= d[m][0]
        elif start[1] < 1 or start[1] > n:
            start[1] -= d[m][1]
    return start
n = 5
move = ['R','R','R','U','D','D']
print(solution(n,move))

#시각
#완전탐색
from datetime import datetime, timedelta
def solution(n):
    answer = 0
    time = datetime.strptime('00:00:00', '%H:%M:%S')
    ntime = datetime.strptime(str(n).rjust(2,'0')+':59:59','%H:%M:%S')
    while time < ntime:
        time += timedelta(seconds=1)
        if '3' in str(time):
            answer += 1
    return answer
n = 5
print(solution(n))

#왕실의 나이트
def solution(night):
    answer = 0
    nxny = [[-2,-1],[-2,1],[-1,-2],[-1,2],[1,-2],[1,2],[2,-1],[2,1]]
    r = int(night[1])
    c = int(ord(night[0])) - int(ord('a')) + 1
    for xy in nxny:
        if 1 <= r+xy[0] <= 8 and 1 <= c+xy[1] <= 8:
            answer += 1
    return answer
print(solution('c2'))

#게임 개발
def solution(n,m,r,c,d,game_map):
    answer = 1
    dx = [-1,0,1,0]
    dy = [0,1,0,-1]
    direction = [3, 0, 1, 2]
    cnt = 0
    while 1:
        game_map[r][c] = 2 #방문한 칸 2
        d = direction[d]   #방향 이동  
        new_r = r + dx[d]  #한 칸 앞으로
        new_c = c + dy[d]
        if game_map[new_r][new_c] == 2 or game_map[new_r][new_c] == 1:
            cnt += 1
            if cnt == 4:
                r -= dx[d]  #현재 방향에서 한 칸 뒤로
                c -= dy[d]  
                if game_map[r][c] == 1 or game_map[r][c] == 2:
                    break
        else:
            cnt = 0
            answer += 1
            r, c = new_r, new_c
    return answer
n, m = 4, 4
r, c, d = 1, 1, 0
game_map = [[1,1,1,1],[1,0,0,1],[1,1,0,1],[1,1,1,1]]
print(solution(n,m,r,c,d,game_map))

# def solution(n,m,r,c,d,game_map):
#     answer = 0
#     left_turn = [[0,-1],[-1,0],[0,1],[1,0]]
#     back = [[1,0],[0,-1],[-1,0],[0,1]]
#     direction = [3, 0, 1, 2]
#     cnt = 0
#     while 1:
#         new_r = r + left_turn[d][0]
#         new_c = c + left_turn[d][1]
#         if game_map[new_r][new_c] == 2 or game_map[new_r][new_c] == 1:
#             cnt += 1
#             if cnt == 4:
#                 r += back[d][0]
#                 c += back[d][1]
#                 if game_map[r][c] == 2:
#                     break
#         else:
#             cnt = 0
#             answer += 1
#             r, c = new_r, new_c
#             game_map[r][c] = 2
#         d = direction[d]
#     return answer