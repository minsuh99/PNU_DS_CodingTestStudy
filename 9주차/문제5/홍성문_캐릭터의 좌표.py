def solution(keyinput, board):
    answer = []
    move = {
        "left":  (-1, 0),
        "right": (1, 0),
        "up":    (0, 1),
        "down":  (0, -1)
    }
    
    x,y= 0,0
    max_x = board[0] // 2
    max_y = board[1] // 2
    
    for i in keyinput:
        dx, dy = move[i]
        if -max_x <= x + dx <= max_x and -max_y <= y + dy <= max_y:
            x += dx
            y += dy
        
    return [x,y]

print(solution(["left", "right", "up", "right", "right"],[11,11]))
print(solution(["down", "down", "down", "down", "down"],[7,9]))

"""
정확성  테스트
테스트 1 〉	통과 (0.01ms, 9.31MB)
테스트 2 〉	통과 (0.00ms, 9.15MB)
테스트 3 〉	통과 (0.01ms, 9.23MB)
테스트 4 〉	통과 (0.00ms, 9.02MB)
테스트 5 〉	통과 (0.01ms, 9.36MB)
테스트 6 〉	통과 (0.00ms, 9.07MB)
테스트 7 〉	통과 (0.01ms, 9.2MB)
테스트 8 〉	통과 (0.01ms, 9.13MB)
테스트 9 〉	통과 (0.01ms, 9.02MB)
테스트 10 〉	통과 (0.00ms, 9.26MB)
테스트 11 〉	통과 (0.01ms, 9.26MB)
채점 결과
정확성: 100.0
합계: 100.0 / 100.0
"""