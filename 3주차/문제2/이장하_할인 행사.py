from collections import Counter

def solution(want, number, discount):
    answer = 0
    
    # 원하는 제품과 개수를 키 : 밸류 형식의 딕셔너리로 생성
    arr = dict(zip(want,number))

    # i날짜 부터 10일 간
    for i in range(len(discount)-9):
        # 10일 간 할인하는 제품과 개수를 카운트한 딕셔너리와 arr을 비교
        ls = Counter(discount[i:i+10])
        if arr == ls:
            answer += 1
    return answer

'''
정확성  테스트
테스트 1 〉	통과 (16.77ms, 10.5MB)
테스트 2 〉	통과 (100.83ms, 14.7MB)
테스트 3 〉	통과 (23.27ms, 11.1MB)
테스트 4 〉	통과 (122.24ms, 15.8MB)
테스트 5 〉	통과 (72.54ms, 12.8MB)
테스트 6 〉	통과 (11.34ms, 10.6MB)
테스트 7 〉	통과 (47.31ms, 11.4MB)
테스트 8 〉	통과 (159.02ms, 17.2MB)
테스트 9 〉	통과 (31.54ms, 10.9MB)
테스트 10 〉	통과 (79.22ms, 13.7MB)
테스트 11 〉	통과 (16.44ms, 10.6MB)
테스트 12 〉	통과 (0.03ms, 9.96MB)
'''
