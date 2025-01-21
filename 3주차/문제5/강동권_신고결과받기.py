def solution(id_list, report, k):
    answer = []
    report = list(set(report))
    reportee = {id_: [] for id_ in id_list}
    reported = {id_: 0 for id_ in id_list}
    
    for r in report:
        a, b = r.split()
    
        reportee[a].append(b)

        reported[b] += 1
    
    banned = [key for key, value in reported.items() if value >= k]
    
    for user in id_list:
        count=0
        for r in reportee[user]:
            if r in banned:
                count+=1
        answer.append(count)
         
    return answer

# 테스트 1 〉	통과 (0.02ms, 9.98MB)
# 테스트 2 〉	통과 (0.02ms, 10.4MB)
# 테스트 3 〉	통과 (1430.34ms, 39.2MB)
# 테스트 4 〉	통과 (0.04ms, 10.2MB)
# 테스트 5 〉	통과 (0.04ms, 10.3MB)
# 테스트 6 〉	통과 (1.44ms, 10.3MB)
# 테스트 7 〉	통과 (2.91ms, 10.5MB)
# 테스트 8 〉	통과 (2.63ms, 11.1MB)
# 테스트 9 〉	통과 (363.97ms, 23.8MB)
# 테스트 10 〉	통과 (67.73ms, 23.8MB)
# 테스트 11 〉	통과 (803.00ms, 39.3MB)
# 테스트 12 〉	통과 (0.46ms, 10.4MB)
# 테스트 13 〉	통과 (0.23ms, 10.3MB)
# 테스트 14 〉	통과 (482.57ms, 22.5MB)
# 테스트 15 〉	통과 (96.81ms, 32.8MB)
# 테스트 16 〉	통과 (0.17ms, 10.3MB)
# 테스트 17 〉	통과 (0.23ms, 10.2MB)
# 테스트 18 〉	통과 (0.74ms, 10.4MB)
# 테스트 19 〉	통과 (1.37ms, 10.3MB)
# 테스트 20 〉	통과 (416.00ms, 22.6MB)
# 테스트 21 〉	통과 (633.85ms, 32.7MB)
# 테스트 22 〉	통과 (0.01ms, 10.4MB)
# 테스트 23 〉	통과 (0.01ms, 10.2MB)
# 테스트 24 〉	통과 (0.01ms, 10.3MB)
