def solution(N, stages):
    answer = []
    result = {}
    
    for i in range(1, N+1):
        user = 0
        fail = 0
        
        for j in stages:
            if j > i:
                user += 1
            elif j == i:
                user += 1
                fail += 1
                
        if user == 0:
            result[i] = 0
        else:
            result[i] = fail / user

    new_result = sorted(result.items(), key=lambda x: x[1], reverse=True)
    for i in new_result:
        answer.append(i[0])
        
    return answer

'''
테스트 1 〉	통과 (0.02ms, 10.2MB)
테스트 2 〉	통과 (0.53ms, 10.2MB)
테스트 3 〉	통과 (228.31ms, 10.5MB)
테스트 4 〉	통과 (1154.19ms, 10.9MB)
테스트 5 〉	통과 (4602.98ms, 14.9MB)
테스트 6 〉	통과 (4.16ms, 10.2MB)
테스트 7 〉	통과 (43.96ms, 10.2MB)
테스트 8 〉	통과 (1158.73ms, 10.8MB)
테스트 9 〉	통과 (4625.47ms, 14.8MB)
테스트 10 〉	통과 (484.84ms, 10.8MB)
테스트 11 〉	통과 (1181.26ms, 10.8MB)
테스트 12 〉	통과 (705.86ms, 11.3MB)
테스트 13 〉	통과 (1816.14ms, 11.3MB)
테스트 14 〉	통과 (0.09ms, 10.1MB)
테스트 15 〉	통과 (49.09ms, 10.6MB)
테스트 16 〉	통과 (20.17ms, 10.3MB)
테스트 17 〉	통과 (53.04ms, 10.6MB)
테스트 18 〉	통과 (21.38ms, 10.3MB)
테스트 19 〉	통과 (4.31ms, 10.2MB)
테스트 20 〉	통과 (36.27ms, 10.4MB)
테스트 21 〉	통과 (66.35ms, 10.8MB)
테스트 22 〉	통과 (4864.31ms, 18.3MB)
테스트 23 〉	통과 (67.13ms, 11.6MB)
테스트 24 〉	통과 (216.63ms, 11.6MB)
테스트 25 〉	통과 (0.01ms, 10.1MB)
테스트 26 〉	통과 (0.01ms, 10.1MB)
테스트 27 〉	통과 (0.01ms, 10.2MB)
'''