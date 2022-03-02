#백준 17626번 Four Squares
#https://www.acmicpc.net/problem/17626
#처음에 점화식을 세워서 풀려다가 점화식으로 깔끔하게 코딩할 수 없을 것 같아 math 라이브러리를 이용하여 수학적으로 접근했음
#처음 입력받은 수의 루트값이 자연수라면 1을 출력하고 아닐때는 별도 로직으로 구현하려고 했으나 결국 구글링으로 답을 찾아보았음
#별도 로직을 구현하면서 스스로 생각을 잘못한게 루트값에서 -1을 하면서 계산하려고 했는데 이 방식은 너무 복잡한 것 같음
#그냥 1부터 루트값까지 루프를 돌면서 탐색하고 n 보다 커지면 break하는 방식으로 했으면 답이 나왔을 것 같음
import math
def fourSquares(n):
    num = math.sqrt(n)
    if num.is_integer():
        return 1
    max_square = int(num)
    for i in range(1,max_square+1):
        if math.pow(i,2) > n:
            break
        elif math.sqrt(n - math.pow(i,2)).is_integer():  #제곱수인지 판별
            return 2

    for i in range(1,max_square+1):
        if math.pow(i,2) > n:
            break
        for j in range(i,max_square+1):
            if math.pow(i,2) + math.pow(j,2)> n:
                break
            elif math.sqrt(n - math.pow(i,2) - math.pow(j,2)).is_integer():
                return 3
    return 4    
n = int(input())
print(fourSquares(n))
