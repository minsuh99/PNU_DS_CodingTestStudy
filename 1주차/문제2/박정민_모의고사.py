def solution(answers):
    answer = []
    num1 = [1,2,3,4,5]
    num2 = [2,1,2,3,2,4,2,5]
    num3 = [3,3,1,1,2,2,4,4,5,5]
    score = [0,0,0]
    
    for i in range(len(answers)):
        if num1[i%5] == answers[i]:
            score[0] += 1
        if num2[i%8] == answers[i]:
            score[1] += 1
        if num3[i%10] == answers[i]:
            score[2] += 1
    
    max_value = max(score[0], score[1], score[2])
    
    if max_value == score[0]:
        answer.append(1)
    if max_value == score[1]:
        answer.append(2)
    if max_value == score[2]:
        answer.append(3)
        
    return answer

'''
테스트 1 〉	통과 (0.01ms, 10.2MB)
테스트 2 〉	통과 (0.01ms, 10.3MB)
테스트 3 〉	통과 (0.01ms, 10.3MB)
테스트 4 〉	통과 (0.01ms, 10.2MB)
테스트 5 〉	통과 (0.02ms, 10.2MB)
테스트 6 〉	통과 (0.02ms, 10.2MB)
테스트 7 〉	통과 (1.87ms, 10.2MB)
테스트 8 〉	통과 (0.42ms, 10.2MB)
테스트 9 〉	통과 (2.40ms, 10.4MB)
테스트 10 〉	통과 (1.10ms, 10.3MB)
테스트 11 〉	통과 (2.48ms, 10.3MB)
테스트 12 〉	통과 (2.18ms, 10.2MB)
테스트 13 〉	통과 (0.14ms, 10.3MB)
테스트 14 〉	통과 (2.51ms, 10.3MB)
'''