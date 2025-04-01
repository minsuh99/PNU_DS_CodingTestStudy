# 처음 제출한 코드

# def solution(participant, completion):
#     answer = ''
    
#     for player in completion:
#         participant.remove(player)
    
#     answer = participant[0]
#     return answer

'''
정확성  테스트
테스트 1 〉	통과 (0.01ms, 10.1MB)
테스트 2 〉	통과 (0.01ms, 10MB)
테스트 3 〉	통과 (1.63ms, 10.2MB)
테스트 4 〉	통과 (3.11ms, 10.4MB)
테스트 5 〉	통과 (3.22ms, 10.3MB)
테스트 6 〉	통과 (0.00ms, 10.1MB)
테스트 7 〉	통과 (0.00ms, 10.1MB)
효율성  테스트
테스트 1 〉	실패 (시간 초과)
테스트 2 〉	실패 (시간 초과)
테스트 3 〉	실패 (시간 초과)
테스트 4 〉	실패 (시간 초과)
테스트 5 〉	실패 (시간 초과)
채점 결과
정확성: 58.3
효율성: 0.0
합계: 58.3 / 100.0
'''


def solution(participant, completion):
    answer = ''
    
    participant_dict = {}
    
    for player in participant:
        if player not in participant_dict:
            participant_dict[player] = 1
        else:
            participant_dict[player] += 1
    
    for player in completion:
        participant_dict[player] -= 1
    
    # value가 1인 key를 바로 찾아내는 쉬운 메소드가 없을까
    final_idx = list(participant_dict.values()).index(1) 
    answer = list(participant_dict.keys())[final_idx]
    return answer

'''
정확성  테스트
테스트 1 〉	통과 (0.01ms, 10MB)
테스트 2 〉	통과 (0.01ms, 10.1MB)
테스트 3 〉	통과 (0.14ms, 10.2MB)
테스트 4 〉	통과 (0.28ms, 10.4MB)
테스트 5 〉	통과 (0.27ms, 10.3MB)
테스트 6 〉	통과 (0.00ms, 10.1MB)
테스트 7 〉	통과 (0.00ms, 10.1MB)
효율성  테스트
테스트 1 〉	통과 (18.29ms, 21.7MB)
테스트 2 〉	통과 (28.05ms, 25.2MB)
테스트 3 〉	통과 (38.54ms, 27.6MB)
테스트 4 〉	통과 (41.51ms, 33.9MB)
테스트 5 〉	통과 (42.36ms, 33.9MB)
채점 결과
정확성: 58.3
효율성: 41.7
합계: 100.0 / 100.0
'''