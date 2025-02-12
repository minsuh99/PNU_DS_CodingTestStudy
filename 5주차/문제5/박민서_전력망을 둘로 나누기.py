# Union-Find를 이용해 부분집합이 2개인 경우를 찾아 연결된 노드의 개수 차이를 구함
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

def solution(n, wires):
    answer = 9999
    
    for i in range(len(wires)):
        temp_wires = [wires[j] for j in range(len(wires)) if j != i]
        parents = [j for j in range(n)]
        for wire in temp_wires:
            if find(parents, wire[0] - 1) == find(parents, wire[1] - 1):
                continue
            else:
                union(parents, wire[0] - 1 , wire[1] - 1)
        
        check_list = [find(parents, j) for j in range(n)]
        subset_list = list(set(check_list))
        if len(subset_list) == 2:
            cnt1, cnt2 = 0, 0
            for node in check_list:
                if node == subset_list[0]:
                    cnt1 += 1
                elif node == subset_list[1]:
                    cnt2 += 1
        answer = min(answer, abs(cnt1 - cnt2))
    return answer

'''
정확성  테스트
테스트 1 〉	통과 (18.32ms, 10.2MB)
테스트 2 〉	통과 (16.69ms, 10.2MB)
테스트 3 〉	통과 (13.41ms, 10.2MB)
테스트 4 〉	통과 (12.96ms, 10.2MB)
테스트 5 〉	통과 (14.39ms, 10.2MB)
테스트 6 〉	통과 (0.04ms, 10.4MB)
테스트 7 〉	통과 (0.03ms, 10.2MB)
테스트 8 〉	통과 (0.65ms, 10.3MB)
테스트 9 〉	통과 (0.51ms, 10.2MB)
테스트 10 〉	통과 (13.97ms, 10.3MB)
테스트 11 〉	통과 (17.80ms, 10.4MB)
테스트 12 〉	통과 (15.47ms, 10.3MB)
테스트 13 〉	통과 (13.54ms, 10.2MB)
채점 결과
정확성: 100.0
합계: 100.0 / 100.0
'''