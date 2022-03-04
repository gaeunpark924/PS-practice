#백준 2309번 일곱 난쟁이
#https://www.acmicpc.net/problem/2309
#입력 받는 수의 범위가 9 로 정해져 있어 combinations를 이용해서 9 명의 난쟁이 중에 7명의 난쟁이를 뽑는 모든 조합을 만들어서 풀었다.
#7명의 난쟁이의 키의 합이 100이면 키를 출력하고 break해서 더이상 탐색하지 않고 종료한다.
#combinations을 사용한 문제는 오랜만에 풀어보는데 잊어버리지 않도록 종종 풀어야 겠다!
from itertools import combinations
height = [int(input()) for _ in range(9)]
height = sorted(height)
#combinations로 72개 조합 생성
for value in combinations(height,7):
    if sum(value)==100:
        for i in range(7):
            print(value[i])
        break

        
#백준 1929번 소수 구하기
#https://www.acmicpc.net/problem/1929
#처음 푼 풀이
#소수의 정의를 이용해서 2부터 모든 수를 나누고 나머지가 0 이면 소수가 아니라고 판별했다. -> 시간초과
import sys
def getPrimeNumber(m, n):
    for i in range(m,n+1):
        if i == 1:
            continue
        else:
            prime_num = True
            for j in range(2,i//2+1):
                if i%j == 0:
                    prime_num = False
                    break
            if prime_num:
                print(i)
            prime_num = True
    return
m, n = sys.stdin.readline().split()
getPrimeNumber(int(m),int(n))

#다른 방법이 있을 것 같아서 검색해서 에라토스테네스의 체를 이용하여 풀었다.
#i가 소수인지 판별하기 위해서 2부터 i//2까지만 나눠주면 된다고 생각했는데
#정답을 보니 i//2 보다 더 작은 값인 제곱근까지만 계산 하면 된다!
import sys
def getPrimeNumber(m, n):
    prime_num = [True] * (n+1)
    for i in range(2, int(n**0.5)+1):   #N까지의 소수 검사할 때 제곱근까지만 하면 된다.****************
        if prime_num[i]:
            for j in range(i*2, n+1, i):
                prime_num[j] = False
    for i in range(m,n+1):
        if i <= 1:
            continue
        if prime_num[i] == True:
            print(i)                   
    return
m, n = sys.stdin.readline().split()
getPrimeNumber(int(m),int(n))
