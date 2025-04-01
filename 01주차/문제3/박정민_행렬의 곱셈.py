def solution(arr1, arr2):
    answer = []
    for row in range(len(arr1)):
        answer.append([])
        for col in range(len(arr2[0])):
            sum = 0
            for i in range(len(arr1[0])):
                sum += arr1[row][i] * arr2[i][col]
            answer[row].append(sum)
    return answer

'''
테스트 1 〉	통과 (3.09ms, 10.2MB)
테스트 2 〉	통과 (61.89ms, 10.9MB)
테스트 3 〉	통과 (70.40ms, 11.1MB)
테스트 4 〉	통과 (1.55ms, 10.4MB)
테스트 5 〉	통과 (45.99ms, 10.8MB)
테스트 6 〉	통과 (29.05ms, 10.8MB)
테스트 7 〉	통과 (1.88ms, 10.2MB)
테스트 8 〉	통과 (0.56ms, 10.3MB)
테스트 9 〉	통과 (0.44ms, 10.3MB)
테스트 10 〉	통과 (44.82ms, 10.7MB)
테스트 11 〉	통과 (4.21ms, 10.2MB)
테스트 12 〉	통과 (1.20ms, 10.4MB)
테스트 13 〉	통과 (53.80ms, 10.7MB)
테스트 14 〉	통과 (73.18ms, 10.8MB)
테스트 15 〉	통과 (21.02ms, 10.4MB)
테스트 16 〉	통과 (7.84ms, 10.5MB)
'''