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
    if nextnod_min == 0:                    #방문할 노드가 없으면 backpropagation
        a1 = mark.index(root)               #시작노드 index
        if a1 == 0:                         #맨 처음 root 노드로 올라가면 출력하고 dfs 종료
            for j in range(len(mark)):
                print(mark[j], end=' ')
            return
        else:                        
            dfsRecursion(graph, mark[a1-1], mark) #바로 위 노드로 올라감
            return
    else:                                   #방문할 노드가 있으면 그 노드를 시작으로 dfs  
        dfsRecursion(graph, min, mark)  
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
