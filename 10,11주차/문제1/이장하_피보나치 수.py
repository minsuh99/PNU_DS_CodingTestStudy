def solution(n):
    F = [0, 1]
    for i in range(2, n+1):
        F.append(F[i-1] + F[i-2])
    return F[-1]%1234567


'''
정확성  테스트
테스트 1 〉    통과 (0.01ms, 9.26MB)
테스트 2 〉    통과 (0.00ms, 9.22MB)
테스트 3 〉    통과 (0.01ms, 9.25MB)
테스트 4 〉    통과 (0.01ms, 9.35MB)
테스트 5 〉    통과 (0.01ms, 9.09MB)
테스트 6 〉    통과 (0.01ms, 9.19MB)
테스트 7 〉    통과 (0.66ms, 9.31MB)
테스트 8 〉    통과 (0.33ms, 9.3MB)
테스트 9 〉    통과 (0.10ms, 9.26MB)
테스트 10 〉    통과 (0.66ms, 9.32MB)
테스트 11 〉    통과 (0.08ms, 9.14MB)
테스트 12 〉    통과 (0.21ms, 9.28MB)
테스트 13 〉    통과 (541.56ms, 456MB)
테스트 14 〉    통과 (526.14ms, 438MB)
'''
