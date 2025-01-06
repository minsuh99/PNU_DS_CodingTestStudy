
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

