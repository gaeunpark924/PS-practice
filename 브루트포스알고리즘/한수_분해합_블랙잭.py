#브루트포스는 거의 다 완전탐색
#한수
#https://www.acmicpc.net/problem/1065
#한수: 양의 정수의 각 자리가 등차수열을 이루는 수 ex) 123, 321
#입력: 1000보다 작거나 같은 수
def han_number(x):
    #자릿수 구하기
    s1,s2 = x//10,x%10
    t1,t2 = s1//10,s1%10
    i1,i2 = t1//10,t1%10
    #한수인지 확인
    if x > 100 and x < 1000:      #100 초과, 1000 미만이면 계산
        if t2-s2 == i2-t2:
            return 1
        else:
            return 0
    elif x == 1000 or x == 100:   #1000, 100일 때 예외처리
        return 0
    else:                         #십의 자리수는 모두 한수
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

#한수_다른풀이 1)
for n in range(1, num+1) :
    if n > 99 :
        nums = list(map(int, str(n)))               #파이썬 문법을 이용해서 자릿수대로 분리하는 법*** 
        if nums[0] - nums[1] == nums[1] - nums[2] : #등차수열 확인
            hansu+=1
            
#한수_다른풀이 2)
def solution():
    number = int(input())
    answer = 0
    if number < 100:                                #나 말고 다른 스터디원들은 대부분 두 자릿수는 미리 예외처리를 해놓고 풀이함
        answer = number
        print(answer)
    else:
        answer = 99
        for n in range(100,number+1):
            first = int(n / 100)
            second = int((n % 100) / 10)
            third = int((n % 100) % 10)
            if (first - second) == (second - third):
                answer += 1
        print(answer)
            
#분해합
#https://www.acmicpc.net/problem/2231
#245의 분해합은 256(=245+2+4+5)이다. 245는 256의 생성자라고 한다
def solution(n):
    #분해합
    result = 0
    for i in range(1,n):            #n//2 부터 해도 됨. 시간 단축
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
#분해합_다른풀이 1) 시간 최적화                          #내 풀이보다 더 좋은 풀이************** 
target = int(input())
min_target = abs(target - (len(str(target)) * 9))       #생성자의 최소값을 구하는 것. 자릿수 만큼 9를 뺌
for i in range(min_target, target):
    temp = sum(map(int, str(i)))
    result = i + temp
    if result == target:
        print(i)
        break
else:
    print(0)

#블랙잭
#https://www.acmicpc.net/problem/2798
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

#블랙잭_다른풀이 1) 외부 라이브러리 사용X 삼중 반복문 사용. 조합 문제를 이렇게도 구현할 수 있다는 것 알아두기
n,m = list(map(int, input().split(' ')))
cards = list(map(int, input().split(' ')))
result = 0
length = len(cards)
# 3개만 뽑으니까 3중 반복문도 가능
for i in range (0, length):
    for j in range(i+1, length):
        for k in range (j+1, length):
            sum_value = cards[i]+cards[j]+cards[k]
            if sum_value <=m:
                result = max(result, sum_value)
print(result)
