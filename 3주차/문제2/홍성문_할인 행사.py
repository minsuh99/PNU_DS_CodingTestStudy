from collections import Counter

def solution(want, number, discount):
    answer = 0

    matching = {}

    for i,product in enumerate(want):
        matching[product] = number[i]

    for i in range(len(discount)-9):
        boundary = Counter(discount[i:i+10]) # Counter는 몰라서 검색함..

        if matching == boundary:
            answer +=1
        
    return answer

print(solution(["banana", "apple", "rice", "pork", "pot"],[3, 2, 2, 2, 1],
               ["chicken", "apple", "apple", "banana", "rice", "apple", "pork", "banana", "pork", "rice", "pot", "banana", "apple", "banana"]))
print(solution(["apple"],[10],["banana", "banana", "banana", "banana", "banana", "banana", "banana", "banana", "banana", "banana"]))

"""
정확성  테스트
테스트 1 〉	통과 (16.53ms, 10.5MB)
테스트 2 〉	통과 (150.44ms, 14.8MB)
테스트 3 〉	통과 (39.71ms, 11MB)
테스트 4 〉	통과 (139.39ms, 15.7MB)
테스트 5 〉	통과 (63.30ms, 12.8MB)
테스트 6 〉	통과 (11.14ms, 10.3MB)
테스트 7 〉	통과 (34.14ms, 11.4MB)
테스트 8 〉	통과 (158.30ms, 17.2MB)
테스트 9 〉	통과 (45.09ms, 11.1MB)
테스트 10 〉	통과 (84.64ms, 13.5MB)
테스트 11 〉	통과 (18.29ms, 10.5MB)
테스트 12 〉	통과 (0.03ms, 10.1MB)
채점 결과
정확성: 100.0
합계: 100.0 / 100.0
"""