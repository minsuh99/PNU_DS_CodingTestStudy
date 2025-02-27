 def solution(n):
     global answer
     answer = 0
     board = [0]*n
    
     def back(row, col):
         # 이전에 놓은 퀸들의 행 탐색
         for i in range(row):
             # 같은 열이거나 대각선인 경우 돌아감
             if board[i] == col or row - i == abs(board[i] - col):
                 return False
         return True
    
     def nqueen(row):
         global answer
         # 마지막 행까지 놓았다면 결과 + 1
         if row == n:
             answer += 1
             return
        
         for col in range(n):
             board[row] = col
             if back(row, col):
                 # 이번 row의 col에 놓아도 되면 다음 행으로 내려간다
                 nqueen(row + 1)
        
     nqueen(0)
     return answer


'''
정확성  테스트
테스트 1 〉    통과 (0.01ms, 10.3MB)
테스트 2 〉    통과 (0.01ms, 10.3MB)
테스트 3 〉    통과 (0.02ms, 10.2MB)
테스트 4 〉    통과 (0.18ms, 10.4MB)
테스트 5 〉    통과 (0.56ms, 10.3MB)
테스트 6 〉    통과 (2.31ms, 10.4MB)
테스트 7 〉    통과 (21.42ms, 10.2MB)
테스트 8 〉    통과 (62.10ms, 10.3MB)
테스트 9 〉    통과 (278.76ms, 10.2MB)
테스트 10 〉    통과 (1664.34ms, 10MB)
테스트 11 〉    통과 (8875.20ms, 10.3MB)
'''
