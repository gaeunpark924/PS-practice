import sys
from collections import deque
sys.setrecursionlimit(100000)

def dfsRecursion(graph, root, mark):
    if root not in mark:                    #방문하지 않았으면 리스트에 추가
        mark.append(root)
    nextnode_min = 0
    if root in graph:                       #딕셔너리에 키가 있으면
        for i in graph[root]:
            if i not in mark:               #방문하지 않은 노드 찾기
                nextnode_min = i
                break
    #backpropagation or 재귀함수 호출
    if nextnode_min == 0:                    #방문할 노드가 없으면 backpropagation
        a1 = mark.index(root)               #시작노드 index
        if a1 == 0:                         #맨 처음 root 노드로 올라가면 출력하고 dfs 종료
            for j in range(len(mark)):
                print(mark[j], end=' ')
            return
        else:                        
            dfsRecursion(graph, mark[a1-1], mark) #바로 위 노드로 올라감
            return
    else:                                   #방문할 노드가 있으면 그 노드를 시작으로 dfs  
        dfsRecursion(graph, nextnode_min, mark)  
        return

def bfsQueue(graph, root, queue, mark):  #간선 리스트, 시작 노드, 간선 리스트 길이, 큐
    mark[root] = 1                      #시작 정점 마킹
    while(1):                           #queue에 순서대로 담기
        print(root, end = ' ')    
        if root in graph:               #딕셔너리에 키가 있으면 #if not (graph.get(root) is None)
            for i in graph[root]:
                if mark[i] == 0:
                    queue.append(i)
                    mark[i] = 1
        if not queue:                   #queue가 비어있으면 종료
            break
        else:
            root = queue.popleft()
    return

N, M, V = map(int, input().split())

graph = dict()
for i in range(M):
    a, b = map(int, input().split())
    if a in graph:                      #graph.keys() 이렇게 안 써도 됨
        graph[a].append(b)
    else:
        graph[a] = [b]
    if b in graph:
        graph[b].append(a)
    else:
        graph[b] = [a]
        
#딕셔너리 value 정렬
for key, value in graph.items():
    value = sorted(value)
    graph[key] = value
    
#dfs 깊이우선탐색
mark = []
dfsRecursion(graph, V, mark)
print()

#bfs 너비 우선 탐색
queue=deque([])
mark = []
for i in range(N+1):              
    mark.append(0)
bfsQueue(graph,V, queue, mark)

# 반례 1
# #bfs에서 위 노드로 올라가는 코드에서 문제 발생 4 500 600 1000 까지만 출력됨
# #더이상 확인할 노드가 없을 때 bfs를 끝내야 하는데 이부분 코드를 잘못함
# #queue의 끝에서 두번째 노드까지만 확인 하고 맨 끝 노드는 확인하지 않았음
# #아래 예시처럼 500, 600은 방문할 노드가 없고 1000에서 방문할 노드가 생기는 경우는 포함할 수 가 없음
# #괜히 시간 때문에 복잡하게 설계할 생각 말고 직관적으로 설계하자!
# 1000 10 4
# 4 1000
# 1000 1
# 1000 2
# 1000 3
# 1000 4
# 4 500
# 4 600
# 2 5
# 5 9
# 1 24
# 답
# 4 500 600 1000 1 24 2 5 9 3
# 4 500 600 1000 1 2 3 24 5 9
# # 반례 2
# #bfs에서 queue에 넣을 때 작은걸 먼저 넣어야 함
# #시간때문에 sorted 함수를 쓰지 않고 했는데, 코드를 잘못 짜서 반례2 통과 못함
# #sorted 안 쓰고는 너무 어려워서 그냥 sorted 사용
# 4 3 1
# 1 4
# 1 3
# 1 2
# # 답
# 1 2 3 4
# 1 2 3 4
# 반례 3
# #리스트로 받고 람다로 정렬하면 
# 4 5
# 4 10 이래야 하는데
# 4 10
# 5 4 이렇게 된다 그냥 입력받을때 딕셔너리로 받으면 쉽게 해결할 수 잇을듯..
# 10 10 4
# 5 4
# 6 4
# 6 8
# 8 9
# 1 10
# 2 10
# 10 3
# 8 2
# 1 7
# 4 10
# 4 5 6 8 2 10 1 7 3 9
# 4 5 6 10 8 1 2 3 9 7 #bfs 틀림  4 10 5 6 1 2 3 8 7 9
# # 결국에 리스트에서 딕셔너리로 변경해서 풀음
