#백준 17626번 Four Squares
#https://www.acmicpc.net/problem/17626
#처음에 점화식을 세워서 풀려다가 점화식으로 깔끔하게 코딩할 수 없을 것 같아 math 라이브러리를 이용하여 수학적으로 접근했음
#처음 입력받은 수의 루트값이 자연수라면 1을 출력하고 아닐때는 별도 로직으로 구현하려고 했으나 결국 구글링으로 답을 찾아보았음
#별도 로직을 구현하면서 스스로 생각을 잘못한게
#제곱수 중 가장 큰 값을 1씩 줄여나가면서 하다보면 풀릴거라고 생각했음 그런데 이 방식은 너무 복잡한 것 같음
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


#백준 1463번 1로 만들기
#https://www.acmicpc.net/problem/1463
#내 풀이(틀림)
#점화식.....
#3으로 나누어 떨어지면, 3으로 나눈다
def makeOne(n):
    if n == 0:
        return 0
    div_three = [n]
    div_two = [n]
    minus_one = [n]
    i = 0
    result = 0
    while(1):
        mn = min(div_three[i],div_two[i],minus_one[i])
        if mn%3 == 0 or mn%2 == 0:
            if mn%3 == 0 and mn%2 == 0:
                div_three.append(mn//3)
                div_two.append(mn//2)
            else:
                if mn%3 == 0:
                    div_three.append(mn//3)
                    div_two.append(mn)
                elif mn%2 == 0:
                    div_two.append(mn//2)
                    div_three.append(mn)
        else:
            div_three.append(mn)
            div_two.append(mn)
        minus_one.append(mn-1)
        i += 1
        print('출력')
        print(div_three)
        print(div_two)
        print(minus_one)
        if div_three[i] == 1 or div_two[i] == 1 or minus_one[i] == 1:
            result = i
            break
    return result
#가져온 풀이 https://hongcoding.tistory.com/46
#길이가 n+1인 배열을 만들고
#3으로 나누거나, 2로 나누거나, 1을 더하는 연산을 하는게 아니라(내가 한 방식)
#그 전 결과를 이용해서 값을 구한다
#n 이 1일 때는 0, n이 2일 때는 1, n이 3일 때는 1, n이 4일 때는 2 .. 이런식으로 계속 계산해나간다
#점화식: 전의 결과를 다음 결과에 이용한다
#10->9->3->1
#9->3->1
#3->1
def makeOne(n):
    dp = [0] * (n+1)
    for i in range(2, n+1):
        dp[i] = dp[i-1] + 1   #2와 3으로 나누어 떨어지지 않으면 무조건 1을 빼야함
        if i%2 == 0:        #2로 나누고
            dp[i] = min(dp[i],dp[i//2]+1)
        if i%3 == 0:        #3으로 나누고
            dp[i] = min(dp[i],dp[i//3]+1)
    return dp[n]
n = int(input())
print(makeOne(n))

