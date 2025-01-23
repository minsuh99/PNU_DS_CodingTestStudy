def solution(want, number, discount):
    temp = []
    total = []
    num = len(number)
    answer = 0
    for i in range(len(want)):
        temp.append(want[i])
        total += temp * number[i]
        temp = []
    total_sort = sorted(total)
    for k in range(len(discount) - num):
        if discount[k] not in total:
            pass
        else:
            y = sorted(discount[k:(k+len(total))])
            if total_sort == y:
                answer += 1
    return answer

# 테스트 1 〉	통과 (7.07ms, 10.5MB)
# 테스트 2 〉	통과 (60.65ms, 14.8MB)
# 테스트 3 〉	통과 (14.98ms, 11MB)
# 테스트 4 〉	통과 (63.44ms, 15.5MB)
# 테스트 5 〉	통과 (23.95ms, 13MB)
# 테스트 6 〉	통과 (4.43ms, 10.3MB)
# 테스트 7 〉	통과 (14.26ms, 11.3MB)
# 테스트 8 〉	통과 (82.07ms, 17.4MB)
# 테스트 9 〉	통과 (10.85ms, 10.9MB)
# 테스트 10 〉	통과 (31.12ms, 13.7MB)
# 테스트 11 〉	통과 (15.93ms, 10.5MB)
# 테스트 12 〉	통과 (0.02ms, 10.1MB)