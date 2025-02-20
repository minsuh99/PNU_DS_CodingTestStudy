from collections import deque

def solution(n, computers):
    visited = set()  # 방문한 노드를 저장
    answer = 0  # 파티션 개수

    def partitions(start):
        queue = deque([start])  
        partition = set([start])  

        while queue:
            node = queue.popleft()
            for neighbor in range(n): 
                if computers[node][neighbor] == 1 and neighbor not in visited:
                    visited.add(neighbor)
                    queue.append(neighbor)
                    partition.add(neighbor)  # 같은 파티션에 포함

        return partition

    for i in range(n):  
        if i not in visited:
            visited.add(i)
            partition = partitions(i)  # 새로운 파티션 찾기
            answer += 1  # 새로운 파티션 발견 시 개수 증가

    return answer
