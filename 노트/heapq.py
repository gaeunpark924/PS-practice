import heapq
#최소힙
def heapsort(iterable):
    h = []
    result = []
    #모든 원소를 차례대로 힙에 삽입
    for value in iterable:
        heapq.heappush(h, value)
    #힙에 삽입된 모든 원소를 차례대로 꺼내어 담기
    for _ in range(len(h)):
        result.append(heapq.heappop(h))
    return result
#최대힙
def heapsort(iterable):
    h = []
    result = []
    #모든 원소를 차례대로 힙에 삽입
    for value in iterable:
        heapq.heappush(h, -value)
    #힙에 삽입된 모든 원소를 차례대로 꺼내어 담기
    for _ in range(len(h)):
        result.append(-heapq.heappop(h))
    return result

result = heapsort([1,3,5,7,9,2,4,6,8,0])
print(result)

#heap
#최소힙 작은 것부터 꺼냄
#최대힙제공X 최대 힙을 구현해야 할 때는 원소의 부호를 임시로 변경하고 힙에서 원소를 꺼낸 뒤에 다시 원소의 부호를 바꾼다.
#PriorityQueue 라이브러리보다 보통 빠르게 동작함