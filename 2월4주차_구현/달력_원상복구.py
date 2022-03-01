#백준 20207번 달력
#https://www.acmicpc.net/problem/20207
#일정이 연속되는 부분의 처음과 끝 index와 연속되는 부분에서 최대 일정 수를 구해서 면적을 구하는 문제
#처음에 그림이랑 첫번째 예시만 보고 달력의 길이가 12인줄 알았음 첫번째 예시 통과하고 수정하느라 시간이 더 걸림
#2차원 배열의 max값을 구하는 코드 추가하고 마지막이 0으로 끝나지 않는 경우를 포함하기 위해 +1 만큼 길이를 더해줌
def coating(N, schedule):
    mx = max(map(max, schedule))    #2차원 배열의 max값 구함**구글링으로 찾음
    cal = [0 for _ in range(mx+1)]
    #max를 구함
    for value in schedule:
        for i in range(value[0]-1,value[1]-1+1):
            cal[i] += 1
    idx = -1
    maxSchedule = -1
    result = 0
    for i in range(mx+1):
        if cal[i] != 0:
            if idx == -1:
                idx = i
            maxSchedule = max(maxSchedule,cal[i])
        elif cal[i] == 0 and idx != -1:
            result += (i-idx)*maxSchedule
            idx = -1
            maxSchedule = -1
    if result == 0:
        result += mx*maxSchedule
    return result
N = int(input())
schedule = []
for i in range(N):
    schedule.append(list(map(int,input().split())))
print(coating(N, schedule))

#백준 22858번 원상복구
#https://www.acmicpc.net/problem/22858
#한번 되돌리는 함수를 만들고 섞은 횟수만큼 함수 호출
def toOriginal(N,afterMix,D):
    beforeMix = [0 for _ in range(N)]
    for i in range(N):
        beforeMix[D[i]-1] = afterMix[i]
    return beforeMix
N, K = input().split()
afterMix = list(map(int,input().split()))
D = list(map(int,input().split()))
for _ in range(int(K)):
    afterMix = toOriginal(int(N),afterMix,D)
print(" ".join(map(str, afterMix)))   #int 리스트 join 으로 출력하는 법**구글링으로 찾음
