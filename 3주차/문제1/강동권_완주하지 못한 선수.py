from collections import Counter

def solution(participant, completion):
    participant_count = Counter(participant)
    completion_count = Counter(completion)
    
    # Subtract the completion counts from the participant counts
    participant_count.subtract(completion_count)
    
    # The remaining participant with a count > 0 is the one who didn't finish
    for key, value in participant_count.items():
        if value > 0:
            return key
# 테스트 1 〉	통과 (0.01ms, 10.2MB)
# 테스트 2 〉	통과 (0.01ms, 10.1MB)
# 테스트 3 〉	통과 (0.38ms, 10.2MB)
# 테스트 4 〉	통과 (0.78ms, 10.6MB)
# 테스트 5 〉	통과 (0.73ms, 10.5MB)
# 테스트 6 〉	통과 (0.01ms, 10.1MB)
# 테스트 7 〉	통과 (0.01ms, 10.2MB)
# 효율성  테스트
# 테스트 1 〉	통과 (26.78ms, 24.3MB)
# 테스트 2 〉	통과 (39.73ms, 27.7MB)
# 테스트 3 〉	통과 (46.03ms, 30.1MB)
# 테스트 4 〉	통과 (63.08ms, 38.9MB)
# 테스트 5 〉	통과 (58.12ms, 39MB)
