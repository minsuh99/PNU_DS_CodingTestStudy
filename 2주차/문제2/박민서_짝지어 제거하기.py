def solution(s):
    answer = -1
    stack = []
    
    for char in s:
        if not stack or char not in stack: # stack 안에 없는 문자면 push
            stack.append(char)
        else:
            if char == stack[-1]: # stack 안에 있는 문자인데, stack의 마지막과 같은 문자면 pop
                stack.pop()
            else:
                stack.append(char) # 아니면 push
    if len(stack) == 0: # stack이 안 비어있다면 0, 비어있다면 1
        answer = 1
    else:
        answer = 0
                
    return answer

'''
정확성  테스트
테스트 1 〉	통과 (0.00ms, 10.2MB)
테스트 2 〉	통과 (10.20ms, 10.3MB)
테스트 3 〉	통과 (47.53ms, 10.3MB)
테스트 4 〉	통과 (49.68ms, 10.7MB)
테스트 5 〉	통과 (55.70ms, 10.6MB)
테스트 6 〉	통과 (41.70ms, 10.6MB)
테스트 7 〉	통과 (56.47ms, 10.6MB)
테스트 8 〉	통과 (44.76ms, 10.6MB)
테스트 9 〉	통과 (0.00ms, 10.3MB)
테스트 10 〉	통과 (0.04ms, 10.1MB)
테스트 11 〉	통과 (0.01ms, 10.1MB)
테스트 12 〉	통과 (0.00ms, 10.3MB)
테스트 13 〉	통과 (0.01ms, 10.2MB)
테스트 14 〉	통과 (0.00ms, 10.3MB)
테스트 15 〉	통과 (0.01ms, 10.2MB)
테스트 16 〉	통과 (0.01ms, 10.3MB)
테스트 17 〉	통과 (0.01ms, 10.3MB)
테스트 18 〉	통과 (0.00ms, 10.2MB)
효율성  테스트
테스트 1 〉	통과 (104.38ms, 16.3MB)
테스트 2 〉	통과 (88.68ms, 11.7MB)
테스트 3 〉	통과 (481.38ms, 12.3MB)
테스트 4 〉	통과 (466.51ms, 12.3MB)
테스트 5 〉	통과 (397.74ms, 12.3MB)
테스트 6 〉	통과 (393.50ms, 12.3MB)
테스트 7 〉	통과 (489.36ms, 12.3MB)
테스트 8 〉	통과 (335.93ms, 14.6MB)
채점 결과
정확성: 61.2
효율성: 38.8
합계: 100.0 / 100.0
'''
