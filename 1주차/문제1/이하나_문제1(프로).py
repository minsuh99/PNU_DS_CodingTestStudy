# 결과적으로 실패했는데 이유를 모르겠음...?!!!

def solution(numbers):
    n = 0
    answer = set()
    while n < (len(numbers)-1):
        for i in range(1, len(numbers)-n):
            num = numbers[n] + numbers[n+i]
            answer.add(num)
        n = n + 1
    return list(answer)

# 리스트에 2개만 넣어서 테스트 케이스 추가해도 잘 됨!
#  테스트 1 〉	통과 (0.01ms, 10.4MB)
#  테스트 2 〉	통과 (0.01ms, 10.2MB)
#  테스트 3 〉	통과 (0.01ms, 10.3MB)
#  테스트 4 〉	실패 (0.01ms, 10.1MB) #여기 실패
#  테스트 5 〉	실패 (0.01ms, 10.2MB) #여기 실패
#  테스트 6 〉	통과 (0.04ms, 10.2MB)
#  테스트 7 〉	통과 (0.54ms, 10.2MB)
#  테스트 8 〉	통과 (1.07ms, 10.2MB)
#  테스트 9 〉	통과 (0.53ms, 10.1MB)

# GPT 통해서 해결

def solution(numbers):
    n = 0
    answer = set()
    while n < (len(numbers)-1):
        for i in range(1, len(numbers)-n):
            num = numbers[n] + numbers[n+i]
            answer.add(num)
        n = n + 1
    return sorted(answer)

# sorted 안 한 게 문제였음... ㅠㅠ
# 그리고 gpt가 for문 2개로 바꾸는 것이 속도면에서 좋다고 함!

# 테스트 1 〉	통과 (0.01ms, 10.2MB)
# 테스트 2 〉	통과 (0.01ms, 10.2MB)
# 테스트 3 〉	통과 (0.01ms, 10.2MB)
# 테스트 4 〉	통과 (0.01ms, 10.2MB)
# 테스트 5 〉	통과 (0.02ms, 10.3MB)
# 테스트 6 〉	통과 (0.06ms, 10.2MB)
# 테스트 7 〉	통과 (0.53ms, 10.2MB)
# 테스트 8 〉	통과 (0.54ms, 10.2MB)
# 테스트 9 〉	통과 (0.60ms, 10.2MB)

# 아래는 gpt 수정 예시

def solution(numbers):
    answer = set()
    for i in range(len(numbers)):
        for j in range(i + 1, len(numbers)):
            answer.add(numbers[i] + numbers[j])
    return sorted(answer)  # 정렬된 리스트 반환