import sys
a1= int(input())
li = [0] * 10001   #자연수니까
for i in range(a1):
    #li[int(input())] += 1
    li[int(sys.stdin.readline())] += 1
cnt = 0
for i in range(10001):     #100001번 반복하는게 if문으로 중간에 break 하는 것보다 빠름.. 조건문이랑 += 연산 때문에 그런가보다....
    while(li[i] > 0):
        sys.stdout.write("{}\n".format(i))
        li[i] -= 1
        cnt += 1
    if cnt >= a1:
        break