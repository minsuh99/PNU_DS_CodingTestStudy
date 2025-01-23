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
'''




