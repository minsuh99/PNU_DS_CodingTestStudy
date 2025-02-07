from collections import deque

def solution(phone_book):
    answer = True
    queue = deque()
    queue.append(phone_book)
    while(queue):
        phone_book=queue.popleft()
        numbers=[[] for _ in range(10)]
        for number in phone_book:
            if len(number)==0:
                return False
            numbers[int(number[0])].append(number[1:])
        for array in numbers:
            if len(array)>1:
                queue.append(array)
    return answer

# 정확성  테스트
# 테스트 1 〉	통과 (0.02ms, 10.4MB)
# 테스트 2 〉	통과 (0.03ms, 10.2MB)
# 테스트 3 〉	통과 (0.03ms, 10.5MB)
# 테스트 4 〉	통과 (0.05ms, 10.3MB)
# 테스트 5 〉	통과 (0.03ms, 10.5MB)
# 테스트 6 〉	통과 (0.03ms, 10.4MB)
# 테스트 7 〉	통과 (0.03ms, 10.3MB)
# 테스트 8 〉	통과 (0.03ms, 10.3MB)
# 테스트 9 〉	통과 (0.03ms, 10.3MB)
# 테스트 10 〉	통과 (0.03ms, 10.3MB)
# 테스트 11 〉	통과 (0.03ms, 10.5MB)
# 테스트 12 〉	통과 (0.03ms, 10.3MB)
# 테스트 13 〉	통과 (0.03ms, 10.3MB)
# 테스트 14 〉	통과 (1.85ms, 10.4MB)
# 테스트 15 〉	통과 (2.59ms, 10.5MB)
# 테스트 16 〉	통과 (4.03ms, 10.6MB)
# 테스트 17 〉	통과 (4.08ms, 10.4MB)
# 테스트 18 〉	통과 (5.09ms, 10.5MB)
# 테스트 19 〉	통과 (5.50ms, 10.8MB)
# 테스트 20 〉	통과 (6.28ms, 10.7MB)
# 효율성  테스트
# 테스트 1 〉	통과 (3.18ms, 11.5MB)
# 테스트 2 〉	통과 (3.24ms, 11.5MB)
# 테스트 3 〉	통과 (1292.02ms, 62.4MB)
# 테스트 4 〉	통과 (475.56ms, 44.5MB)
