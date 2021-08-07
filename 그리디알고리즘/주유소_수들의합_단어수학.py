#주유소(난이도 **** 처음 생각했던 풀이는 3번 서브태스크에서 통과 못해서 다르게 풀어서 통과)
a = int(input())
distance = list(map(int, input().split()))
money = list(map(int, input().split()))
result = 0
min_money = money[0]
result += money[0]*distance[0]
for i in range(1, a-1):
    if money[i] < min_money:
        min_money = money[i]
    result += min_money*distance[i]
print(result)


#수들의합
#서로 다른 N개의 자연수의 합이 S라고 한다. S를 알 때, 자연수 N의 최댓값을 구하는 문제
#S에서 1부터 시작해서 자연수를 차례대로 뺀다
#i를 뺐을때 남은 값이 i보다 작다면 더이상 뺄 수 없으므로 종료
a = int(input())
index = 0
for i in range(a):
    if a - i <= i:
        index = i
        break
    else:
        a = a - i
if a == 1:
    print(1)
else:
    print(index)
#수들의합 다른 풀이
a = int(input())
n = 1
while((n*(n+1))/2 <= a):
    n+=1
print(n-1)

#단어수학
#알파벳별로 자리수를 계산해서 백의 자리 수면 100, 십의 자리수면 10으로 al 딕셔너리에 저장
#딕셔너리 value를 다 더하고 오름차순으로 정렬
#맨 왼쪽에 있는 문자를 9, 그다음 문자를 8 이런 식으로 숫자를 정함
#->단어 합의 최대값을 구함
a = int(input())
word = []
al = dict()
for i in range(a):
    x = input()
    word.append(x)
    for j in range(1,len(x)+1):
        tmp = pow(10,j-1)
        if x[-j] in al:
            al[x[-j]].append(tmp)
            continue
        else:
            al[x[-j]] = [tmp]
for index, value in al.items():
    al[index] = sum(value)

al_sorted = sorted(al.items(), key=lambda x: x[1], reverse=True)

cnt = 9
result = 0
for i in al_sorted:
    result += cnt*i[1]
    cnt -= 1
print(result)