
# def solution(numbers):
#     answer = []
    
#     for i in range(0,len(numbers)):
#         for j in range(i+1, len(numbers)):
#             answer.append(numbers[i]+numbers[j])
            
#             answer.sort()
#     return answer

# 초기 코드 : list에 중복된거 고려 안하고 모든 경우의 수 추가

def solution(numbers):
    answer = []
    
    for i in range(0,len(numbers)):
        for j in range(i+1, len(numbers)):
            sum = numbers[i]+numbers[j]
            if sum not in answer:
                answer.append(sum)
            answer.sort()
    return answer

#메모리: MB, 시간:  ms
# 테스트 1 〉	통과 (0.01ms, 10.3MB)
# 테스트 2 〉	통과 (0.01ms, 10.1MB)
# 테스트 3 〉	통과 (0.01ms, 9.99MB)
# 테스트 4 〉	통과 (0.01ms, 10.3MB)
# 테스트 5 〉	통과 (0.04ms, 10.2MB)
# 테스트 6 〉	통과 (0.18ms, 10.3MB)
# 테스트 7 〉	통과 (14.34ms, 10.1MB)
# 테스트 8 〉	통과 (3.54ms, 10.1MB)
# 테스트 9 〉	통과 (0.59ms, 10.2MB)
