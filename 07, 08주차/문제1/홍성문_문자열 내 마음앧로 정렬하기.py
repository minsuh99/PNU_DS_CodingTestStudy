## 초기 코드- 모든값을 비교해서 비효율적
def solution(strings, n):
    for i in range(len(strings)):
        for j in range(i+1, len(strings)):
            if strings[i][n] > strings[j][n]:
                strings[i], strings[j] = strings[j], strings[i]
            elif strings[i][n] == strings[j][n] and strings[i] > strings[j]:
                strings[i], strings[j] = strings[j], strings[i]
    return strings

## 선택 정렬
def solution(strings, n):
    for i in range(len(strings)):
        min_idx = i  # 가장 작은 값의 위치 저장
        for j in range(i + 1, len(strings)):
            if strings[j][n] < strings[min_idx][n] or (strings[j][n] == strings[min_idx][n] and strings[j] < strings[min_idx]):
                min_idx = j  # 더 작은 값을 찾으면 min_idx 업데이트
        strings[i], strings[min_idx] = strings[min_idx], strings[i]  # 한 번만 교환
    return strings

## 버블 정렬
def solution(strings, n):
    for i in range(len(strings) - 1):  
        for j in range(len(strings) - 1 - i):  # 앞에서부터 비교 정렬
            if strings[j][n] > strings[j + 1][n] or (strings[j][n] == strings[j + 1][n] and strings[j] > strings[j + 1]):
                strings[j], strings[j + 1] = strings[j + 1], strings[j]  # 자리 바꿈
    return strings

print(solution(["sun", "bed", "car"],1))
print(solution(["abce", "abcd", "cdx"],2))

"""
정확성  테스트
테스트 1 〉	통과 (0.00ms, 9.95MB)
테스트 2 〉	통과 (0.01ms, 10MB)
테스트 3 〉	통과 (0.08ms, 10.1MB)
테스트 4 〉	통과 (0.06ms, 10.3MB)
테스트 5 〉	통과 (0.01ms, 10.1MB)
테스트 6 〉	통과 (0.18ms, 10.3MB)
테스트 7 〉	통과 (0.03ms, 10.1MB)
테스트 8 〉	통과 (0.03ms, 9.95MB)
테스트 9 〉	통과 (0.01ms, 10.1MB)
테스트 10 〉	통과 (0.20ms, 10.4MB)
테스트 11 〉	통과 (0.01ms, 10.1MB)
테스트 12 〉	통과 (0.30ms, 10.3MB)
채점 결과
정확성: 100.0
합계: 100.0 / 100.0
"""