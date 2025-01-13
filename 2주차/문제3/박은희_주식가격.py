# 처음 답 틀림
# def solution(prices):
#     answer = []
#     for i in range(len(prices)):
#         time = 0
#         for j in range(i+1, len(prices)):
#             if prices[i] > prices[j]:
#                 time += 1
#                 answer.append(time)
#     answer.append(0)
#     print(answer)
#     return answer
#  출력 〉	[1, 0] ?? 뭐지...
        
# 고쳐보려고 했는데 모르겠음!!!!

        


'''

prices =  초단위로 기록된 주식가격
가격이 떨어지지 않은 초

1. 가격 받기
2. 가격 +1 돌면서 금액 큰지 확인
3. 크면 시간에 +1
4. 마지막 0 추가
4. 전부 다 돌았는데 없으면 0000출력되게 -> 이건 어케? 일단 보륲

'''