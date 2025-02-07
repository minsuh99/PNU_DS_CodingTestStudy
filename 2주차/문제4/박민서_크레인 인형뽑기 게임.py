def solution(board, moves):
    answer = 0
    cur_board = [] # 현재 보드 상태를 나타낼 리스트
    basket = [] # 인형 뽑고 담을 리스트
    for lst in (zip(*board)): # 같은 열을 하나의 리스트로 담기 위한 작업
        cur_board.append([i for i in lst if i > 0]) # 효율적인 pop을 하기 위해 빈 공간 (0)을 제거
    for move in moves:
        if not cur_board[move - 1]: # 인형을 뽑을 때 인형이 없다면 패스
            continue
        else:
            doll = cur_board[move - 1].pop(0)
        if not basket or basket[-1] != doll: # basket안에 아무것도 없으면 push, 맨 위에 올려져 있는 인형이 다르면 push
            basket.append(doll)
        else:
            answer += 2 # 2개씩 없어지니까
            basket.pop()
    return answer


'''
테스트 1 〉	통과 (0.01ms, 10.3MB)
테스트 2 〉	통과 (0.02ms, 10MB)
테스트 3 〉	통과 (0.01ms, 10.1MB)
테스트 4 〉	통과 (0.26ms, 10.2MB)
테스트 5 〉	통과 (0.01ms, 10.2MB)
테스트 6 〉	통과 (0.02ms, 10.2MB)
테스트 7 〉	통과 (0.04ms, 10.2MB)
테스트 8 〉	통과 (0.09ms, 10.3MB)
테스트 9 〉	통과 (0.09ms, 10.2MB)
테스트 10 〉	통과 (0.10ms, 10.3MB)
테스트 11 〉	통과 (0.16ms, 10.1MB)
'''