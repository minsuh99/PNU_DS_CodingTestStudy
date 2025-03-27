def solution(brown, yellow):
    brown_half = brown // 2
    for i in range(2, brown_half):
        if (i-1)*(brown_half-i-1) == yellow:
            return [brown_half-i+1, i+1]
        

# 테스트 1 〉	통과 (0.00ms, 9.34MB)
# 테스트 2 〉	통과 (0.00ms, 9.24MB)
# 테스트 3 〉	통과 (0.12ms, 9.33MB)
# 테스트 4 〉	통과 (0.00ms, 9.14MB)
# 테스트 5 〉	통과 (0.00ms, 9.34MB)
# 테스트 6 〉	통과 (0.04ms, 9.25MB)
# 테스트 7 〉	통과 (0.10ms, 9.21MB)
# 테스트 8 〉	통과 (0.11ms, 9.14MB)
# 테스트 9 〉	통과 (0.10ms, 9.1MB)
# 테스트 10 〉	통과 (0.14ms, 9.23MB)
# 테스트 11 〉	통과 (0.00ms, 9.34MB)
# 테스트 12 〉	통과 (0.00ms, 9.25MB)
# 테스트 13 〉	통과 (0.00ms, 9.22MB)