def solution(n):

    a = 0
    b = 1 #초기값 지정
    
    for i in range(2,n+1):
        c = (a+b) % 1234567 
        a = b
        b = c # 업데이트
        
    return b

print(solution(3))
print(solution(5))

"""
정확성  테스트
테스트 1 〉	통과 (0.00ms, 9.15MB)
테스트 2 〉	통과 (0.00ms, 9.28MB)
테스트 3 〉	통과 (0.01ms, 9.17MB)
테스트 4 〉	통과 (0.01ms, 9.25MB)
테스트 5 〉	통과 (0.00ms, 9.27MB)
테스트 6 〉	통과 (0.00ms, 9.18MB)
테스트 7 〉	통과 (0.11ms, 9.14MB)
테스트 8 〉	통과 (0.07ms, 9.34MB)
테스트 9 〉	통과 (0.04ms, 9.25MB)
테스트 10 〉	통과 (0.26ms, 9.28MB)
테스트 11 〉	통과 (0.04ms, 9.26MB)
테스트 12 〉	통과 (0.08ms, 9.16MB)
테스트 13 〉	통과 (8.86ms, 9.2MB)
테스트 14 〉	통과 (15.50ms, 9.2MB)
채점 결과
정확성: 100.0
합계: 100.0 / 100.0
"""