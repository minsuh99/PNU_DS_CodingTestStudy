from itertools import permutations

def solution(numbers):
    num_str = []
    for i in numbers:
        num_str.append(str(i))
    num = sorted(num_str, key=lambda x:x[0], reverse=True)

    answer = ""
    
    for i in range(9, 0, -1):
        temp_1 = []
        temp_2 = []
        for j in num:
            if j[0] == str(i):
                temp_1.append(j)
        if len(temp_1) > 1:
            for k in list(permutations(temp_1, len(temp_1))):
                temp_2.append(str("".join(k)))
            temp_2_sort = sorted(temp_2, reverse=True)
            answer = answer + temp_2_sort[0]
        elif len(temp_1) == 1:
            answer = answer + temp_1[0]
    
    return answer


# 테스트 1 〉	실패 (시간 초과)
# 테스트 2 〉	실패 (시간 초과)
# 테스트 3 〉	실패 (시간 초과)
# 테스트 4 〉	실패 (시간 초과)
# 테스트 5 〉	실패 (시간 초과)
# 테스트 6 〉	실패 (시간 초과)
# 테스트 7 〉	실패 (0.07ms, 9.16MB)
# 테스트 8 〉	통과 (0.04ms, 9.26MB)
# 테스트 9 〉	통과 (0.06ms, 9.16MB)
# 테스트 10 〉	실패 (0.04ms, 9.39MB)
# 테스트 11 〉	실패 (0.09ms, 9.16MB)
# 테스트 12 〉	통과 (0.02ms, 9.27MB)
# 테스트 13 〉	통과 (0.02ms, 9.16MB)
# 테스트 14 〉	통과 (0.03ms, 9.24MB)
# 테스트 15 〉	통과 (0.02ms, 9.16MB)

# 왜 틀렸는지 모르겠어서 GPT

# 0이 들어갈 수도 있었네??

from itertools import permutations

def solution(numbers):
    num_str = []
    for i in numbers:
        num_str.append(str(i))
    num = sorted(num_str, key=lambda x:x[0], reverse=True)

    answer = ""
    
    for i in range(9, -1, -1):
        temp_1 = []
        temp_2 = []
        for j in num:
            if j[0] == str(i):
                temp_1.append(j)
        if len(temp_1) > 1:
            for k in list(permutations(temp_1, len(temp_1))):
                temp_2.append(str("".join(k)))
            temp_2_sort = sorted(temp_2, reverse=True)
            answer = answer + temp_2_sort[0]
        elif len(temp_1) == 1:
            answer = answer + temp_1[0]
    
    return answer

# range만 (9, -1, -1)로 바꿔서 틀린건 없어졌지만... 시간초과는 많다아..;;

from itertools import permutations

def solution(numbers):
    num_str = []
    for i in numbers:
        num_str.append(str(i))
    num = sorted(num_str, key=lambda x:x[0], reverse=True)

    answer = ""
    
    for i in range(9, -1, -1):
        temp_1 = []
        temp_2 = []
        for j in num:
            if j[0] == str(i):
                temp_1.append(j)
        if len(temp_1) > 1:
            for k in list(permutations(temp_1, len(temp_1))):
                temp_2.append(str("".join(k)))
            temp_2_sort = sorted(temp_2, reverse=True)
            answer = answer + temp_2_sort[0]
        elif len(temp_1) == 1:
            answer = answer + temp_1[0]
    
    return answer
