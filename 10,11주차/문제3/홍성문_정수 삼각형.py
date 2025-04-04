def solution(triangle):
    def dfs(x, y, total):
        if x == len(triangle) - 1:
            return total + triangle[x][y]

        # 왼쪽 아래로 
        left = dfs(x + 1, y, total + triangle[x][y])
        # 오른쪽 아래로 
        right = dfs(x + 1, y + 1, total + triangle[x][y])

        # 둘 중 더 큰 값
        return max(left, right)

    return dfs(0, 0, 0)

print(solution([[7], [3, 8], [8, 1, 0], [2, 7, 4, 4], [4, 5, 2, 6, 5]]))

# 아니 첨에 완전 탐색 밖에 생각 안나서 돌렸는데 시간 초과..
"""
정확성  테스트
테스트 1 〉	통과 (0.05ms, 9.1MB)
테스트 2 〉	통과 (0.57ms, 9.28MB)
테스트 3 〉	통과 (9.78ms, 9.21MB)
테스트 4 〉	실패 (시간 초과)
테스트 5 〉	실패 (시간 초과)
테스트 6 〉	실패 (시간 초과)
테스트 7 〉	실패 (시간 초과)
테스트 8 〉	실패 (시간 초과)
테스트 9 〉	통과 (0.07ms, 9.23MB)
테스트 10 〉	실패 (시간 초과)
효율성  테스트
테스트 1 〉	실패 (시간 초과)
테스트 2 〉	실패 (시간 초과)
테스트 3 〉	실패 (시간 초과)
테스트 4 〉	실패 (시간 초과)
테스트 5 〉	실패 (시간 초과)
테스트 6 〉	실패 (시간 초과)
테스트 7 〉	실패 (시간 초과)
테스트 8 〉	실패 (시간 초과)
테스트 9 〉	실패 (시간 초과)
테스트 10 〉	실패 (시간 초과)
채점 결과
정확성: 32.1
효율성: 0.0
합계: 32.1 / 100.0
"""
def solution(triangle):

    for i in range(1, len(triangle)): # 첫번째 줄 제외하고 i는 1부터 
        for j in range(len(triangle[i])):
            # 왼쪽 끝이면 바로 위칸에서만 더함함
            if j == 0:
                triangle[i][j] += triangle[i - 1][j]

            # 오른쪽 끝이면 위칸 왼쪽에서만 더함함
            elif j == len(triangle[i]) - 1:
                triangle[i][j] += triangle[i - 1][j - 1]

            # 가운데면 위쪽 두 칸 중 더 큰 값에서 옴
            else:
                triangle[i][j] += max(triangle[i - 1][j - 1], triangle[i - 1][j])

    # 마지막 줄에서 가장 큰 값이 정답
    return max(triangle[-1])

print(solution([[7], [3, 8], [8, 1, 0], [2, 7, 4, 4], [4, 5, 2, 6, 5]]))

"""
정확성  테스트
테스트 1 〉	통과 (0.02ms, 9.33MB)
테스트 2 〉	통과 (0.05ms, 9.34MB)
테스트 3 〉	통과 (0.09ms, 9.23MB)
테스트 4 〉	통과 (0.35ms, 9.34MB)
테스트 5 〉	통과 (1.30ms, 9.3MB)
테스트 6 〉	통과 (0.38ms, 9.27MB)
테스트 7 〉	통과 (1.41ms, 9.15MB)
테스트 8 〉	통과 (0.29ms, 9.13MB)
테스트 9 〉	통과 (0.02ms, 9.26MB)
테스트 10 〉 통과 (0.26ms, 9.18MB)
효율성  테스트
테스트 1 〉	통과 (45.27ms, 13.3MB)
테스트 2 〉	통과 (34.54ms, 12.2MB)
테스트 3 〉	통과 (50.51ms, 13.7MB)
테스트 4 〉	통과 (45.01ms, 13.3MB)
테스트 5 〉	통과 (40.98ms, 12.9MB)
테스트 6 〉	통과 (53.98ms, 14MB)
테스트 7 〉	통과 (50.15ms, 13.5MB)
테스트 8 〉	통과 (38.93ms, 12.6MB)
테스트 9 〉	통과 (78.23ms, 13MB)
테스트 10 〉 통과 (52.04ms, 13.6MB)
채점 결과
정확성: 64.3
효율성: 35.7
합계: 100.0 / 100.0
"""