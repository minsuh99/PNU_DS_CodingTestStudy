def solution(numbers):
    answer = set()
    for i in range(len(numbers)):
        for j in range(1+i, len(numbers)):
            k = numbers[i] + numbers[j]
            answer.add(k)
    answer = list(answer)
    return sorted(answer)

'''
테스트 1 〉	통과 (0.01ms, 10.1MB)
테스트 2 〉	통과 (0.01ms, 10.2MB)
테스트 3 〉	통과 (0.01ms, 10MB)
테스트 4 〉	통과 (0.01ms, 10.3MB)
테스트 5 〉	통과 (0.02ms, 10.2MB)
테스트 6 〉	통과 (0.06ms, 10.1MB)
테스트 7 〉	통과 (0.55ms, 10.2MB)
테스트 8 〉	통과 (0.50ms, 10.2MB)
테스트 9 〉	통과 (0.77ms, 10.1MB)
'''