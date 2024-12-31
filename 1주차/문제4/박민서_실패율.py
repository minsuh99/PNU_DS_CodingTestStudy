def solution(N, stages):
    answer = []
    challenge_people = len(stages)
    fail_ratio = []
    
    for stage in range(1, N+1):
        not_clear_people = stages.count(stage)
        pass_people = challenge_people - not_clear_people
        
        if challenge_people != 0:
            fail_ratio.append((stage, not_clear_people / challenge_people))
        else:
            fail_ratio.append((stage, 0))
        challenge_people -= not_clear_people
    
    temp = [c[0] for c in sorted(fail_ratio, key=lambda x: (-x[1], x[0]))]
                
    return temp

# 메모리: 14.9 MB, 시간: 1520.16 ms
# 시간 복잡도: O(N) 보다 그 이상 예상
# 여러번 제출, 시간 꽤 오래 걸림(런타임 에러)

'''처음 코드'''

# def solution(N, stages):
#     answer = []
#     not_clear_stage = []
#     challenge_stage  = []
#     fail_ratio = []
    
#     for stage in range(1, N+1):
#         not_clear_stage.append(len([i for i in stages if i <= stage and i > stage - 1])) '''여기서 시간 오래 걸림'''
#         challenge_stage.append(len([i for i in stages if i >= stage]))
    
#     fail_ratio = [not_clear_stage[i] / challenge_stage[i] for i in range(N)]
    
#     temp = sorted(fail_ratio, reverse=True)
    
#     while len(answer) != N:
#         max_ratio = temp[0]
#         for i in range(len(fail_ratio)):
#             if fail_ratio[i] == max_ratio and i + 1 not in answer:
#                 answer.append(i + 1)
#                 temp.pop(0)
                
#     return answer
