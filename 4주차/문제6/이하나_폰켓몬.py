def solution(nums):
    count = len(nums) / 2
    set_nums = set(nums)
    
    if count >= len(set_nums):
        answer = len(set_nums)
    elif count < len(set_nums):
        answer = count
    
    return answer


# 테스트 1 〉	통과 (0.00ms, 10.2MB)
# 테스트 2 〉	통과 (0.00ms, 10.2MB)
# 테스트 3 〉	통과 (0.01ms, 10.1MB)
# 테스트 4 〉	통과 (0.01ms, 10.2MB)
# 테스트 5 〉	통과 (0.00ms, 10.2MB)
# 테스트 6 〉	통과 (0.01ms, 10MB)
# 테스트 7 〉	통과 (0.01ms, 10.1MB)
# 테스트 8 〉	통과 (0.01ms, 10.3MB)
# 테스트 9 〉	통과 (0.01ms, 10.3MB)
# 테스트 10 〉	통과 (0.01ms, 10.1MB)
# 테스트 11 〉	통과 (0.01ms, 10.3MB)
# 테스트 12 〉	통과 (0.05ms, 10.1MB)
# 테스트 13 〉	통과 (0.06ms, 10.3MB)
# 테스트 14 〉	통과 (0.06ms, 10.2MB)
# 테스트 15 〉	통과 (0.04ms, 10.1MB)
# 테스트 16 〉	통과 (1.04ms, 11MB)
# 테스트 17 〉	통과 (0.40ms, 10.6MB)
# 테스트 18 〉	통과 (0.40ms, 10.6MB)
# 테스트 19 〉	통과 (0.34ms, 10.4MB)
# 테스트 20 〉	통과 (0.41ms, 10.4MB)