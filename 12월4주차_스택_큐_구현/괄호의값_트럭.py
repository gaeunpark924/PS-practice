#백준 13335번 트럭
https://www.acmicpc.net/problem/13335

from collections import deque

def truck(N,W,L,truck_weight):
    bridge = deque([])
    truck_on_bridge = 0
    answer = 0
    tmp = 0
    while(truck_weight):
        answer += 1
        if len(bridge) >= W:
            tmp = 1
            if bridge.popleft() != 0 :
                truck_on_bridge -= 1  
        if sum(bridge) + truck_weight[0] <= L and truck_on_bridge < W:
            bridge.append(truck_weight.popleft())
            truck_on_bridge += 1
        else:
            bridge.append(0)
    if tmp == 1:
        while(bridge):
            bridge.popleft()
            answer += 1
            if (sum(bridge) == 0):
                break
    else:
        answer += W 
    return answer

N, W, L = input().split(' ')
N = int(N)
W = int(W)
L = int(L)
truck_weight = deque([int(i)for i in input().split(' ')])
print(truck(N,W,L,truck_weight))