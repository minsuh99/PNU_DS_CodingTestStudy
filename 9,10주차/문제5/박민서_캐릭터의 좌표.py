def solution(keyinput, board):
    max_width = board[0] // 2
    max_height = board[1] // 2
    
    cur = [0, 0]
    
    for key in keyinput:
        if key == "left":
            cur[0] = max((-1) * max_width, cur[0] - 1)
        elif key == "right":
            cur[0] = min(max_width, cur[0] + 1)
        elif key == "down":
            cur[1] = max((-1) * max_height, cur[1] - 1)
        elif key == "up":
            cur[1] = min(max_height, cur[1] + 1)
    return cur

'''
정확성  테스트
테스트 1 〉	통과 (0.01ms, 9.39MB)
테스트 2 〉	통과 (0.00ms, 9.27MB)
테스트 3 〉	통과 (0.01ms, 9.1MB)
테스트 4 〉	통과 (0.01ms, 9.29MB)
테스트 5 〉	통과 (0.01ms, 9.26MB)
테스트 6 〉	통과 (0.01ms, 9.3MB)
테스트 7 〉	통과 (0.02ms, 9.2MB)
테스트 8 〉	통과 (0.01ms, 9.27MB)
테스트 9 〉	통과 (0.01ms, 9.39MB)
테스트 10 〉	통과 (0.00ms, 9.3MB)
테스트 11 〉	통과 (0.02ms, 9.29MB)
채점 결과
정확성: 100.0
합계: 100.0 / 100.0
'''