def solution(cards1, cards2, goal):
    for word in goal:
        if cards1 and word == cards1[0]: # cards1에 카드가 있고, 맨 앞에 단어가 다음 단어랑 같다면 카드 pop
            cards1.pop(0)
        elif cards2 and word == cards2[0]: # cards2에 카드가 있고, 맨 앞에 단어가 다음 단어랑 같다면 카드 pop
            cards2.pop(0)
        else: # 두 경우 다 안 되면 문장을 못 만드니까 No 출력
            return "No"
    
    return "Yes"

'''
테스트 1 〉	통과 (0.00ms, 10.2MB)
테스트 2 〉	통과 (0.00ms, 10.2MB)
테스트 3 〉	통과 (0.00ms, 10.3MB)
테스트 4 〉	통과 (0.00ms, 10.2MB)
테스트 5 〉	통과 (0.00ms, 10.2MB)
테스트 6 〉	통과 (0.00ms, 10.2MB)
테스트 7 〉	통과 (0.00ms, 10.3MB)
테스트 8 〉	통과 (0.00ms, 10.2MB)
테스트 9 〉	통과 (0.00ms, 10.3MB)
테스트 10 〉	통과 (0.00ms, 10.3MB)
테스트 11 〉	통과 (0.01ms, 10.2MB)
테스트 12 〉	통과 (0.01ms, 10.1MB)
테스트 13 〉	통과 (0.00ms, 10.2MB)
테스트 14 〉	통과 (0.01ms, 10.2MB)
테스트 15 〉	통과 (0.01ms, 10.2MB)
테스트 16 〉	통과 (0.01ms, 10.2MB)
테스트 17 〉	통과 (0.01ms, 10.2MB)
테스트 18 〉	통과 (0.01ms, 10.2MB)
테스트 19 〉	통과 (0.00ms, 10.3MB)
테스트 20 〉	통과 (0.01ms, 10.1MB)
테스트 21 〉	통과 (0.00ms, 10.3MB)
테스트 22 〉	통과 (0.01ms, 10.2MB)
테스트 23 〉	통과 (0.00ms, 10.2MB)
테스트 24 〉	통과 (0.00ms, 10.2MB)
테스트 25 〉	통과 (0.00ms, 10.1MB)
'''