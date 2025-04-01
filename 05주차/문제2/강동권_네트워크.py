def solution(n, computers):
    answer = n
    parent = [i for i in range(n)]
    rank = [0] * n
    
    def find(x):
        if parent[x]!=x:
            parent[x] = find(parent[x])
        return parent[x]
    
    def union(a, b, n):
        rootA = find(a)
        rootB = find(b)

        if rootA != rootB:
            if rank[rootA] < rank[rootB]:
                parent[rootA] = rootB
            elif rank[rootA] > rank[rootB]:
                parent[rootB] = rootA
            else:
                parent[rootB] = rootA
                rank[rootA] += 1
            n-=1
        return n

    for i in range(n):
        for j in range(n):
            if i<j and computers[i][j]:
                answer=union(i,j,answer)
    
    return answer

# 테스트 1 〉	통과 (0.01ms, 10.4MB)
# 테스트 2 〉	통과 (0.01ms, 10.3MB)
# 테스트 3 〉	통과 (0.05ms, 10.3MB)
# 테스트 4 〉	통과 (0.05ms, 10.4MB)
# 테스트 5 〉	통과 (0.00ms, 10.2MB)
# 테스트 6 〉	통과 (0.20ms, 10.2MB)
# 테스트 7 〉	통과 (0.02ms, 10.3MB)
# 테스트 8 〉	통과 (0.13ms, 10.2MB)
# 테스트 9 〉	통과 (0.08ms, 10.3MB)
# 테스트 10 〉	통과 (0.09ms, 10.2MB)
# 테스트 11 〉	통과 (0.59ms, 10.3MB)
# 테스트 12 〉	통과 (0.46ms, 10.2MB)
# 테스트 13 〉	통과 (0.23ms, 10.3MB)
