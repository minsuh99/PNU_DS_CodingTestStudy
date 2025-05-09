def solution(s):
    stack = []
    for i in range(0,len(s)):
        next=s[i]
        if not stack:
            stack.append(next)
        else:
            if stack[-1]==next:
                stack.pop()
            else:
                stack.append(next)
    if not stack:
        return 1
    else:
        return 0

# 정확성  테스트
# 테스트 1 〉	통과 (0.00ms, 10.1MB)
# 테스트 2 〉	통과 (13.50ms, 10.4MB)
# 테스트 3 〉	통과 (12.30ms, 10.6MB)
# 테스트 4 〉	통과 (12.55ms, 10.6MB)
# 테스트 5 〉	통과 (12.43ms, 10.6MB)
# 테스트 6 〉	통과 (12.82ms, 10.6MB)
# 테스트 7 〉	통과 (12.85ms, 10.6MB)
# 테스트 8 〉	통과 (12.17ms, 10.6MB)
# 테스트 9 〉	통과 (0.00ms, 10.3MB)
# 테스트 10 〉	통과 (0.02ms, 10.1MB)
# 테스트 11 〉	통과 (0.00ms, 10.3MB)
# 테스트 12 〉	통과 (0.00ms, 10.1MB)
# 테스트 13 〉	통과 (0.00ms, 10.1MB)
# 테스트 14 〉	통과 (0.01ms, 10.1MB)
# 테스트 15 〉	통과 (0.01ms, 10.1MB)
# 테스트 16 〉	통과 (0.01ms, 10.2MB)
# 테스트 17 〉	통과 (0.01ms, 10.2MB)
# 테스트 18 〉	통과 (0.00ms, 10.2MB)
# 효율성  테스트
# 테스트 1 〉	통과 (112.96ms, 16.3MB)
# 테스트 2 〉	통과 (114.04ms, 11.9MB)
# 테스트 3 〉	통과 (113.30ms, 12.3MB)
# 테스트 4 〉	통과 (110.86ms, 12.2MB)
# 테스트 5 〉	통과 (113.31ms, 12.3MB)
# 테스트 6 〉	통과 (113.68ms, 12.2MB)
# 테스트 7 〉	통과 (115.38ms, 12.3MB)
# 테스트 8 〉	통과 (114.21ms, 14.7MB
