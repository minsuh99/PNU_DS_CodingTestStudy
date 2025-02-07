def solution(enroll, referral, seller, amount):
    answer = []
    
    recommend = { } 
    profit = { } 
    
    for i in range(len(enroll)):
        recommend[enroll[i]] = referral[i]  
        profit[enroll[i]] = 0 

    def profit_cal(name, money):
        while name != '-' and money >= 1: 
            give = money // 10  
            profit[name] += money - give
            
            name = recommend[name] #중복 업데이트하는거 땜에 조금 고생함..
            money = give 

    for i in range(len(seller)):
        profit_cal(seller[i], amount[i] * 100)
        
    for name in enroll:
        answer.append(profit[name])

    return answer

"""
정확성  테스트
테스트 1 〉	통과 (0.02ms, 10.2MB)
테스트 2 〉	통과 (0.08ms, 10.2MB)
테스트 3 〉	통과 (0.08ms, 10.3MB)
테스트 4 〉	통과 (0.13ms, 10.4MB)
테스트 5 〉	통과 (1.75ms, 10.3MB)
테스트 6 〉	통과 (2.94ms, 12.6MB)
테스트 7 〉	통과 (3.88ms, 12.6MB)
테스트 8 〉	통과 (4.61ms, 12.7MB)
테스트 9 〉	통과 (17.13ms, 13.8MB)
테스트 10 〉	통과 (155.98ms, 20.9MB)
테스트 11 〉	통과 (139.12ms, 20.6MB)
테스트 12 〉	통과 (111.54ms, 20.5MB)
테스트 13 〉	통과 (114.63ms, 20.6MB)
채점 결과
정확성: 100.0
합계: 100.0 / 100.0
"""