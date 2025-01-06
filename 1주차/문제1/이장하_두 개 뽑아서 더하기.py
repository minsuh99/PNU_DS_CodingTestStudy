def solution(numbers):
    # 두 수를 더해서 만들 수 있는 수는 중복이 없어야 하므로 집합 구조를 사용
    SET = set()
    l = len(numbers)
    # i번째 인데스 수와 i+1 부터 l까지 수들의 각각 합을 집합에 추가
    for i in range(l-1):
        for j in range(i+1,l):
            SET.add(numbers[i]+numbers[j])
    # 집합을 정렬된 리스트로 변환
    answer = sorted(SET)
    return answer


'''
[level 1] 두 개 뽑아서 더하기 - 68644

성능 요약
메모리: 10.1 MB, 시간: 0.91 ms

구분
코딩테스트 연습 > 월간 코드 챌린지 시즌1

채점결과
정확성: 100.0
합계: 100.0 / 100.0
'''
