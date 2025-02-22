def solution(n):
    def backtrack(row, cols, diag1, diag2):
        if row == n:  
            return 1  
        count = 0
        for col in range(n):
            if col in cols or (row - col) in diag1 or (row + col) in diag2:
                continue  
           
            count += backtrack(row + 1, 
                               cols | {col}, 
                               diag1 | {row - col}, 
                               diag2 | {row + col})
        return count

    return backtrack(0, set(), set(), set())

# 테스트 1 〉	통과 (0.01ms, 10.1MB)
# 테스트 2 〉	통과 (0.01ms, 10.2MB)
# 테스트 3 〉	통과 (0.01ms, 10.2MB)
# 테스트 4 〉	통과 (0.07ms, 9.96MB)
# 테스트 5 〉	통과 (0.21ms, 10.1MB)
# 테스트 6 〉	통과 (0.82ms, 10.2MB)
# 테스트 7 〉	통과 (3.03ms, 10MB)
# 테스트 8 〉	통과 (12.29ms, 10.2MB)
# 테스트 9 〉	통과 (53.75ms, 10.2MB)
# 테스트 10 〉	통과 (261.06ms, 10.2MB)
# 테스트 11 〉	통과 (1391.95ms, 10.2MB)
