#백준 9655번 돌게임
# https://www.acmicpc.net/problem/9655
# 1 또는 3만 가져갈 수 있으니 남은 돌의 개수가 홀수, 짝수인지 판별해서
# 홀수이면 먼저 시작한 상근이가 이기고 짝수이면 창영이가 이깁니다
def solution_stone_game(n):
    return "CY" if n%2 == 0 else "SK"  
n = int(input())
print(solution_stone_game(n))