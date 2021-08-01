from collections import deque

def dfs(graph, start):
    visited = []
    stack = [start]
    while stack:
        current = stack.pop()
        if current not in visited:
            visited.append(current)
            if current in graph:
                stack += sorted(list(graph[current] - set(visited)),reverse=True)
    return visited

def bfs(graph, start):
    visited = []
    queue = deque([start])
    count = 0
    while queue:
        current = queue.popleft()
        if current not in visited:
            visited.append(current)
            if current in graph:
                queue += sorted(list(graph[current] - set(visited)))   #방문하지 않은 노드만 queue에 넣음
        count += 1
    return visited

N, M, V = map(int, input().split())

graph = dict()
for i in range(M):
    a, b = map(int, input().split())
    if a in graph:                      #graph.keys() 이렇게 안 써도 됨
        graph[a].add(b)
    else:
        graph[a] = set([b])
    if b in graph:
        graph[b].add(a)
    else:
        graph[b] = set([a])
        
    
#dfs 깊이우선탐색
result = dfs(graph,V)

for i in result:
    print(i, end=' ')
print()
        
#bfs 너비우선탐색
result = bfs(graph,V)
for i in result:
    print(i, end=' ')
print()
