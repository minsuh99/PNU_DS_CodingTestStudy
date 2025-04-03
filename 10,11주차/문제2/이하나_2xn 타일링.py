def solution(n):
    # 조합(n-1C1) 의도
    answer = 1
    for i in range(1, (n//2)+1):
        temp = 1
        for j in range(0, i):
            temp *= (n-i-j) / (i-j)
        answer += temp
    return (answer % 1000000007)

# 실패 떴음... 이유: 분수가 아니라 소수로 바뀌면서 소실되는 부분 생김


def solution(n):
    answer = 0
    for i in range(0, (n // 2) + 1):
        total_tiles = n - i  # 1칸짜리 (n - 2*i)개 + 2칸짜리 i개
        twos = i
        # 자리 중에서 2칸짜리 i개 놓을 수 있는 경우의 수
        ways = 1
        for j in range(1, twos + 1):
            ways = ways * (total_tiles - twos + j) // j
        answer = (answer + ways) % 1000000007
    return answer

# 내 방식을 살리면서 GPT가 바꿔준 코드


# 테스트 1 〉	통과 (6231.01ms, 9.25MB)
# 테스트 2 〉	통과 (95.67ms, 9.2MB)
# 테스트 3 〉	통과 (2925.52ms, 9.19MB)
# 테스트 4 〉	실패 (시간 초과)
# 테스트 5 〉	통과 (47.10ms, 9.2MB)
# 테스트 6 〉	통과 (7965.02ms, 9.25MB)
# 테스트 7 〉	통과 (42.97ms, 9.07MB)
# 테스트 8 〉	통과 (4369.00ms, 9.11MB)
# 테스트 9 〉	통과 (3978.26ms, 9.25MB)
# 테스트 10 〉	실패 (시간 초과)
# 테스트 11 〉	통과 (1777.31ms, 9.3MB)
# 테스트 12 〉	통과 (113.28ms, 9.2MB)
# 테스트 13 〉	통과 (203.55ms, 9.13MB)
# 테스트 14 〉	통과 (1844.45ms, 9.25MB)