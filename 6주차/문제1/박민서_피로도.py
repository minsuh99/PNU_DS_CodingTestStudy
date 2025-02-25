def solution(k, dungeons):
    answer = -1 # 최대 탐험 던전 개수
    visited = [False for _ in range(len(dungeons))] # 그 요소를 방문했는지 안했는지를 담을 변수
    
    def backtrack(cur_k, count): # cur_k = 현재 피로도, count = 현재 던전 탐험 개수수
        nonlocal answer # 최댓값 항상 유지하기 위해
        answer = max(answer, count) # 최댓값 업데이트
        
        for i in range(len(dungeons)): # 던전 탐색
            if not visited[i]: # 방문 안 했으면?
                min_k, minus_k = dungeons[i]
                if cur_k >= min_k: # 던전 탐색할 체력이 있으면
                    visited[i] = True # 탐색
                    backtrack(cur_k - minus_k, count + 1) # 체력 업데이트 후 재귀
                    visited[i] = False # backtrack 함수 탈출한 후 방문 안 한걸로 업데이트
    backtrack(k, 0) # 초기 상태
    return answer

'''
k = 80 dungeons = [[80,20],[50,40],[30,10]]
i = 0 cur_k = 60
  |__ i = 1 cur_k = 20
    |__ i = 2 cur_k = -10 (실패)
  |__  i = 2 cur_k = 50
    |__ i = 1 cur_k = 10 (성공)

i = 1 cur_k = 40
  |__ i = 0  min_k가 80이라 거쳐가지 않음
    |__ i = 2 (X)
  |__  i = 2 cur_k = 30
    |__ i = 0 min_k가 80이라 거쳐가지 않음

i = 2 cur_k = 70
  |__ i = 0  min_k가 80이라 거쳐가지 않음
    |__ i = 1 (X)
  |__  i = 1 cur_k = 30
    |__ i = 0 min_k가 80이라 거쳐가지 않음
'''


'''
정확성  테스트
테스트 1 〉	통과 (0.07ms, 10.2MB)
테스트 2 〉	통과 (0.06ms, 10.2MB)
테스트 3 〉	통과 (0.05ms, 10.2MB)
테스트 4 〉	통과 (0.49ms, 10.3MB)
테스트 5 〉	통과 (1.60ms, 10.2MB)
테스트 6 〉	통과 (5.34ms, 10.2MB)
테스트 7 〉	통과 (20.23ms, 10.2MB)
테스트 8 〉	통과 (42.53ms, 10.2MB)
테스트 9 〉	통과 (0.03ms, 10.3MB)
테스트 10 〉	통과 (1.02ms, 10.3MB)
테스트 11 〉	통과 (0.01ms, 10.2MB)
테스트 12 〉	통과 (2.00ms, 10.3MB)
테스트 13 〉	통과 (0.48ms, 10.2MB)
테스트 14 〉	통과 (0.10ms, 10.2MB)
테스트 15 〉	통과 (0.04ms, 10.2MB)
테스트 16 〉	통과 (0.08ms, 10.4MB)
테스트 17 〉	통과 (0.11ms, 10.2MB)
테스트 18 〉	통과 (0.02ms, 10.3MB)
테스트 19 〉	통과 (0.15ms, 10.2MB)
채점 결과
정확성: 100.0
합계: 100.0 / 100.0
'''

'''
처음 생각한 그냥 순열을 이용한 방법
딱히 많은 경우가 아니라서 가능한가봄
from itertools import permutations


def solution(k, dungeons):
    answer = -1
    for permutation in list(permutations(dungeons, len(dungeons))):
        cur_k = k
        count = 0
        
        for i in range(len(permutation)):
            if cur_k >= permutation[i][0] and cur_k - permutation[i][1] >= 0:
                cur_k -= permutation[i][1]
                count += 1
            else:
                break
        
        if count == len(dungeons):
            return len(dungeons)
        
        if count > answer:
            answer = count
    return answer
'''