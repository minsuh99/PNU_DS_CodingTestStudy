def solution(id_list, report, k):
    # 정지시킨 유저수를 계산할 딕셔너리
    answer = {id : 0 for id in id_list}
    
    # 신고당한 유저별로 신고한 유저를 담을 딕셔너리
    DICT = {id : set() for id in id_list}
    
    # 동일한 유저에 대한 신고는 1회로 처리하므로 중복제거
    report = set(report)
    
    for rep in report:
        a, b = rep.split()
        # 나를 신고한 유저를 담음
        DICT[b].add(a)
    
    for key, value in DICT.items():
        # 신고를 k번 이상 당해 정지된 유저
        if len(value) >= k:
            # 정지된 유저를 신고한 유저의 결과 +1
            for val in value:
                answer[val] += 1
    
    # 정지시킨 결과 수를 리스트로 변환
    answer = list(answer.values())
    return answer


'''
정확성  테스트
테스트 1 〉	통과 (0.01ms, 10.3MB)
테스트 2 〉	통과 (0.02ms, 10MB)
테스트 3 〉	통과 (164.15ms, 52.2MB)
테스트 4 〉	통과 (0.03ms, 10.3MB)
테스트 5 〉	통과 (0.03ms, 10.3MB)
테스트 6 〉	통과 (0.81ms, 10.6MB)
테스트 7 〉	통과 (1.38ms, 10.5MB)
테스트 8 〉	통과 (1.66ms, 11.2MB)
테스트 9 〉	통과 (71.94ms, 30.5MB)
테스트 10 〉	통과 (64.17ms, 30.3MB)
테스트 11 〉	통과 (131.89ms, 52.1MB)
테스트 12 〉	통과 (0.24ms, 10.2MB)
테스트 13 〉	통과 (0.22ms, 10.1MB)
테스트 14 〉	통과 (45.15ms, 25.4MB)
테스트 15 〉	통과 (74.35ms, 42.4MB)
테스트 16 〉	통과 (0.13ms, 10.2MB)
테스트 17 〉	통과 (0.20ms, 10.3MB)
테스트 18 〉	통과 (0.42ms, 10.2MB)
테스트 19 〉	통과 (0.57ms, 10.3MB)
테스트 20 〉	통과 (47.00ms, 25.3MB)
테스트 21 〉	통과 (96.56ms, 42.5MB)
테스트 22 〉	통과 (0.01ms, 10.4MB)
테스트 23 〉	통과 (0.01ms, 10MB)
테스트 24 〉	통과 (0.01ms, 10MB)
'''
