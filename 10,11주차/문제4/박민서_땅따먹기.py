def solution(land):
    my_list = [[0 for _ in range(4)] for _ in range(len(land))]
    my_list[-1] = land[-1]
    
    for i in range(len(my_list) - 2, -1, -1):
        for j in range(len(my_list[i])):
            my_list[i][j] = land[i][j] + max([my_list[i+1][k] for k in range(len(my_list[i+1])) if k != j])
    return max(my_list[0])

'''
정확성  테스트
테스트 1 〉	통과 (4.51ms, 9.45MB)
테스트 2 〉	통과 (4.79ms, 9.51MB)
테스트 3 〉	통과 (4.50ms, 9.46MB)
테스트 4 〉	통과 (4.75ms, 9.48MB)
테스트 5 〉	통과 (4.50ms, 9.37MB)
테스트 6 〉	통과 (4.75ms, 9.39MB)
테스트 7 〉	통과 (4.45ms, 9.5MB)
테스트 8 〉	통과 (4.47ms, 9.5MB)
테스트 9 〉	통과 (4.87ms, 9.5MB)
테스트 10 〉	통과 (4.84ms, 9.52MB)
테스트 11 〉	통과 (4.57ms, 9.39MB)
테스트 12 〉	통과 (4.73ms, 9.4MB)
테스트 13 〉	통과 (4.62ms, 9.46MB)
테스트 14 〉	통과 (4.76ms, 9.52MB)
테스트 15 〉	통과 (4.80ms, 9.49MB)
테스트 16 〉	통과 (4.89ms, 9.55MB)
테스트 17 〉	통과 (4.48ms, 9.48MB)
테스트 18 〉	통과 (4.56ms, 9.48MB)
효율성  테스트
테스트 1 〉	통과 (446.61ms, 42.3MB)
테스트 2 〉	통과 (489.22ms, 42.5MB)
테스트 3 〉	통과 (441.92ms, 42.5MB)
테스트 4 〉	통과 (439.58ms, 42.4MB)
채점 결과
정확성: 59.8
효율성: 40.2
합계: 100.0 / 100.0
'''