#백준 20291번 파일정리
#https://www.acmicpc.net/problem/20291
#딕셔너리 자료형을 이용해서 확장자 수를 카운트하고
#join을 이용해서 출력함
n = int(input())
fileD = dict()
for i in range(n): #반복문 n
    filename = input().split('.')[1]
    if filename in fileD:
        fileD[filename] += 1
    else:
        fileD[filename] = 1
for i in sorted(fileD.items()): #반복문 n
    print(' '.join(map(str,i)))
    
#백준 171413번 단어뒤집기2
#https://www.acmicpc.net/problem/17413
#평균 110ms 
#print를 여러번 쓰는데 보기 안 좋음 출력은 print를 마지막에 한 번만 하도록 하기
#처음 푼 풀이인데, 처음 통과하고 이 풀이를 응용해서 print를 한 번만 쓰도록 수정해보고, if문을 tmp를 기준으로도 바꿔봤는데 모두 이거보다 느렸음..... 왜지...
#처음에 split('정규식',문자열) 이렇게 해서 '<' '>' ' ' 기준으로 나눠서 풀어보려고 했는데 검색해보니 이렇게 푼 사람은 아무도 없음 문자열 조작 문제는 머리를 써서 푸는 유형은 거의 없는 것 같다.
#문제 풀 때 독창적으로 풀 생각하지말고 규칙에 맞게 풀기
x = input()
tmp = False
answer = ''
for i in range(len(x)):
    if x[i] == '<':
        print(answer[::-1],end='')
        tmp = True
        answer = '<'
        continue
    elif x[i] == '>':
        print(answer+'>',end='')
        answer = ''
        tmp = False
        continue
    elif x[i] == ' ' and not tmp:
        print(answer[::-1]+' ',end='')
        answer = ''
    else:
        answer += x[i]
if answer:
    print(answer[::-1],end='')
    
#다른 사람 풀이
#입력을 받은 문자열을 리스트로 변환 <ab> -> ['<','a','b','>']
#index를 이용해서 리스트에 직접 접근하는 방식
#뒤집을 때는 list의 reverse 이용함
#백준에서 100ms 이내로 통과하는 풀이
#https://hongcoding.tistory.com/62
import sys
word = list(sys.stdin.readline().rstrip())

i = 0
start = 0

while i < len(word):
    if word[i] == "<":       # 열린 괄호를 만나면
        i += 1 
        while word[i] != ">":      # 닫힌 괄호를 만날 때 까지
            i += 1 
        i += 1               # 닫힌 괄호를 만난 후 인덱스를 하나 증가시킨다
    elif word[i].isalnum(): # 숫자나 알파벳을 만나면
        start = i
        while i < len(word) and word[i].isalnum():
            i+=1
        tmp = word[start:i] # 숫자,알파벳 범위에 있는 것들을
        tmp.reverse()       # 뒤집는다
        word[start:i] = tmp
    else:                   # 괄호도 아니고 알파,숫자도 아닌것 = 공백
        i+=1                # 그냥 증가시킨다

print("".join(word))
    
    
