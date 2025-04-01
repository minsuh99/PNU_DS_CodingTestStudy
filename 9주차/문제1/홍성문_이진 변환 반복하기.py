def solution(s):
    answer = []
    count = 0
    remove = 0

    while s != "1":
        zero = s.count("0")
        remove += zero
        s = s.replace("0", "")
        
        s = bin(len(s))[2:] # 이진수 변환하는거 기억 안나서 찾아봄
        count += 1

    return [count, remove]


print(solution("110010101001"))
print(solution("01110"))
print(solution("1111111"))

"""
정확성  테스트
테스트 1 〉	통과 (0.01ms, 9.1MB)
테스트 2 〉	통과 (2.41ms, 9.38MB)
테스트 3 〉	통과 (0.01ms, 9.08MB)
테스트 4 〉	통과 (0.01ms, 9.09MB)
테스트 5 〉	통과 (0.01ms, 9.13MB)
테스트 6 〉	통과 (0.01ms, 9.23MB)
테스트 7 〉	통과 (0.03ms, 9.13MB)
테스트 8 〉	통과 (0.02ms, 9.26MB)
테스트 9 〉	통과 (0.51ms, 9.28MB)
테스트 10 〉	통과 (1.89ms, 9.32MB)
테스트 11 〉	통과 (1.39ms, 9.27MB)
채점 결과
정확성: 100.0
합계: 100.0 / 100.0
"""