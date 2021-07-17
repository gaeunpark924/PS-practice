from functools import cmp_to_key
def solution(numbers):
    li = list(map(str, numbers))                 #숫자 리스트 -> 문자열 리스트
    result = sorted(li, key=cmp_to_key(compare)) #cmp_to_key 으로 정렬 *** #cmp_to_key는 정렬할 함수를 커스터마이징할 수 있음
    answer ="".join(result)                      #문자열 리스트 모든 요소를 합해서 하나의 문자열로 출력
    answer = str(int(answer))                    # [0,0,0,0] 인 경우 예외처리. "0000" -> 0 -> "0"
    return answer
def compare(x, y):                               #문자열 2개 파라미터
    a1 = x + y                                   #순서를 다르게 해서 더함
    a2 = y + x
    if int(a1) > int(a2):                        #x가 앞에 있는게 더 크면 음수 리턴
        return -1                               
    elif int(a1) < int(a2):                      #y가 앞에 있는게 더 크면 양수리턴
        return 1                                 
    else:                                        #같으면 0 리턴
        return 0                    
