def solution(topping):
    toppings = len(topping)
    answer = 0
    for i in range(0, toppings-1):
        left = set(topping[0:(i+1)])
        right = set(topping[(i+1):toppings])
        if len(left) == len(right):
            answer += 1
    return answer

# 테스트 1 〉	통과 (2214.87ms, 9.53MB)
# 테스트 2 〉	실패 (시간 초과)
# 테스트 3 〉	실패 (시간 초과)
# 테스트 4 〉	실패 (시간 초과)
# 테스트 5 〉	실패 (시간 초과)
# 테스트 6 〉	실패 (시간 초과)
# 테스트 7 〉	실패 (시간 초과)
# 테스트 8 〉	실패 (시간 초과)
# 테스트 9 〉	실패 (시간 초과)
# 테스트 10 〉	실패 (시간 초과)
# 테스트 11 〉	실패 (시간 초과)
# 테스트 12 〉	통과 (2802.57ms, 11.8MB)
# 테스트 13 〉	실패 (시간 초과)
# 테스트 14 〉	실패 (시간 초과)
# 테스트 15 〉	실패 (시간 초과)
# 테스트 16 〉	실패 (시간 초과)
# 테스트 17 〉	실패 (시간 초과)
# 테스트 18 〉	실패 (시간 초과)
# 테스트 19 〉	실패 (시간 초과)
# 테스트 20 〉	실패 (시간 초과)


def solution(topping):
    category = set(topping)
    category_half = len(category) // 2
    toppings = len(topping)
    answer = 0
    for i in range(0, toppings-1):
        left = set(topping[0:(i+1)])
        if len(left) < category_half:
            continue
        right = set(topping[(i+1):toppings])
        if len(right) < category_half:
            continue
        if len(left) == len(right):
            answer += 1
    return answer

# 테스트 1 〉	통과 (2958.22ms, 9.63MB)
# 테스트 2 〉	실패 (시간 초과)
# 테스트 3 〉	실패 (시간 초과)
# 테스트 4 〉	실패 (시간 초과)
# 테스트 5 〉	실패 (시간 초과)


# 아잇.. 모르겠다

def solution(topping):
    toppings = len(topping)
    answer = 0
    now = 0
    left = set()
    right = set()
    for i in range(0, toppings-1):
        if topping[i] in left:
            if topping[i] in topping[(i+1):]:
                if now == 0:
                    continue
                elif now == 1:
                    answer += 1
                    continue
        left = set(topping[:(i+1)])
        right = set(topping[(i+1):])
        if len(left) == len(right):
            answer += 1
            now = 1
        else:
            now = 0
    return answer


# 테스트 1 〉	통과 (652.99ms, 9.83MB)
# 테스트 2 〉	실패 (시간 초과)
# 테스트 3 〉	통과 (9689.97ms, 11.4MB)
# 테스트 4 〉	통과 (9001.08ms, 10.6MB)
# 테스트 5 〉	실패 (시간 초과)
# 테스트 6 〉	실패 (시간 초과)
# 테스트 7 〉	실패 (시간 초과)
# 테스트 8 〉	실패 (시간 초과)
# 테스트 9 〉	실패 (시간 초과)
# 테스트 10 〉	실패 (시간 초과)
# 테스트 11 〉	실패 (시간 초과)
# 테스트 12 〉	통과 (2769.73ms, 12MB)
# 테스트 13 〉	실패 (시간 초과)
# 테스트 14 〉	실패 (시간 초과)
# 테스트 15 〉	실패 (시간 초과)
# 테스트 16 〉	실패 (시간 초과)
# 테스트 17 〉	실패 (시간 초과)
# 테스트 18 〉	실패 (시간 초과)
# 테스트 19 〉	실패 (시간 초과)
# 테스트 20 〉	실패 (시간 초과)