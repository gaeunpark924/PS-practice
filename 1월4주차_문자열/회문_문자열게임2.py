#백준 17609번 회문
#https://www.acmicpc.net/problem/17609
#슬라이싱을 이용해서 확인
def isPalindrome(pe, n):
    for i in range(n):
        if pe[i] == pe[i][::-1]:    #회문인지 확인
            print(0)
        else:
            strX = pe[i]
            i = 0
            result = 0
            for i in range(0,len(strX)//2):
                start = i
                end = len(strX)-i-1 #-(i+1)
                left = strX[start]
                right = strX[end]
                if left != right:
                    #유사회문. start가 없는 경우, end가 없는 경우 둘 다 계산
                    tmp1 = strX[:start] + strX[start+1:]
                    if tmp1 == tmp1[::-1]:  #유사회문
                        result = 1
                        break
                    else:
                        tmp1 = strX[:end] + strX[end+1:]
                        if tmp1 == tmp1[::-1]:   #유사회문
                            result = 1
                            break
                        else:
                            result = 2           #둘 다 아닐때
                            break
            if result == 0 and len(strX)%2 != 0:   #길이가 홀 수 이면서 aabaa 일때. 위 반복문에서 걸러내지못함
                tmp1 = strX[0:len(strX)//2] + strX[len(strX)//2+1:]
                if tmp1 == tmp1[::-1]:
                    result = 1
                else:
                    result = 2
            if result !=0:
                print(result)                
n = int(input())
pe = [input() for i in range(n)]
isPalindrome(pe,n)

#백준 20437번 문자열게임2 https://www.acmicpc.net/problem/20437
#처음보는 문제 유형이라 다른 사람의 코드(https://jinu0418.tistory.com/26)를 참고했다
def string_game(w,k):
    string_num = dict()
    #K개 이상인 문자를 세서 딕셔너리에 저장
    for i in range(len(w)):
        if w.count(w[i]) >= k:
            if w[i] in string_num:
                string_num[w[i]].append(i)
            else:
                string_num[w[i]] = [i]
    if not string_num:   #딕셔너리에 저장된 값이 없으면 -1 출력
        return (-1,)
    min_str = 10000
    max_str = 0
    for idx_list in string_num.values():
        for j in range(len(idx_list)-(k-1)):
            tmp = idx_list[j+k-1]-idx_list[j]+1  ##3번, 4번 조건 동시에 충족하는 코드. j 부터 j + k-1 까지
            if tmp < min_str:
                min_str = tmp
            if tmp > max_str:
                max_str = tmp
    return min_str, max_str
n = int(input())
for i in range(n):
    w = input()
    k = int(input())
    print(*string_game(w,k))
