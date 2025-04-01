from collections import Counter

def solution(topping):
    answer = 0
    # 각 토핑별 개수 = 철수
    DICT = Counter(topping)
    # 동생
    SET = set()
    
    for top in topping:
        # 토핑을 순서대로 하나씩 뺌
        DICT[top] -= 1
        # 토핑이 0개가 되면 제거
        if DICT[top] == 0:
            del DICT[top]
        # 뺀 토핑은 동생에게
        SET.add(top)
        
        # 철수와 동생이 가진 토핑 종류가 같을때
        if len(DICT) == len(SET):
            answer += 1
        # 동생의 종류가 많아지면 즉시 종료
        elif len(DICT) < len(SET):
            break
    
    return answer


'''
정확성  테스트
테스트 1 〉    통과 (4.74ms, 9.43MB)
테스트 2 〉    통과 (35.13ms, 13.9MB)
테스트 3 〉    통과 (47.59ms, 9.91MB)
테스트 4 〉    통과 (44.06ms, 9.98MB)
테스트 5 〉    통과 (489.64ms, 17.6MB)
테스트 6 〉    통과 (409.49ms, 50.6MB)
테스트 7 〉    통과 (351.78ms, 50.5MB)
테스트 8 〉    통과 (519.94ms, 50.5MB)
테스트 9 〉    통과 (67.06ms, 49.4MB)
테스트 10 〉    통과 (67.98ms, 49.5MB)
테스트 11 〉    통과 (10.67ms, 10MB)
테스트 12 〉    통과 (5.22ms, 10.4MB)
테스트 13 〉    통과 (522.92ms, 49.5MB)
테스트 14 〉    통과 (580.71ms, 49.4MB)
테스트 15 〉    통과 (531.41ms, 49.4MB)
테스트 16 〉    통과 (579.46ms, 49.5MB)
테스트 17 〉    통과 (425.36ms, 49.5MB)
테스트 18 〉    통과 (460.17ms, 50.5MB)
테스트 19 〉    통과 (243.02ms, 50.5MB)
테스트 20 〉    통과 (183.70ms, 50.5MB)
'''
