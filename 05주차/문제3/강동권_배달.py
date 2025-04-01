import math
from collections import deque

def solution(N, road, K):
    answer = 0
    graph = [[] for _ in range(N)]  
    distance = [float('inf')] * N  
    distance[0] = 0

    for a, b, cost in road:
        graph[a - 1].append((b - 1, cost))
        graph[b - 1].append((a - 1, cost))

    queue = deque([0])
    
    while queue:
        cur = queue.popleft()
        for neighbor, cost in graph[cur]:
            if distance[neighbor] > distance[cur] + cost:
                distance[neighbor] = distance[cur] + cost
                queue.append(neighbor) # we need to update once a node's distance has been updated

    answer = sum(1 for d in distance if d <= K)

    return answer

# 테스트 1 〉	통과 (0.03ms, 10.2MB)
# 테스트 2 〉	통과 (0.02ms, 10.1MB)
# 테스트 3 〉	통과 (0.02ms, 10.1MB)
# 테스트 4 〉	통과 (0.03ms, 10MB)
# 테스트 5 〉	통과 (0.02ms, 10.2MB)
# 테스트 6 〉	통과 (0.02ms, 10MB)
# 테스트 7 〉	통과 (0.02ms, 10.1MB)
# 테스트 8 〉	통과 (0.02ms, 10.2MB)
# 테스트 9 〉	통과 (0.03ms, 10.2MB)
# 테스트 10 〉	통과 (0.03ms, 10.2MB)
# 테스트 11 〉	통과 (0.03ms, 10.1MB)
# 테스트 12 〉	통과 (0.07ms, 10.1MB)
# 테스트 13 〉	통과 (0.03ms, 10.2MB)
# 테스트 14 〉	통과 (2.20ms, 10.4MB)
# 테스트 15 〉	통과 (1.57ms, 10.3MB)
# 테스트 16 〉	통과 (0.04ms, 10MB)
# 테스트 17 〉	통과 (0.03ms, 10MB)
# 테스트 18 〉	통과 (0.50ms, 10.1MB)
# 테스트 19 〉	통과 (1.33ms, 10.5MB)
# 테스트 20 〉	통과 (0.23ms, 10.1MB)
# 테스트 21 〉	통과 (2.31ms, 10.5MB)
# 테스트 22 〉	통과 (0.42ms, 10.1MB)
# 테스트 23 〉	통과 (3.58ms, 10.6MB)
# 테스트 24 〉	통과 (1.16ms, 10.4MB)
# 테스트 25 〉	통과 (3.10ms, 10.6MB)
# 테스트 26 〉	통과 (2.71ms, 10.5MB)
# 테스트 27 〉	통과 (3.21ms, 10.7MB)
# 테스트 28 〉	통과 (2.63ms, 10.4MB)
# 테스트 29 〉	통과 (2.80ms, 10.4MB)
# 테스트 30 〉	통과 (1.45ms, 10.6MB)
# 테스트 31 〉	통과 (0.05ms, 10.1MB)
# 테스트 32 〉	통과 (0.07ms, 10.2MB)
