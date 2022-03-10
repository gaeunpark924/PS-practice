#백준 11000번 강의실 배정
#https://www.acmicpc.net/status?user_id=gaeuns&problem_id=11000&from_mine=1
#우선순위큐를 사용해서 풀었고 시간초과가 나서 애를 먹음
#처음 풀이(시간초과)
#전체 시간복잡도 O(N**2)
#처음에 큐를 사용해야 할 것 같다는 생각은 했지만 우선순위 큐까지 생각하지 못했다
#빈 강의실이 있는지 확인하려면 시간표에 있는 강의들 중에 가장 이르게 끝나는 시간을 알아야 한다.
#끝나는 시간은 end_time 이라는 리스트에 저장했는데
#큐에서 popleft를 할 때마다 min 함수를 사용해서 최소값을 찾았다.
from collections import deque

def classAssign(timetable):
    timetable.sort(key=lambda x:x[0])   
    timetable_q =deque(timetable)
    class_room = 1
    end_time = [timetable_q.popleft()[1]]
    while timetable_q:      # O(N) 
        time = timetable_q.popleft()
        x = min(end_time)   # O(N) 리스트에서 최소값, 최대값을 찾는 건 O(N)
        if time[0] >= x:
            end_time[end_time.index(x)] = time[1]
        else:
            class_room += 1
            end_time.append(time[1])    
    return class_room
n = int(input())
timetable = [list(map(int,input().split())) for _ in range(n)]
print(classAssign(timetable))

#그 다음 heapq 자료구조를 이용해서 풀이했는데 시간초과가 발생했다.
#2차원 배열을 정렬하는 코드를 그냥 sort()로 수정하고
#입력을 sys로 변경하니 바로 통과가 되었다.
#sys 때문인 것 같다
import heapq
import sys
def classAssign(n, timetable):
    timetable.sort()
    class_room = 1
    end_time = [] 
    heapq.heappush(end_time,timetable[0][1])
    for i in range(1,n):            #O(N)
        time = timetable[i]
        min_end = end_time[0]        #가장 작은 항목 접근
        if time[0] < min_end:
            class_room += 1
        else:
            heapq.heappop(end_time)  #가장 작은 항목 반환 O(logN)
        heapq.heappush(end_time,time[1])  #O(logN)
    #전체 시간복잡도 O(NlogN)
    return class_room
n = int(sys.stdin.readline())
timetable = [list(map(int,sys.stdin.readline().split())) for _ in range(n)]
print(classAssign(n, timetable))


#파이썬 우선순위큐 모듈
import heapq
heap = []
heapq.heappush(heap, 4)
heapq.heappush(heap, 1)
heapq.heappush(heap, 7)
heapq.heappush(heap, 3)   #O(logN)
#전체를 출력하면 순서대로 안 나오고 pop 해서 하나씩 출력해야 함
for i in range(4):
    print(heapq.heappop(heap))

#기존에 있던 리스트를 heap으로 만드는 법
heap = [3,4,5,6,7,1]
heap.heapify(heap) #O(N)
print(heap)

#삭제
heap = [1, 2, 7, 3, 4]
print(heapq.heappop(heap)) #O(logN)
print(heap)
