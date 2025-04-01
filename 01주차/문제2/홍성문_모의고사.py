# def solution(answers):
#     answer = []
#     count1 = 0
#     count2 = 0
#     count3 = 0
    
#     st1 = [1,2,3,4,5]
#     st2 = [2,1,2,3,2,4,2,5]
#     st3 = [3,3,1,1,2,2,4,4,5,5]
    
#     for i in range(len(answers)):
#             if answers[i] == st1[i]:
#                 count1 +=1
#             if answers[i] == st2[i]:
#                 count2 +=1
#             if answers[i] == st3[i]:
#                 count3 +=1
                
#     if max(count1, count2, count3) == count1:
#         answer.append(1)
#     if max(count1, count2, count3) == count2:
#         answer.append(2)
#     if max(count1, count2, count3) == count3:
#         answer.append(3)
    
#     return answer

# 초기 코드 : 해당문제는 통과했으나 answer길이가 st의 길이보다 클 때 index error 발생할 수 있음


def solution(answers):
    answer = []
    count1 = 0
    count2 = 0
    count3 = 0
    
    st1 = [1,2,3,4,5]
    st2 = [2,1,2,3,2,4,2,5]
    st3 = [3,3,1,1,2,2,4,4,5,5]
    
    for i in range(len(answers)):
            if answers[i] == st1[i % len(st1)]:
                count1 +=1
            if answers[i] == st2[i % len(st2)]:
                count2 +=1
            if answers[i] == st3[i % len(st3)]:
                count3 +=1
                
    if max(count1, count2, count3) == count1:
        answer.append(1)
    if max(count1, count2, count3) == count2:
        answer.append(2)
    if max(count1, count2, count3) == count3:
        answer.append(3)
    
    return answer

# st1[i] 대신 st1[i % len(st1)] 쓰면 찍는 패턴의 인덱스 반복 가능해서 index error 해결
#메모리: MB, 시간:  ms