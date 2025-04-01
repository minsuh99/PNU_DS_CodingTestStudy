# 행렬의 곱셈

def solution(arr1, arr2):
    row = len(arr1)
    col = len(arr2[0])
    num = len(arr1[0])

    # 빈 리스트 먼저 만들기
    answer = []
    for i in range(row):
        inside = [] # 안쪽 리스트로 사용할 빈 리스트 생성
        for j in range(col):
            inside.append(0)
        answer.append(inside)
    
    for i in range(row):
        for j in range(col):
            for k in range(num):
                answer[i][j] += arr1[i][k] * arr2[k][j]
    return answer

# 시간이 오래 걸리는 문제가 있음!! ㅜㅜ
# 테스트 1 〉	통과 (4.53ms, 10.3MB)
# 테스트 2 〉	통과 (93.99ms, 10.9MB)
# 테스트 3 〉	통과 (101.66ms, 11MB)
# 테스트 4 〉	통과 (1.98ms, 10.1MB)
# 테스트 5 〉	통과 (71.54ms, 10.7MB)
# 테스트 6 〉	통과 (40.30ms, 10.8MB)
# 테스트 7 〉	통과 (1.97ms, 10.4MB)
# 테스트 8 〉	통과 (0.76ms, 10MB)
# 테스트 9 〉	통과 (0.60ms, 10MB)
# 테스트 10 〉	통과 (68.55ms, 10.6MB)
# 테스트 11 〉	통과 (6.05ms, 10.2MB)
# 테스트 12 〉	통과 (0.96ms, 10.2MB)
# 테스트 13 〉	통과 (49.69ms, 10.8MB)
# 테스트 14 〉	통과 (103.06ms, 10.8MB)
# 테스트 15 〉	통과 (40.51ms, 10.6MB)
# 테스트 16 〉	통과 (9.91ms, 10.4MB)