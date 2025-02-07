def solution(n,a,b):
    answer = 1
    
    # 케이스 8, 4, 5, 3 >> 이 경우가 안 됨 따라서 아래 if문 필요
    if a < b:
        pass
    elif b < a:
        temp = a
        a = b
        b = temp
    
    while (b % 2) != 0 or (b - a) != 1:
        if a % 2 == 0:
            a = a / 2
        elif a % 2 == 1:
            a = (a + 1) / 2
        if b % 2 == 0:
            b = b / 2
        elif b % 2 == 1:
            b = (b + 1) / 2
        answer += 1
    
    return answer

# 테스트 1 〉	통과 (0.00ms, 10.2MB)
# 테스트 2 〉	통과 (0.00ms, 10.4MB)
# 테스트 3 〉	통과 (0.01ms, 10.3MB)
# 테스트 4 〉	통과 (0.01ms, 10.3MB)
# 테스트 5 〉	통과 (0.01ms, 10.2MB)
# 테스트 6 〉	통과 (0.01ms, 10.2MB)
# 테스트 7 〉	통과 (0.01ms, 10.2MB)
# 테스트 8 〉	통과 (0.01ms, 10.2MB)
# 테스트 9 〉	통과 (0.01ms, 10.1MB)
# 테스트 10 〉	통과 (0.01ms, 10.3MB)
# 테스트 11 〉	통과 (0.01ms, 10.2MB)
# 테스트 12 〉	통과 (0.01ms, 10.3MB)
# 테스트 13 〉	통과 (0.01ms, 10.3MB)
# 테스트 14 〉	통과 (0.01ms, 10.2MB)
# 테스트 15 〉	통과 (0.01ms, 10.2MB)
# 테스트 16 〉	통과 (0.01ms, 10.3MB)
# 테스트 17 〉	통과 (0.01ms, 10.2MB)
# 테스트 18 〉	통과 (0.01ms, 10.3MB)
# 테스트 19 〉	통과 (0.01ms, 10.2MB)
# 테스트 20 〉	통과 (0.01ms, 10.2MB)
# 테스트 21 〉	통과 (0.01ms, 10.2MB)
# 테스트 22 〉	통과 (0.01ms, 10.2MB)
# 테스트 23 〉	통과 (0.01ms, 10.2MB)
# 테스트 24 〉	통과 (0.01ms, 10.2MB)
# 테스트 25 〉	통과 (0.00ms, 10.2MB)
# 테스트 26 〉	통과 (0.00ms, 10.2MB)
# 테스트 27 〉	통과 (0.01ms, 10.3MB)
# 테스트 28 〉	통과 (0.01ms, 10.4MB)
# 테스트 29 〉	통과 (0.01ms, 10.2MB)
# 테스트 30 〉	통과 (0.01ms, 10.4MB)
# 테스트 31 〉	통과 (0.02ms, 10.2MB)
# 테스트 32 〉	통과 (0.01ms, 10.1MB)
# 테스트 33 〉	통과 (0.01ms, 10.4MB)
# 테스트 34 〉	통과 (0.01ms, 10.3MB)