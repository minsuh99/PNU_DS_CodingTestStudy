def solution(numbers):
    answer = []
    for i in range(len(numbers)-1):
        for j in range(i+1, len(numbers)):
            if numbers[i] + numbers[j] in answer:
                pass
            else:
                answer.append(numbers[i] + numbers[j])
    answer.sort()
    return answer

# 메모리: 10.2 MB, 시간: 6.95 ms
# 시간복잡도: O(n^3) 예상
