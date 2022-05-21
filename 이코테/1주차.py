#큰 수의 법칙
def big_number(n,m,k,num_li):
    num_li.sort()
    first = num_li[-1]
    second = num_li[-2]
    #각각 더해지는 횟수를 구함
    answer = first*((m // (k+1))*k + (m % (k+1)))  #가장 큰 수가 더해지는 횟수
    answer += second*(m // (k+1))   #두번 째로 큰 수가 더해지는 횟수
    return answer
n, m, k = map(int,input().split())
num_li = list(map(int,input().split()))
print(big_number(n,m,k,num_li))
# #숫자 카드 게임
def card_game(n,m,number_card):
    max_val = float('-inf')
    for row in number_card:
        mn = min(row)
        max_val = max(mn, max_val)     #max 값
    return max_val
n, m = map(int,input().split())
number_card = []
for i in range(n):
    number_card.append(list(map(int,input().split())))
print(card_game(n,m,number_card))

#처음 풀이
def one(n,k):
    count = 0
    while n > 1:
        if n%k == 0:
            n /= k
        else:
            n -= 1
        count += 1
    return count
#최적화
def one(n,k):
    count = 0
    while n > 1:
        if n%k == 0:
            n /= k
            count += 1
        else:
            count += n%k #n이 k로 나누어 떨어질 때까지 빼기
            n -= n%k
    return count
n, k = map(int,input().split())
print(one(n,k))