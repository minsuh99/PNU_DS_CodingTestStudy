def solution(keyinput, board):
    answer = [0, 0]
    board_width = board[0] // 2
    board_height = board[1] // 2
    for i in keyinput:
        if i == "left":
            if answer[0] > -1 * (board_width):
                answer[0] -= 1
        elif i == "right":
            if answer[0] < (board_width):
                answer[0] += 1
        elif i == "up":
            if answer[1] < (board_height):
                answer[1] += 1
        elif i == "down":
            if answer[1] > -1 * (board_height):
                answer[1] -= 1
            
    return answer





# 테스트 1 〉	통과 (0.01ms, 9.36MB)
# 테스트 2 〉	통과 (0.00ms, 9.23MB)
# 테스트 3 〉	통과 (0.01ms, 9.29MB)
# 테스트 4 〉	통과 (0.00ms, 9.3MB)
# 테스트 5 〉	통과 (0.01ms, 9.28MB)
# 테스트 6 〉	통과 (0.01ms, 9.25MB)
# 테스트 7 〉	통과 (0.01ms, 9.18MB)
# 테스트 8 〉	통과 (0.01ms, 9.13MB)
# 테스트 9 〉	통과 (0.01ms, 9.36MB)
# 테스트 10 〉	통과 (0.00ms, 9.36MB)
# 테스트 11 〉	통과 (0.00ms, 9.3MB)