## 1. 완전탐색
#from itertools import permutations
#
#
#def solution(k, dungeons):
#    answer = -1
#    
#    # 던전들의 모든 순열을 생성후 완전탐색
#    for perm in permutations(dungeons, len(dungeons)):
#        hp = k
#        cnt = 0
#        
#        for need, spend in perm:
#            if hp >= need:
#                hp -= spend
#                cnt += 1
#            else:
#                break
#        
#        if cnt > answer:
#            answer = cnt
#    
#    return answer


'''
정확성  테스트
테스트 1 〉    통과 (0.02ms, 10MB)
테스트 2 〉    통과 (0.02ms, 10.1MB)
테스트 3 〉    통과 (0.03ms, 10.1MB)
테스트 4 〉    통과 (0.06ms, 10.2MB)
테스트 5 〉    통과 (0.36ms, 9.91MB)
테스트 6 〉    통과 (4.32ms, 10.1MB)
테스트 7 〉    통과 (22.03ms, 10.1MB)
테스트 8 〉    통과 (25.42ms, 10.1MB)
테스트 9 〉    통과 (0.04ms, 10.2MB)
테스트 10 〉    통과 (2.64ms, 10.1MB)
테스트 11 〉    통과 (0.02ms, 10.2MB)
테스트 12 〉    통과 (16.28ms, 10.1MB)
테스트 13 〉    통과 (12.51ms, 10.1MB)
테스트 14 〉    통과 (9.30ms, 10.3MB)
테스트 15 〉    통과 (9.81ms, 10.2MB)
테스트 16 〉    통과 (2.06ms, 10.2MB)
테스트 17 〉    통과 (9.47ms, 10.1MB)
테스트 18 〉    통과 (0.01ms, 10.2MB)
테스트 19 〉    통과 (0.05ms, 10.2MB)
'''


 # 2. 백트래킹
 def solution(k, dungeons):
     answer = -1
     N = len(dungeons)
     visited = [False] * N
    
     def back(k, cnt, dungeons):
         nonlocal answer
         # 탐험한 최대 던전 수 업데이트
         if cnt > answer:
             answer = cnt
        
         # 던전의 방문여부를 기록해야 하므로 인덱스를 같이
         for i, (need, spend) in enumerate(dungeons):
             # 던전의 필요 피로도보다 많이 남아있고 아직 방문하지 않은 경우
             if k >= need and not visited[i]:
                 # 방문처리
                 visited[i] = True
                 # 피로도를 깎고 탐험한 던전수를 늘려서 아직 탐험하지 않은 다음 던전들을 탐험
                 back(k - spend, cnt + 1, dungeons)
                 # 뒤에 던전을 먼저 탐험한 뒤에 앞에 던전을 탐험할 수 있으니 재방문처리
                 visited[i] = False

     back(k, 0, dungeons)
     return answer


'''
정확성  테스트
테스트 1 〉    통과 (0.03ms, 10.3MB)
테스트 2 〉    통과 (0.03ms, 10.2MB)
테스트 3 〉    통과 (0.02ms, 10.1MB)
테스트 4 〉    통과 (0.20ms, 10.1MB)
테스트 5 〉    통과 (0.79ms, 10.1MB)
테스트 6 〉    통과 (2.22ms, 10MB)
테스트 7 〉    통과 (13.87ms, 10.1MB)
테스트 8 〉    통과 (38.25ms, 10.2MB)
테스트 9 〉    통과 (0.02ms, 10.1MB)
테스트 10 〉    통과 (0.73ms, 10.2MB)
테스트 11 〉    통과 (0.01ms, 10.1MB)
테스트 12 〉    통과 (1.63ms, 10.1MB)
테스트 13 〉    통과 (0.42ms, 10.2MB)
테스트 14 〉    통과 (0.11ms, 10.1MB)
테스트 15 〉    통과 (0.03ms, 10.2MB)
테스트 16 〉    통과 (0.04ms, 10MB)
테스트 17 〉    통과 (0.12ms, 10.1MB)
테스트 18 〉    통과 (0.04ms, 9.98MB)
테스트 19 〉    통과 (0.07ms, 10.2MB)
'''
