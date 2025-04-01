from collections import defaultdict, deque


def solution(n, wires):
    # 트리 생성
    tree = defaultdict(list)
    for a, b in wires:
        tree[a].append(b)
        tree[b].append(a)
    
    # 너비 우선 탐색으로 연결을 끊은 전력망에서 start 송전탑이 포함된 전력망 내의 송전탑 개수를 셈
    def bfs(start, ban, n):
        q = deque()
        q.append(start)
        # 방문 여부
        visited = [False] * (n+1)
        while q:
            now = q.popleft()
            visited[now] = True
            for nxt in tree[now]:
                # 다음 노드가 전선을 끊을 송전탑이 아니고 방문한 적이 없을 때
                if nxt != ban and not visited[nxt]:
                    visited[nxt] = True
                    q.append(nxt)
        # 방문을 한 노드 == 연결이 되어있는 송전탑 개수
        return visited.count(True)

    # 모든 송전탑이 연결된 상태로 초기화
    answer = n
    
    # 연결된 전선을 끊었을 때 두 전력망의 송전탑 개수 차가 최소가 되는 정답 찾기
    for a, b in wires:
        answer = min(answer, abs(bfs(a, b, n) - bfs(b, a, n)))
    
    return answer


'''
정확성  테스트
테스트 1 〉    통과 (2.96ms, 10MB)
테스트 2 〉    통과 (5.18ms, 10.4MB)
테스트 3 〉    통과 (2.37ms, 10.2MB)
테스트 4 〉    통과 (2.43ms, 10.3MB)
테스트 5 〉    통과 (3.02ms, 10.3MB)
테스트 6 〉    통과 (0.02ms, 10.2MB)
테스트 7 〉    통과 (0.11ms, 10.2MB)
테스트 8 〉    통과 (0.14ms, 10.1MB)
테스트 9 〉    통과 (0.12ms, 10.2MB)
테스트 10 〉    통과 (2.44ms, 10.2MB)
테스트 11 〉    통과 (2.88ms, 10.1MB)
테스트 12 〉    통과 (2.71ms, 10.2MB)
테스트 13 〉    통과 (2.65ms, 10.2MB)
'''
