def solution(dirs):
    a = 0
    b = 0
    dot = [a, b]
    count_set = set()
    for i in dirs:
        a0 = a
        b0 = b
        if i == "U":
            b += 1
        elif i == "D":
            b -= 1
        elif i == "R":
            a += 1
        elif i == "L":
            a -= 1
        if a > 5:
            a = 5
        if a < -5:
            a = -5
        if b > 5:
            b = 5
        if b < -5:
            b = -5
        if not (a0 == a) & (b0 == b):
            count_set.add((a0, b0, a, b))
            count_set.add((a, b, a0, b0))
    return int(len(count_set)) / 2

# 처음에 count_set.add((a0, b0, a, b)) 이것만 해서 방향이 달라지면 정답이 틀렸음
# 그래서 두 점을 앞뒤로 모두 넣었음
# 테스트 1 〉	통과 (0.03ms, 10.2MB)
# 테스트 2 〉	통과 (0.01ms, 10.4MB)
# 테스트 3 〉	통과 (0.01ms, 10.2MB)
# 테스트 4 〉	통과 (0.12ms, 10.3MB)
# 테스트 5 〉	통과 (0.12ms, 10.2MB)
# 테스트 6 〉	통과 (0.06ms, 10.2MB)
# 테스트 7 〉	통과 (0.02ms, 10.2MB)
# 테스트 8 〉	통과 (0.06ms, 10.1MB)
# 테스트 9 〉	통과 (0.04ms, 10.4MB)
# 테스트 10 〉	통과 (0.06ms, 10.2MB)
# 테스트 11 〉	통과 (0.04ms, 10.2MB)
# 테스트 12 〉	통과 (0.07ms, 10.2MB)
# 테스트 13 〉	통과 (0.10ms, 10.4MB)
# 테스트 14 〉	통과 (0.09ms, 10.4MB)
# 테스트 15 〉	통과 (0.10ms, 10.2MB)
# 테스트 16 〉	통과 (0.24ms, 10.3MB)
# 테스트 17 〉	통과 (0.48ms, 10.2MB)
# 테스트 18 〉	통과 (0.28ms, 10.3MB)
# 테스트 19 〉	통과 (0.24ms, 10.2MB)
# 테스트 20 〉	통과 (0.25ms, 10.1MB)