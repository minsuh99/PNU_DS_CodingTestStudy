# 백트래킹 써보고 싶은데 처음은 일단 쌩으로 해봤는데 됐음
# 던전 수가 최대가 8이라 그런걸지도

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
정확성  테스트
테스트 1 〉	통과 (0.03ms, 10.3MB)
테스트 2 〉	통과 (0.03ms, 10.1MB)
테스트 3 〉	통과 (0.10ms, 10.1MB)
테스트 4 〉	통과 (0.02ms, 10.3MB)
테스트 5 〉	통과 (1.18ms, 10.3MB)
테스트 6 〉	통과 (7.54ms, 10.3MB)
테스트 7 〉	통과 (69.67ms, 14.8MB)
테스트 8 〉	통과 (79.47ms, 14.9MB)
테스트 9 〉	통과 (0.10ms, 10.1MB)
테스트 10 〉	통과 (6.39ms, 10.3MB)
테스트 11 〉	통과 (0.02ms, 10.4MB)
테스트 12 〉	통과 (48.99ms, 14.8MB)
테스트 13 〉	통과 (41.17ms, 14.8MB)
테스트 14 〉	통과 (38.36ms, 14.9MB)
테스트 15 〉	통과 (37.24ms, 14.9MB)
테스트 16 〉	통과 (4.06ms, 10.3MB)
테스트 17 〉	통과 (39.82ms, 14.8MB)
테스트 18 〉	통과 (0.03ms, 10.1MB)
테스트 19 〉	통과 (0.10ms, 10.1MB)
채점 결과
정확성: 100.0
합계: 100.0 / 100.0
'''