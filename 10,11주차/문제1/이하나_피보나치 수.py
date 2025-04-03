def solution(n):
    for i in range(2, n+1):
        if i == 2:
            one = 0
            two = 1
            three = one + two
            one = 1
            two = three
        else:
            one = two
            two = three
            three = one + two
        if i == n:
            return (three % 1234567)
        

# 테스트 1 〉	통과 (0.00ms, 9.27MB)
# 테스트 2 〉	통과 (0.00ms, 9.21MB)
# 테스트 3 〉	통과 (0.00ms, 9.36MB)
# 테스트 4 〉	통과 (0.00ms, 9.23MB)
# 테스트 5 〉	통과 (0.00ms, 9.26MB)
# 테스트 6 〉	통과 (0.00ms, 9.26MB)
# 테스트 7 〉	통과 (0.18ms, 9.21MB)
# 테스트 8 〉	통과 (0.09ms, 9.16MB)
# 테스트 9 〉	통과 (0.07ms, 9.1MB)
# 테스트 10 〉	통과 (0.20ms, 9.16MB)
# 테스트 11 〉	통과 (0.05ms, 9.23MB)
# 테스트 12 〉	통과 (0.07ms, 9.2MB)
# 테스트 13 〉	통과 (167.66ms, 9.29MB)
# 테스트 14 〉	통과 (146.62ms, 9.23MB)