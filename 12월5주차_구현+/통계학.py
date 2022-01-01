#백준 2108번 통계학
#https://www.acmicpc.net/problem/2108
#input으로 입력 받으면 시간 초과가 나서 sys 사용했더니 통과됐습니다
import collections
import sys
def solution(n, integer_l):
    
    print(round(sum(integer_l)/n)) #산술평균

    integer_l_s = sorted(integer_l) #오름차순 정렬
    print(integer_l_s[n//2])  #중앙값
    
    counter_dict = collections.Counter(integer_l_s) 
    most_common_value = counter_dict.most_common(2) #최빈값 2개 추출

    if n > 1 and most_common_value[0][1] == most_common_value[1][1]:
        print(most_common_value[1][0]) #두 번째로 작은 값 추출
    else:
        print(most_common_value[0][0]) 
    
    print(integer_l_s[-1]-integer_l_s[0]) #범위

    return

n = int(sys.stdin.readline().rstrip())
integer_l = []
for i in range(n):
    integer_l.append(int(sys.stdin.readline().rstrip()))
solution(n, integer_l)
