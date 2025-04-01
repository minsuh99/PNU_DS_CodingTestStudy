# 모의고사 문제

def solution(answers):
    count1 = 0
    count2 = 0
    count3 = 0
    for i in range(len(answers)):
        if i+1 % 5 == 0:
            num1 = 5
        else:
            num1 = i+1 % 5
        if i % 2 == 0:
            num2 = 2
        elif i+1 % 8 == 2:
            num2 = 1
        elif i+1 % 8 == 4:
            num2 = 3
        elif i+1 % 8 == 6:
            num2 = 4
        elif i+1 % 8 == 0:
            num2 = 5
        if (i+1 % 10 == 0) or (i+1 % 10 == 9):
            num3 = 5
        elif (i+1 % 10 == 8) or (i+1 % 10 == 7):
            num3 = 4
        elif (i+1 % 10 == 6) or (i+1 % 10 == 5):
            num3 = 2
        elif (i+1 % 10 == 4) or (i+1 % 10 == 3):
            num3 = 1
        elif (i+1 % 10 == 2) or (i+1 % 10 == 1):
            num3 = 3
        if answers[i] == num1:
            count1 += 1
        if answers[i] == num2:
            count2 += 1
        if answers[i] == num3:
            count3 += 1
    list = [count1, count2, count3]
    answer_final = []
    for i in range(3):
        if list[i] == max(list):
            answer_final.append(i+1)
    return answer_final

# 틀린 이유: gpt에 따르면 연산자 우선순위 문제가 있다고 함!

# 테스트 1 〉	실패 (0.02ms, 10.2MB)
# 테스트 2 〉	통과 (0.01ms, 10.2MB)
# 테스트 3 〉	통과 (0.01ms, 10.2MB)
# 테스트 4 〉	통과 (0.01ms, 10.4MB)
# 테스트 5 〉	실패 (0.04ms, 10.2MB)
# 테스트 6 〉	실패 (0.05ms, 10.2MB)
# 테스트 7 〉	통과 (6.99ms, 10.2MB)
# 테스트 8 〉	통과 (2.71ms, 10.3MB)
# 테스트 9 〉	실패 (12.47ms, 10.4MB)
# 테스트 10 〉	실패 (3.64ms, 10.2MB)
# 테스트 11 〉	실패 (10.29ms, 10.3MB)
# 테스트 12 〉	실패 (7.07ms, 10.3MB)
# 테스트 13 〉	실패 (0.63ms, 10.4MB)
# 테스트 14 〉	통과 (9.75ms, 10.3MB)

# 위의 코드 그대로 괄호만 추가함! 완성!

def solution(answers):
    count1 = 0
    count2 = 0
    count3 = 0
    for i in range(len(answers)):
        if (i+1) % 5 == 0:
            num1 = 5
        else:
            num1 = (i+1) % 5
        if (i % 2) == 0:
            num2 = 2
        elif (i+1) % 8 == 2:
            num2 = 1
        elif (i+1) % 8 == 4:
            num2 = 3
        elif (i+1) % 8 == 6:
            num2 = 4
        elif (i+1) % 8 == 0:
            num2 = 5
        if ((i+1) % 10 == 0) or ((i+1) % 10 == 9):
            num3 = 5
        elif ((i+1) % 10 == 8) or ((i+1) % 10 == 7):
            num3 = 4
        elif ((i+1) % 10 == 6) or ((i+1) % 10 == 5):
            num3 = 2
        elif ((i+1) % 10 == 4) or ((i+1) % 10 == 3):
            num3 = 1
        elif ((i+1) % 10 == 2) or ((i+1) % 10 == 1):
            num3 = 3
        if answers[i] == num1:
            count1 += 1
        if answers[i] == num2:
            count2 += 1
        if answers[i] == num3:
            count3 += 1
    list = [count1, count2, count3]
    answer_final = []
    for i in range(3):
        if list[i] == max(list):
            answer_final.append(i+1)
    return answer_final

# 테스트 1 〉	통과 (0.02ms, 10.3MB)
# 테스트 2 〉	통과 (0.01ms, 10.4MB)
# 테스트 3 〉	통과 (0.01ms, 10.2MB)
# 테스트 4 〉	통과 (0.01ms, 10.2MB)
# 테스트 5 〉	통과 (0.04ms, 10.2MB)
# 테스트 6 〉	통과 (0.05ms, 10.4MB)
# 테스트 7 〉	통과 (6.58ms, 10.3MB)
# 테스트 8 〉	통과 (2.18ms, 10.3MB)
# 테스트 9 〉	통과 (6.82ms, 10.3MB)
# 테스트 10 〉	통과 (3.15ms, 10.4MB)
# 테스트 11 〉	통과 (6.90ms, 10.3MB)
# 테스트 12 〉	통과 (6.76ms, 10.3MB)
# 테스트 13 〉	통과 (0.41ms, 10.2MB)
# 테스트 14 〉	통과 (7.37ms, 10.3MB)


# 아래는 gpt가 고쳐준 것

def solution(answers):
    count1, count2, count3 = 0, 0, 0 # 이런 부분 단순화 시키고
    
    # 패턴 정의
    num1_pattern = [1, 2, 3, 4, 5]
    num2_pattern = [2, 1, 2, 3, 2, 4, 2, 5]
    num3_pattern = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    
    for i in range(len(answers)):
        num1 = num1_pattern[i % 5]
        num2 = num2_pattern[i % 8]
        num3 = num3_pattern[i % 10]
        
        if answers[i] == num1:
            count1 += 1
        if answers[i] == num2:
            count2 += 1
        if answers[i] == num3:
            count3 += 1
    
    # 최대값을 가진 사람 찾기
    counts = [count1, count2, count3]
    result = [i+1 for i, count in enumerate(counts) if count == max(counts)]
    
    return result

