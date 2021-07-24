#소트인사이드
a = list(input())
li = sorted(a, reverse = True)
print(int("".join(li)))

#좌표정렬하기
a = int(input())
li = []
for i in range(a):
    li.append(list(map(int, input().split())))

li.sort(key=lambda x: (x[0], x[1]))
for i in range(a):
    print(li[i][0], li[i][1])
    
#국영수
n = int(input())
li = []
for i in range(n):
    name, a, b, c = input().split()
    li.append([name, int(a), int(b), int(c)])

li.sort(key = lambda x: (-x[1] , x[2], -x[3], x[0]))
for i in range(n):
    print(li[i][0])
