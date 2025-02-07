# def solution(participant, completion):
#     DICT = {} 
#     for com in completion:
#         c = hash(com)
#         if c not in DICT:
#             DICT[c] = 1
#         else:
#             DICT[c] += 1
    
#     for par in participant:
#         p = hash(par)
        
#         if p not in DICT or DICT[p] == 0:
#             return par
#         else:
#             DICT[p] -= 1
#     return

# 첫번째 풀이는 value에 카운트가 들어가므로 아래 풀이가 더 해시에 적합하고 효율적인거 같음
def solution(participant, completion):
    hash_table = {}
    
    # 해시 키 값들의 총합
    hash_sum = 0
    
    # 참가자들을 해시 테이블에 저장
    for par in participant:
        p = hash(par)
        hash_table[p] = par
        # 참가자들의 키 값들을 다 더함
        hash_sum += p
    
    # 완주자들의 키 값들을 참가자들의 키 값들의 합에서 뺌
    for com in completion:
        hash_sum -= hash(com)

    # hash_sum은 완주하지 못한 참가자의 해시 키 값이 됨
    return hash_table[hash_sum]


'''
정확성  테스트
테스트 1 〉	통과 (0.01ms, 10.2MB)
테스트 2 〉	통과 (0.01ms, 10.3MB)
테스트 3 〉	통과 (0.32ms, 10.3MB)
테스트 4 〉	통과 (0.61ms, 10.4MB)
테스트 5 〉	통과 (0.64ms, 10.6MB)
테스트 6 〉	통과 (0.00ms, 10.1MB)
테스트 7 〉	통과 (0.01ms, 10.2MB)
효율성  테스트
테스트 1 〉	통과 (19.58ms, 23.9MB)
테스트 2 〉	통과 (28.19ms, 28.1MB)
테스트 3 〉	통과 (33.73ms, 31.3MB)
테스트 4 〉	통과 (41.18ms, 37.7MB)
테스트 5 〉	통과 (40.99ms, 37.7MB)
'''
