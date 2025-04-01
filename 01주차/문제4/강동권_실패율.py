def solution(N, stages):
    stuck=[0]*(N+1)
    answer = []
    
    for stage in stages:
        stuck[stage-1]+=1
    
    errorRates=[0]*N
    
    count=stuck[N]
    for i in range(N-1,-1,-1):
        count+=stuck[i]
        if count==0:
            errorRates[i]=0
        else:
            errorRates[i]=stuck[i]/count
        
    answer=sorted(range(len(errorRates)), key=lambda i: (-errorRates[i], i))
    for i in range(0,len(answer)):
        answer[i]+=1
        
    return answer

# 테스트 1 〉	통과 (0.02ms, 10.2MB)
# 테스트 2 〉	통과 (0.08ms, 10.3MB)
# 테스트 3 〉	통과 (1.21ms, 10.6MB)
# 테스트 4 〉	통과 (7.58ms, 10.7MB)
# 테스트 5 〉	통과 (16.64ms, 15MB)
# 테스트 6 〉	통과 (0.11ms, 10.2MB)
# 테스트 7 〉	통과 (0.71ms, 10.5MB)
# 테스트 8 〉	통과 (7.11ms, 10.8MB)
# 테스트 9 〉	통과 (16.49ms, 15.1MB)
# 테스트 10 〉	통과 (7.54ms, 10.9MB)
# 테스트 11 〉	통과 (8.03ms, 10.8MB)
# 테스트 12 〉	통과 (12.08ms, 11.2MB)
# 테스트 13 〉	통과 (13.68ms, 11.3MB)
# 테스트 14 〉	통과 (0.02ms, 10.4MB)
# 테스트 15 〉	통과 (5.13ms, 10.6MB)
# 테스트 16 〉	통과 (2.74ms, 10.4MB)
# 테스트 17 〉	통과 (5.34ms, 10.6MB)
# 테스트 18 〉	통과 (2.97ms, 10.3MB)
# 테스트 19 〉	통과 (0.54ms, 10.2MB)
# 테스트 20 〉	통과 (3.91ms, 10.4MB)
# 테스트 21 〉	통과 (7.87ms, 10.8MB)
# 테스트 22 〉	통과 (18.54ms, 18MB)
# 테스트 23 〉	통과 (15.71ms, 11.7MB)
# 테스트 24 〉	통과 (15.61ms, 11.7MB)
# 테스트 25 〉	통과 (0.01ms, 10.2MB)
# 테스트 26 〉	통과 (0.01ms, 10.4MB)
# 테스트 27 〉	통과 (0.01ms, 10.2MB)
