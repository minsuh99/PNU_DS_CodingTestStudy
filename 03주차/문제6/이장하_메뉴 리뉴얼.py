from collections import defaultdict
from itertools import combinations

def solution(orders, course):
    answer = []
    # 코스 종류별로 메뉴 구성을 담을 딕셔너리
    DICT = {i: defaultdict(int) for i in course}
    
    # 코스 종류별로 메뉴 구성의 조합이 나온 횟수를 딕셔너리에 담음
    for co in course:
        for order in orders:
            if len(order) >= co:
                for com in list(map(''.join, combinations(sorted(list(order)), co))):
                    DICT[co][com] += 1

    # 각 코스별로 가장 많이 주문된 메뉴 구성들을 정답에 담음
    for _, dic in DICT.items():
        if dic.values():
            max_ = max(dic.values())
            if max_ >= 2:
                for key, value in dic.items():
                    if value == max_:
                        answer.append(key)

    # 최종 결과는 문자열순으로 정렬
    answer = sorted(answer)
    return answer


'''
정확성  테스트
테스트 1 〉	통과 (0.13ms, 10.3MB)
테스트 2 〉	통과 (0.08ms, 9.97MB)
테스트 3 〉	통과 (0.13ms, 10.2MB)
테스트 4 〉	통과 (0.08ms, 10.2MB)
테스트 5 〉	통과 (0.08ms, 10MB)
테스트 6 〉	통과 (0.19ms, 10.2MB)
테스트 7 〉	통과 (0.21ms, 10.3MB)
테스트 8 〉	통과 (1.55ms, 10MB)
테스트 9 〉	통과 (0.98ms, 10.1MB)
테스트 10 〉	통과 (1.66ms, 10.5MB)
테스트 11 〉	통과 (0.86ms, 10.3MB)
테스트 12 〉	통과 (1.01ms, 10.3MB)
테스트 13 〉	통과 (1.45ms, 10.3MB)
테스트 14 〉	통과 (0.99ms, 10.6MB)
테스트 15 〉	통과 (2.36ms, 10.4MB)
테스트 16 〉	통과 (0.33ms, 10.2MB)
테스트 17 〉	통과 (0.37ms, 10.4MB)
테스트 18 〉	통과 (0.11ms, 10.2MB)
테스트 19 〉	통과 (0.03ms, 10.3MB)
테스트 20 〉	통과 (0.24ms, 10.3MB)
'''
