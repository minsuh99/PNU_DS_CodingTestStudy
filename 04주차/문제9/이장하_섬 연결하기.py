def solution(n, costs):
    answer = 0
    '''
    모든 섬들이 통행할 수 있도록 사이클이 발생하지 않게 연결되고 비용이 최소인
    트리를 최소 신장 트리(MST)라고 함
    최소 신장 트리를 만드는 알고리즘 중 크루스칼 알고리즘을 사용하여 문제를 품
    '''
    
    edges = []
    
    # 건설 비용이 적은 다리부터 차례대로 건설하면 최소 비용이므로 비용 순으로 정렬
    for a, b, cost in costs:
        edges.append((cost, a, b))
    edges.sort()
    
    # 부모 노드를 나타내는 배열
    # 아무 다리도 연결하지 않은 상태에서 부모는 자기 자신
    parent = [i for i in range(n)]
    
    # 부모 노드를 찾는 함수
    def find(x):
        if parent[x] != x:
            return find(parent[x])
        return x

    # 사이클이 발생하지 않는 두 노드의 부모를 작은 숫자로 업데이트
    def union(a, b):
        root_a = find(a)
        root_b = find(b)
        
        if root_a < root_b:
            parent[root_b] = root_a
        else:
            parent[root_a] = root_b

    # 건설 비용이 낮은 다리부터 건설
    for edge in edges:
        cost, a, b = edge
        '''
        섬과 섬의 부모가 다른 경우에만 다리를 건설
        부모가 같은 섬이라면 두 섬을 연결하면 사이클이 발생
        부모가 같다면 부모를 기점으로 서로 연결이 되어 있는 것
        '''
        if find(a) != find(b):
            # 부모가 다를 경우 다리를 건설하고 부모 노드의 숫자가 큰 섬의 부모 노드를 작은 숫자로 업데이트
            union(a,b)
            # 건설된 다리의 비용을 전체 건설비용에 더함
            answer += cost

    return answer


'''
정확성  테스트
테스트 1 〉    통과 (0.01ms, 10.2MB)
테스트 2 〉    통과 (0.01ms, 10.1MB)
테스트 3 〉    통과 (0.03ms, 9.98MB)
테스트 4 〉    통과 (0.04ms, 10.3MB)
테스트 5 〉    통과 (0.02ms, 10.2MB)
테스트 6 〉    통과 (0.06ms, 10.2MB)
테스트 7 〉    통과 (0.07ms, 10.2MB)
테스트 8 〉    통과 (0.02ms, 10.2MB)
'''
