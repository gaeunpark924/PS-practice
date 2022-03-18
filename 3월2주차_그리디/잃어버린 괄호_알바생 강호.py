#백준 1541번 잃어버린 괄호 https://www.acmicpc.net/problem/1541
#예전에 한 번 푼 문제였는데 다시 풀으니까 못 풀겠음
#-로 split하고 + 계산
#그 이후에는 그냥 순서대로 - 를 계산해주면 되는 거였음
def threeNum(li,MINMAX):
    if MINMAX == 'mn':
        return min((li[0]-li[1])-li[2],li[0]-(li[1]-li[2]))
    elif MINMAX == 'mx':
        return max((li[0]-li[1])-li[2],li[0]-(li[1]-li[2]))
def bracketGreedy(bracket):
    bracket_li = bracket.split('-')
    if len(bracket_li) == 1:
        return sum(map(int, bracket.split('+')))
    elif len(bracket_li) == 2:
        return sum(map(int, bracket_li[0].split('+'))) - sum(map(int, bracket_li[1].split('+')))
    else:
        sum_li = []
        for value in bracket_li:
            sum_li.append(sum(map(int, value.split('+'))))
        if len(sum_li)%2 == 0:
            tmp = 'mn'
        else:
            tmp = 'mx'
        for i in range(len(sum_li)-1,1,-2):
            sum_li[i-2] = threeNum(list(map(int, sum_li[i-2:i+1])),tmp)
            if tmp == 'mn':
                tmp = 'mx'
            else:
                tmp = 'mn'
        return sum_li[0]
#다른 풀이
#최초로 - 가 나오면 그 뒤는 - 로 계산하면 됨
def bracketGreedy(bracket):
    result = 0
    s = bracket.split('-')
    for value in s[0].split('+'):
        result += int(value)
    if len(s) == 1:      # - 가 없으면 그냥 return 한다. 없어도 s[1:]는 [] 이어서 오류는 발생하지 않는다. 
        return result
    for i in s[1:]:
        for j in i.split('+'):
            result -= int(j)
    return result
bracket = input()
print(bracketGreedy(bracket))

#백준 1758번 알바생 강호
#https://www.acmicpc.net/status?user_id=gaeuns&problem_id=1758&from_mine=1
#알바생 강호
#원래 주려고 생각했던 돈이 큰 사람의 등수를 높게 해야 함 
#내림차순으로 정렬하고 반복문을 사용해서 양수일 때 더해줌
#반대로 생각해서 오름차순으로 정렬해서 풀다가 못 풀겠어서 구글링 해서 찾아봄
def starbucks(N,guest_tip):
    guest_tip.sort(reverse=True)
    result = 0
    for i in range(len(guest_tip)):
        if guest_tip[i] - i > 0:
            result += guest_tip[i] - i
    return result
N = int(input())
guest_tip = [ int(input()) for _ in range(N) ]
print(starbucks(N,guest_tip))
    
