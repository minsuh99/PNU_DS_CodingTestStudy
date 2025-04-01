from collections import Counter

def solution(participant, completion):
    # 리스트 빈도 계산
    participant_count = Counter(participant)
    completion_count = Counter(completion)
    
    # 값 차이 확인
    for i in participant_count:
        if participant_count[i] != completion_count[i]:
            return i


'''
마라톤 완주하지 못한 선수

빈도 받고
입력 차이 계산


정확성  테스트
테스트 1 〉	통과 (0.02ms, 10.1MB)
테스트 2 〉	통과 (0.02ms, 10.3MB)
테스트 3 〉	통과 (0.15ms, 10.2MB)
테스트 4 〉	통과 (0.29ms, 10.5MB)
테스트 5 〉	통과 (0.25ms, 10.2MB)
테스트 6 〉	통과 (0.03ms, 10.1MB)
테스트 7 〉	통과 (0.02ms, 10.1MB)
효율성  테스트
테스트 1 〉	통과 (17.92ms, 24.3MB)
테스트 2 〉	통과 (30.00ms, 27.8MB)
테스트 3 〉	통과 (29.99ms, 30.1MB)
테스트 4 〉	통과 (36.26ms, 38.9MB)
테스트 5 〉	통과 (31.71ms, 38.9MB)


'''




