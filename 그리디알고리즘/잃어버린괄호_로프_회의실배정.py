#잃어버린 괄호(난이도 *** 문제 푸는 아이디어가 생각이 잘 안남)
#-를 기준으로 문자열 split
#나눠진 문자열의 + 계산
#문자열을 합치고 - 계산

a = input()

new_str = a.split('-')

for i in range(len(new_str)):
    x = list(map(int, new_str[i].split('+')))
    new_str[i] = sum(x)
for j in range(1,len(new_str)):
    new_str[j] = new_str[j-1]-new_str[j]

print(new_str[-1])

#로프(난이도 * 그리디 알고리즘 중에서 가장 쉬웠던 문제)
a = int(input())
l1 = []
for i in range(a):
    l1.append(int(input()))
l1 = sorted(l1)

store_l1 = []
for i in range(a):
    x = l1[i]*(a-i)
    store_l1.append(x)
print(max(store_l1))

#회의실 배정(난이도 **** 시작시간과 끝나는 시간이 같은 경우 예외처리가 어려웠음)
#시작시간, 끝나는 시간을 딕셔너리에 넣고 value값 정렬. key값 정렬해서 리스트에 넣음
#key 리스트의 인덱스 0번의 회의 시작(x[0]), 끝나는(x[1]) 시간을 x에 저장
#끝나는 시간보다 작으면서 길이가 더 짧은 회의가 있으면 교체함
#이 과정을 key 리스트가 끝날 때까지 반복
a = int(input())
meeting_hour = dict()
for i in range(a):
    a1, a2 = input().split()
    a1 = int(a1)
    a2 = int(a2)

    if a1 in meeting_hour:
        meeting_hour[a1].append(a2)
    else:
        meeting_hour[a1] = [a2]

for index, value in meeting_hour.items():
    meeting_hour[index] = sorted(value)

l1 = sorted(meeting_hour)

idx = 0
##최소한의 회의 시간 찾기
result = []
while(1):
    x = [l1[idx], meeting_hour[l1[idx]][0]]
    if x[0] != x[1]:
        sub_l1 = []
        for i in range(idx+1, len(l1)):
            if l1[i] < x[1]:
                sub_l1.append(l1[i])
            else:
                break
        for i in range(len(sub_l1)):
            x1 = [sub_l1[i], meeting_hour[sub_l1[i]][0]]
            if x1[1] < x[1]:
                x = x1
    result.append(x)

    if x[0] != x[1]:
        if x[1] > l1[-1]:
            print(len(result))
            break
        else:
            for i in range(l1.index(x[0]),len(l1)):
                if l1[i] >= x[1]:
                    idx = i
                    break
            continue
    elif x[0] == x[1]:
        if len(meeting_hour[x[0]]) != 1:
            meeting_hour[x[0]].pop(0)
        else: 
            if x[1] >= l1[-1]:
                print(len(result))
                break
            else:
                for i in range(l1.index(x[0]),len(l1)):
                    if l1[i] > x[1]:
                        idx = i
                        break
                continue