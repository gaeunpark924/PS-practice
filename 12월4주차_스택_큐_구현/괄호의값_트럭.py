#백준 2504번  https://www.acmicpc.net/problem/2504
# 풀이 https://it-garden.tistory.com/279 출처
# 문제 풀다가 런타임 에러가 계속 떠서 못 풀었습니다.
# 위에는 검색해서 가져온 풀이입니다.(https://it-garden.tistory.com/279)
# 1.stack에서 pop한 값이 숫자일 때는 t에 숫자를 더하고
# 2.숫자가 아닌 문자일때는 올바른 괄호열이라고 판단하면  2 또는 3을 append합니다. 올바르지 않으면 0을 출력하고 함수를 종료합니다.
# stack에서 pop한 값이 문자가 나오거나 stack 길이가 0이 될 때까지 while문으로 계속 pop 합니다. 
# 입력받은 문자열인 input_parenthesis 를 한 번 돌고 나면
# stack에 있는 숫자를 모두 더하고 ‘(’, ‘[’가 있으면 0을 출력하고 함수를 종료합니다.
def solution_parenthesis(input_parenthesis):
    stack = []
    c = 0
    for input_value in input_parenthesis:
        if input_value == ')':
            t = 0
            while len(stack) != 0:
                top = stack.pop()
                if top == '(':
                    if t == 0:
                        stack.append(2)
                    else:
                        stack.append(2*t)
                    break
                elif top == '[':
                    print(0)
                    return #exit(0)
                else:
                    t = t + int(top)
        elif input_value == ']':
            t = 0
            while len(stack) != 0:
                top = stack.pop()
                if top == '[':
                    if t == 0:
                        stack.append(3)
                    else:
                        stack.append(3*t)
                    break
                elif top == '(':
                    print(0)
                    return #exit(0)
                else:
                    t = t + int(top)
        else:
            stack.append(input_value) 
    for i in stack:
        if i == '(' or i == '[':
            print(0)
            return
        else:
            c += i
    return c

input_parenthesis = list(input())
print(solution_parenthesis(input_parenthesis))

#백준 13335번 트럭 https://www.acmicpc.net/problem/13335
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
