def solution(s):
    answer = []
    temp = s[2:-2].split("},{") # 요소들 분리
    temp = [i.split(",") for i in temp] 
    temp.sort(key=len) # 길이순으로 정렬
    temp = [set(i) for i in temp] # 원소들의 차이를 보기 위해 set으로 변경
    
    for i in range(len(temp)):
        value = list(temp[i] - set(answer))[0] # 만약 answer에 없는 원소면
        answer.append(value) # answer에 추가
    
    answer = [int(i) for i in answer]
    
    return answer
# 시간이 많이 안 걸려서 이중 반복문 써도 됐을듯
'''
정확성  테스트
테스트 1 〉	통과 (0.03ms, 10.4MB)
테스트 2 〉	통과 (0.02ms, 10.3MB)
테스트 3 〉	통과 (0.02ms, 10.2MB)
테스트 4 〉	통과 (0.06ms, 10.5MB)
테스트 5 〉	통과 (0.17ms, 10.4MB)
테스트 6 〉	통과 (0.35ms, 10.5MB)
테스트 7 〉	통과 (4.33ms, 12.9MB)
테스트 8 〉	통과 (13.19ms, 18.5MB)
테스트 9 〉	통과 (5.73ms, 13.9MB)
테스트 10 〉	통과 (14.94ms, 19.2MB)
테스트 11 〉	통과 (22.31ms, 22.3MB)
테스트 12 〉	통과 (30.32ms, 27.4MB)
테스트 13 〉	통과 (27.52ms, 27.3MB)
테스트 14 〉	통과 (27.99ms, 27.6MB)
테스트 15 〉	통과 (0.02ms, 10.4MB)
채점 결과
정확성: 100.0
합계: 100.0 / 100.0
'''