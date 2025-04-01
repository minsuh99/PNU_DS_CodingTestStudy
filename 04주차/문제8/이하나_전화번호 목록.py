def solution(phone_book):
    answer = True
    phone_book.sort()
    for i in range(len(phone_book)):
        num = len(phone_book[i])
        for j in range(i+1, len(phone_book)):
            if num < len(phone_book[j]):
                if phone_book[i] == phone_book[j][0:num]:
                    answer = False
                    break
    return answer

# 효율성 테스트 모두 시간 초과
# 테스트 1 〉	통과 (0.01ms, 10.1MB)
# 테스트 2 〉	통과 (0.01ms, 10.1MB)
# 테스트 3 〉	통과 (0.01ms, 10.1MB)
# 테스트 4 〉	통과 (0.01ms, 10.1MB)
# 테스트 5 〉	통과 (0.01ms, 10.1MB)
# 테스트 6 〉	통과 (0.01ms, 10.2MB)
# 테스트 7 〉	통과 (0.01ms, 10.1MB)
# 테스트 8 〉	통과 (0.01ms, 10.2MB)
# 테스트 9 〉	통과 (0.01ms, 10.2MB)
# 테스트 10 〉	통과 (0.01ms, 10.3MB)
# 테스트 11 〉	통과 (0.01ms, 10.1MB)
# 테스트 12 〉	통과 (0.01ms, 10.1MB)
# 테스트 13 〉	통과 (0.01ms, 10.1MB)
# 테스트 14 〉	통과 (72.16ms, 10.2MB)
# 테스트 15 〉	통과 (132.07ms, 10.3MB)
# 테스트 16 〉	통과 (108.18ms, 10.3MB)
# 테스트 17 〉	통과 (161.25ms, 10.2MB)
# 테스트 18 〉	통과 (381.09ms, 10.2MB)
# 테스트 19 〉	통과 (463.51ms, 10.2MB)
# 테스트 20 〉	통과 (612.04ms, 10.2MB)