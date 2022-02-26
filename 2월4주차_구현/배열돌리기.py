#백준 17276번 배열 돌리기
#https://www.acmicpc.net/problem/17276
#45도씩 회전시킴
def rotate45(n,input_matrix):
    h = (n+1)//2-1
    for i in range(n):
        for j in range(n):
            if i == j and i <= h:
                swapT, input_matrix[i][j] = input_matrix[i][j], input_matrix[h][j]
                swapT, input_matrix[i][h] = input_matrix[i][h], swapT
                swapT, input_matrix[i][-j-1] = input_matrix[i][-j-1], swapT
                swapT, input_matrix[h][-j-1] = input_matrix[h][-j-1], swapT
                swapT, input_matrix[-i-1][-j-1] = input_matrix[-i-1][-j-1], swapT
                swapT, input_matrix[-i-1][h] = input_matrix[-i-1][h], swapT
                swapT, input_matrix[-i-1][j] = input_matrix[-i-1][j], swapT
                swapT, input_matrix[h][j] = input_matrix[h][j], swapT
                input_matrix[i][j] = swapT
    return input_matrix
def rotateMatrix(n,d,input_matrix):
    if (d==360 or d==0):
        return input_matrix
    elif (d>=0):
        for _ in range(d//45):
            rotate45(n,input_matrix)
    elif (d<=0):
        for _ in range((360+d)//45):
            rotate45(n,input_matrix)
    return  input_matrix
T = int(input())
for _ in range(T):
    n, d = input().split(' ')
    input_matrix = []
    for i in range(int(n)):
        input_matrix.append(input().split())
    result = rotateMatrix(int(n), int(d), input_matrix)
    for i in range(int(n)):
        for j in range(int(n)):
            print(result[i][j]+' ',end='')
        print()
