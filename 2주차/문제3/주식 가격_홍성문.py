# 초기 코드 ->  테스트 1 제외 다 실패
# def solution(prices):
#     answer = []

#     for i in range(len(prices)):
#         count = 0 
#         for j in range(i+1, len(prices)):
#             if prices[i] <= prices[j]:
#                 count += 1
#         answer.append(count)

#     return answer

# 정확성  테스트
# 테스트 1 〉	통과 (0.01ms, 10.1MB)
# 테스트 2 〉	실패 (0.36ms, 9.96MB)
# 테스트 3 〉	실패 (27.13ms, 10.1MB)
# 테스트 4 〉	실패 (77.52ms, 10.4MB)
# 테스트 5 〉	실패 (72.25ms, 10.2MB)
# 테스트 6 〉	실패 (0.17ms, 10MB)
# 테스트 7 〉	실패 (13.99ms, 10.2MB)
# 테스트 8 〉	실패 (18.99ms, 10.4MB)
# 테스트 9 〉	실패 (0.13ms, 10.1MB)
# 테스트 10 〉	실패 (49.68ms, 10.1MB)

# 효율성  테스트
# 테스트 1 〉	실패 (시간 초과)
# 테스트 2 〉	실패 (시간 초과)
# 테스트 3 〉	실패 (시간 초과)
# 테스트 4 〉	실패 (시간 초과)
# 테스트 5 〉	실패 (시간 초과)

def solution(prices):
    answer = []

    for i in range(len(prices)):
        count = 0
        for j in range(i + 1, len(prices)):
            count += 1 #처음에는 항상 1초 증가, 마지막은 어차피 루프X 라서 0
            if prices[i] > prices[j]: 
                break  # ★break문 써서 반복루프 중단
        answer.append(count)  

    return answer


print(solution([1,2,3,2,3]))

# 정확성  테스트
# 테스트 1 〉	통과 (0.01ms, 9.91MB)
# 테스트 2 〉	통과 (0.05ms, 10.3MB)
# 테스트 3 〉	통과 (0.88ms, 10.2MB)
# 테스트 4 〉	통과 (0.87ms, 10MB)
# 테스트 5 〉	통과 (0.90ms, 10.3MB)
# 테스트 6 〉	통과 (0.03ms, 10.3MB)
# 테스트 7 〉	통과 (0.42ms, 10.3MB)
# 테스트 8 〉	통과 (0.46ms, 10.2MB)
# 테스트 9 〉	통과 (0.03ms, 10MB)
# 테스트 10 〉	통과 (0.87ms, 10.2MB)

# 효율성  테스트
# 테스트 1 〉	통과 (121.06ms, 18.8MB)
# 테스트 2 〉	통과 (95.10ms, 17.5MB)
# 테스트 3 〉	통과 (151.19ms, 19.5MB)
# 테스트 4 〉	통과 (108.37ms, 18.3MB)
# 테스트 5 〉	통과 (71.81ms, 17MB)

# 채점 결과
# 정확성: 66.7
# 효율성: 33.3
# 합계: 100.0 / 100.0

