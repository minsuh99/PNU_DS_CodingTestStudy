# 모든 타일로 직사각형을 채워야 하니 -> 가로, 세로가 정수
# 총 타일 개수의 약수를 이용
def solution(brown, yellow):
    answer = []
    
    target = brown + yellow
    divisor = []
    
    for i in range(1, int(target ** (0.5))+1): # 약수는 제곱근까지 확인 (중복 제거)
        if target % i == 0:
            divisor.append((target // i, i)) # 가로가 더 기니까, (큰 수, 작은수)로 저장
            # 예를 들어, 총 타일의 개수가 12라면,
            # [(12, 1), (6, 2), (4, 3)]
    
    for tup in divisor[::-1]: # 가능성 높은 경우부터 계산
        if (tup[0] - 2) * (tup[1] - 2) == yellow: # 상하좌우에서 1을 빼면 가운데의 yellow 개수의 타일이 나와야함
            return [tup[0], tup[1]]
    
    return answer


'''
정확성  테스트
테스트 1 〉	통과 (0.01ms, 9.36MB)
테스트 2 〉	통과 (0.02ms, 9.32MB)
테스트 3 〉	통과 (0.07ms, 9.36MB)
테스트 4 〉	통과 (0.02ms, 9.33MB)
테스트 5 〉	통과 (0.02ms, 9.27MB)
테스트 6 〉	통과 (0.05ms, 9.32MB)
테스트 7 〉	통과 (0.08ms, 9.21MB)
테스트 8 〉	통과 (0.07ms, 9.32MB)
테스트 9 〉	통과 (0.07ms, 9.29MB)
테스트 10 〉	통과 (0.08ms, 9.34MB)
테스트 11 〉	통과 (0.01ms, 9.32MB)
테스트 12 〉	통과 (0.01ms, 9.27MB)
테스트 13 〉	통과 (0.02ms, 9.32MB)
채점 결과
정확성: 100.0
합계: 100.0 / 100.0
'''