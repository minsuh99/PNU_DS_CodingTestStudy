def solution(participant, completion):
    participant_dict = {}
    for p in participant:
        participant_dict[p] = participant_dict.get(p, 0) + 1
        
    for c in completion:
        participant_dict[c] -= 1
        
    for answer, value in participant_dict.items():
        if value > 0:
            return answer