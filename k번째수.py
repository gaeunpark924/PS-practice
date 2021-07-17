def solution(array, commands):
    answer = []                   
    for x in commands:
        arr1 = array[x[0]-1:x[1]]       # 리스트 슬라이싱
        arr1.sort()                     # 오름차순 정렬
        answer.append(arr1[x[2]-1])     # 정렬한 리스트에서 특정 인덱스값 append
    
    return answer
