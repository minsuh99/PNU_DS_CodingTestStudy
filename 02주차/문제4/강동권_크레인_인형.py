def solution(board, moves):
    answer = 0
    stack =[0]
    for move in moves:
        for i in range(len(board)):
            if board[i][move-1]!=0:
                if stack[-1]==board[i][move-1]:
                    answer+=2
                    stack.pop()
                    board[i][move-1]=0
                else:
                    stack.append(board[i][move-1])
                    board[i][move-1]=0
                break  
    return answer

# 테스트 1 〉	통과 (0.02ms, 10.1MB)
# 테스트 2 〉	통과 (0.02ms, 10.2MB)
# 테스트 3 〉	통과 (0.02ms, 10.4MB)
# 테스트 4 〉	통과 (1.33ms, 10.3MB)
# 테스트 5 〉	통과 (0.02ms, 10.3MB)
# 테스트 6 〉	통과 (0.02ms, 10.2MB)
# 테스트 7 〉	통과 (0.08ms, 10.3MB)
# 테스트 8 〉	통과 (0.33ms, 10.3MB)
# 테스트 9 〉	통과 (0.30ms, 10.2MB)
# 테스트 10 〉	통과 (0.40ms, 10.2MB)
# 테스트 11 〉	통과 (0.76ms, 10.2MB)
