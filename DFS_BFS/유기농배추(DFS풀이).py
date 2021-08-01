import copy
def number(graph, M, N, cx, cy, stack):
    #상하좌우 확인
    x = [-1,0,0,1]
    y = [0,-1,1,0]
    sub_one_list = set([])
    for i in range(4):
        nx, ny = cx+x[i], cy+y[i]
        if nx < 0 or nx > N-1 or ny < 0 or ny > M-1:
            continue
        else:
            a1 = graph[nx][ny]
            if a1 == 1 and not ((nx,ny) in stack):
                sub_one_list.add((nx,ny))                #set의 원소로 튜플 사용
                                                         #리스트처럼 변형(immutable)할 수 있는 것은 딕셔너리의 키 or set의 원소로 사용할 수 없음.
    return sub_one_list
  
#stack으로 구현한 dfs 변형
def dfs_ground(graph, M, N, one_list):

    visited = []

    mark_graph = copy.deepcopy(graph)
    if len(one_list) == 0:                          #배추가 없는 경우
        return 0, []
    area = 1

    while one_list:                                 #dfs에서 변형한 부분     #배추 리스트에 배추가 없으면 탐색 종료
        start = one_list.pop(0)                     #배추 리스트 맨 앞 데이터
        stack = [tuple(start)]                      #stack = [(),()]
        
        while stack:
            n1 = stack.pop()
            mark_graph[n1[0]][n1[1]] = area
            if list(n1) in one_list:                #배추리스트에 있으면 삭제*********************
                one_list.remove(list(n1))
            if n1 not in visited:
                visited.append(n1)                  #visited = [(), ()]
                s1 = number(graph, M, N, n1[0], n1[1], stack)   
                stack += s1 - set(visited)
        area +=1
    return area-1 


a = int(input())

for i in range(a):
    M, N, K = input().split()   #M: 가로 N: 세로
    #graph
    ground = [[0 for i in range(int(M))] for j in range(int(N))]   #모두 0인 2차원 리스트 만들기 
    
    #배추 리스트
    one_list=[]
    for j in range(int(K)):
        x, y = input().split()
        one_list.append([int(y), int(x)])                          #배추 리스트 만들기*******************  
        ground[int(y)][int(x)] = 1                                     

    print(dfs_ground(ground, int(M), int(N), one_list))
