def solution(new_id):
    import re
    #대문자 -> 소문자
    new_id=new_id.lower()
    
    #숫자, 소문자 . - _ 아닌 것 제거 
    #정규식 사용 
    p = re.compile('[a-z0-9\-_.]')                            #패턴 생성   
    new_id = p.findall(new_id)                                #정규식과 매치되는 모든 문자열을 리스트로 돌려준다
    
    #리스트를 문자열로 
    new_id ="".join(new_id)                                   #['z', '-', '.', '.'] 리스트를 'z-..' 문자열로
    
    #연속된 . 제거
    result = new_id[0]
    for i in range(1,len(new_id)):
            if new_id[i] !=".":
                result += new_id[i]
            elif new_id[i] =="." and new_id[i-1] != new_id[i]:
                result += new_id[i]
    new_id = result

    #처음과 마지막 문자가 .이면 제거
    if new_id != "" and new_id[0] == '.':
        new_id=new_id[1:]

    if new_id != "" and new_id[-1] == '.':
        new_id=new_id[:-1]
    
    #문자열이 비어있으면
    if new_id == "":
        new_id = 'a'
    
    #길이 16 이상이면
    if len(new_id) >=16:
        new_id = new_id[:15]

    #마지막 문자가 . 이면 제거
    if new_id[-1] == '.':
        new_id=new_id[:-1]
    
    #길이가 2보다 작으면 3이 될 때까지 마지막 문자 더해줌
    while(len(new_id)<=2):
        new_id = new_id+new_id[-1]
    answer = new_id
    return answer
