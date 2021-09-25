#치킨배달
#https://www.acmicpc.net/problem/15686

#1)집과 치킨집 위치를 리스트에 저장한다
#2)치킨집을 기준으로 모든 집과 치킨 거리를 구해서 리스트에 저장한다.
#3)combination으로 가능한 치킨집 경우의 수를 구한다. 치킨집 순서대로 0 ~ x-1까지 번호를 매겨서 번호로 경우의 수 구함
#4-1)치킨 거리 리스트에서 필요한 치킨집 행만 가져와서 전치행렬을 구하면 행은 집이 되고 열은 치킨집이 된다.
#4-2)전치행렬에서 min함수를 이용해서 집과 치킨집과의 최소 거리를 구한다.
#4-3)모두 더해서 도시 치킨 거리를 구한다.
#5)반복문으로 4-1 ~ 3 을 반복한다.

#2048문제에서 썼던 zip(*)을 다시 사용하였다.
#치킨 거리를 치킨집을 행으로 하여 계산해두고(*) 치킨집 경우의 수에 따라서 필요한 행만 가져다가 리스트를 만들고
#그 리스트를 zip(*) 전치(*)하여 각 행마다 min 함수를 써서 간단하게 각각의 집마다 최소 거리를 구하였다.
#치킨 거리를 미리 계산하니까 시간 단축을 크게 할 수 있었다
from itertools import combinations
from collections import deque
def solution(n,m,city):
    #집, 치킨집 위치
    house = []
    chicken = []
    for i in range(n):
        for j in range(n):
            if city[i][j] == 1:
                house.append([i,j])
            elif city[i][j] == 2:
                chicken.append([i,j])
    #조합
    com_l1 = deque(list(combinations(range(0,len(chicken)), m)))
    #치킨거리 계산
    chicken_dist = []
    sub = []
    for i in range(len(chicken)):
        for j in range(len(house)):
            sub.append(abs(chicken[i][0]-house[j][0]) + abs(chicken[i][1]- house[j][1]))
        chicken_dist.append(sub)
        sub = []
    house_cnt = len(house)
    #최소거리 계산
    #city_chick_l1 = []
    min_city_chick_dist = 100000000000
    sub_dist = []
    while com_l1:
        x = com_l1.popleft()
        for i in range(len(x)):
            sub_dist.append(chicken_dist[x[i]])
        sub_dist = list(zip(*sub_dist))
        city_chick_dist = 0
        for i in range(house_cnt):
            city_chick_dist += min(sub_dist[i])
        min_city_chick_dist = min(city_chick_dist,min_city_chick_dist)
        #city_chick_l1.append(city_chick_dist)
        sub_dist = []
    return min_city_chick_dist #min(city_chick_l1)

n, m = map(int,input().split())
city = [list(map(int,input().split())) for i in range(n)]
print(solution(n,m,city))

#한윤정이 이탈리아에 가서 아이스크림을 사먹는데
#https://www.acmicpc.net/problem/2422
#처음에 입력을 dictionary로 안 받았더니 뒤에 가서 정리가 안돼서 딕셔너리로 수정함
#가능한 단일 조합(2개)을 모두 생성하고 피해야 하는 단일 조합을 지웠다. 이 과정에서 list가 아닌 set을 이용해서 시간을 단축하였음
#전 풀이에서는 list.remove를 사용해서 시간 초과가 발생했다.
#그리고 함수를 사용해서 3개 조합을 찾았는데, 원래 재귀로 하려다가 3개밖에 되지 않아서 그냥 일반 함수로 구현하였다.
#세번째 아이스크림은 첫번째, 두번째 아이스크림 모두에 영향을 받아서 재귀함수나 일반 함수를 사용해서 탐색하는 방식이 아니면 풀기 어려울 것 같다.
def solution(n,m, graph):
    #전체 조합을 저장하는 딕셔너리 생성 
    graph2 = dict()
    for i in range(1,1+n):
        xset = set({i})
        graph2[i] = set(j for j in range(1,1+n) if j not in xset)
    #전체 조합에서 피해야 하는 아이스크림 조합을 지운다
    #set 자료형을 사용해서 시간 단축함
    #처음에는 list의 remove를 사용해서 시간초과
    for key, value in graph2.items():
        if key in graph:
            graph2[key] = value - graph[key]
    #함수 호출
    result = 0
    for i in range(1,n+1):
        for j in graph2[i]:
            result += ice_search(graph2,i,j)    
    return int(result/6)
def ice_search(graph,i,j):
    cnt = 0
    for s in graph[j]:
        #첫 번째, 두 번째 아이스크림과 조합할 수 있는 아이스크림 찾기
        if s != i and s in graph[i]:
            cnt += 1
    return cnt
n, m = map(int,input().split())
graph = dict()
for i in range(m):
    a, b = map(int, input().split())
    if a in graph:
        graph[a].add(b)
    else:
        graph[a] = set([b])
    if b in graph:
        graph[b].add(a)
    else:
        graph[b] = set([a])
print(solution(n,m, graph))
