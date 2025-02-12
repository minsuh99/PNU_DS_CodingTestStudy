def solution(participant, completion):
    for i in participant:
        if i not in completion:
            answer = i
            break
        if i in completion:
            completion.remove(i)
    return answer

# 테스트 1 〉	통과 (0.00ms, 10.1MB)
# 테스트 2 〉	통과 (0.01ms, 10.2MB)
# 테스트 3 〉	통과 (0.94ms, 10.2MB)
# 테스트 4 〉	통과 (8.84ms, 10.3MB)
# 테스트 5 〉	통과 (7.40ms, 10.2MB)
# 테스트 6 〉	통과 (0.00ms, 10.2MB)
# 테스트 7 〉	통과 (0.00ms, 10.1MB)

# 효율성 다 실패 ㅜㅜ
