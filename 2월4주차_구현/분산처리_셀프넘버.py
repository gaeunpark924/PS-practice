#백준 1009번 분산처리
#https://www.acmicpc.net/problem/4673
#처음 풀이
#시간 초과 발생
#a를 10으로 나눈 나머지를 곱합
#곱하면서 10으로 나눠줌
import sys
def distributedSystem(a,b):
    t = a%10
    x = 1
    for i in range(b):
        x = (x*t) % 10
    return x
t = int(sys.stdin.readline())
for i in range(t):
    a, b = sys.stdin.readline().split() #input().split()
    print(distributedSystem(int(a),int(b)))
#10으로 나누면 일의자리만 확인하면 되고 나머지에 규칙이 존재함
#그 규칙을 이용해서 조건문을 사용해 풀이함
import sys
def distributedSystem(a,b):
    t = a%10
    if t == 0:
        x = 10
    elif t == 1 or t == 5 or t == 6:
        x = t
    elif t == 2 or t == 8:
        if t == 2:
            li2 = [6,2,4,8]
            x = li2[b%4]
        else:
            li8 = [6,8,4,2]
            x = li8[b%4]
    elif t == 3 or t == 7:
        if t == 3:
            li3 = [1,3,9,7]
            x = li3[b%4]
        else:
            li7 = [1,7,9,3]
            x = li7[b%4]
    elif t == 4 or t == 9:
        if t == 4:
            li4 = [6,4]
            x = li4[b%2]
        else:
            li9 = [1,9]
            x = li9[b%2]        
    return x
t = int(sys.stdin.readline())
for i in range(t):
    a, b = sys.stdin.readline().split()
    print(distributedSystem(int(a),int(b)))

#백준 4673번 셀프넘버
#https://www.acmicpc.net/problem/4673
#1~10000까지 셀프넘버 계산
#반복문으로 1부터10000까지 생성자를 만들어서 해당 생성자로 만들 수 있는 셀프넘버를 계산함
#셀프넘버가 계속 증가하는게 아니기 때문에 아래 방식으로 하면 통과 못함
tmp = 0
for i in range(1,10001):
    j = i
    seq = 0
    if j < 10:
        seq = i + i
    else:
        while j > 10:
            seq += j % 10
            j = j % 10
        seq += i
    end = False
    #print(seq)
    for j in range(tmp+1,seq):
        if j > 70:
            end = True
            break
        print(j)
    if end:
        break
    tmp = seq
#위 방법으로 하면 안될 것 같아서 구글링해서 풀이 검색함
#숫자를 str로 만들고 반복문으로 각 자리를 더해줌
#셀프넘버를 set에 넣고 1~10000까지의 집합에서 셀프넘버 set을 빼고 정렬함
#하나씩 출력
num = set(range(1,10001))
self_num = set()
for i in range(1,10001):
    for j in str(i):    
        i += int(j)     
    self_num.add(i)

self_num = sorted(num-self_num)
for i in self_num:
    print(i)
