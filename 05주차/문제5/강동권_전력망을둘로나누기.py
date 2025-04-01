import math

def solution(n, wires):
    answer = n
    visited = [0] * n

    def DFS(cur):
        nonlocal answer
        visited[cur - 1] = 1
        leaf = 1
        under = 0

        for w in wires:
            if w[0] == cur:
                if not visited[w[1] - 1]:
                    under += DFS(w[1])
                    leaf = 0
            elif w[1] == cur:
                if not visited[w[0] - 1]:
                    under += DFS(w[0])
                    leaf = 0  

        if cur != 1:
            cut = under + 1
            answer = min(answer, abs(n - 2 * cut))

        if leaf:
            return leaf
        else:
            return under + 1

    DFS(1)
    return answer

# 테스트 1 〉	통과 (1.04ms, 10.2MB)
# 테스트 2 〉	통과 (0.80ms, 10.2MB)
# 테스트 3 〉	통과 (0.64ms, 10.1MB)
# 테스트 4 〉	통과 (0.68ms, 10.2MB)
# 테스트 5 〉	통과 (0.77ms, 10.1MB)
# 테스트 6 〉	통과 (0.01ms, 10.1MB)
# 테스트 7 〉	통과 (0.01ms, 10MB)
# 테스트 8 〉	통과 (0.05ms, 10.1MB)
# 테스트 9 〉	통과 (0.04ms, 10.1MB)
# 테스트 10 〉	통과 (0.67ms, 10.3MB)
# 테스트 11 〉	통과 (0.82ms, 10.2MB)
# 테스트 12 〉	통과 (0.75ms, 10.1MB)
# 테스트 13 〉	통과 (0.64ms, 10.1MB)
