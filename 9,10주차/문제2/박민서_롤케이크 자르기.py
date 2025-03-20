# 반복문 안에서 set()을 생성하는것 때문에 시간 초과가 남.
# Counter는 직접 생성해도 될 것 같음.
from collections import Counter

def solution(topping):
    answer = 0
    
    cur_topping = dict(Counter(topping))
    
    young_brother = set(topping) # 동생에 모든 토핑 다 주고
    old_brother = set() # 토핑이 비어있는 형에게 주는 방식
    
    for t in topping:
        old_brother.add(t) # 형에 토핑 추가
        cur_topping[t] -= 1 # topping[i:] 이런식으로 슬라이싱 하는 것도 반복문 안에서 시간 초과
        if cur_topping[t] == 0: # 자르고 난 후 토핑이 없다면
            young_brother.remove(t) # 동생 토핑에서 제거
            # young_brother -= set([t])
        
        if len(old_brother) == len(young_brother):
            answer += 1        
    
    return answer

'''
정확성  테스트
테스트 1 〉	통과 (3.96ms, 9.46MB)
테스트 2 〉	통과 (53.11ms, 14.7MB)
테스트 3 〉	통과 (40.30ms, 9.85MB)
테스트 4 〉	통과 (52.18ms, 10MB)
테스트 5 〉	통과 (282.92ms, 17.6MB)
테스트 6 〉	통과 (408.64ms, 50.7MB)
테스트 7 〉	통과 (435.87ms, 50.5MB)
테스트 8 〉	통과 (465.35ms, 50.7MB)
테스트 9 〉	통과 (462.92ms, 49.5MB)
테스트 10 〉	통과 (403.29ms, 49.6MB)
테스트 11 〉	통과 (30.66ms, 10MB)
테스트 12 〉	통과 (4.85ms, 10.9MB)
테스트 13 〉	통과 (479.68ms, 49.6MB)
테스트 14 〉	통과 (514.46ms, 49.5MB)
테스트 15 〉	통과 (469.92ms, 49.6MB)
테스트 16 〉	통과 (470.16ms, 49.6MB)
테스트 17 〉	통과 (539.46ms, 49.7MB)
테스트 18 〉	통과 (448.86ms, 50.7MB)
테스트 19 〉	통과 (540.91ms, 50.5MB)
테스트 20 〉	통과 (434.27ms, 50.6MB)
채점 결과
정확성: 100.0
합계: 100.0 / 100.0
'''