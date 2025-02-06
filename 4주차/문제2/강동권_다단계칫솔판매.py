def solution(enroll, referral, seller, amount):
    profit_dict = {name: 0 for name in enroll}
    
    referral_dict = dict(zip(enroll, referral))

    for s, a in zip(seller, amount):
        profit = a * 100
        person = s
        
        while person != "-" and profit > 0:
            fee = profit // 10
            profit_dict[person] += profit - fee  
            
            person = referral_dict.get(person, "-")  
            profit = fee  

    return [profit_dict[name] for name in enroll]

# 테스트 1 〉	통과 (0.02ms, 10.2MB)
# 테스트 2 〉	통과 (0.08ms, 10.2MB)
# 테스트 3 〉	통과 (0.04ms, 10.1MB)
# 테스트 4 〉	통과 (0.12ms, 10.3MB)
# 테스트 5 〉	통과 (1.54ms, 10.3MB)
# 테스트 6 〉	통과 (2.14ms, 12.5MB)
# 테스트 7 〉	통과 (2.26ms, 12.4MB)
# 테스트 8 〉	통과 (3.35ms, 12.6MB)
# 테스트 9 〉	통과 (13.94ms, 13.1MB)
# 테스트 10 〉	통과 (120.03ms, 20.9MB)
# 테스트 11 〉	통과 (110.44ms, 20.6MB)
# 테스트 12 〉	통과 (101.22ms, 20.5MB)
# 테스트 13 〉	통과 (107.97ms, 20.4MB)
