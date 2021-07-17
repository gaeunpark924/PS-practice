def solution(board, moves):
    h = len(board)
    w = len(board[0])
    
    li = []                     # 맨 위 index 넣을 빈 리스트 생성
    for i in range(w):
        li.append(h-1)          # h-1로 초기화

    for i in range(h):          # 리스트에 가장 위에 있는 인형의 행 index
        for j in range(w):
            if board[i][j] != 0 and li[j] == h-1:
                li[j] = i
    cnt = 0
    li2 = []                    # 뽑은 인형을 넣을 list
    for i in moves:
        if li[i-1] > h-1:       #인형이 없을 때 #li의 값이 h-1 보다 클때
            continue

        x = board[li[i-1]][i-1]   # 인형 뽑기
        board[li[i-1]][i-1] = 0
        li[i-1] += 1              # 맨 위 index 저장한 리스트 수정
          
        if not li2:               # 뽑은 인형 리스트가 비어있는 경우
            li2.append(x)
        elif li2[-1] != x:        # 마지막 값이랑 다를 때
            li2.append(x)
        elif li2[-1] == x:
            li2.pop()
            cnt += 2     

    return cnt
