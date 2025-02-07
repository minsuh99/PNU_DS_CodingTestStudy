def solution(n, costs):
    answer=0
    cost_matrix = [[987654321 for _ in range(n)] for _ in range(n)]
    for c in costs:
        cost_matrix[c[0]][c[1]] = cost_matrix[c[1]][c[0]] = c[2]
    
    visited = set()
    visited.add(0)
    
    min=[-1,987654321]
    for i in range(1,n):
        if cost_matrix[i][0] < min[1]:
            min=[i,cost_matrix[i][0]]
    answer+=min[1]
    visited.add(min[0])
    
    while len(visited)<n:
        min=[-1,-1,987654321]
        for j in visited:
            for i in range(1,n):
                if (i not in visited) and (cost_matrix[i][j] < min[2]):
                     min=[j,i,cost_matrix[i][j]]                          
        if (min[1] != -1):
            answer+=min[2]
            visited.add(min[1])
                          
    return answer

# 테스트 1 〉	통과 (0.02ms, 10.1MB)
# 테스트 2 〉	통과 (0.03ms, 10.1MB)
# 테스트 3 〉	통과 (0.09ms, 10.2MB)
# 테스트 4 〉	통과 (0.27ms, 10.1MB)
# 테스트 5 〉	통과 (0.03ms, 10.2MB)
# 테스트 6 〉	통과 (0.09ms, 10.1MB)
# 테스트 7 〉	통과 (0.14ms, 10.1MB)
# 테스트 8 〉	통과 (0.02ms, 10.2MB)
