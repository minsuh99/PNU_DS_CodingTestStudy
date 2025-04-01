def solution(arr1, arr2):
    answer = []
    for i in range(len(arr1)):
        result = []
        for j in range(len(arr2[0])):
            multi = 0
            for k in range(len(arr1[0])):
                multi += arr1[i][k] * arr2[k][j]
            result.append(multi)
        answer.append(result)
    return answer



'''
테스트 1 〉	통과 (3.24ms, 10.3MB)
테스트 2 〉	통과 (73.53ms, 11MB)
테스트 3 〉	통과 (99.46ms, 11.1MB)
테스트 4 〉	통과 (1.36ms, 10.3MB)
테스트 5 〉	통과 (47.80ms, 10.8MB)
테스트 6 〉	통과 (31.28ms, 11MB)
테스트 7 〉	통과 (1.25ms, 10.2MB)
테스트 8 〉	통과 (0.55ms, 10.2MB)
테스트 9 〉	통과 (0.44ms, 10.2MB)
테스트 10 〉	통과 (57.15ms, 10.6MB)
테스트 11 〉	통과 (4.19ms, 10.4MB)
테스트 12 〉	통과 (0.75ms, 10.4MB)
테스트 13 〉	통과 (34.41ms, 10.8MB)
테스트 14 〉	통과 (68.59ms, 10.9MB)
테스트 15 〉	통과 (21.11ms, 10.4MB)
테스트 16 〉	통과 (6.31ms, 10.6MB)

'''
