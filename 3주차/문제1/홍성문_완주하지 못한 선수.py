def solution(participant, completion):
    answer = ''

    participant.sort()
    completion.sort()

    for i in range(len(completion)):
        if participant[i] != completion[i]:
            answer = participant[i]
            break
    
    if answer == '':
        answer = participant[-1]
        
    return answer 

print(solution(["leo", "kiki", "eden"],["eden", "kiki"]))
print(solution(["marina", "josipa", "nikola", "vinko", "filipa"],["josipa", "filipa", "marina", "nikola"]))
print(solution(["mislav", "stanko", "mislav", "ana"],["stanko", "ana", "mislav"]))

"""
정확성  테스트
테스트 1 〉	통과 (0.01ms, 10.3MB)
테스트 2 〉	통과 (0.01ms, 10.1MB)
테스트 3 〉	통과 (0.21ms, 10.2MB)
테스트 4 〉	통과 (0.63ms, 10.1MB)
테스트 5 〉	통과 (0.42ms, 10.4MB)
테스트 6 〉	통과 (0.00ms, 10.3MB)
테스트 7 〉	통과 (0.01ms, 10.1MB)
효율성  테스트
테스트 1 〉	통과 (30.54ms, 18MB)
테스트 2 〉	통과 (54.98ms, 22.1MB)
테스트 3 〉	통과 (68.83ms, 24.7MB)
테스트 4 〉	통과 (74.59ms, 26.2MB)
테스트 5 〉	통과 (71.85ms, 26.3MB)
채점 결과
정확성: 58.3
효율성: 41.7
합계: 100.0 / 100.0
"""