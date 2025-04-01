def solution(s):
    answer = []
    ans1 = 0 # 단계수
    ans2 = 0 # 제거한 0 개수
    temp = 0
    
    while s != "1":
        s_remove0 = "".join([i for i in s if i != '0'])
        temp = len(s_remove0)
        ans2 += (len(s) - temp)
        s = str(bin(temp))[2:] # 출력 결과가 0b~~ 이렇게 됨"
        ans1 += 1
    answer = [ans1, ans2]


    return answer

'''
정확성  테스트
테스트 1 〉	통과 (0.02ms, 9.26MB)
테스트 2 〉	통과 (3.68ms, 9.35MB)
테스트 3 〉	통과 (0.01ms, 9.27MB)
테스트 4 〉	통과 (0.01ms, 9.2MB)
테스트 5 〉	통과 (0.01ms, 9.15MB)
테스트 6 〉	통과 (0.08ms, 9.26MB)
테스트 7 〉	통과 (0.12ms, 9.24MB)
테스트 8 〉	통과 (0.05ms, 9.1MB)
테스트 9 〉	통과 (3.96ms, 10.1MB)
테스트 10 〉	통과 (5.63ms, 9.7MB)
테스트 11 〉	통과 (3.32ms, 9.16MB)
채점 결과
정확성: 100.0
합계: 100.0 / 100.0
'''