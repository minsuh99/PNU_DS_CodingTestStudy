def solution(board, moves):
    baguni = []  
    answer = 0  

    for i in moves:
        col = i - 1 
        for row in range(len(board)):  
            if board[row][col] == 0:
                pass
            else: 
                doll = board[row][col]  
                board[row][col] = 0  #뽑고나면 0으로 설정
          
                if baguni and baguni[-1] == doll:
                    baguni.pop()  
                    answer += 2  
                else:
                    baguni.append(doll)  
                break # 한번에 한 열에 있는 인형만 뽑고 중단

    return answer

#0 0 0 0 0
#0 0 1 0 3
#0 2 5 0 1
#4 2 4 4 2
#3 5 1 3 1

#1 5 3 5 1 2 1 4 -> 4 3 1 1 3 2 X 4 (+2개)
#                   4 3 3 2 X 4 (+2개)
#                   4 2 X 4

print(solution([[0,0,0,0,0],[0,0,1,0,3],[0,2,5,0,1],[4,2,4,4,2],[3,5,1,3,1]],[1,5,3,5,1,2,1,4]))

# 정확성  테스트
# 테스트 1 〉	통과 (0.02ms, 10.2MB)
# 테스트 2 〉	통과 (0.04ms, 10MB)
# 테스트 3 〉	통과 (0.03ms, 10.1MB)
# 테스트 4 〉	통과 (1.18ms, 10.2MB)
# 테스트 5 〉	통과 (0.03ms, 10.1MB)
# 테스트 6 〉	통과 (0.02ms, 10.2MB)
# 테스트 7 〉	통과 (0.07ms, 10.1MB)
# 테스트 8 〉	통과 (0.49ms, 10.1MB)
# 테스트 9 〉	통과 (0.25ms, 10.2MB)
# 테스트 10 〉	통과 (0.31ms, 10.1MB)
# 테스트 11 〉	통과 (0.63ms, 10.2MB)

