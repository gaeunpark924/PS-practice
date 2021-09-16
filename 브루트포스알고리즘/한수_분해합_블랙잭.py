#한수
def han_number(x):
    #자릿수 구하기
    s1,s2 = x//10,x%10
    t1,t2 = s1//10,s1%10
    i1,i2 = t1//10,t1%10
    #한수인지 확인
    if x > 100 and x < 1000:
        if t2-s2 == i2-t2:
            return 1
        else:
            return 0
    elif x == 1000 or x == 100:
        return 0
    else:
        return 1
def solution(a):
    cnt = 0
    for i in range(1,a+1):
        x = han_number(i)
        if x == 1:
            cnt += 1
    return cnt
a = int(input())
print(solution(a))

#분해합
def solution(n):
    #분해합
    #245의 분해합은 256(=245+2+4+5)이다. 245는 256의 생성자라고 한다
    result = 0
    for i in range(1,n):
        new_i = i
        decom_sum = i
        while new_i > 0:
            decom_sum += new_i%10
            new_i = new_i//10
        if decom_sum == n:
            result = i
            break
    return result
N = int(input())
print(solution(N))

#블랙잭
from itertools import combinations
#N개의 카드에서 3장을 뽑아 M이 넘지 않는 수가 되게 하기
def solution(n,m,num_card):
    x = list(combinations(num_card, 3))
    result = []
    for i in x:
        result.append(sum(i))
    result = sorted(result)
    for i in range(len(result)):
        if result[i] > m:
            return result[i-1]
    return result[-1]
N, M = map(int,input().split())
num_card = list(map(int,input().split()))
print(solution(N,M,num_card))
