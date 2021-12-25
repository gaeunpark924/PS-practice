#https://www.acmicpc.net/problem/2493
def top2(n, top_stack):
    answer = [0 for i in range(n)]
    sub_stack = []
    for i in range(n):
        new = top_stack.pop()
        while(sub_stack):
            if (sub_stack[-1][0] <= new):
                sub_stack_pop = sub_stack.pop()
                answer[sub_stack_pop[1]] = n-i
            else:
                break
        sub_stack.append([new,n-i-1])
    for i in range(n):
        print(answer[i],end=" ")
    return

n = int(input())
top_stack = [int(i) for i in input().split(' ')]
top2(n,top_stack)