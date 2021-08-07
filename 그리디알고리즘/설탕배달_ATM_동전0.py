#설탕배달 (난이도 ** 동전0이랑 같은 문제)
x = int(input())
mn = 0
count = 0
while(1):
    if x == 3:
        count += 1
        break
    elif x == 1 or x == 2 or x == 4:
        count = -1
        break
    elif x == 0:
        break

    if x % 5 == 0:
        count += x//5
        break
    elif x % 5 != 0 and x % 3 == 0:
        mn = count + x // 3
        x -= 5
        count += 1
    elif x > 5:
        x -= 5
        count += 1
if mn != 0:
    if count != -1:
        count = min(mn, count)
    elif count == -1:
        count = mn
print(count)

#ATM
#돈을 인출하는데 필요한 시간의 최솟값
#시간 list를 오름차순으로 정렬
#시간이 적게 걸리는 사람을 앞으로 배치
#모든 사람이 돈을 인출했을때 시간이 가장 적게 걸림
n = int(input())
time_list = list(map(int, input().split()))
time_list = sorted(time_list)

for i in range(1, len(time_list)):
    time_list[i] = time_list[i] + time_list[i-1]

print(sum(time_list))

#동전 0(난이도 *** 설탕배달이랑 같은 문제인데 조건이 더 까다로운 문제)
#동전 list를 내림차순으로 정렬
#인덱스 0부터 total을 나눔
#몫이 해당 동전의 개수가 되고 나머지가 다시 total이 되어서 다음 동전 개수를 구하는데 사용
n, total = input().split()
n = int(n)
total = int(total)
money = []
for i in range(n):
    money.append(int(input()))

money = sorted(money, reverse=True)

count = 0
for i in money:
    count += total//i
    total = total % i
print(count)