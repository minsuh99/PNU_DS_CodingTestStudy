# Union-Find 스스로 짜보기
def find(parents, x):
    if parents[x] == x:
        return x
    parents[x] = find(parents, parents[x])
    return parents[x]

def union(parents, x, y):
    x, y = min(x, y), max(x, y)
    root1 = find(parents, x)
    root2 = find(parents, y)
    
    parents[root2] = root1

def solution(n, computers):
    computers_edge = [] # 효과적인 입력을 위한 edge 추출
    # 아니라면 computers을 돌면서 computers[i][j] == 1인 지점을 직접 찾아서 union-find 적용하는 것도 방법
    for i in range(len(computers)):
        for j in range(i, len(computers[0])):
            if i == j:
                continue
            if computers[i][j] == 1:
                computers_edge.append([i, j])
                
    parents = [i for i in range(n)]
    
    for edge in computers_edge:
        if find(parents, edge[0]) == find(parents, edge[1]):
            continue
        else:
            union(parents, edge[0], edge[1])
    
    return len(set(list([find(parents, i) for i in range(n)]))) # 부분집합들의 개수


'''
정확성  테스트
테스트 1 〉	통과 (0.02ms, 10.2MB)
테스트 2 〉	통과 (0.01ms, 10.4MB)
테스트 3 〉	통과 (0.06ms, 10.2MB)
테스트 4 〉	통과 (0.06ms, 10.1MB)
테스트 5 〉	통과 (0.01ms, 10.3MB)
테스트 6 〉	통과 (0.23ms, 10.3MB)
테스트 7 〉	통과 (0.03ms, 10.2MB)
테스트 8 〉	통과 (0.18ms, 10.2MB)
테스트 9 〉	통과 (0.11ms, 10.2MB)
테스트 10 〉	통과 (0.12ms, 10.2MB)
테스트 11 〉	통과 (0.63ms, 10.3MB)
테스트 12 〉	통과 (0.64ms, 10.3MB)
테스트 13 〉	통과 (0.27ms, 10.2MB)
채점 결과
정확성: 100.0
합계: 100.0 / 100.0
'''