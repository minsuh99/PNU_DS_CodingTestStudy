def solution(brown, yellow):
    answer = []
    t = brown + yellow
    
    for h in range(3, t):
        if t % h == 0: # 정수로 나누어 떨어져야함
            w = t // h
            if w >= h and (w -2)*(h - 2) == yellow: # 양끝 두줄 * 위아래 두줄 제외하면 노란색
                return [w , h]

print(solution(10,2))
print(solution(8,1))
print(solution(24,24))

"""
정확성  테스트
테스트 1 〉	통과 (0.00ms, 9.14MB)
테스트 2 〉	통과 (0.00ms, 9.26MB)
테스트 3 〉	통과 (0.06ms, 9.17MB)
테스트 4 〉	통과 (0.00ms, 9.26MB)
테스트 5 〉	통과 (0.00ms, 9.15MB)
테스트 6 〉	통과 (0.04ms, 9.13MB)
테스트 7 〉	통과 (0.05ms, 9.25MB)
테스트 8 〉	통과 (0.10ms, 9.14MB)
테스트 9 〉	통과 (0.05ms, 9.14MB)
테스트 10 〉	통과 (0.07ms, 9.13MB)
테스트 11 〉	통과 (0.00ms, 9.26MB)
테스트 12 〉	통과 (0.00ms, 9.12MB)
테스트 13 〉	통과 (0.00ms, 9.35MB)
채점 결과
정확성: 100.0
합계: 100.0 / 100.0
"""