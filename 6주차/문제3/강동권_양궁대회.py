def solution(n, info):
    def points(shot):
        score = 0
        for i in range(11):
            if shot[i] > info[i]:
                score += 10 - i
            elif info[i] > 0:
                score -= 10 - i
        return score

    max_diff = 0
    answer = []

    def backtrack(shot, arrows, idx):
        nonlocal max_diff, answer
        
        # Base Case: 모든 점수를 확인했을 때
        if idx == 11:
            if arrows > 0:
                shot[10] += arrows  # Remaining Arrows to 0
            
            diff = points(shot)
            if diff > max_diff:
                max_diff = diff
                answer = shot.copy()
            elif diff == max_diff:
                # Tie Breaker
                if answer:
                    for i in range(10, -1, -1):
                        if shot[i] > answer[i]:
                            answer = shot.copy()
                            break
                        elif shot[i] < answer[i]:
                            break
                else:
                    answer = shot.copy()

            shot[10] -= arrows
            return

        # Case 1: not hitting those points
        backtrack(shot, arrows, idx + 1)

        # Case 2: earning those points
        if arrows > info[idx]:
            shot[idx] = info[idx] + 1
            backtrack(shot, arrows - shot[idx], idx + 1)
            shot[idx] = 0 

    backtrack([0] * 11, n, 0)

    return answer if (answer and max_diff !=0) else [-1]

# 테스트 1 〉	통과 (0.12ms, 10.2MB)
# 테스트 2 〉	통과 (1.97ms, 10.3MB)
# 테스트 3 〉	통과 (1.82ms, 10.1MB)
# 테스트 4 〉	통과 (0.83ms, 10.3MB)
# 테스트 5 〉	통과 (2.09ms, 10.2MB)
# 테스트 6 〉	통과 (2.08ms, 10.2MB)
# 테스트 7 〉	통과 (0.71ms, 10.4MB)
# 테스트 8 〉	통과 (0.29ms, 10.3MB)
# 테스트 9 〉	통과 (1.22ms, 10.2MB)
# 테스트 10 〉	통과 (0.27ms, 10.4MB)
# 테스트 11 〉	통과 (0.47ms, 10.1MB)
# 테스트 12 〉	통과 (0.47ms, 10.3MB)
# 테스트 13 〉	통과 (1.33ms, 10.1MB)
# 테스트 14 〉	통과 (1.96ms, 10.3MB)
# 테스트 15 〉	통과 (1.84ms, 10.4MB)
# 테스트 16 〉	통과 (1.60ms, 10.3MB)
# 테스트 17 〉	통과 (0.73ms, 10.3MB)
# 테스트 18 〉	통과 (0.12ms, 10.3MB)
# 테스트 19 〉	통과 (0.03ms, 10.3MB)
# 테스트 20 〉	통과 (1.90ms, 10.4MB)
# 테스트 21 〉	통과 (1.85ms, 10.3MB)
# 테스트 22 〉	통과 (2.38ms, 10.2MB)
# 테스트 23 〉	통과 (0.26ms, 10.4MB)
# 테스트 24 〉	통과 (2.39ms, 10.2MB)
# 테스트 25 〉	통과 (1.98ms, 10.4MB)
