#프로그래머스 고득점 Kit H-Index
#https://programmers.co.kr/learn/courses/30/lessons/42747
#처음에 H-Index가 무엇인지 이해하는게 어려웠음
#리스트를 정렬해야겠다는 생각을 하는건 어렵지 않고 반례를 처리하는게 까다로웠던 문제
def solution(citations):
    answer = 0
    citations.sort(reverse=True)
    length = len(citations)
    if citations[0] == 0:
        return 0
    for index, value in enumerate(citations):
        h = index+1
        if index == length-1:
            answer = length #value 아님
        else:
            if h == value:
                answer = h
                break
            elif h < value:
                if citations[index+1] < h: 
                    answer = h
                    break
            elif h > value:
                answer = value
                break
    return answer
