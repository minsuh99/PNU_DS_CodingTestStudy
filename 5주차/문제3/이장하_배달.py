from collections import defaultdict


def solution(N, road, K):
    # 인접 리스트 만들기
    graph = defaultdict(list)
    
    # 무방향 그래프
    for a, b, c in road:
        graph[a].append((b,c))
        graph[b].append((a,c))

    # 거리 배열 초기화
    distance = [float("inf")] * (N+1)
    distance[1] = 0
    
    # 노드 수 만큼 반복
    for _ in range(N):
        for a in range(1, N+1):
            for b, c in graph[a]:
                 # 현재 노드 a를 거쳐 b로 가는 경로의 거리가 기존의 b까지의 거리보다 짧은 경우
                if distance[a] + c < distance[b]:
                    # 최단거리 갱신
                    distance[b] = distance[a] + c
    
    # K 시간 이하로 배달이 가능한 마을의 수
    return len(list(x for x in distance if x <= K))


'''
정확성  테스트
테스트 1 〉    통과 (0.04ms, 10MB)
테스트 2 〉    통과 (0.02ms, 10.1MB)
테스트 3 〉    통과 (0.04ms, 10.1MB)
테스트 4 〉    통과 (0.14ms, 10.2MB)
테스트 5 〉    통과 (0.24ms, 10.3MB)
테스트 6 〉    통과 (0.03ms, 10.1MB)
테스트 7 〉    통과 (0.03ms, 10.2MB)
테스트 8 〉    통과 (0.05ms, 10.2MB)
테스트 9 〉    통과 (0.03ms, 10.2MB)
테스트 10 〉    통과 (0.07ms, 10MB)
테스트 11 〉    통과 (0.07ms, 10.2MB)
테스트 12 〉    통과 (0.36ms, 10.3MB)
테스트 13 〉    통과 (0.24ms, 10MB)
테스트 14 〉    통과 (5.00ms, 10.4MB)
테스트 15 〉    통과 (8.30ms, 10.5MB)
테스트 16 〉    통과 (0.11ms, 10.3MB)
테스트 17 〉    통과 (0.22ms, 9.96MB)
테스트 18 〉    통과 (2.42ms, 10.1MB)
테스트 19 〉    통과 (9.70ms, 10.3MB)
테스트 20 〉    통과 (1.96ms, 10.2MB)
테스트 21 〉    통과 (19.97ms, 10.4MB)
테스트 22 〉    통과 (3.24ms, 10.2MB)
테스트 23 〉    통과 (14.70ms, 10.5MB)
테스트 24 〉    통과 (8.44ms, 10.3MB)
테스트 25 〉    통과 (17.04ms, 10.4MB)
테스트 26 〉    통과 (39.49ms, 10.5MB)
테스트 27 〉    통과 (32.58ms, 10.4MB)
테스트 28 〉    통과 (18.66ms, 10.3MB)
테스트 29 〉    통과 (24.30ms, 10.3MB)
테스트 30 〉    통과 (17.78ms, 10.4MB)
테스트 31 〉    통과 (0.64ms, 10.2MB)
테스트 32 〉    통과 (1.06ms, 10.3MB)
'''
