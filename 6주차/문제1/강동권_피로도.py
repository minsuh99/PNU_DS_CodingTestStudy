from collections import deque
import math

def solution(k, dungeons):
    answer = -1
    q=deque()
    
    for i in range(len(dungeons)):
        
        if k>=dungeons[i][1]:
            beat = [False]*len(dungeons)
            beat[i]=True
            q.append([beat.copy(),k-dungeons[i][1],1])
        
    while q:
        beat, health, count = q.popleft()
        for i in range(len(dungeons)):
            if (not beat[i]) and health>=dungeons[i][0]:
                health-=dungeons[i][1]
                beat[i]=True
                count+=1
                if count!=len(dungeons):
                    answer=max(answer,count)
                    q.append([beat.copy(),health,count])
                else:
                    answer=len(dungeons)
                    q.clear()
                       
    return answer

# 테스트 1 〉	통과 (0.05ms, 10.2MB)
# 테스트 2 〉	통과 (0.04ms, 10.2MB)
# 테스트 3 〉	통과 (0.03ms, 10.2MB)
# 테스트 4 〉	통과 (0.15ms, 10.4MB)
# 테스트 5 〉	통과 (1.43ms, 10.2MB)
# 테스트 6 〉	통과 (4.05ms, 10.3MB)
# 테스트 7 〉	통과 (26.03ms, 12.8MB)
# 테스트 8 〉	통과 (64.77ms, 15.5MB)
# 테스트 9 〉	통과 (0.04ms, 10.2MB)
# 테스트 10 〉	통과 (1.43ms, 10.3MB)
# 테스트 11 〉	통과 (0.02ms, 10.3MB)
# 테스트 12 〉	통과 (2.76ms, 10.3MB)
# 테스트 13 〉	통과 (0.36ms, 10.3MB)
# 테스트 14 〉	통과 (0.13ms, 10.2MB)
# 테스트 15 〉	통과 (0.05ms, 10.1MB)
# 테스트 16 〉	통과 (0.06ms, 10.2MB)
# 테스트 17 〉	통과 (0.14ms, 10.2MB)
# 테스트 18 〉	통과 (0.03ms, 10.2MB)
# 테스트 19 〉	통과 (0.09ms, 10MB)
