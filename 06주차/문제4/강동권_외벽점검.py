from itertools import permutations

def solution(n, weak, dist):
    length = len(weak)
    weak += [w + n for w in weak]  # Handle circular nature
    answer = float('inf')

    dist.sort(reverse=True)  # Try the strongest friends first

    # Try starting at each weak point
    for start in range(length):
        for friends in permutations(dist):  # Try different friend orders
            count = 1  # Number of friends used
            position = weak[start] + friends[0]  # First friend covers up to this position

            for i in range(start, start + length):  # Traverse weak points
                if weak[i] > position:  # Need another friend
                    count += 1
                    if count > len(dist):  # Too many friends needed
                        break
                    position = weak[i] + friends[count - 1]  # Extend coverage

            answer = min(answer, count)

    return answer if answer <= len(dist) else -1

# 테스트 1 〉	통과 (0.07ms, 10.1MB)
# 테스트 2 〉	통과 (0.07ms, 10.3MB)
# 테스트 3 〉	통과 (781.04ms, 10.2MB)
# 테스트 4 〉	통과 (704.16ms, 9.99MB)
# 테스트 5 〉	통과 (1.64ms, 10.3MB)
# 테스트 6 〉	통과 (138.77ms, 10.2MB)
# 테스트 7 〉	통과 (0.04ms, 10.3MB)
# 테스트 8 〉	통과 (0.30ms, 10.4MB)
# 테스트 9 〉	통과 (0.28ms, 10MB)
# 테스트 10 〉	통과 (1263.60ms, 10.2MB)
# 테스트 11 〉	통과 (1239.71ms, 10.2MB)
# 테스트 12 〉	통과 (1222.34ms, 10.4MB)
# 테스트 13 〉	통과 (1136.89ms, 10.2MB)
# 테스트 14 〉	통과 (1368.29ms, 10.3MB)
# 테스트 15 〉	통과 (1198.79ms, 10.1MB)
# 테스트 16 〉	통과 (986.94ms, 10.2MB)
# 테스트 17 〉	통과 (1038.01ms, 10.3MB)
# 테스트 18 〉	통과 (1126.74ms, 10.2MB)
# 테스트 19 〉	통과 (871.93ms, 10.4MB)
# 테스트 20 〉	통과 (1022.69ms, 10.3MB)
# 테스트 21 〉	통과 (945.57ms, 10.1MB)
# 테스트 22 〉	통과 (0.31ms, 10.1MB)
# 테스트 23 〉	통과 (0.30ms, 10.3MB)
# 테스트 24 〉	통과 (0.32ms, 10.2MB)
# 테스트 25 〉	통과 (344.76ms, 10.2MB)
