def solution(n, computers):
    # 처음에는 각각의 컴퓨터가 네트워크
    global answer
    answer = n
    
    # 방문한 노드를 체크할 리스트
    visited = [False] * (n+1)
    
    # 깊이 우선 탐색으로 연결되는 모든 컴퓨터를 탐색
    def dfs(computers, v, visited):
        global answer
        visited[v] = True
        
        # 인접행렬이므로 컴퓨터 개수만큼 반복 
        for c in range(n):
            # 탐색할 컴퓨터 c가 자신 v와 다르고, 연결이 되어있고, 방문한 적이 없는 경우
            if c!= v and computers[v][c] == 1 and not visited[c]:
                # 연결이 되었으므로 네트워크 개수 -1
                answer -= 1
                # 다음 연결 재귀로 탐색
                dfs(computers, c, visited)
    
    # 시작지점이 정해져 있는게 아니므로(0에서만 시작할 경우 떨어져 있는 네트워크를 탐색 못함) 전체 탐색
    for i in range(n):
        # 이미 방문한 컴퓨터는 네트워크 연결이 되어 있으므로 넘김
        if not visited[i]:
            dfs(computers, i, visited)
    
    return answer


'''
정확성  테스트
테스트 1 〉    통과 (0.01ms, 10.2MB)
테스트 2 〉    통과 (0.01ms, 10.2MB)
테스트 3 〉    통과 (0.04ms, 10.3MB)
테스트 4 〉    통과 (0.04ms, 10.3MB)
테스트 5 〉    통과 (0.00ms, 10.2MB)
테스트 6 〉    통과 (0.19ms, 10.2MB)
테스트 7 〉    통과 (0.03ms, 10.2MB)
테스트 8 〉    통과 (0.28ms, 10.3MB)
테스트 9 〉    통과 (0.09ms, 10.2MB)
테스트 10 〉    통과 (0.09ms, 10.4MB)
테스트 11 〉    통과 (0.71ms, 10.3MB)
테스트 12 〉    통과 (0.53ms, 10.2MB)
테스트 13 〉    통과 (0.28ms, 10.1MB)
'''
