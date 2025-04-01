def solution(keyinput, board):
    col, row = board[0]//2, board[1]//2
    x, y = 0, 0
    delta = {"up": (0, 1), "down": (0, -1), "left": (-1, 0), "right": (1, 0)}
    for key in keyinput:
        dx, dy = delta[key]
        if -col <= x + dx <= col and -row <= y + dy <= row:
            x += dx
            y += dy
    return [x, y]


'''
정확성  테스트
테스트 1 〉    통과 (0.01ms, 9.16MB)
테스트 2 〉    통과 (0.00ms, 9.05MB)
테스트 3 〉    통과 (0.01ms, 9.27MB)
테스트 4 〉    통과 (0.01ms, 9.18MB)
테스트 5 〉    통과 (0.01ms, 9.18MB)
테스트 6 〉    통과 (0.00ms, 9.1MB)
테스트 7 〉    통과 (0.02ms, 9.06MB)
테스트 8 〉    통과 (0.01ms, 9.22MB)
테스트 9 〉    통과 (0.01ms, 9.26MB)
테스트 10 〉    통과 (0.00ms, 9.06MB)
테스트 11 〉    통과 (0.00ms, 9.25MB)
'''
