# 프로그래머스 Lv2 문자열압축
# https://programmers.co.kr/learn/courses/30/lessons/60057
# 2020 카카오 신입 공채

def stringCompression(input_s, n):
    result = []
    tmp = False

    for i in range(0, len(input_s), n):
        if input_s[i + n:i + 2*n] == input_s[i:i + n]:
            if tmp:
                result[-2] = str(int(result[-2]) + 1)
            else:
                result.append('2')
                result.append(input_s[i:i + n])
                tmp = True
        else:
            if tmp:
                tmp = False
            else:
                result.append(input_s[i:i + n])

    return len("".join(result))


def solution(s):
    answer = len(s)

    for i in range(1, len(s) // 2 + 1):
        answer = min(stringCompression(s, i), answer)

    return answer



# 프로그래머스 Lv3 자물쇠와열쇠
# https://programmers.co.kr/learn/courses/30/lessons/60059
# 2020 카카오 신입 공채

def solution(key, lock):
    M = len(key[0])  # key 크기
    N = len(lock[0])  # lock 크기

    # 자물쇠 넓히기
    board = [[0] * (M * 2 + N) for _ in range(M * 2 + N)]
    for i in range(N):
        for j in range(N):
            board[i + M][j + M] = lock[i][j]

    # 처음
    for i in range(1, M + N):
        for j in range(1, M + N):
            attach(key, board, M, N, i, j)
            if check(board, N, M):
                return True
            detach(key, board, M, N, i, j)

    # 90도, 180도 270도 회전
    answer = False
    for i in range(3):
        rotate90(key, M)
        for j in range(1, M + N):
            for s in range(1, M + N):
                attach(key, board, M, N, j, s)
                if check(board, N, M):
                    answer = True
                    break
                detach(key, board, M, N, j, s)
            if answer:
                break

    return answer


# 카를 넣는다
def attach(key, board, M, N, i, j):
    for s in range(M):
        for t in range(M):
            board[i + s][j + t] += key[s][t]

    return


# 키를 뺀다
def detach(key, board, M, N, i, j):
    for s in range(M):
        for t in range(M):
            board[i + s][j + t] -= key[s][t]

    return


# 모두 1인지 확인
def check(board, N, M):
    all_one = True
    for i in range(M, M + N):
        for j in range(M, M + N):
            if board[i][j] != 1:
                all_one = False
                break
        if not all_one:
            break
            
    return all_one


# 90도 회전
def rotate90(key, M):
    for i in range(M // 2):
        for j in range(M):
            if i <= j and i + j < M - 1:
                key[j][M - 1 - i], swap = key[i][j], key[j][M - 1 - i]
                swap, key[M - 1 - i][M - 1 - j] = key[M - 1 - i][M - 1 - j], swap
                key[M - 1 - j][i], swap = swap, key[M - 1 - j][i]
                key[i][j] = swap

    return

# 90도 회전 - 짧은 코드
a = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(list(map(list, zip(*a[::-1]))))