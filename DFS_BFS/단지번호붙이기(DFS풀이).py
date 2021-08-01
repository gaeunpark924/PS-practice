import copy
def number(graph, a, cx, cy, stack):
    #상하좌우 확인
    x = [-1,0,0,1]
    y = [0,-1,1,0]
    sub_one_list = set([])
    for i in range(4):
        nx, ny = cx+x[i], cy+y[i]
        if nx < 0 or nx > a-1 or ny < 0 or ny > a-1:
            continue
        else:
            a1 = graph[nx][ny]
            if a1 == 1 and not ((nx,ny) in stack):
                sub_one_list.add((nx,ny))               #set의 원소로 tuple 사용 리스트는 안됨
    return sub_one_list

def dfs_stack(graph, a, one_list):

    visited = []

    mark_graph = copy.deepcopy(graph)
    if len(one_list) == 0:                              #집이 없으면 0 리턴
        return 0, []
    area = 1
    count_house = [0]
    while one_list:                                     #dfs에서 추가된 부분 #집 리스트가 없어질 때까지 반복
        start = one_list.pop(0)
        stack = [tuple(start)]                          #stack = [(), ()]
        cnt = 0
        while stack:
            n1 = stack.pop()
            mark_graph[n1[0]][n1[1]] = area
            cnt += 1
            
            if list(n1) in one_list:
                one_list.remove(list(n1))
            if n1 not in visited:
                visited.append(n1)                     #visited = [(),()]
                s1 = number(graph, a, n1[0], n1[1], stack)
                stack += s1 - set(visited)
        count_house.append(cnt)
        area +=1
    return area-1, count_house[1:]
    
a = int(input())
graph = []
one_list = []
for i in range(a):
    graph.append([int(j) for j in input()])
    for s in range(a):
        if graph[i][s] == 1:
            one_list.append([i,s])                     #집 리스트 생성*********************************

area, count=dfs_stack(graph, a, one_list)
print(area)
for i in sorted(count):
    print(i)
