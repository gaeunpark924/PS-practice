#백준 20300번 서강근육맨
#https://www.acmicpc.net/problem/20300
#로컬 최적해를 구하는 그리디 알고리즘을 사용하는 문제로
#2개를 더한 값이 최소가 되려면 오름차순으로 정렬하고 가장 작은 값과 가장 큰 값을 더해나가면 됨
#더한 결과 중에서 가장 큰 값이 정답임

N = int(input())
muscle_loss = list(map(int,input().split()))
muscle_loss.sort()

if N%2 == 0:
    M = 0
    for i in range(N//2):
        M = max(muscle_loss[i]+muscle_loss[-i-1],M)
else:
    M = muscle_loss[N-1]
    for i in range(N//2):
        M = max(muscle_loss[i]+muscle_loss[-i-2],M)
print(M)

#백준 16953번 A->B
#https://www.acmicpc.net/problem/16953
#완전탐색이나 아무튼 탐색해서 풀어야 겠다고 생각함
#최근에 탐색 관련 문제를 풀어보지 않아서 처음에 좀 당황했다. 하나의 유형만 풀지 않고 다양하게 풀어봐야겠다.
#난이도가 낮은 그리디 문제는 로컬최적해를 떠올리면 쉽게 해결할 수 있는데 난이도가 높은 그리디 문제는 쉽게 생각나지 않고 최적해를 구하는 방식으로는 시간내에 해결할 수 없을 것 같다.
#BFS 풀이
from collections import deque

def abBfs(a,b):
    queue = deque([(a,1)])
    result = -1
    while queue:
        i, cnt = queue.popleft()
        if i == b:
            result = cnt
            break
        if i*2 <= b:
            queue.append((i*2, cnt+1))
        if int(str(i)+'1') <= b:
            queue.append((int(str(i)+'1'),cnt+1))
    return result
a, b = map(int,input().split())
print(abBfs(a,b))
