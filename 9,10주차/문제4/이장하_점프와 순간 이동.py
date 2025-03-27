def solution(n):
    ans = 0
    # 현재까지 온 거리가 길어야 순간이동 했을 때 이득이므로 반대로 계산
    while n > 0:
        # 2로 나눠지는 만큼 나누고 안되면 1씩 움직임
        ans += n % 2
        n //= 2
    return ans


'''
정확성  테스트
테스트 1 〉    통과 (0.00ms, 9.21MB)
테스트 2 〉    통과 (0.00ms, 9.11MB)
테스트 3 〉    통과 (0.00ms, 9.01MB)
테스트 4 〉    통과 (0.00ms, 9.21MB)
테스트 5 〉    통과 (0.00ms, 9.2MB)
테스트 6 〉    통과 (0.00ms, 9.13MB)
테스트 7 〉    통과 (0.00ms, 9.03MB)
테스트 8 〉    통과 (0.00ms, 8.98MB)
테스트 9 〉    통과 (0.00ms, 9.1MB)
테스트 10 〉    통과 (0.00ms, 9.17MB)
테스트 11 〉    통과 (0.00ms, 9.05MB)
테스트 12 〉    통과 (0.00ms, 9.11MB)
테스트 13 〉    통과 (0.00ms, 9.18MB)
테스트 14 〉    통과 (0.00ms, 9.02MB)
테스트 15 〉    통과 (0.01ms, 9.12MB)
테스트 16 〉    통과 (0.00ms, 9.21MB)
테스트 17 〉    통과 (0.00ms, 9.09MB)
테스트 18 〉    통과 (0.00ms, 9.16MB)
효율성  테스트
테스트 1 〉    통과 (0.00ms, 8.99MB)
테스트 2 〉    통과 (0.00ms, 9.15MB)
테스트 3 〉    통과 (0.00ms, 9.25MB)
테스트 4 〉    통과 (0.00ms, 9.14MB)
테스트 5 〉    통과 (0.00ms, 9.03MB)
테스트 6 〉    통과 (0.00ms, 8.92MB)
테스트 7 〉    통과 (0.01ms, 9.16MB)
테스트 8 〉    통과 (0.01ms, 9.02MB)
테스트 9 〉    통과 (0.00ms, 9.17MB)
테스트 10 〉    통과 (0.02ms, 8.89MB)
'''
