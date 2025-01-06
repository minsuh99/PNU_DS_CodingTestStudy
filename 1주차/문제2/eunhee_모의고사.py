def solution(answers):
    supo1 = [1,2,3,4,5]
    supo2 = [2,1,2,3,2,4,2,5]
    supo3 = [3,3,1,1,2,2,4,4,5,5]
    
    ans = [0,0,0]
    for i in range(len(answers)):
        if answers[i] == supo1[i % len(supo1)]:
            ans[0] +=1
        if answers[i] == supo2[i % len(supo2)]:
            ans[1] +=1
        if answers[i] == supo3[i % len(supo3)]:
            ans[2] +=1
            
    answer = []
    if max(ans) == ans[0]:
        answer.append(1)
    if max(ans) == ans[1]:
        answer.append(2)
    if max(ans) == ans[2]:
        answer.append(3)
    return answer

'''

테스트 1 〉	통과 (0.03ms, 10.3MB)
테스트 2 〉	통과 (0.01ms, 10.2MB)
테스트 3 〉	통과 (0.01ms, 10.2MB)
테스트 4 〉	통과 (0.01ms, 10.2MB)
테스트 5 〉	통과 (0.03ms, 10.2MB)
테스트 6 〉	통과 (0.03ms, 10.2MB)
테스트 7 〉	통과 (1.79ms, 10.4MB)
테스트 8 〉	통과 (0.59ms, 10.2MB)
테스트 9 〉	통과 (3.24ms, 10.1MB)
테스트 10 〉	통과 (1.50ms, 10.3MB)
테스트 11 〉	통과 (3.49ms, 10.3MB)
테스트 12 〉	통과 (4.16ms, 10.3MB)
테스트 13 〉	통과 (0.20ms, 10.2MB)
테스트 14 〉	통과 (3.44ms, 10.3MB)

'''