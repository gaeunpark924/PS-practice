#프로그래머스 타겟 넘버
#https://programmers.co.kr/learn/courses/30/lessons/43165
#오랜만에 그래프 문제를 풀어서 좀 오래걸렸던 것 같다
#깊이 우선 탐색 DFS 알고리즘을 사용했고 재귀로 풀었다.
#pop이나 popleft를 사용하지 않고 데이터 위치(인덱스)를 파라미터로 넘겨주었다.
#answer를 전역변수로 만들었는데, 재귀를 쓸 때 전역변수를 사용하는 것이 좋은 풀이인지는 모르겠다.
answer = 0
def dfs_target_number(idx, result, n, numbers, target):
    global answer
    if idx == n:
        if result == target:
            answer += 1
        return
    else:
        dfs_target_number(idx+1, result+numbers[idx], n, numbers, target)
        dfs_target_number(idx+1, result-numbers[idx], n, numbers, target)
def solution(numbers, target):
    global answer
    n = len(numbers)
    dfs_target_number(0, 0, n, numbers, target)
    return answer
numbers = [[1,1,1,1,1],[4,1,2,1]]
target = [3, 4]
for i in range(2):
    print(solution(numbers[i],target[i]))
