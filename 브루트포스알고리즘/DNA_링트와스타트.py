#DNA
#https://www.acmicpc.net/problem/1969
#combination 사용하지 않음
#가장 많이 사용된 알파벳이 거리도 가장 짧을 것이기 때문에 자릿수 별로 알파벳을 카운트하여 가장 높은 것을 모아서 문자열을 생성함
#문자열이 여러개면 사전순으로 배열하라고 해서 마지막에 sort하여 계산
def solution(n,m,dna):
    result = ""
    distance = 0
    for i in range(m):
        dna_d1 = dict()
        min = 0
        for j in range(n):
            if dna[j][i] in dna_d1:
                dna_d1[dna[j][i]] += 1
            else:
                dna_d1[dna[j][i]] = 1
            min = max(min, dna_d1[dna[j][i]])
        sub=[]
        for key, value in dna_d1.items():
            if value == min:
                sub.append(key)
        if len(sub) > 1:
            sub.sort()
        distance += n - dna_d1[sub[0]]
        result += sub[0]
    print(result)
    print(distance)
    return result
n, m = map(int,input().split())
dna = []
for i in range(n):
    dna.append(input())
solution(n,m,dna)

#링트와 스타트
#python으로 풀었더니 시간초과가 떠서 pypy로 통과시킨 문제 아무래도 너무 어렵게 푼거 같다.
#combination으로 모든 경우의 수를 계산하여 풀었음
#다른 문제들처럼 미리 계산해둘만한 값이 없어서 모든 값을 계산하느라 시간이 오래걸림
#combination을 이용해서 팀 경우의 수를 구하는게 조금 헷갈렸던 문제
#ex: 선수가 5명 (1,2)와 (3,4,5)팀일때 (1,2)를 계산하고 (3,4,5)를 계산해서 뺄셈해야 하는데.
#combination 결과는 (1,2) 다음에 (1,3) 으로 되어있어서 연속해서 계산할 수 없었음
#combination 결과가 가운데를 기준으로 (1,2)(1,3)...(2,4,5)(3,4,5) 처럼 대칭으로 나오는 걸 발견해서 가운데를 기준으로 combination 결과를 자르고
#각자 계산해서 하나는 왼쪽에서 오른쪽으로 다른 하나는 역순으로 해서 뺄셈하였다.

#https://www.acmicpc.net/problem/15661
from itertools import combinations
def solution(n,s):
    for i in range(n):
        for j in range(n):
            if i != j:
                x = s[i][j] + s[j][i]
                if i < j:
                    s[i][j], s[j][i] = x, 0
                else:
                    s[j][i], s[i][j] = x, 0
    player = list(range(1,n+1))
    player_com = []
    player_com_right = []
    for i in range(2,n-1):
        com = list(combinations(player,i))
        if i >= n//2+1:
            player_com_right.extend(com)
            continue
        if i == n//2 and n%2 == 0:
            player_com.extend(com[:len(com)//2])
            player_com_right.extend(com[len(com)//2:])
            continue   
        player_com.extend(com)
    
    max = 100000000000
    result = []
    for player in player_com:
        i,j = player[0]-1, player[1]-1
        power = s[i][j] if i < j else s[j][i]
        if 2 < len(player):
            power = power_search(s, player, 2, power)
        result.append(power)

    result_right = []
    for player in player_com_right:
        i,j = player[0]-1, player[1]-1
        power = s[i][j] if i < j else s[j][i]
        if 2 < len(player):
            power = power_search(s, player,2, power)
        result_right.append(power)

    max = 100000000000000
    for i in range(len(result)):
        max = min(max,abs(result[i]-result_right[-i-1]))
        if max == 0:
            break
    return max
def power_search(s, player, idx, power):
    for i in range(idx-1,-1,-1):
        x = player[idx]-1
        y = player[i]-1
        power += s[x][y] if x < y else s[y][x]
    idx += 1
    if idx < len(player):
        power = power_search(s, player,idx, power)
    return power
n = int(input())
s = []
for i in range(n):
    x = list(map(int, input().split()))
    s.append(x)
print(solution(n,s))
