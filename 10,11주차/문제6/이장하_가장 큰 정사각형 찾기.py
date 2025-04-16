# from collections import defaultdict

# def solution(board):
#     DICT = defaultdict(list)
    
#     for i in range(len(board)):
#         for j in range(len(board[0])):
#             if board[i][j]:
#                 DICT[1].append((i,j))
      # 오른쪽 아래 3개가 같으면 하나 더 큰 정사각형이 만들어짐
#     delta = [(1,0), (0,1), (1,1)]
#     l = 1
#     while DICT[l]:
#         x, y = DICT[l].pop(0)
        
#         flag = 0
#         for dx, dy in delta:
#             nx, ny = x + dx, y + dy
            
#             if 0 <= nx < len(board) and 0 <= ny < len(board[0]):
#                 if board[nx][ny] == l:
#                     flag += 1
                    
#         if flag == 3:
#             board[x][y] += 1
#             DICT[l+1].append((x,y))

#         if not DICT[l]:
#             l += 1

#     return (l-1)**2


def solution(board):

    max_s = 0
    # 아래 반복문의 예외 조건으로 첫번째 가로 또는 세로줄에 1이 있는 경우 정사각형 크기 1부터 시작
    if 1 in board[0] or 1 in list(zip(*board))[0]:
        max_s = 1
    # (1,1)부터 시작해서 현재 위치에서 왼쪽 위로 사각형이 있으면, 왼쪽 위 3개의 최소값 + 1이 정사각형 크기
    for i in range(1, len(board)):
        for j in range(1, len(board[0])):
            if board[i][j] and board[i-1][j] and board[i][j-1] and board[i-1][j-1]:
                board[i][j] = min(board[i-1][j], board[i][j-1], board[i-1][j-1]) + 1
                if board[i][j] > max_s:
                    # 최대 크기 업데이트
                    max_s = board[i][j]
    return max_s**2
   

'''
정확성  테스트
테스트 1 〉    통과 (0.00ms, 9.39MB)
테스트 2 〉    통과 (0.02ms, 9.34MB)
테스트 3 〉    통과 (0.04ms, 9.34MB)
테스트 4 〉    통과 (0.06ms, 9.3MB)
테스트 5 〉    통과 (0.06ms, 9.4MB)
테스트 6 〉    통과 (0.01ms, 9.25MB)
테스트 7 〉    통과 (0.01ms, 9.29MB)
테스트 8 〉    통과 (0.01ms, 9.3MB)
테스트 9 〉    통과 (0.02ms, 9.32MB)
테스트 10 〉    통과 (0.05ms, 9.12MB)
테스트 11 〉    통과 (0.03ms, 9.3MB)
테스트 12 〉    통과 (0.02ms, 9.19MB)
테스트 13 〉    통과 (0.02ms, 9.29MB)
테스트 14 〉    통과 (0.02ms, 9.17MB)
테스트 15 〉    통과 (0.03ms, 9.3MB)
테스트 16 〉    통과 (0.05ms, 9.24MB)
테스트 17 〉    통과 (0.08ms, 9.16MB)
테스트 18 〉    통과 (2.55ms, 9.26MB)
테스트 19 〉    통과 (1.72ms, 9.3MB)
효율성  테스트
테스트 1 〉    통과 (574.86ms, 30.4MB)
테스트 2 〉    통과 (599.13ms, 29.8MB)
테스트 3 〉    통과 (667.38ms, 30MB)
'''
