def solution(prices):
    answer=[]
    for i,p in enumerate(prices):
        count=1
        for j in range(i+1, len(prices)-1):
            if prices[j]<p:
                answer.append(count)
                count=0
                break
            count+=1
        if count!=0:
            answer.append(count)
    answer[-1]=0     
    return answer

# 정확성  테스트
# 테스트 1 〉	통과 (0.01ms, 10.1MB)
# 테스트 2 〉	통과 (0.05ms, 10.2MB)
# 테스트 3 〉	통과 (1.26ms, 10.2MB)
# 테스트 4 〉	통과 (0.64ms, 10.5MB)
# 테스트 5 〉	통과 (0.86ms, 10.4MB)
# 테스트 6 〉	통과 (0.03ms, 10.2MB)
# 테스트 7 〉	통과 (0.38ms, 10.2MB)
# 테스트 8 〉	통과 (0.45ms, 10.2MB)
# 테스트 9 〉	통과 (0.05ms, 10.2MB)
# 테스트 10 〉	통과 (1.73ms, 10.3MB)
# 효율성  테스트
# 테스트 1 〉	통과 (109.39ms, 18.8MB)
# 테스트 2 〉	통과 (84.22ms, 17.5MB)
# 테스트 3 〉	통과 (134.98ms, 19.5MB)
# 테스트 4 〉	통과 (97.39ms, 18.1MB)
# 테스트 5 〉	통과 (64.03ms, 17.1MB)
