#선택정렬
def selectionsort(li):             
    for i in range(len(li)):
        mn_index = li.index(min(li[i:]))
        li[i], li[mn_index] = li[mn_index], li[i]
    return li
  
#버블정렬  
def bubblesort(li):               
    for i in range(len(li)-1):
        if li[i] > li[i+1]:
            li[i], li[i+1] = li[i+1], li[i]
    return li
  
#합병정렬
def mergesort(li):
    if len(li) == 1:                     #길이가 1이면 리턴
        return li
    elif len(li) == 2:                   #길이가 2이면 sort
        if li[0] > li[1]:
            result = [li[1],li[0]]
        else:
            result = [li[0],li[1]]
        return result
    elif len(li) != 2:                   #길이가 2가 아니면 재귀함수호출
        result1 = mergesort(li[:len(li)//2+1])
        result2 = mergesort(li[len(li)//2+1:])
        
        #변수 2개
        cnt1, cnt2 = 0, 0
        result3 = []
        while(cnt1 < len(result1) and cnt2 < len(result2)):
            if result1[cnt1] > result2[cnt2]:
                result3.append(result2[cnt2])
                cnt2 += 1
                continue
            elif result1[cnt1] < result2[cnt2]:
                result3.append(result1[cnt1])
                cnt1 += 1
                continue
            else:                                               #입력 숫자가 중복되지 않아서 지워도 됨
                result3.append([result1(cnt1), result2(cnt2)])
                cnt1 += 1
                cnt2 += 1

        if cnt1 == len(result1):
            result3 += result2[cnt2:]
        elif cnt2 == len(result2):
            result3 += result1[cnt1:]
        return result3
#합병정렬2
def merge(li):
    result = [[x] for x in li]
    return result
def sort_merge(li):
    result1 = []
    result2 = []
    if len(li) == 1:
        return li
    if len(li) == 2:                   #길이가 2이면 sort
        if li[0][0] > li[1][0]:
            return [li[1],li[0]]
        else:
            return li

    if len(li) > 2:                   #길이가 2가 아니면 재귀함수호출
        result1 = sort_merge(li[:len(li)//2])
        result2 = sort_merge(li[len(li)//2:])

        cnt1, cnt2 = 0, 0
        result3 = []
        while(cnt1 < len(result1) and cnt2 < len(result2)):
            if result1[cnt1] > result2[cnt2]:
                result3.append(result2[cnt2])
                cnt2 += 1
            else:
                result3.append(result1[cnt1])
                cnt1 += 1

        if cnt1 == len(result1):
            result3 += result2[cnt2:]
        elif cnt2 == len(result2):
            result3 += result1[cnt1:]
        return result3
 
from random import *
#퀵정렬1
def quicksort(li, pivot):
    a_1 = li[pivot]                  #pivot 숫자 변수에 저장
    
    if len(li) == 2:                 #리스트 길이가 3보다 작으면 정렬
        if li[0] > li[1]:
            return [li[1],li[0]]
        elif li[0] <= li[1]:
            return li
    elif len(li) == 1:
        return li

    sub_li = [a_1]
    for i in range(len(li)):      
        if li[i] < a_1:
            sub_li.insert(0, li[i])  #pivot보다 작은 수
        elif li[i] > a_1:
            sub_li.append(li[i])     #pivot보다 큰 수

    index = sub_li.index(a_1)       
    a = quicksort(sub_li[:index],randint(0,index-1)) if index > 1 else sub_li[:index]   #길이 2부터 재귀
    b = quicksort(sub_li[index+1:],randint(0,len(li)-index-2)) if len(li)-index > 1 else sub_li[index+1:]

    result = a
    result.append(a_1)
    result = result + b
    return result
#퀵정렬2  
def quicksort(li, pivot):   #리스트 2개
    a_1 = li[pivot]                  #pivot 숫자 변수에 저장
    if len(li) == 1:
        return li

    if len(li) == 2:                 #리스트 길이가 3보다 작으면 정렬
        if li[0] > li[1]:
            return [li[1],li[0]]
        else:
            return li
    else:
        left = []
        right = []
        for i in range(len(li)):
            if li[i] < a_1:
                left.append(li[i])
            elif li[i] > a_1:
                right.append(li[i])

        if not left:
            b = quicksort(right, randint(0,len(right)-1))
            a = []
        elif not right:
            a = quicksort(left, randint(0,len(left)-1))
            b = []
        else:
            a = quicksort(left, randint(0,len(left)-1))
            b = quicksort(right, randint(0,len(right)-1))
            
        result = a
        result.append(a_1)
        result = result + b
        return result
      
a1= int(input())
li = []
for i in range(a1):
    li.append(int(input()))
#퀵정렬
#li = quicksort(li, randint(0,a1-1))
#합병정렬 함수 2개
# li = merge(li)
# li = sort_merge(li)
#버블정렬
# for i in range(a1):
#     li = bubblesort(li)
#나머지
li = mergesort(li)

for i in range(a1):
    print(li[i])
