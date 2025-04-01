# 백트래킹 기본 구조를 작성한 후 세밀한 알고리즘은 gpt 도움받음.. 이해가 될랑말랑.. 아직은 너무 어려운 구조

def solution(n):
    answer = 0
    chess_board = [[0 for _ in range(n)] for _ in range(n)] # 체스판 2차원 배열
    
    def put_queens(row, col): # 퀸을 놓을 수 있는지 체크
        for i in range(row): # 같은 열인지 체크
            if chess_board[i][col]:
                return False
        
        for i in range(1, row + 1): # 대각선 방향에 퀸이 있는지 체크
            condition1 = ((row - i >= 0) and (col - i >= 0) and (chess_board[row - i][col - i] == 1)) # 왼쪽 위 대각선 체크
            condition2 = ((row - i >= 0) and (col + i < n) and (chess_board[row - i][col + i] == 1)) # 오른쪽 위 대각선 체크
            # condition3 = ((row + i < n) and (col - i >= 0) and (chess_board[row + i][col - i] == 0)) # 왼쪽 아래 대각선 체크
            # condition4 = ((row + i < n) and (col + i < n) and (chess_board[row + i][col + i] == 0)) # 오른쪽 아래 대각선 체크
            # row가 커지는 방향으로 퀸을 놓고 있기에 아마 아래쪽 대각선은 체크하지 않는 모양이다.
            
            # if not (condition1 and condition2 and condition3 and condition4):
            #     return False
            if condition1:
                return False
            if condition2:
                return False
        return True
        
    
    def backtrack(row):
        nonlocal answer
        if row == n: # 마지막 행까지 도달했으면
            answer += 1 # 잘 놓은거니까 정답
            return
        
        for col in range(n): # 어느 열에 놓을까
            if put_queens(row, col): # 놓을 수 있다면
                chess_board[row][col] = 1 # 놓고
                backtrack(row + 1) # 다음 열로 진행
                chess_board[row][col] = 0
    backtrack(0) # 초기 열부터 체크
        
    return answer

# def backtrack(필요한 변수):
#     if 백트래킹 종료할 조건:
#         ~~~
#         return
    
#     for i in range(~):
#         if 진행 조건:
#             ~ 변화를 주고
#             backtrack(i + 1) # 다음 스텝 체크
#             ~ 다시 변화한걸 되돌려놓는 구조
# backtrack(초기 상태)
# 내가 이해한 백트래킹 초기 구조
'''
정확성  테스트
테스트 1 〉	통과 (0.01ms, 9.98MB)
테스트 2 〉	통과 (0.01ms, 10.3MB)
테스트 3 〉	통과 (0.02ms, 10.3MB)
테스트 4 〉	통과 (0.18ms, 10.1MB)
테스트 5 〉	통과 (0.67ms, 10.1MB)
테스트 6 〉	통과 (2.80ms, 10.2MB)
테스트 7 〉	통과 (12.40ms, 10.3MB)
테스트 8 〉	통과 (60.60ms, 10.2MB)
테스트 9 〉	통과 (295.76ms, 10.3MB)
테스트 10 〉	통과 (1614.17ms, 10.3MB)
테스트 11 〉	통과 (9319.01ms, 10.3MB)
채점 결과
정확성: 100.0
합계: 100.0 / 100.0
'''