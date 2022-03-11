#백준 3085번 사탕게임
#https://www.acmicpc.net/problem/3085
#부르트포스로 하나씩 계산하면서 풀었음
#열 방향 탐색을 쉽게 하기 위해 zip을 이용하여 전치시킨 보드를 생성함
#최대 연속 사탕 개수를 구하는 함수의 argument로 전치시킨 보드와 기존 보드를 전달해서 값을 계산한다.
#이때, 리스트는 call by reference 로 참조할 주소만 전달하므로 메모리 사용량을 줄일 수 있다.
def continuousPart(n, board, trans_board):
    mx_length = 1
    length = 1
    trans_length = 1
    for i in range(n):
        length = 1
        trans_length = 1
        for j in range(1,n):
            if board[i][j] == board[i][j-1]:
                length += 1
            else:
                mx_length = max(mx_length,length)
                length = 1
            if trans_board[i][j] == trans_board[i][j-1]:
                trans_length += 1
            else:
                mx_length = max(mx_length,trans_length)
                trans_length = 1
        mx_length = max(mx_length,trans_length, length)
    return max(mx_length,trans_length, length)
    
def bomboni(n,board,trans_board):
    mx_result = 1
    for i in range(n):
        for j in range(n):
            if j+1 < n and board[i][j] != board[i][j+1]:
                board[i][j], board[i][j+1] = board[i][j+1], board[i][j]
                trans_board[j][i], trans_board[j+1][i] = trans_board[j+1][i], trans_board[j][i]
                mx_result = max(continuousPart(n,board,trans_board),mx_result)
                board[i][j], board[i][j+1] = board[i][j+1], board[i][j]
                trans_board[j][i], trans_board[j+1][i] = trans_board[j+1][i], trans_board[j][i]
            if i+1 < n and board[i][j] != board[i+1][j]:
                board[i][j], board[i+1][j] = board[i+1][j], board[i][j]
                trans_board[j][i], trans_board[j][i+1] = trans_board[j][i+1], trans_board[j][i]
                mx_result = max(continuousPart(n,board,trans_board),mx_result)
                board[i][j], board[i+1][j] = board[i+1][j], board[i][j]
                trans_board[j][i], trans_board[j][i+1] = trans_board[j][i+1], trans_board[j][i]
    return mx_result
n = int(input())
board = [list(input()) for _ in range(n)]
trans_board = [list(x) for x in zip(*board)]
print(bomboni(n,board,trans_board))

#백준 1476번 날짜 계산
#https://www.acmicpc.net/problem/1476
#처음에는 E+(15의 배수), S+(28의 배수), M+(19의 배수) 가 모두 같아지는 수를 찾으려고 했는데,
#이렇게 풀면 쉽게 풀리지 않는다.
#15, 28, 19의 배수들의 사이에 규칙을 찾지 못해서 반복문을 계속 해서 돌려야 하고 비교 process도 복잡해질 것 같았다.
#문제와 반대로 우리가 알고 있는 년도를 증가시키는 방식으로 풀어야 한다.
def calculateDate(E,S,M):
    e,s,m = 1,1,1
    result = 1
    while(True):
        if e == E and s == S and m == M:
            break
        e+=1
        s+=1
        m+=1
        if e == 16:
            e = 1
        if s == 29:
            s = 1
        if m == 20:
            m = 1
        result += 1
    return result
E, S, M = map(int, input().split())
print(calculateDate(E,S,M))
