def solution(triangle):
    N = len(triangle)
    for i in range(1, N):
        for j in range(i+1):
            if j == 0:
                triangle[i][j] += triangle[i-1][j]
            elif j == i:
                triangle[i][j] += triangle[i-1][j-1]
            else:
                triangle[i][j] += max(triangle[i-1][j], triangle[i-1][j-1])
    return max(triangle[-1])


'''
정확성  테스트
테스트 1 〉    통과 (0.02ms, 9.37MB)
테스트 2 〉    통과 (0.02ms, 9.2MB)
테스트 3 〉    통과 (0.04ms, 9.28MB)
테스트 4 〉    통과 (0.15ms, 9.38MB)
테스트 5 〉    통과 (1.12ms, 9.34MB)
테스트 6 〉    통과 (0.32ms, 9.18MB)
테스트 7 〉    통과 (1.12ms, 9.26MB)
테스트 8 〉    통과 (0.25ms, 9.26MB)
테스트 9 〉    통과 (0.01ms, 9.25MB)
테스트 10 〉    통과 (0.15ms, 9.28MB)
효율성  테스트
테스트 1 〉    통과 (35.12ms, 13.2MB)
테스트 2 〉    통과 (27.54ms, 12.3MB)
테스트 3 〉    통과 (44.51ms, 13.8MB)
테스트 4 〉    통과 (37.69ms, 13.3MB)
테스트 5 〉    통과 (33.04ms, 12.9MB)
테스트 6 〉    통과 (46.04ms, 14MB)
테스트 7 〉    통과 (39.48ms, 13.5MB)
테스트 8 〉    통과 (32.87ms, 12.7MB)
테스트 9 〉    통과 (34.27ms, 12.9MB)
테스트 10 〉    통과 (43.54ms, 13.8MB)
'''
