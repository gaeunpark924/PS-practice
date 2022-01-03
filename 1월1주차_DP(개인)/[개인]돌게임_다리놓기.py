#백준 9655번 돌게임
# https://www.acmicpc.net/problem/9655
# 1 또는 3만 가져갈 수 있으니 남은 돌의 개수가 홀수, 짝수인지 판별해서
# 홀수이면 먼저 시작한 상근이가 이기고 짝수이면 창영이가 이깁니다
def solution_stone_game(n):
    return "CY" if n%2 == 0 else "SK"  
n = int(input())
print(solution_stone_game(n))

#백준 1010번 https://www.acmicpc.net/problem/1010
# DP문제여서 일부러 점화식을 만들어서 풀었습니다.
# n과 m이 같을 때는 경우의 수가 1 이고
# m-1 경우의 수에 m/((m-1)-(n-1)) 을 곱하면 m 의 경우의 수가 된다.
def solution_bridge(t, site_west_east):
    for i in range(t):
        n = site_west_east[i][0]
        m = site_west_east[i][1]
        case = [1]
        if n == 1:
            print(m)
            continue
        for j in range(n+1,m+1): #j n,n+1,,,,,,m
            case.append(round(case[-1]*(j/((j-1)-(n-1)))))
        print(case[-1])
    return
t = int(input())
site_west_east = [list(map(int,input().split())) for _ in range(t)]
solution_bridge(t, site_west_east)
