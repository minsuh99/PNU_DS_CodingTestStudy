from collections import Counter

def solution(want, number, discount):
    answer = 0
    sl = {key: value for key, value in zip(want, number)}

    for i in range(0,len(discount)-9):
        discount_count = Counter(discount[i:i+10])
        valid=1
        for key, value in sl.items():  
            if discount_count[key] < value:  
                valid = 0
                break
        if valid:
            answer += 1
        
    return answer

# 테스트 1 〉	통과 (22.52ms, 10.6MB)
# 테스트 2 〉	통과 (177.35ms, 14.8MB)
# 테스트 3 〉	통과 (28.05ms, 11.2MB)
# 테스트 4 〉	통과 (160.81ms, 15.6MB)
# 테스트 5 〉	통과 (75.18ms, 12.9MB)
# 테스트 6 〉	통과 (12.34ms, 10.5MB)
# 테스트 7 〉	통과 (43.65ms, 11.5MB)
# 테스트 8 〉	통과 (233.83ms, 17.3MB)
# 테스트 9 〉	통과 (43.84ms, 11.2MB)
# 테스트 10 〉	통과 (107.24ms, 13.8MB)
# 테스트 11 〉	통과 (20.12ms, 10.6MB)
# 테스트 12 〉	통과 (0.03ms, 10.2MB)
