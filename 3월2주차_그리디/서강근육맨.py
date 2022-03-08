#백준 20300번 서강근육맨
#https://www.acmicpc.net/problem/20300
#로컬 최적해를 구하는 그리디 알고리즘을 사용하는 문제로
#2개를 더한 값이 최소가 되려면 오름차순으로 정렬하고 가장 작은 값과 가장 큰 값을 더해나가면 됨
#더한 결과 중에서 가장 큰 값이 정답임

N = int(input())
muscle_loss = list(map(int,input().split()))
muscle_loss.sort()

if N%2 == 0:
    M = 0
    for i in range(N//2):
        M = max(muscle_loss[i]+muscle_loss[-i-1],M)
else:
    M = muscle_loss[N-1]
    for i in range(N//2):
        M = max(muscle_loss[i]+muscle_loss[-i-2],M)
print(M)
