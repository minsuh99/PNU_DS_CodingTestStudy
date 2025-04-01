# 처음 코드

# def solution(prices):
#     answer = [0 for _ in range(len(prices))]
    
#     for i in range(len(prices)):
#         price = prices[i]
#         if i + 1 != len(prices):
#             check_prices = prices[i+1:]
#             for _ in range(len(check_prices)):
#                 answer[i] += 1
#                 if check_prices.pop(0) < price:
#                     break                
        
#     return answer

# stack 관련 문제라 .pop()을 이용해서 하려다 보니
# 효율성은 0점으로 나왔다. 정확성 테스트 실행시간이 2ms도 안 나와서 의문
# 문제 지문 해석에서 많이 갈릴 거 같음
# 문제에서 얘기하고자 하는건 다음 시간으로 넘어가기 직전은 주가 유지를 한 것으로 보는 듯

# 최종 제출 코드
def solution(prices):
    answer = [0 for _ in range(len(prices))]
    
    for i in range(len(prices) - 1):
        for j in range(i + 1, len(prices)):
            answer[i] += 1
            if prices[j] < prices[i]:
                break
        
    return answer

'''
정확성  테스트
테스트 1 〉	통과 (0.01ms, 10.3MB)
테스트 2 〉	통과 (0.09ms, 10.2MB)
테스트 3 〉	통과 (0.83ms, 10.2MB)
테스트 4 〉	통과 (1.42ms, 10.3MB)
테스트 5 〉	통과 (1.17ms, 10.3MB)
테스트 6 〉	통과 (0.03ms, 10.1MB)
테스트 7 〉	통과 (0.52ms, 10.2MB)
테스트 8 〉	통과 (1.11ms, 10.2MB)
테스트 9 〉	통과 (0.04ms, 10.3MB)
테스트 10 〉	통과 (1.07ms, 10.4MB)
효율성  테스트
테스트 1 〉	통과 (156.30ms, 18.7MB)
테스트 2 〉	통과 (121.81ms, 17.6MB)
테스트 3 〉	통과 (194.37ms, 19.5MB)
테스트 4 〉	통과 (137.33ms, 18.1MB)
테스트 5 〉	통과 (91.92ms, 17MB)
채점 결과
정확성: 66.7
효율성: 33.3
합계: 100.0 / 100.0
'''