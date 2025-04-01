def solution(numbers):
    answer = []
    for i in range(len(numbers)) :
        for j in range(len(numbers)) :
            if i != j :
                answer.append(numbers[i] + numbers[j])
    answer = sorted(set(answer))
    return answer


'''
테스트 1 〉	통과 (0.01ms, 10.1MB)
테스트 2 〉	통과 (0.01ms, 10.1MB)
테스트 3 〉	통과 (0.01ms, 10.1MB)
테스트 4 〉	통과 (0.01ms, 10.3MB)
테스트 5 〉	통과 (0.02ms, 10.2MB)
테스트 6 〉	통과 (0.06ms, 10.2MB)
테스트 7 〉	통과 (1.15ms, 10.3MB)
테스트 8 〉	통과 (1.22ms, 10.3MB)
테스트 9 〉	통과 (1.18ms, 10.2MB)

'''
