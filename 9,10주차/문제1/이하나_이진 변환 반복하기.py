def solution(s):
    count = 0
    count_zero = 0
    new_s = s
    while new_s != "1":
        temp_s = ""
        for i in new_s:
            if i == "0":
                count_zero += 1
            elif i == "1":
                temp_s += i
        count += 1
        amount = len(temp_s)

        # 최대는 2의 17
        new_s = 0
        for i in range(17, -1, -1):
            if amount >= (2**i):
                new_s += (10**i)
                amount -= (2**i)
        new_s = str(new_s)
        
    return [count, count_zero]


# 테스트 1 〉	통과 (0.05ms, 9.21MB)
# 테스트 2 〉	통과 (7.45ms, 9.4MB)
# 테스트 3 〉	통과 (0.03ms, 9.29MB)
# 테스트 4 〉	통과 (0.02ms, 9.23MB)
# 테스트 5 〉	통과 (0.03ms, 9.29MB)
# 테스트 6 〉	통과 (0.10ms, 9.29MB)
# 테스트 7 〉	통과 (0.14ms, 9.16MB)
# 테스트 8 〉	통과 (0.06ms, 9.09MB)
# 테스트 9 〉	통과 (8.37ms, 9.24MB)
# 테스트 10 〉	통과 (21.34ms, 9.48MB)
# 테스트 11 〉	통과 (6.72ms, 9.46MB)