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
