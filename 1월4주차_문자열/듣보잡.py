# 백준 1764번 https://www.acmicpc.net/problem/1764
# 집합 자료구조의 & 연산을 사용함
# 집합은 순서가 보장되지 않으므로 & 연산 결과를 리스트로 만들어서 정렬
# sys.stdin을 사용하지 않으면 5316ms로 채점하는데 오래걸림
# input을 sys.stdin으로 바꾸면 128ms로 수정 전보다 훨씬 빠르게 통과됨
import sys 
n, m = map(int,sys.stdin.readline().split())
not_listen_set = {sys.stdin.readline() for _ in range(n)}   
not_watch_set = {sys.stdin.readline() for _ in range(m)}
not_listen_watch = list(not_listen_set & not_watch_set)
not_listen_watch.sort()     
l = len(not_listen_watch)
print(l)
for i in range(l):      
    sys.stdout.write(not_listen_watch[i])
