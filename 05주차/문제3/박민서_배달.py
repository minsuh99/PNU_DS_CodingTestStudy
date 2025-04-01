# 다익스트라 알고리즘 이용 (검색,, 힙큐를 안 써보고 해보기 위함)
def min_dist_node(N, visited, dist): # 현재 노드에 인접한 노드들 중 최단거리의 노드 반환
    min_dist = float("inf")
    node = 0
    
    for i in range(1, N+1):
        if dist[i] < min_dist and not visited[i]:
            min_dist = dist[i]
            node = i
    return node



def solution(N, road, K):
    answer = 0
    graph = [[float("inf") for _ in range(N + 1)] for _ in range(N + 1)] # 그래프 가중치 담을 배열 (딕셔너리로 해도 됨)
    visited = [False for _ in range(N + 1)] # 방문했는지 안 했는지 담을 배열
    dist = [float("inf") for _ in range(N + 1)] # 시작 노드로부터 최단 거리를 담을 배열
    graph[1][1] = 0 # 시작점(1)은 거리 0으로 초기화 (dist[1] = 0을 빼먹은듯)
    visited[1] = True # 시작점은 방문했다고 초기화
    
    for r in road: # 입력값 road로 부터
        node1, node2, w = map(int, r)
        if graph[node1][node2] > w: # 같은 edge, 다른 가중치가 있는 경우도 있어서, 가장 작은 거리를 가지는 가중치만 반영
            graph[node1][node2] = w
            graph[node2][node1] = w
            
    start_node = 1
    
    for i in range(1, N + 1):
        if graph[start_node][i] != float("inf"): # 현재 노드로부터 연결이 되어 있다면
            dist[i] = graph[start_node][i] # 연결된 거리로 업데이트
            
    for i in range(1, N + 1):
        min_node = min_dist_node(N, visited, dist) # 최단거리인 노드 찾고
        visited[min_node] = True # 방문했다고 업데이트
            
        for j in range(1, N + 1):
            if graph[min_node][j] != float("inf") \
            and dist[min_node] + graph[min_node][j] < dist[j]:
                # 최단거리인 노드를 거쳐가는 경로들 중 최단거리로 업데이트
                dist[j] = dist[min_node] + graph[min_node][j]
        
    
    answer = sum([True for d in dist if d <= K])
    return answer

'''
정확성  테스트
테스트 1 〉	통과 (0.08ms, 10.3MB)
테스트 2 〉	통과 (0.05ms, 10.3MB)
테스트 3 〉	통과 (0.06ms, 10.3MB)
테스트 4 〉	통과 (0.05ms, 10.4MB)
테스트 5 〉	통과 (0.15ms, 10.4MB)
테스트 6 〉	통과 (0.06ms, 10.3MB)
테스트 7 〉	통과 (0.08ms, 10.4MB)
테스트 8 〉	통과 (0.09ms, 10.4MB)
테스트 9 〉	통과 (0.04ms, 10.2MB)
테스트 10 〉	통과 (0.13ms, 10.3MB)
테스트 11 〉	통과 (0.13ms, 10.3MB)
테스트 12 〉	통과 (1.01ms, 10.3MB)
테스트 13 〉	통과 (0.44ms, 10.3MB)
테스트 14 〉	통과 (1.85ms, 10.3MB)
테스트 15 〉	통과 (1.59ms, 10.3MB)
테스트 16 〉	통과 (0.23ms, 10.3MB)
테스트 17 〉	통과 (0.74ms, 10.4MB)
테스트 18 〉	통과 (1.45ms, 10.5MB)
테스트 19 〉	통과 (2.20ms, 10.4MB)
테스트 20 〉	통과 (1.98ms, 10.3MB)
테스트 21 〉	통과 (2.92ms, 10.4MB)
테스트 22 〉	통과 (2.18ms, 10.3MB)
테스트 23 〉	통과 (3.61ms, 10.4MB)
테스트 24 〉	통과 (2.50ms, 10.3MB)
테스트 25 〉	통과 (2.31ms, 10.5MB)
테스트 26 〉	통과 (2.40ms, 10.6MB)
테스트 27 〉	통과 (1.90ms, 10.5MB)
테스트 28 〉	통과 (2.24ms, 10.5MB)
테스트 29 〉	통과 (2.36ms, 10.7MB)
테스트 30 〉	통과 (4.07ms, 10.5MB)
테스트 31 〉	통과 (2.02ms, 10.3MB)
테스트 32 〉	통과 (1.16ms, 10.3MB)
채점 결과
정확성: 100.0
합계: 100.0 / 100.0
'''